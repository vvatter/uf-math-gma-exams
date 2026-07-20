#!/usr/bin/env python3
"""Extract structured exam datasets from downloaded source PDFs using vision."""

from __future__ import annotations

import argparse
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import hashlib
from html import escape
import json
import os
from pathlib import Path
import re
import shutil
import unicodedata
from typing import Iterator, Literal

from openai import OpenAI
import pymupdf
from pydantic import BaseModel, ConfigDict, Field


DEFAULT_MODEL = "gpt-5.6-sol"
PROMPT_VERSION = "exam-extraction-v17"
NATIVE_EVIDENCE_VERSION = "native-text-c0-sanitized-v1"
VISION_ONLY_EVIDENCE_VERSION = "page-images-only-v1"
PILOT_IDS = [
    "logic-phd-2023-may",
    "logic-phd-2009-jan",
    "logic-phd-2006-may",
    "topology-phd-1994-aug",
    "analysis-phd-1994-may",
    "analysis-first-year-2015-jan-part-2",
    "differential-geometry-phd-1992-may",
    "pde-phd-2001-may",
]
MONTH_ORDER = {
    month: index
    for index, month in enumerate(
        (
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        ),
        start=1,
    )
}


class ReviewCategory(str, Enum):
    VISUAL_CONTENT = "visual-content"
    SHARED_CONTEXT = "shared-context"
    CROSS_REFERENCE = "cross-reference"
    TRANSCRIPTION = "transcription"
    CORRECTION = "correction"
    NUMBERING_TRANSFORMATION = "numbering-transformation"
    INSTRUCTION_REWRITE = "instruction-rewrite"
    NUMBERING = "numbering"
    INSTRUCTIONS = "instructions"


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ConcernStatus(str, Enum):
    SUSPECTED = "suspected"
    CONFIRMED = "confirmed"


class ProblemConcern(StrictModel):
    status: ConcernStatus
    explanation: str = Field(
        description="Cautious editorial explanation using MathJax TeX delimiters"
    )


class Subpart(StrictModel):
    label: str = Field(description="Original displayed label, such as (a), A., 1., or i.")
    text: str = Field(description="Subpart text without its label, using MathJax TeX delimiters")
    subparts: list[Subpart] = Field(
        description="Nested labeled parts in source order; empty when there are none"
    )


class ProblemTextBlock(StrictModel):
    type: Literal["text"] = "text"
    text: str = Field(description="Problem-stem text using MathJax TeX delimiters")


class TikzBlock(StrictModel):
    type: Literal["tikz"] = "tikz"
    id: str = Field(
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
        description="Stable figure identifier used in generated asset filenames",
    )
    alt: str = Field(description="Plain-language alternative text for the figure")
    libraries: list[str] = Field(
        default_factory=list,
        description="TikZ libraries required by this figure",
    )
    options: list[str] = Field(
        default_factory=list,
        description="Options added to the generated tikzpicture environment",
    )
    height_lines: int = Field(
        default=6,
        ge=1,
        le=24,
        description="Maximum rendered height in text lines for PDF and HTML",
    )
    code: str = Field(
        description="Body of the tikzpicture without document or environment wrappers"
    )


ProblemBodyBlock = ProblemTextBlock | TikzBlock


class Problem(StrictModel):
    body: list[ProblemBodyBlock] = Field(
        description="Ordered text and manually verified figure blocks in the problem stem"
    )
    subparts: list[Subpart] = Field(
        description="Labeled parts in source order; empty when there are none"
    )
    concerns: list[ProblemConcern] = Field(
        default_factory=list,
        description="Known or suspected mathematical problems in the source question",
    )


class ReviewFlag(BaseModel):
    category: ReviewCategory
    problem_indices: list[int] = Field(
        description="One-based positions of affected problems in document reading order"
    )
    source_pages: list[int]
    message: str
    original_text: str | None
    corrected_text: str | None
    context: str | None


class NumberingMode(str, Enum):
    RESTART = "restart"
    CONTINUE = "continue"


class DocumentType(str, Enum):
    EXAM = "exam"
    PRACTICE_PROBLEMS = "practice-problems"


class InstructionsBlock(StrictModel):
    type: Literal["instructions"] = "instructions"
    text: str


class ProblemBlock(StrictModel):
    type: Literal["problem"] = "problem"
    problem: Problem


SectionContentBlock = InstructionsBlock | ProblemBlock


class SectionBlock(StrictModel):
    type: Literal["section"] = "section"
    heading: str = Field(description="Exact displayed part, section, or topic heading")
    numbering: NumberingMode
    content: list[SectionContentBlock]


ExamContentBlock = InstructionsBlock | ProblemBlock | SectionBlock


class ModelExtraction(StrictModel):
    content: list[ExamContentBlock]
    review_flags: list[ReviewFlag]


class ExamRecord(StrictModel):
    schema_version: Literal[3] = 3
    id: str
    subject: str
    subject_tag: str
    year: int | None
    month: str | None
    part: int | None
    pdf_url: str
    content: list[ExamContentBlock]
    practice_variant: Literal["A", "B"] | None = None
    document_type: DocumentType = DocumentType.EXAM
    problem_count: int | None = None


class LegacyProblem(StrictModel):
    number: int = Field(ge=1)
    text: str
    subparts: list[Subpart]


class LegacyExamRecord(StrictModel):
    schema_version: Literal[1] = 1
    id: str
    subject: str
    subject_tag: str
    year: int
    month: str
    part: int | None
    pdf_url: str
    instructions: str | None
    problems: list[LegacyProblem]


@dataclass(frozen=True)
class SourceExam:
    id: str
    subject: str
    subject_tag: str
    year: int | None
    month: str | None
    part: int | None
    pdf_url: str
    pdf_path: Path
    sha256: str
    download_sha256: str
    practice_variant: Literal["A", "B"] | None = None
    document_type: DocumentType = DocumentType.EXAM
    problem_count: int | None = None


@dataclass(frozen=True)
class ExamSelection:
    ids: tuple[str, ...]
    skipped_completed: int = 0
    deferred_by_limit: int = 0


SYSTEM_PROMPT = r"""You extract the useful mathematical content of an exam into structured data.
This is not archival OCR. Preserve the questions, their mathematical meaning, and meaningful
instructions. Discard visual layout and administrative document furniture.

AUTHORITATIVE METADATA
The user supplies the subject, month, year, part, and URL. Do not extract or correct metadata from
the PDF. Ignore printed titles, dates, days, and metadata conflicts in the page images.

CONTENT TO OMIT
Omit titles that duplicate metadata, department branding, names and signature fields, grading
grids, page numbers, headers, footers, answer space, blank pages, scan noise, and point values.
Omit instructions about writing names, using separate sheets, or similar logistics. Preserve
authored requirements about clarity, detail, showing work, legibility, proofs, and conclusions.

CONTENT STRUCTURE
Return the meaningful document content in reading order as instruction, problem, and section
blocks. A section represents a displayed part, section, topic, or comparable named division.
Preserve its complete displayed heading exactly, including words, numerals, and topic names. Do not
create sections merely for pages, columns, visual spacing, or unlabeled groups. A section normally
contains instruction and problem blocks in source order. Do not nest sections.

If a displayed section label and a direction share one line before following problems, put the
label or named title in heading and put the direction in the section's first instruction block. For
example, "I. State the following theorems:" becomes heading "I." followed by instructions "State
the following theorems." A labeled direction that only governs or selects previously listed
problems is an instruction-only section: put the label or named title in heading, put the direction
in an instruction block, and set restart or continue to reflect the source's numbering policy. For
example, "II. Prove one of the theorems 8 or 9." becomes heading "II" followed by instructions
"Prove one of the theorems 8 or 9." A labeled line that itself states an independent mathematical
task is a section with a problem block even when no separately numbered problem follows. For
example, "II. Prove that
\((L^1)^*=L^\infty\)." contains a problem. For a standalone mathematical task with no printed
integer label, use the section's source-appropriate restart or continue policy to derive its
displayed number. Add a numbering-transformation flag documenting that the presentation assigned a
number to an unnumbered task.

INSTRUCTIONS
Use as many instruction blocks as the source requires. Put each block at its source position: at
exam level when it applies generally, or inside a section when it occurs there. Instructions may
appear between problems. Preserve selection rules, expected proof/detail level, allowed methods or
materials, and shared notation. Preserve wording and sentence-level detail as closely as possible.
Do not combine separate instruction blocks, summarize, stylistically improve, generalize, or move
them merely to produce a single preamble. If point values are the only signal that groups require
different response depth, express that distinction without scores. Removing excluded logistics
does not require a review flag.

PROBLEMS
Do not paraphrase, summarize, modernize, solve, or add to a problem. Join visual line wraps and
remove line-break hyphenation. The order of problem blocks determines their numbers; do not include
the source's top-level number in problem text. Put the problem stem in one text block in its body.
Never return a tikz block: those blocks are reserved for separately reviewed, manually authored
figures added after extraction. Use an empty body when a problem immediately begins with subparts.
Put each labeled part in the subparts array, preserve its label exactly in label, and do not repeat
that label in text. Recurse for nested labeled parts. Use an empty subparts array when none exist.

MATHEMATICAL CONCERNS
When the source is legible but a problem appears mathematically false, underdetermined, internally
inconsistent, or missing a necessary definition or hypothesis, preserve the source wording and add
a suspected concern to that problem. Explain the issue precisely and cautiously without solving or
rewriting the problem. Use MathJax delimiters in the explanation. Never mark a concern confirmed;
only a person may confirm one. Use an empty concerns array when no mathematical concern is present.
Do not use a concern for text or notation that cannot be read reliably; preserve the best-supported
reading and add a transcription review flag instead.

NUMBERING
Preserve ordinary integer top-level problem numbering through block order, including sequences that
restart inside a section. Set a section's numbering to "restart" when its first output problem starts
again at 1; set it to "continue" when its first output problem continues the preceding integer
sequence. The first problem in the exam or first section begins at 1. Problems must be consecutive
within their source numbering sequence.

The schema intentionally supports only integer top-level numbers. If the source uses noninteger or
compound top-level labels such as A-C, 1A-1C, or 5, 5-prime, 6, 6-prime, normalize only that exam to
one consecutive sequence in reading order. Set section numbering to describe the normalized output,
minimally update instructions that cite those labels, and add numbering-transformation and
instruction-rewrite flags as applicable. Do not normalize ordinary integer numbering that merely
restarts inside a section.

MATHEMATICS
Use Unicode for prose and MathJax-compatible TeX for mathematics. Use \(...\) for inline math and
\[...\] for display math. Do not use dollar-sign delimiters. Never copy ASCII control characters
from native PDF text; reconstruct the intended visible text or TeX from the page image. Preserve
notation and mathematical meaning exactly.

NAMES AND EPONYMS
Use the standard spelling and diacritics for every unambiguously identified mathematician, even
when the source omits a diacritic or uses an ASCII transliteration (for example, Gödel rather than
Goedel). In established names for theorems, methods, inequalities, and other mathematical objects,
use an en dash between the names of different people (for example, Hahn–Banach, Radon–Nikodym,
Gram–Schmidt, and Borsuk–Ulam). Preserve a hyphen that is actually part of one person's surname.
These are controlled presentation normalizations, not source corrections, so do not add correction
review flags for them. If a person's identity or the appropriate name form is genuinely ambiguous,
preserve the source reading and add a transcription review flag rather than guessing.

REVIEW REFERENCES
In every review flag, identify affected problems by their one-based position in overall document
reading order, ignoring instruction and section blocks. These problem_indices are not displayed
problem numbers. Use an empty list for an exam-level issue that affects no specific problem.

CORRECTIONS
Preserve the source reading unless the intended correction is uniquely determined by the immediate
mathematical context. Every correction, however obvious, requires a correction review flag with the
original text, corrected text, immediate context, problem index, and source page. If a correction is
not uniquely determined, retain the source reading. Add a problem concern when the legible source
has a mathematical defect; add a transcription review flag when the source reading itself is
uncertain.

SERIOUS REVIEW
If a figure, diagram, graph, or table carries information that cannot be transcribed completely and
unambiguously, transcribe the surrounding words but do not invent or reconstruct the visual. Add a
visual-content flag. A table that can be represented completely as MathJax or structured text without
losing information should be transcribed and does not require a visual-content flag. Put shared
notation or material in an instruction block at its source position; flag it only when its scope
remains genuinely unclear. Do not flag a clear cross-problem reference merely because it exists;
flag one only when its target or meaning is broken or ambiguous. Flag uncertain words or math,
unclear numbering, and instructions that may no longer agree with numbering. Findings do not stop
extraction. A legible mathematical issue belongs in the problem's concerns rather than the serious
review queue. Return null for correction-only fields when they do not apply."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".part")
    if isinstance(value, BaseModel):
        content = value.model_dump_json(indent=2)
    else:
        content = json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True)
    temporary.write_text(content + "\n", encoding="utf-8")
    os.replace(temporary, path)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".part")
    temporary.write_text(content, encoding="utf-8")
    os.replace(temporary, path)


def archive_files(paths: list[Path], history_root: Path) -> None:
    existing = [path for path in paths if path.exists()]
    if not existing:
        return
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    destination = history_root / timestamp
    destination.mkdir(parents=True, exist_ok=False)
    for path in existing:
        shutil.move(path, destination / path.name)


def part_from_manifest(record: dict[str, object]) -> int | None:
    label = str(record.get("source_label") or "")
    match = re.search(r"\bpart\s*(\d+)\b", label, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def load_sources(manifest_path: Path) -> dict[str, SourceExam]:
    raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources: dict[str, SourceExam] = {}
    for item in raw["exams"]:
        pdf_path = Path(item["path"])
        exam_id = item["id"]
        source = SourceExam(
            id=exam_id,
            subject=item["subject"],
            subject_tag=item["subject_tag"],
            year=item.get("year"),
            month=item.get("month"),
            part=part_from_manifest(item),
            pdf_url=item["download_url"],
            pdf_path=pdf_path,
            sha256=item["sha256"],
            download_sha256=item.get("download_sha256", item["sha256"]),
            practice_variant=item.get("practice_variant"),
            document_type=DocumentType(item.get("document_type", "exam")),
            problem_count=item.get("problem_count"),
        )
        if exam_id in sources:
            raise RuntimeError(f"duplicate exam identifier in manifest: {exam_id}")
        sources[exam_id] = source
    return sources


def source_sort_key(source: SourceExam) -> tuple[object, ...]:
    return (
        source.subject_tag,
        source.year is None,
        source.year or 0,
        MONTH_ORDER.get(source.month or "", 13),
        source.month or "",
        source.practice_variant or "",
        source.document_type.value,
        source.part or 0,
        source.id,
    )


def select_exam_ids(
    sources: dict[str, SourceExam],
    explicit_ids: list[str],
    *,
    pilot: bool,
    all_exams: bool,
    subject_tags: list[str] | None,
    limit: int | None,
    force: bool,
) -> ExamSelection:
    subject_tags = subject_tags or []
    modes = sum(
        (
            bool(explicit_ids),
            pilot,
            all_exams,
            bool(subject_tags),
        )
    )
    if modes != 1:
        raise ValueError(
            "choose exactly one selection mode: exam IDs, --pilot, --all, or --subject"
        )
    bulk_selection = all_exams or bool(subject_tags)
    if limit is not None and limit < 1:
        raise ValueError("--limit must be at least 1")
    if limit is not None and not bulk_selection:
        raise ValueError("--limit requires --all or --subject")

    if pilot:
        requested = list(PILOT_IDS)
    elif explicit_ids:
        requested = list(dict.fromkeys(explicit_ids))
    else:
        requested_subjects = set(subject_tags)
        known_subjects = {source.subject_tag for source in sources.values()}
        unknown_subjects = sorted(requested_subjects - known_subjects)
        if unknown_subjects:
            raise ValueError("unknown subject tags: " + ", ".join(unknown_subjects))
        requested = [
            source.id
            for source in sorted(sources.values(), key=source_sort_key)
            if source.document_type == DocumentType.EXAM
            and (all_exams or source.subject_tag in requested_subjects)
        ]

    missing = [exam_id for exam_id in requested if exam_id not in sources]
    if missing:
        raise ValueError("exam IDs not found in manifest: " + ", ".join(missing))
    unsupported = [
        exam_id
        for exam_id in requested
        if sources[exam_id].document_type != DocumentType.EXAM
    ]
    if unsupported:
        raise ValueError(
            "practice-problem collections require extract_practice_problems.py: "
            + ", ".join(unsupported)
        )

    skipped_completed = 0
    if bulk_selection and not force:
        selected: list[str] = []
        for exam_id in requested:
            if exam_json_path(sources[exam_id]).exists():
                skipped_completed += 1
            else:
                selected.append(exam_id)
        requested = selected

    deferred_by_limit = 0
    if limit is not None and len(requested) > limit:
        deferred_by_limit = len(requested) - limit
        requested = requested[:limit]

    return ExamSelection(
        ids=tuple(requested),
        skipped_completed=skipped_completed,
        deferred_by_limit=deferred_by_limit,
    )


def clean_native_text(text: str) -> str:
    return "".join(
        character
        for character in text
        if ord(character) >= 32 or character in "\n\t"
    ).strip()


def render_pages(source: SourceExam, workdir: Path, dpi: int) -> list[dict[str, object]]:
    page_dir = workdir / "pages"
    page_dir.mkdir(parents=True, exist_ok=True)
    scale = dpi / 72
    rendered: list[dict[str, object]] = []
    with pymupdf.open(source.pdf_path) as document:
        for index, page in enumerate(document, start=1):
            image_path = page_dir / f"{index:04d}.png"
            if not image_path.exists():
                pixmap = page.get_pixmap(
                    matrix=pymupdf.Matrix(scale, scale),
                    colorspace=pymupdf.csRGB,
                    alpha=False,
                )
                pixmap.save(image_path)
            image_bytes = image_path.read_bytes()
            rendered.append(
                {
                    "page_number": index,
                    "image_path": str(image_path),
                    "image_data_url": "data:image/png;base64,"
                    + base64.b64encode(image_bytes).decode("ascii"),
                    "native_text": clean_native_text(page.get_text("text")),
                }
            )
    return rendered


def extraction_prompt(
    source: SourceExam,
    pages: list[dict[str, object]],
    include_native_text: bool = True,
) -> str:
    if include_native_text:
        native = "\n\n".join(
            f"PAGE {page['page_number']} NATIVE TEXT (untrusted evidence):\n"
            + (str(page["native_text"]) or "(none)")
            for page in pages
        )
    else:
        native = "Native PDF text is intentionally omitted. Use the page images only."
    part_text = str(source.part) if source.part is not None else "none"
    date_text = (
        f"{source.month.title()} {source.year}"
        if source.year is not None and source.month is not None
        else "undated practice exam"
    )
    practice_text = source.practice_variant or "none"
    return f"""CATALOG METADATA (authoritative; do not infer from PDF):
Subject: {source.subject}
Subject tag: {source.subject_tag}
Date: {date_text}
Practice variant: {practice_text}
Part: {part_text}
Current PDF URL: {source.pdf_url}
Source pages: {len(pages)}

PAGE IMAGES are supplied before this text in page order. Native text below is optional evidence and
may be empty, corrupt, or inaccurate for mathematics. Trust the page images when they disagree.

{native}
"""


def call_model(
    client: OpenAI,
    source: SourceExam,
    pages: list[dict[str, object]],
    model: str,
    reasoning: str,
    include_native_text: bool,
) -> tuple[ModelExtraction, str | None, dict[str, object] | None]:
    content: list[dict[str, object]] = []
    for page in pages:
        content.append(
            {"type": "input_text", "text": f"SOURCE PAGE {page['page_number']}"}
        )
        content.append(
            {
                "type": "input_image",
                "image_url": page["image_data_url"],
                "detail": "high",
            }
        )
    content.append(
        {
            "type": "input_text",
            "text": extraction_prompt(source, pages, include_native_text),
        }
    )
    response = client.responses.parse(
        model=model,
        reasoning={"effort": reasoning},
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content},
        ],
        text_format=ModelExtraction,
    )
    if response.output_parsed is None:
        raise RuntimeError(f"{model} returned no parsed extraction for {source.id}")
    usage = response.usage.model_dump(mode="json") if response.usage else None
    return response.output_parsed, response.id, usage


def has_ascii_control_characters(value: object) -> bool:
    if isinstance(value, BaseModel):
        return has_ascii_control_characters(value.model_dump(mode="json"))
    if isinstance(value, dict):
        return any(has_ascii_control_characters(item) for item in value.values())
    if isinstance(value, list):
        return any(has_ascii_control_characters(item) for item in value)
    if isinstance(value, str):
        return any(ord(character) < 32 and character not in "\n\t" for character in value)
    return False


def repair_control_characters(
    client: OpenAI,
    extraction: ModelExtraction,
    model: str,
    reasoning: str,
) -> tuple[ModelExtraction, str | None, dict[str, object] | None]:
    escaped = json.dumps(
        extraction.model_dump(mode="json"),
        ensure_ascii=True,
        sort_keys=True,
    )
    response = client.responses.parse(
        model=model,
        reasoning={"effort": reasoning},
        input=[
            {
                "role": "system",
                "content": (
                    "Repair encoding corruption in an already transcribed exam extraction. "
                    "The JSON contains escaped ASCII C0 control characters such as "
                    "\\u0001 or \\u001d where TeX backslashes and MathJax delimiters were "
                    "intended. Remove every control character and reconstruct valid "
                    "MathJax using \\(...\\) and \\[...\\]. Do not alter any wording, "
                    "mathematics, structure, labels, or review findings beyond the minimum "
                    "encoding repair. Return the complete repaired extraction."
                ),
            },
            {"role": "user", "content": escaped},
        ],
        text_format=ModelExtraction,
    )
    if response.output_parsed is None:
        raise RuntimeError(f"{model} returned no parsed control-character repair")
    usage = response.usage.model_dump(mode="json") if response.usage else None
    return response.output_parsed, response.id, usage


def walk_subparts(subparts: list[Subpart]) -> Iterator[Subpart]:
    for subpart in subparts:
        yield subpart
        yield from walk_subparts(subpart.subparts)


def iter_content_blocks(exam: ExamRecord) -> Iterator[InstructionsBlock | ProblemBlock]:
    for block in exam.content:
        if isinstance(block, SectionBlock):
            yield from block.content
        else:
            yield block


def iter_problems(exam: ExamRecord) -> Iterator[Problem]:
    for block in iter_content_blocks(exam):
        if isinstance(block, ProblemBlock):
            yield block.problem


def iter_tikz_blocks(exam: ExamRecord) -> Iterator[TikzBlock]:
    for problem in iter_problems(exam):
        for block in problem.body:
            if isinstance(block, TikzBlock):
                yield block


def iter_numbered_problems(exam: ExamRecord) -> Iterator[tuple[int, int, Problem]]:
    """Yield absolute index, displayed number, and problem in reading order."""
    for problem_index, displayed_number, _section_heading, problem in iter_problem_locations(
        exam
    ):
        yield problem_index, displayed_number, problem


def iter_problem_locations(
    exam: ExamRecord,
) -> Iterator[tuple[int, int, str | None, Problem]]:
    """Yield stable index, displayed number, section heading, and problem."""
    problem_index = 0
    displayed_number = 0
    for block in exam.content:
        if isinstance(block, InstructionsBlock):
            continue
        if isinstance(block, ProblemBlock):
            problem_index += 1
            displayed_number += 1
            yield problem_index, displayed_number, None, block.problem
            continue
        if block.numbering == NumberingMode.RESTART:
            displayed_number = 0
        for item in block.content:
            if isinstance(item, ProblemBlock):
                problem_index += 1
                displayed_number += 1
                yield problem_index, displayed_number, block.heading.strip(), item.problem


def all_content(exam: ExamRecord) -> Iterator[str]:
    for block in iter_content_blocks(exam):
        if isinstance(block, InstructionsBlock):
            yield block.text
            continue
        for body_block in block.problem.body:
            if isinstance(body_block, ProblemTextBlock):
                yield body_block.text
        for concern in block.problem.concerns:
            yield concern.explanation
        for subpart in walk_subparts(block.problem.subparts):
            yield subpart.text


MATHJAX_EXPRESSION = re.compile(r"\\\((?:.|\n)*?\\\)|\\\[(?:.|\n)*?\\\]")


def unwrapped_unicode_math(text: str) -> set[str]:
    """Find Unicode math glyphs that should be represented by TeX."""
    prose = MATHJAX_EXPRESSION.sub("", text)
    return {
        character
        for character in prose
        if unicodedata.category(character) == "Sm"
        or "\u0370" <= character <= "\u03ff"
        or "\u1d2c" <= character <= "\u1d6a"
        or "\u2070" <= character <= "\u209f"
        or "\U0001d400" <= character <= "\U0001d7ff"
    }


def migrate_legacy_exam(legacy: LegacyExamRecord) -> ExamRecord:
    content: list[ExamContentBlock] = []
    if legacy.instructions is not None:
        content.append(InstructionsBlock(text=legacy.instructions))
    content.extend(
        ProblemBlock(
            problem=Problem(
                body=[ProblemTextBlock(text=problem.text)] if problem.text else [],
                subparts=problem.subparts,
            )
        )
        for problem in legacy.problems
    )
    return ExamRecord(
        id=legacy.id,
        subject=legacy.subject,
        subject_tag=legacy.subject_tag,
        year=legacy.year,
        month=legacy.month,
        part=legacy.part,
        pdf_url=legacy.pdf_url,
        content=content,
    )


def validate_exam(exam: ExamRecord, source: SourceExam, flags: list[ReviewFlag]) -> list[str]:
    errors: list[str] = []
    if exam.id != source.id:
        errors.append("identifier does not match source")
    if exam.subject != source.subject or exam.subject_tag != source.subject_tag:
        errors.append("subject metadata does not match source")
    if (
        exam.year,
        exam.month,
        exam.part,
        exam.practice_variant,
        exam.document_type,
        exam.problem_count,
    ) != (
        source.year,
        source.month,
        source.part,
        source.practice_variant,
        source.document_type,
        source.problem_count,
    ):
        errors.append("document, date, practice variant, or part metadata does not match source")
    has_date = exam.year is not None or exam.month is not None
    if has_date and (exam.year is None or exam.month is None):
        errors.append("year and month must either both be present or both be absent")
    if exam.document_type == DocumentType.PRACTICE_PROBLEMS:
        if has_date or exam.part is not None or exam.practice_variant is not None:
            errors.append("practice-problem collections cannot have a date, part, or variant")
        if exam.problem_count is None or exam.problem_count < 1:
            errors.append("practice-problem collections require a positive problem count")
    else:
        if exam.problem_count is not None:
            errors.append("ordinary exams cannot declare a practice-problem count")
        if exam.practice_variant is not None and has_date:
            errors.append("practice exams cannot have a year or month")
        if exam.practice_variant is None and not has_date:
            errors.append("a record without a date must be a practice exam")
    if exam.pdf_url != source.pdf_url:
        errors.append("PDF URL does not match current manifest URL")
    problems = list(iter_problems(exam))
    if exam.problem_count is not None and len(problems) != exam.problem_count:
        errors.append(
            f"record declares {exam.problem_count} problems but contains {len(problems)}"
        )
    instructions = [
        block.text for block in iter_content_blocks(exam) if isinstance(block, InstructionsBlock)
    ]
    if not problems and not any(text.strip() for text in instructions):
        errors.append("record contains neither problems nor a notice")
    for block in exam.content:
        if isinstance(block, InstructionsBlock):
            if not block.text.strip():
                errors.append("instruction block is empty")
            continue
        if isinstance(block, ProblemBlock):
            continue
        if not block.heading.strip():
            errors.append("section heading is empty")
        if not block.content:
            errors.append(f"section {block.heading!r} is empty")
        for item in block.content:
            if isinstance(item, InstructionsBlock) and not item.text.strip():
                errors.append(f"section {block.heading!r} contains an empty instruction block")
    for problem_index, problem in enumerate(problems, start=1):
        if not problem.body and not problem.subparts:
            errors.append(f"problem index {problem_index} has no content")
        for body_block in problem.body:
            if isinstance(body_block, ProblemTextBlock):
                if not body_block.text.strip():
                    errors.append(f"problem index {problem_index} has an empty text block")
                continue
            if not body_block.alt.strip():
                errors.append(f"problem index {problem_index} has empty figure alt text")
            if not body_block.code.strip():
                errors.append(f"problem index {problem_index} has empty TikZ code")
            if any(
                marker in body_block.code
                for marker in (
                    r"\documentclass",
                    r"\begin{document}",
                    r"\end{document}",
                    r"\begin{tikzpicture}",
                    r"\end{tikzpicture}",
                )
            ):
                errors.append(
                    f"problem index {problem_index} TikZ code contains a document or picture wrapper"
                )
        for subpart in walk_subparts(problem.subparts):
            if not subpart.label.strip():
                errors.append(f"problem index {problem_index} has an empty subpart label")
            if not subpart.text.strip() and not subpart.subparts:
                errors.append(f"problem index {problem_index} has an empty subpart")
        explanations = [concern.explanation.strip() for concern in problem.concerns]
        if any(not explanation for explanation in explanations):
            errors.append(f"problem index {problem_index} has an empty concern")
        if len(explanations) != len(set(explanations)):
            errors.append(f"problem index {problem_index} has duplicate concerns")
        for concern_index, explanation in enumerate(explanations, start=1):
            if characters := unwrapped_unicode_math(explanation):
                displayed = " ".join(sorted(characters))
                errors.append(
                    f"problem index {problem_index} concern {concern_index} contains "
                    f"Unicode math outside MathJax delimiters: {displayed}"
                )
    figure_ids = [figure.id for figure in iter_tikz_blocks(exam)]
    if len(figure_ids) != len(set(figure_ids)):
        errors.append("TikZ figure IDs are not unique within the exam")
    for text in all_content(exam):
        if any(ord(character) < 32 and character not in "\n\t" for character in text):
            errors.append("content contains an ASCII control character")
        if text.count(r"\(") != text.count(r"\)"):
            errors.append("unbalanced inline MathJax delimiters")
        if text.count(r"\[") != text.count(r"\]"):
            errors.append("unbalanced display MathJax delimiters")
        if "$" in text:
            errors.append("dollar-sign math delimiters are not allowed")
    for flag in flags:
        if any(index < 1 or index > len(problems) for index in flag.problem_indices):
            errors.append("review flag refers to an unknown problem index")
        if flag.category == ReviewCategory.CORRECTION and not all(
            [flag.original_text, flag.corrected_text, flag.context]
        ):
            errors.append("correction flag lacks original, corrected, or context text")
    return list(dict.fromkeys(errors))


def exam_json_path(source: SourceExam) -> Path:
    return source.pdf_path.parent / f"{source.id}.json"


def exam_html_path(source: SourceExam) -> Path:
    return source.pdf_path.parent / "index.html"


def exam_tex_path(source: SourceExam) -> Path:
    return source.pdf_path.parent / f"{source.id}.tex"


def exam_pdf_path(source: SourceExam) -> Path:
    return source.pdf_path.parent / f"{source.id}.pdf"


def exam_figure_png_path(source: SourceExam, figure: TikzBlock) -> Path:
    return source.pdf_path.parent / f"{source.id}.{figure.id}.png"


def checkpoint_path(source: SourceExam, build_root: Path) -> Path:
    return build_root / source.id / "extraction.json"


def has_current_extraction(source: SourceExam, build_root: Path) -> bool:
    output_path = exam_json_path(source)
    saved_path = checkpoint_path(source, build_root)
    if not output_path.exists() or not saved_path.exists():
        return False
    try:
        output = json.loads(output_path.read_text(encoding="utf-8"))
        checkpoint = json.loads(saved_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return (
        output.get("schema_version") == 3
        and checkpoint.get("schema_version") == 3
        and checkpoint.get("prompt_version") == PROMPT_VERSION
        and checkpoint.get("source_sha256") == source.sha256
        and checkpoint.get("validation_errors") == []
    )


def build_exam(source: SourceExam, extraction: ModelExtraction) -> ExamRecord:
    return ExamRecord(
        id=source.id,
        subject=source.subject,
        subject_tag=source.subject_tag,
        year=source.year,
        month=source.month,
        part=source.part,
        pdf_url=source.pdf_url,
        content=extraction.content,
        practice_variant=source.practice_variant,
        document_type=source.document_type,
        problem_count=source.problem_count,
    )


def figure_png_filename(exam_id: str, figure: TikzBlock) -> str:
    return f"{exam_id}.{figure.id}.png"


def exam_title(exam: ExamRecord | SourceExam) -> str:
    if exam.document_type == DocumentType.PRACTICE_PROBLEMS:
        return "Algebra First-Year Exam, Practice Problems"
    if exam.subject.startswith("First Year "):
        title = f"{exam.subject.removeprefix('First Year ')} First-Year Exam"
    elif exam.subject.startswith("PhD "):
        title = f"{exam.subject.removeprefix('PhD ')} PhD Exam"
    elif exam.subject.endswith(" Qualifying Exam"):
        title = f"{exam.subject.removesuffix(' Qualifying Exam')} Qualifying Exam"
    else:
        title = f"{exam.subject} Exam"
    if exam.practice_variant is not None:
        title = title.removesuffix(" Exam") + f" Practice Exam {exam.practice_variant}"
    elif exam.year is not None and exam.month is not None:
        title += f", {exam.month.title()} {exam.year}"
    else:
        raise ValueError(f"exam has neither a date nor a practice variant: {exam.id}")
    if exam.part is not None:
        title += f", Part {exam.part}"
    return title


PROJECT_SOURCE_URL = "https://github.com/vvatter/uf-math-gma-exams"
PAGE_UPDATED_ISO = "2026-07-20"
PAGE_UPDATED_LABEL = "July 20, 2026"


def subject_display_name(subject: str, subject_tag: str) -> str:
    name = subject.strip()
    if subject_tag.endswith("-qualifying") and name.endswith(" Qualifying Exam"):
        return name.removesuffix(" Qualifying Exam")
    if subject_tag.endswith("-first-year") and name.startswith("First Year "):
        return name.removeprefix("First Year ")
    if subject_tag.endswith("-phd") and name.startswith("PhD "):
        return name.removeprefix("PhD ")
    raise ValueError(f"subject name does not match its tag: {subject!r}, {subject_tag!r}")


def subject_archive_title(subject: str, subject_tag: str) -> str:
    name = subject_display_name(subject, subject_tag)
    if subject_tag.endswith("-qualifying"):
        return f"{name} Qualifying Exams"
    if subject_tag.endswith("-first-year"):
        return f"{name} First-Year Exams"
    if subject_tag.endswith("-phd"):
        return f"{name} PhD Exams"
    raise ValueError(f"subject tag has no recognized archive level: {subject_tag}")


DISPLAY_MATH_BLOCK = re.compile(r"(\\\[(?:.|\n)*?\\\])")
COMPUTER_MODERN_CSS = (
    "https://cdn.jsdelivr.net/npm/computer-modern@0.1.3/cmu-serif.css"
)
MATHJAX_SCRIPT = "https://cdn.jsdelivr.net/npm/mathjax@4/tex-chtml.js"


def render_html_text(text: str, indentation: int) -> list[str]:
    """Render escaped prose and display-math blocks without interpreting TeX."""
    prefix = " " * indentation
    lines: list[str] = []
    for segment in DISPLAY_MATH_BLOCK.split(text.strip()):
        if not segment.strip():
            continue
        if segment.lstrip().startswith(r"\["):
            escaped_math = escape(segment.strip())
            lines.append(f'{prefix}<div class="display-math">{escaped_math}</div>')
            continue
        for paragraph in re.split(r"\n\s*\n", segment.strip()):
            if not paragraph.strip():
                continue
            escaped_lines = [escape(line.strip()) for line in paragraph.splitlines()]
            lines.append(f"{prefix}<p>{'<br>'.join(escaped_lines)}</p>")
    return lines


def html_problem_fallback(problem: Problem) -> str:
    if problem.body or not problem.subparts:
        return ""
    small_numbers = (
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )
    count = (
        small_numbers[len(problem.subparts)]
        if len(problem.subparts) <= 9
        else str(len(problem.subparts))
    )
    noun = "part" if len(problem.subparts) == 1 else "parts"
    return f"This problem has {count} {noun}."


def render_html_subparts(subparts: list[Subpart], indentation: int) -> list[str]:
    prefix = " " * indentation
    lines = [f'{prefix}<ol class="subparts">']
    for subpart in subparts:
        lines.extend(
            [
                f"{prefix}  <li>",
                f'{prefix}    <div class="subpart-row">',
                f'{prefix}      <span class="subpart-label">{escape(subpart.label)}</span>',
                f'{prefix}      <div class="subpart-body">',
            ]
        )
        lines.extend(render_html_text(subpart.text, indentation + 8))
        lines.append(f"{prefix}      </div>")
        lines.append(f"{prefix}    </div>")
        if subpart.subparts:
            lines.extend(render_html_subparts(subpart.subparts, indentation + 4))
        lines.append(f"{prefix}  </li>")
    lines.append(f"{prefix}</ol>")
    return lines


def render_html_concern(concern: ProblemConcern, indentation: int) -> list[str]:
    prefix = " " * indentation
    status = (
        "Suspected error."
        if concern.status == ConcernStatus.SUSPECTED
        else "Confirmed error."
    )
    content = render_html_text(concern.explanation, indentation + 2)
    label = f"<strong>Warning: {status}</strong>"
    if content and content[0].lstrip().startswith("<p>"):
        content[0] = content[0].replace("<p>", f"<p>{label} ", 1)
    else:
        content.insert(0, f"{prefix}  <p>{label}</p>")
    return [
        f'{prefix}<div class="problem-concern" role="note">',
        *content,
        f"{prefix}</div>",
    ]


def render_html_problem(
    problem: Problem, indentation: int, exam_id: str, problem_index: int
) -> list[str]:
    prefix = " " * indentation
    lines = [f'{prefix}<li class="problem" id="problem-{problem_index}">']
    for concern in problem.concerns:
        lines.extend(render_html_concern(concern, indentation + 2))
    fallback = html_problem_fallback(problem)
    if fallback:
        lines.extend(render_html_text(fallback, indentation + 2))
    for body_block in problem.body:
        if isinstance(body_block, ProblemTextBlock):
            lines.extend(render_html_text(body_block.text, indentation + 2))
            continue
        lines.extend(
            [
                f'{prefix}  <figure class="problem-figure">',
                f'{prefix}    <img src="{escape(figure_png_filename(exam_id, body_block), quote=True)}" '
                f'alt="{escape(body_block.alt, quote=True)}"'
                + (
                    f' style="max-height: {body_block.height_lines}lh"'
                    if body_block.height_lines != 6
                    else ""
                )
                + ">",
                f"{prefix}  </figure>",
            ]
        )
    if problem.subparts:
        lines.extend(render_html_subparts(problem.subparts, indentation + 2))
    lines.append(f"{prefix}</li>")
    return lines


def render_html_blocks(
    blocks: list[InstructionsBlock | ProblemBlock],
    displayed_number: int,
    problem_index: int,
    indentation: int,
    exam_id: str,
) -> tuple[list[str], int, int]:
    """Render content while grouping consecutive problems into semantic lists."""
    prefix = " " * indentation
    lines: list[str] = []
    index = 0
    while index < len(blocks):
        block = blocks[index]
        if isinstance(block, InstructionsBlock):
            lines.append(f'{prefix}<div class="instructions">')
            lines.extend(render_html_text(block.text, indentation + 2))
            lines.append(f"{prefix}</div>")
            index += 1
            continue

        start = displayed_number + 1
        lines.append(f'{prefix}<ol class="problems" start="{start}">')
        while index < len(blocks) and isinstance(blocks[index], ProblemBlock):
            problem_block = blocks[index]
            displayed_number += 1
            problem_index += 1
            lines.extend(
                render_html_problem(
                    problem_block.problem,
                    indentation + 2,
                    exam_id,
                    problem_index,
                )
            )
            index += 1
        lines.append(f"{prefix}</ol>")
    return lines, displayed_number, problem_index


def render_html(exam: ExamRecord) -> str:
    title = exam_title(exam)
    escaped_title = escape(title)
    lines = [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        f"  <title>{escaped_title}</title>",
        f'  <link rel="stylesheet" href="{COMPUTER_MODERN_CSS}">',
        f'  <script defer src="{MATHJAX_SCRIPT}"></script>',
        "  <style>",
        "    * { box-sizing: border-box; }",
        "    html { color-scheme: light; background: #fff; }",
        "    body {",
        "      margin: 0;",
        "      color: #191918;",
        '      font-family: "CMU Serif", Georgia, serif;',
        "      font-size: 1.125rem;",
        "      font-weight: 500;",
        "      line-height: 1.58;",
        "    }",
        "    main {",
        "      width: 100%;",
        "      max-width: 48rem;",
        "      margin: 0 auto;",
        "      padding: 3.5rem 2rem 4rem;",
        "    }",
        "    .exam-header {",
        "      margin-bottom: 2.25rem;",
        "      padding-bottom: 1.1rem;",
        "      border-bottom: 2px solid #242421;",
        "    }",
        "    .institution {",
        "      margin: 0 0 .35rem;",
        "      font-size: 1rem;",
        "      font-weight: 700;",
        "    }",
        "    h1, h2 { line-height: 1.18; }",
        "    h1 { margin: 0; font-size: 2.15rem; font-weight: 700; }",
        "    h2 {",
        "      margin: 2.8rem 0 1.25rem;",
        "      padding-bottom: .35rem;",
        "      border-bottom: 1px solid #b8b8b2;",
        "      font-size: 1.4rem;",
        "      font-weight: 700;",
        "    }",
        "    p { margin: 0 0 .8rem; }",
        "    .instructions {",
        "      margin: 1.4rem 0 1.8rem;",
        "      font-style: italic;",
        "    }",
        "    .instructions > :last-child { margin-bottom: 0; }",
        "    .problems { margin: 0; padding-left: 2.4rem; }",
        "    .problem { margin: 0 0 1.65rem; padding-left: .35rem; }",
        "    .problem::marker { font-weight: 700; }",
        "    .problem-concern {",
        "      margin: 0 0 .8rem;",
        "      color: #7a1f1f;",
        "    }",
        "    .problem-concern > :last-child { margin-bottom: 0; }",
        "    .problem > p:first-child, .subpart-body > p:first-child { margin-top: 0; }",
        "    .problem-figure { margin: 1rem 0; }",
        "    .problem-figure img {",
        "      display: block;",
        "      width: auto;",
        "      height: auto;",
        "      max-width: 80%;",
        "      max-height: 6lh;",
        "      margin: 0 auto;",
        "      object-fit: contain;",
        "    }",
        "    .subparts { margin: .7rem 0 0; padding: 0; list-style: none; }",
        "    .subparts .subparts { margin-left: 2.2rem; }",
        "    .subparts > li { margin: .55rem 0; }",
        "    .subpart-row {",
        "      display: grid;",
        "      grid-template-columns: max-content minmax(0, 1fr);",
        "      gap: .5rem;",
        "      align-items: start;",
        "    }",
        "    .subpart-label { font-weight: 700; }",
        "    .subpart-body > :last-child { margin-bottom: 0; }",
        "    .display-math {",
        "      max-width: 100%;",
        "      margin: .8rem 0 1rem;",
        "      overflow-x: auto;",
        "      overflow-y: hidden;",
        "      font-style: normal;",
        "    }",
        "    mjx-container { font-style: normal; }",
        '    mjx-container[display="true"] { margin: .3rem 0 !important; min-width: max-content; }',
        "    footer {",
        "      margin-top: 3.25rem;",
        "      padding-top: 1rem;",
        "      border-top: 1px solid #b8b8b2;",
        "      font-size: 1rem;",
        "    }",
        "    footer ul {",
        "      display: flex;",
        "      flex-wrap: wrap;",
        "      gap: .5rem 1.25rem;",
        "      margin: 0;",
        "      padding: 0;",
        "      list-style: none;",
        "    }",
        "    .page-updated { margin: .65rem 0 0; color: #5f5f5a; font-size: .9rem; }",
        "    a { color: #174f78; text-decoration-thickness: .08em; text-underline-offset: .15em; }",
        "    a:hover { color: #8a321d; }",
        "    a:focus-visible { outline: 3px solid #d28b18; outline-offset: 3px; }",
        "    @media (max-width: 40rem) {",
        "      body { font-size: 1.05rem; }",
        "      main { padding: 2rem 1.15rem 3rem; }",
        "      h1 { font-size: 1.8rem; }",
        "      .problems { padding-left: 2rem; }",
        "      .subparts .subparts { margin-left: 1.25rem; }",
        "    }",
        "    @media print {",
        "      @page { margin: .5in .55in; }",
        "      body { font-size: 11pt; line-height: 1.28; color: #000; }",
        "      main { max-width: none; padding: 0; }",
        "      .exam-header {",
        "        margin-bottom: .6rem;",
        "        padding-bottom: .35rem;",
        "        border-bottom-width: 1px;",
        "      }",
        "      .institution { margin-bottom: .2rem; font-size: 9pt; }",
        "      .institution a { text-decoration: none; }",
        "      h1 { font-size: 17pt; line-height: 1.08; }",
        "      h2 {",
        "        margin: .85rem 0 .4rem;",
        "        padding-bottom: .12rem;",
        "        font-size: 12pt;",
        "        line-height: 1.1;",
        "        break-after: avoid;",
        "      }",
        "      p { margin-bottom: .25rem; }",
        "      .instructions { margin: .4rem 0 .55rem; }",
        "      .problems { padding-left: 1.75rem; }",
        "      .problem { margin-bottom: .55rem; padding-left: .1rem; }",
        "      .problem-concern { margin: 0 0 .3rem; color: #651818; break-after: avoid; }",
        "      .problem-figure { margin: .3rem 0; break-inside: avoid; }",
        "      .subparts { margin-top: .18rem; }",
        "      .subparts .subparts { margin-left: 1.4rem; }",
        "      .subparts > li { margin: .12rem 0; }",
        "      .subpart-row { gap: .3rem; break-inside: avoid; }",
        "      .display-math { margin: .15rem 0 .25rem; overflow: visible; }",
        '      mjx-container[display="true"] { margin: 0 !important; }',
        "      a { color: inherit; }",
        "      footer { display: none; }",
        "    }",
        "  </style>",
        "</head>",
        "<body>",
        '  <main id="main-content">',
        '    <header class="exam-header">',
        '      <p class="institution"><a href="https://www.ufl.edu/">University of Florida</a>, '
        '<a href="https://math.ufl.edu/">Department of Mathematics</a></p>',
        f"      <h1>{escaped_title}</h1>",
        "    </header>",
    ]

    displayed_number = 0
    problem_index = 0
    pending_blocks: list[InstructionsBlock | ProblemBlock] = []

    def flush_pending() -> None:
        nonlocal displayed_number, problem_index
        if not pending_blocks:
            return
        rendered, displayed_number, problem_index = render_html_blocks(
            pending_blocks, displayed_number, problem_index, 4, exam.id
        )
        lines.extend(rendered)
        pending_blocks.clear()

    section_index = 0
    for block in exam.content:
        if not isinstance(block, SectionBlock):
            pending_blocks.append(block)
            continue
        flush_pending()
        section_index += 1
        heading_id = f"section-{section_index}"
        lines.append(f'    <section aria-labelledby="{heading_id}">')
        lines.append(f'      <h2 id="{heading_id}">{escape(block.heading.strip())}</h2>')
        if block.numbering == NumberingMode.RESTART:
            displayed_number = 0
        rendered, displayed_number, problem_index = render_html_blocks(
            block.content, displayed_number, problem_index, 6, exam.id
        )
        lines.extend(rendered)
        lines.append("    </section>")
    flush_pending()

    archive_title = subject_archive_title(exam.subject, exam.subject_tag)
    lines.extend(
        [
            "    <footer>",
            "      <ul>",
            f'        <li><a href="{PROJECT_SOURCE_URL}">Project source</a></li>',
            '        <li><a href="../../../index.html">All exam subjects</a></li>',
            f'        <li><a href="../index.html">{escape(archive_title)}</a></li>',
            f'        <li><a href="{escape(exam.id)}.source.pdf">Original PDF</a></li>',
            "      </ul>",
            f'      <p class="page-updated">Page updated <time datetime="{PAGE_UPDATED_ISO}">{PAGE_UPDATED_LABEL}</time>.</p>',
            "    </footer>",
            "  </main>",
            "</body>",
            "</html>",
        ]
    )
    return "\n".join(lines) + "\n"


def regenerate_presentations(sources: dict[str, SourceExam]) -> int:
    """Regenerate HTML from canonical JSON without model calls."""
    failures: list[str] = []
    rendered = 0
    for exam_id in sorted(sources):
        source = sources[exam_id]
        json_path = exam_json_path(source)
        if not json_path.is_file():
            failures.append(f"{exam_id}: canonical JSON is missing")
            continue
        try:
            exam = ExamRecord.model_validate_json(json_path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            failures.append(f"{exam_id}: {error}")
            continue
        errors = validate_exam(exam, source, [])
        if errors:
            failures.append(f"{exam_id}: {'; '.join(errors)}")
            continue
        write_text(exam_html_path(source), render_html(exam))
        rendered += 1
    if failures:
        raise RuntimeError("presentation regeneration failed:\n" + "\n".join(failures))
    return rendered


def extract_one(
    source: SourceExam,
    build_root: Path,
    model: str,
    reasoning: str,
    dpi: int,
    force: bool,
    include_native_text: bool = True,
) -> tuple[ExamRecord, list[ReviewFlag], bool]:
    source_hash = sha256_file(source.pdf_path)
    if source_hash != source.sha256:
        raise RuntimeError(f"source hash does not match manifest for {source.id}")
    output_path = exam_json_path(source)
    html_path = exam_html_path(source)
    saved_path = checkpoint_path(source, build_root)
    if output_path.exists() and saved_path.exists() and not force:
        checkpoint = json.loads(saved_path.read_text(encoding="utf-8"))
        if checkpoint.get("source_sha256") != source_hash:
            history = checkpoint.setdefault("source_sha256_history", [])
            previous_hash = checkpoint.get("source_sha256")
            if previous_hash and previous_hash not in history:
                history.append(previous_hash)
            checkpoint["source_sha256"] = source_hash
            checkpoint["source_download_sha256"] = source.download_sha256
            checkpoint["source_metadata_refreshed_at"] = datetime.now(timezone.utc).isoformat()
            write_json(saved_path, checkpoint)
        exam = ExamRecord.model_validate_json(output_path.read_text(encoding="utf-8"))
        flags = [ReviewFlag.model_validate(item) for item in checkpoint["review_flags"]]
        errors = validate_exam(exam, source, flags)
        if errors:
            raise RuntimeError(f"cached extraction invalid for {source.id}: {'; '.join(errors)}")
        write_text(html_path, render_html(exam))
        return exam, flags, True
    if saved_path.exists() and not force:
        checkpoint = json.loads(saved_path.read_text(encoding="utf-8"))
        if (
            checkpoint.get("source_sha256") == source_hash
            and checkpoint.get("model_extraction") is not None
        ):
            extraction = ModelExtraction.model_validate(checkpoint["model_extraction"])
            exam = build_exam(source, extraction)
            errors = validate_exam(exam, source, extraction.review_flags)
            if not errors:
                checkpoint["review_flags"] = [
                    item.model_dump(mode="json") for item in extraction.review_flags
                ]
                checkpoint["validation_errors"] = []
                checkpoint["revalidated_at"] = datetime.now(timezone.utc).isoformat()
                write_json(saved_path, checkpoint)
                write_json(output_path, exam)
                write_text(html_path, render_html(exam))
                return exam, extraction.review_flags, True
    if force:
        archive_files(
            [output_path, html_path, saved_path],
            build_root / source.id / "history",
        )

    workdir = build_root / source.id
    pages = render_pages(source, workdir, dpi)
    client = OpenAI()
    extraction, response_id, usage = call_model(
        client,
        source,
        pages,
        model=model,
        reasoning=reasoning,
        include_native_text=include_native_text,
    )
    repair_response_id = None
    repair_usage = None
    if has_ascii_control_characters(extraction):
        extraction, repair_response_id, repair_usage = repair_control_characters(
            client,
            extraction,
            model=model,
            reasoning=reasoning,
        )
    exam = build_exam(source, extraction)
    errors = validate_exam(exam, source, extraction.review_flags)
    checkpoint = {
        "schema_version": 3,
        "prompt_version": PROMPT_VERSION,
        "evidence_version": (
            NATIVE_EVIDENCE_VERSION
            if include_native_text
            else VISION_ONLY_EVIDENCE_VERSION
        ),
        "source_pdf": str(source.pdf_path),
        "source_sha256": source_hash,
        "source_download_sha256": source.download_sha256,
        "model": model,
        "reasoning_effort": reasoning,
        "response_id": response_id,
        "usage": usage,
        "control_repair_response_id": repair_response_id,
        "control_repair_usage": repair_usage,
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "review_flags": [item.model_dump(mode="json") for item in extraction.review_flags],
        "validation_errors": errors,
        "model_extraction": extraction.model_dump(mode="json"),
    }
    write_json(saved_path, checkpoint)
    if errors:
        raise RuntimeError(f"extraction invalid for {source.id}: {'; '.join(errors)}")
    write_json(output_path, exam)
    write_text(html_path, render_html(exam))
    return exam, extraction.review_flags, False


REVIEW_FILES = {
    "corrections": (
        "review-corrections.json",
        "Every uniquely determined source correction made during extraction.",
    ),
    "transformations": (
        "review-transformations.json",
        "Completed normalization of unsupported labels and dependent instruction references.",
    ),
    "serious": (
        "review-serious.json",
        "Unresolved cases that require human review before publication.",
    ),
}


def review_bucket(category: ReviewCategory) -> str:
    if category == ReviewCategory.CORRECTION:
        return "corrections"
    if category in {
        ReviewCategory.NUMBERING_TRANSFORMATION,
        ReviewCategory.INSTRUCTION_REWRITE,
    }:
        return "transformations"
    return "serious"


def review_records(
    source: SourceExam, flags: list[ReviewFlag], bucket: str
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for flag in flags:
        if review_bucket(flag.category) != bucket:
            continue
        records.append(
            {
                "exam_id": source.id,
                "problem_indices": flag.problem_indices,
                "category": flag.category.value,
                "source_pdf": str(source.pdf_path),
                "source_pages": flag.source_pages,
                "message": flag.message,
                "original_text": flag.original_text,
                "corrected_text": flag.corrected_text,
                "context": flag.context,
                "origin": "extraction",
                "status": "open" if bucket == "serious" else "logged",
            }
        )
    return records


def update_review_files(
    directory: Path, completed: dict[str, tuple[SourceExam, list[ReviewFlag]]]
) -> None:
    for bucket, (filename, purpose) in REVIEW_FILES.items():
        path = directory / filename
        existing: list[dict[str, object]] = []
        if path.exists():
            raw = json.loads(path.read_text(encoding="utf-8"))
            existing = raw.get("items", [])
        replaced_ids = set(completed)
        retained = [
            item
            for item in existing
            if item.get("exam_id") not in replaced_ids
            or item.get("origin") == "project"
        ]
        new_items = [
            item
            for exam_id in sorted(completed)
            for item in review_records(*completed[exam_id], bucket)
        ]
        write_json(
            path,
            {
                "schema_version": 2,
                "review_type": bucket,
                "purpose": purpose,
                "items": retained + new_items,
            },
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract structured exam JSON with Sol vision")
    parser.add_argument("exam_ids", nargs="*")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--pilot", action="store_true", help="extract the five pilot exams")
    selection.add_argument(
        "--all",
        action="store_true",
        dest="all_exams",
        help="extract every exam without a canonical JSON record",
    )
    selection.add_argument(
        "--render-all",
        action="store_true",
        help="regenerate every HTML presentation without model calls",
    )
    selection.add_argument(
        "--subject",
        action="append",
        dest="subject_tags",
        metavar="TAG",
        help="extract missing exams for a subject tag; repeat for multiple subjects",
    )
    selection.add_argument(
        "--affected",
        nargs="?",
        const=Path("build/schema-v2/affected-exams.json"),
        type=Path,
        metavar="FILE",
        help="extract IDs from the schema-migration affected list",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="limit a --all or --subject selection after completed records are skipped",
    )
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument("--review-dir", type=Path, default=Path("exams"))
    parser.add_argument("--build-root", type=Path, default=Path("build/extraction"))
    parser.add_argument("--model", default=os.getenv("OPENAI_EXTRACTION_MODEL", DEFAULT_MODEL))
    parser.add_argument("--reasoning", choices=["low", "medium", "high"], default="high")
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--vision-only",
        action="store_true",
        help="omit native PDF text evidence and use rendered page images only",
    )
    parser.add_argument(
        "--skip-current",
        action="store_true",
        help="skip records with a valid checkpoint from the current prompt",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.workers < 1:
        raise SystemExit("--workers must be at least 1")
    if args.dpi < 100:
        raise SystemExit("--dpi must be at least 100")
    sources = load_sources(args.manifest)
    if args.render_all:
        if args.exam_ids:
            raise SystemExit("exam IDs cannot be combined with --render-all")
        count = regenerate_presentations(sources)
        print(f"rendered={count}")
        return 0
    exam_ids = args.exam_ids
    if args.affected is not None:
        if exam_ids:
            raise SystemExit("exam IDs cannot be combined with --affected")
        affected_document = json.loads(args.affected.read_text(encoding="utf-8"))
        exam_ids = affected_document["exam_ids"]
    if args.skip_current and args.affected is None:
        raise SystemExit("--skip-current requires --affected")
    if args.skip_current:
        before = len(exam_ids)
        exam_ids = [
            exam_id
            for exam_id in exam_ids
            if not has_current_extraction(sources[exam_id], args.build_root)
        ]
        print(f"skipped_current={before - len(exam_ids)}")
    try:
        selection = select_exam_ids(
            sources,
            exam_ids,
            pilot=args.pilot,
            all_exams=args.all_exams,
            subject_tags=args.subject_tags,
            limit=args.limit,
            force=args.force,
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    requested = selection.ids
    if args.all_exams or args.subject_tags:
        print(
            f"selected={len(requested)} "
            f"skipped_completed={selection.skipped_completed} "
            f"deferred_by_limit={selection.deferred_by_limit}"
        )
    if not requested:
        print("No exams selected.")
        return 0

    completed: dict[str, tuple[SourceExam, list[ReviewFlag]]] = {}
    failures: dict[str, str] = {}
    extracted_count = 0
    cached_count = 0
    review_flag_count = 0
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                extract_one,
                sources[exam_id],
                args.build_root,
                args.model,
                args.reasoning,
                args.dpi,
                args.force,
                not args.vision_only,
            ): exam_id
            for exam_id in requested
        }
        for future in as_completed(futures):
            exam_id = futures[future]
            try:
                exam, flags, cached = future.result()
            except Exception as error:  # Continue the run so failures can be retried.
                failures[exam_id] = str(error)
                print(f"failed: {exam_id}: {error}")
                continue

            completed[exam_id] = (sources[exam_id], flags)
            update_review_files(
                args.review_dir,
                {exam_id: completed[exam_id]},
            )
            state = "cached" if cached else "extracted"
            if cached:
                cached_count += 1
            else:
                extracted_count += 1
            review_flag_count += len(flags)
            print(
                f"{state}: {exam.id} ({len(list(iter_problems(exam)))} problems, "
                f"{len(flags)} review flags)"
            )

    print(
        f"completed={len(completed)} extracted={extracted_count} cached={cached_count} "
        f"failed={len(failures)} review_flags={review_flag_count}"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
