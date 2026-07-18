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
import json
import os
from pathlib import Path
import re
import shutil
from typing import Iterator

from openai import OpenAI
import pymupdf
from pydantic import BaseModel, Field


DEFAULT_MODEL = "gpt-5.6-sol"
PROMPT_VERSION = "exam-extraction-v5"
PILOT_IDS = [
    "algebra-first-year-2025-may-part-1",
    "topology-first-year-2025-may-part-2",
    "logic-phd-2006-aug",
    "numerical-analysis-phd-2025-aug",
    "topology-phd-2025-may",
]


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


class Subpart(BaseModel):
    label: str = Field(description="Original displayed label, such as (a), A., 1., or i.")
    text: str = Field(description="Subpart text without its label, using MathJax TeX delimiters")
    subparts: list[Subpart] = Field(
        description="Nested labeled parts in source order; empty when there are none"
    )


class Problem(BaseModel):
    number: int = Field(ge=1, description="Final top-level problem number")
    text: str = Field(description="Problem stem without top-level number or subpart text")
    subparts: list[Subpart] = Field(
        description="Labeled parts in source order; empty when there are none"
    )


class ReviewFlag(BaseModel):
    category: ReviewCategory
    problem_numbers: list[int]
    source_pages: list[int]
    message: str
    original_text: str | None
    corrected_text: str | None
    context: str | None


class ModelExtraction(BaseModel):
    instructions: str | None
    problems: list[Problem]
    review_flags: list[ReviewFlag]


class ExamRecord(BaseModel):
    schema_version: int = 1
    id: str
    subject: str
    subject_tag: str
    year: int
    month: str
    part: int | None
    pdf_url: str
    instructions: str | None
    problems: list[Problem]


@dataclass(frozen=True)
class SourceExam:
    id: str
    subject: str
    subject_tag: str
    year: int
    month: str
    part: int | None
    pdf_url: str
    pdf_path: Path
    sha256: str
    download_sha256: str


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

INSTRUCTIONS
Return at most one coherent instructions string. Preserve selection rules, required problem
groups, expected proof/detail level, allowed methods or materials, and notation applying to the
whole exam. If point values are the only signal that problem groups require different response
depth, express the distinction without scores. Keep the instructions consistent with final
problem numbers. If you materially combine distinct instruction blocks or rewrite instructions to
match transformed problem numbers, add an instruction-rewrite review flag describing the completed
change. Preserve the source wording and sentence-level detail as closely as possible. Make only the
minimum edits needed to join instruction blocks, remove excluded logistics, or replace references
after problem renumbering. Do not shorten, summarize, stylistically improve, or generalize authored
instructions. Do not use the instruction-rewrite category merely for removing excluded logistics.

PROBLEMS
Do not paraphrase, summarize, modernize, solve, or add to a problem. Join visual line wraps and
remove line-break hyphenation. Preserve ordinary top-level numbering. Put only the problem stem in
its text field. Put each labeled part in the subparts array, preserve its label exactly in label,
and do not repeat that label in text. Recurse for nested labeled parts. Use an empty subparts array
when none exist.

If one linked PDF restarts top-level numbering under internal parts or sections, replace the
restarted labels with one consecutive global sequence beginning at 1. Do not create a section or
internal-part field. Explain the final problem ranges and their source parts or topics in the single
instructions string, keep all selection rules consistent with the new numbers, and add a numbering
transformation review flag describing the completed change. State the requirements directly in
terms of the final problem numbers. Do not say that final problems merely "correspond to" source
parts when the source part names are not needed to understand what the student must do.

MATHEMATICS
Use Unicode for prose and MathJax-compatible TeX for mathematics. Use \(...\) for inline math and
\[...\] for display math. Do not use dollar-sign delimiters. Preserve notation and mathematical
meaning exactly.

CORRECTIONS
Preserve the source reading unless the intended correction is uniquely determined by the immediate
mathematical context. Every correction, however obvious, requires a correction review flag with the
original text, corrected text, immediate context, problem number, and source page. If a correction
is not uniquely determined, retain the source reading and add a transcription review flag.

SERIOUS REVIEW
If a figure, diagram, graph, or table carries information, transcribe the surrounding words but do
not invent or reconstruct the visual. Add a visual-content flag. Flag shared notation or material
that applies only to some problems and cannot fit coherently in the single instructions string.
Flag cross-problem references, uncertain words or math, unclear numbering, and instructions that
may no longer agree with numbering. Findings do not stop extraction. Return null for correction-only
fields when they do not apply."""


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


def archive(path: Path) -> None:
    if not path.exists():
        return
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    shutil.move(path, path.with_name(f"{path.stem}.{timestamp}{path.suffix}"))


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
        exam_id = pdf_path.stem
        source = SourceExam(
            id=exam_id,
            subject=item["subject"],
            subject_tag=item["subject_tag"],
            year=item["year"],
            month=item["month"],
            part=part_from_manifest(item),
            pdf_url=item["download_url"],
            pdf_path=pdf_path,
            sha256=item["sha256"],
            download_sha256=item.get("download_sha256", item["sha256"]),
        )
        if exam_id in sources:
            raise RuntimeError(f"duplicate exam identifier in manifest: {exam_id}")
        sources[exam_id] = source
    return sources


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
                    "native_text": page.get_text("text").strip(),
                }
            )
    return rendered


def extraction_prompt(source: SourceExam, pages: list[dict[str, object]]) -> str:
    native = "\n\n".join(
        f"PAGE {page['page_number']} NATIVE TEXT (untrusted evidence):\n"
        + (str(page["native_text"]) or "(none)")
        for page in pages
    )
    logic_policy = ""
    if source.subject_tag == "logic-phd":
        logic_policy = r"""

LOGIC POLICY
The source may restart numbering inside named topics or use labels such as 1A, 1B, and 2A.
Replace those top-level labels with one consecutive global sequence beginning at 1. Do not return
a section field. Add a concise sentence to instructions mapping final problem ranges to the source
topic names, such as 'Problems 1-3 concern General Logic.' Derive ranges from the final problems.
Add a numbering-transformation review flag. Preserve any original labels belonging to true
subparts inside their subpart label fields."""
    part_text = str(source.part) if source.part is not None else "none"
    return f"""CATALOG METADATA (authoritative; do not infer from PDF):
Subject: {source.subject}
Subject tag: {source.subject_tag}
Year: {source.year}
Month: {source.month}
Part: {part_text}
Current PDF URL: {source.pdf_url}
Source pages: {len(pages)}
{logic_policy}

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
    content.append({"type": "input_text", "text": extraction_prompt(source, pages)})
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


def walk_subparts(subparts: list[Subpart]) -> Iterator[Subpart]:
    for subpart in subparts:
        yield subpart
        yield from walk_subparts(subpart.subparts)


def all_content(exam: ExamRecord) -> Iterator[str]:
    if exam.instructions:
        yield exam.instructions
    for problem in exam.problems:
        yield problem.text
        for subpart in walk_subparts(problem.subparts):
            yield subpart.text


def validate_exam(exam: ExamRecord, source: SourceExam, flags: list[ReviewFlag]) -> list[str]:
    errors: list[str] = []
    if exam.id != source.id:
        errors.append("identifier does not match source")
    if exam.subject != source.subject or exam.subject_tag != source.subject_tag:
        errors.append("subject metadata does not match source")
    if (exam.year, exam.month, exam.part) != (source.year, source.month, source.part):
        errors.append("date or part metadata does not match source")
    if exam.pdf_url != source.pdf_url:
        errors.append("PDF URL does not match current manifest URL")
    if not exam.problems and not (exam.instructions or "").strip():
        errors.append("record contains neither problems nor a notice")
    numbers = [problem.number for problem in exam.problems]
    if len(numbers) != len(set(numbers)):
        errors.append("top-level problem numbers are not unique")
    expected_numbers = list(range(1, len(numbers) + 1))
    if source.subject_tag == "logic-phd":
        if numbers != expected_numbers:
            errors.append("logic problem numbers are not globally sequential")
        ranges = re.findall(
            r"Problems?\s+(\d+)(?:\s*[\N{EN DASH}-]\s*(\d+))?\s+concern\s+([^.;]+)",
            exam.instructions or "",
            re.IGNORECASE,
        )
        covered = [
            number
            for start, end, _topic in ranges
            for number in range(int(start), int(end or start) + 1)
        ]
        if covered != expected_numbers:
            errors.append("logic instructions do not map every final problem to a topic")
    elif numbers != expected_numbers and not any(
        flag.category == ReviewCategory.NUMBERING for flag in flags
    ):
        errors.append("nonsequential problem numbers lack a numbering review flag")
    for problem in exam.problems:
        if not problem.text.strip() and not problem.subparts:
            errors.append(f"problem {problem.number} has no content")
        for subpart in walk_subparts(problem.subparts):
            if not subpart.label.strip():
                errors.append(f"problem {problem.number} has an empty subpart label")
            if not subpart.text.strip() and not subpart.subparts:
                errors.append(f"problem {problem.number} has an empty subpart")
    for text in all_content(exam):
        if text.count(r"\(") != text.count(r"\)"):
            errors.append("unbalanced inline MathJax delimiters")
        if text.count(r"\[") != text.count(r"\]"):
            errors.append("unbalanced display MathJax delimiters")
        if "$" in text:
            errors.append("dollar-sign math delimiters are not allowed")
    for flag in flags:
        if any(number not in numbers for number in flag.problem_numbers):
            errors.append("review flag refers to an unknown problem number")
        if flag.category == ReviewCategory.CORRECTION and not all(
            [flag.original_text, flag.corrected_text, flag.context]
        ):
            errors.append("correction flag lacks original, corrected, or context text")
    return list(dict.fromkeys(errors))


def exam_json_path(source: SourceExam) -> Path:
    return source.pdf_path.with_suffix(".json")


def exam_markdown_path(source: SourceExam) -> Path:
    return source.pdf_path.with_suffix(".md")


def checkpoint_path(source: SourceExam, build_root: Path) -> Path:
    return build_root / source.id / "extraction.json"


def build_exam(source: SourceExam, extraction: ModelExtraction) -> ExamRecord:
    return ExamRecord(
        id=source.id,
        subject=source.subject,
        subject_tag=source.subject_tag,
        year=source.year,
        month=source.month,
        part=source.part,
        pdf_url=source.pdf_url,
        instructions=extraction.instructions,
        problems=extraction.problems,
    )


def render_subparts(subparts: list[Subpart], depth: int = 0) -> list[str]:
    lines: list[str] = []
    for subpart in subparts:
        indentation = "    " * depth
        continuation = " " * (len(indentation) + 2)
        text_lines = subpart.text.strip().splitlines()
        if text_lines and text_lines[0] != r"\[":
            lines.append(f"{indentation}* {subpart.label} {text_lines[0]}")
            lines.extend(
                continuation + line if line else "" for line in text_lines[1:]
            )
        else:
            lines.append(f"{indentation}* {subpart.label}")
            lines.extend(continuation + line if line else "" for line in text_lines)
        lines.extend(render_subparts(subpart.subparts, depth + 1))
    return lines


def render_markdown(exam: ExamRecord) -> str:
    if exam.subject.startswith("First Year "):
        title = f"{exam.subject.removeprefix('First Year ')}, first year exam"
    elif exam.subject.startswith("PhD "):
        title = f"{exam.subject.removeprefix('PhD ')}, PhD exam"
    else:
        title = f"{exam.subject} exam"
    title += f", {exam.month.title()} {exam.year}"
    if exam.part is not None:
        title += f", Part {exam.part}"
    lines = [f"# {title}", ""]
    if exam.instructions:
        lines.extend([f"*{exam.instructions.strip()}*", ""])
    for problem in exam.problems:
        text_lines = problem.text.strip().splitlines()
        if text_lines:
            if text_lines[0] != r"\[":
                lines.append(f"**{problem.number}.** {text_lines[0]}")
                lines.extend(text_lines[1:])
            else:
                lines.append(f"**{problem.number}.**")
                lines.extend(text_lines)
        elif problem.subparts:
            noun = "part" if len(problem.subparts) == 1 else "parts"
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
            lines.append(
                f"**{problem.number}.** This problem has {count} {noun}."
            )
        else:
            lines.append(f"**{problem.number}.**")
            lines.extend(text_lines)
        lines.extend(render_subparts(problem.subparts))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def extract_one(
    source: SourceExam,
    build_root: Path,
    model: str,
    reasoning: str,
    dpi: int,
    force: bool,
) -> tuple[ExamRecord, list[ReviewFlag], bool]:
    source_hash = sha256_file(source.pdf_path)
    if source_hash != source.sha256:
        raise RuntimeError(f"source hash does not match manifest for {source.id}")
    output_path = exam_json_path(source)
    rendered_path = exam_markdown_path(source)
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
        write_text(rendered_path, render_markdown(exam))
        return exam, flags, True
    if force:
        archive(output_path)
        archive(rendered_path)
        archive(saved_path)

    workdir = build_root / source.id
    pages = render_pages(source, workdir, dpi)
    extraction, response_id, usage = call_model(
        OpenAI(), source, pages, model=model, reasoning=reasoning
    )
    exam = build_exam(source, extraction)
    errors = validate_exam(exam, source, extraction.review_flags)
    checkpoint = {
        "schema_version": 1,
        "prompt_version": PROMPT_VERSION,
        "source_pdf": str(source.pdf_path),
        "source_sha256": source_hash,
        "source_download_sha256": source.download_sha256,
        "model": model,
        "reasoning_effort": reasoning,
        "response_id": response_id,
        "usage": usage,
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "review_flags": [item.model_dump(mode="json") for item in extraction.review_flags],
        "validation_errors": errors,
        "model_extraction": extraction.model_dump(mode="json"),
    }
    write_json(saved_path, checkpoint)
    if errors:
        raise RuntimeError(f"extraction invalid for {source.id}: {'; '.join(errors)}")
    write_json(output_path, exam)
    write_text(rendered_path, render_markdown(exam))
    return exam, extraction.review_flags, False


REVIEW_FILES = {
    "corrections": (
        "review-corrections.json",
        "Every uniquely determined source correction made during extraction.",
    ),
    "transformations": (
        "review-transformations.json",
        "Completed structural transformations such as renumbering and instruction consolidation.",
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
                "problem_numbers": flag.problem_numbers,
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
                "schema_version": 1,
                "review_type": bucket,
                "purpose": purpose,
                "items": retained + new_items,
            },
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract structured exam JSON with Sol vision")
    parser.add_argument("exam_ids", nargs="*")
    parser.add_argument("--pilot", action="store_true", help="extract the five pilot exams")
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument("--review-dir", type=Path, default=Path("exams"))
    parser.add_argument("--build-root", type=Path, default=Path("build/extraction"))
    parser.add_argument("--model", default=os.getenv("OPENAI_EXTRACTION_MODEL", DEFAULT_MODEL))
    parser.add_argument("--reasoning", choices=["low", "medium", "high"], default="high")
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--force", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.pilot and args.exam_ids:
        raise SystemExit("use either --pilot or explicit exam IDs, not both")
    requested = PILOT_IDS if args.pilot else args.exam_ids
    if not requested:
        raise SystemExit("provide exam IDs or use --pilot")
    if args.workers < 1:
        raise SystemExit("--workers must be at least 1")
    if args.dpi < 100:
        raise SystemExit("--dpi must be at least 100")
    sources = load_sources(args.manifest)
    missing = [exam_id for exam_id in requested if exam_id not in sources]
    if missing:
        raise SystemExit("exam IDs not found in manifest: " + ", ".join(missing))

    completed: dict[str, tuple[SourceExam, list[ReviewFlag]]] = {}
    failures: dict[str, str] = {}
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
            ): exam_id
            for exam_id in requested
        }
        for future in as_completed(futures):
            exam_id = futures[future]
            try:
                exam, flags, cached = future.result()
                completed[exam_id] = (sources[exam_id], flags)
                state = "cached" if cached else "extracted"
                print(
                    f"{state}: {exam.id} ({len(exam.problems)} problems, "
                    f"{len(flags)} review flags)"
                )
            except Exception as error:  # Continue the pilot so failures can be compared.
                failures[exam_id] = str(error)
                print(f"failed: {exam_id}: {error}")

    if completed:
        update_review_files(args.review_dir, completed)
    print(f"completed={len(completed)} failed={len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
