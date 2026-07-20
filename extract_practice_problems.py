#!/usr/bin/env python3
"""Extract a large numbered practice-problem collection in resumable page chunks."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Literal

from openai import OpenAI
from pydantic import Field

from extract_exams import (
    DEFAULT_MODEL,
    DocumentType,
    ExamRecord,
    Problem,
    ProblemBlock,
    ProblemTextBlock,
    ReviewCategory,
    ReviewFlag,
    SourceExam,
    StrictModel,
    exam_html_path,
    exam_json_path,
    has_ascii_control_characters,
    load_sources,
    render_html,
    render_pages,
    sha256_file,
    update_review_files,
    validate_exam,
    write_json,
    write_text,
)


PROMPT_VERSION = "practice-problem-chunks-v1"
DEFAULT_ID = "algebra-first-year-practice-problems"


@dataclass(frozen=True)
class ChunkSpec:
    key: str
    pages: tuple[int, ...]
    first_problem: int
    last_problem: int


CHUNKS = (
    ChunkSpec("page-01", (1,), 1, 14),
    ChunkSpec("page-02", (2,), 15, 29),
    ChunkSpec("pages-03-04", (3, 4), 30, 55),
    ChunkSpec("page-05", (5,), 56, 66),
    ChunkSpec("page-06", (6,), 67, 77),
    ChunkSpec("page-07", (7,), 78, 88),
    ChunkSpec("page-08", (8,), 89, 98),
    ChunkSpec("page-09", (9,), 99, 110),
    ChunkSpec("page-10", (10,), 111, 113),
)


class NumberedProblem(StrictModel):
    source_number: int = Field(ge=1)
    problem: Problem


class NumberedReviewFlag(StrictModel):
    category: ReviewCategory
    source_numbers: list[int]
    source_pages: list[int]
    message: str
    original_text: str | None
    corrected_text: str | None
    context: str | None


class ChunkExtraction(StrictModel):
    problems: list[NumberedProblem]
    review_flags: list[NumberedReviewFlag]


SYSTEM_PROMPT = r"""You extract useful mathematical content from a numbered graduate algebra
practice-problem collection. This is not archival OCR. Preserve each question, its mathematical
meaning, and its wording. Do not paraphrase, summarize, modernize, solve, or add to a problem.

CONTENT AND STRUCTURE
Omit the document title, page numbers, headers, footers, and layout. Join visual line wraps and
remove line-break hyphenation. Store each printed top-level problem number only in source_number;
never repeat it in the problem text. Put the stem in one text block in body. Put every labeled part
in subparts, preserve its displayed label exactly, and do not repeat that label in its text. Recurse
for nested parts. Use an empty body when a problem begins immediately with subparts. Never create a
TikZ block.

The supplied pages form one extraction chunk. Consolidate a problem that wraps between supplied
pages into one complete record. Return exactly the requested consecutive source-number range, with
no gaps or duplicates. Do not include a problem outside that range.

MATHEMATICS
Use Unicode for prose and MathJax-compatible TeX for mathematics. Use \(...\) inline and \[...\]
for displays; never use dollar delimiters. Trust the page image over native text for symbols,
exponents, subscripts, matrices, decorated letters, and other mathematics. Transcribe typeset
matrices and arrays as MathJax rather than treating them as figures.

Use the standard spelling and diacritics for unambiguously identified mathematicians. In an
established name joining different people, use an en dash, as in Hahn–Banach. These controlled name
normalizations do not require a correction flag.

CONCERNS AND REVIEW
When a legible problem appears mathematically false, underdetermined, inconsistent, or missing a
necessary hypothesis, preserve its wording and add a suspected concern to the problem. Do not use a
concern for uncertain transcription.

Preserve the source reading unless a correction is uniquely determined by immediate mathematical
context. Every correction requires a correction review flag with original_text, corrected_text,
context, source_numbers, and source_pages. If the source reading is uncertain, preserve the
best-supported reading and add a transcription flag. Clear cross-problem references are valid and
must not be flagged merely because they exist. A visual-content flag is required only when a figure,
diagram, graph, or table carries information that cannot be transcribed completely. Findings do not
stop extraction."""


def chunk_prompt(
    source: SourceExam,
    spec: ChunkSpec,
    pages: list[dict[str, object]],
) -> str:
    native = "\n\n".join(
        f"PAGE {page['page_number']} NATIVE TEXT (untrusted supporting evidence):\n"
        + (str(page["native_text"]) or "(none)")
        for page in pages
    )
    return f"""AUTHORITATIVE COLLECTION METADATA:
Subject: {source.subject}
Document type: practice problems
Current PDF URL: {source.pdf_url}
Primary source pages: {', '.join(str(page) for page in spec.pages)}
Required source problem numbers: {spec.first_problem} through {spec.last_problem}, inclusive

PAGE IMAGES are supplied before this text in page order. Native text may be corrupt or inaccurate
for mathematics. Trust the images when they disagree.

{native}
"""


def call_model(
    source: SourceExam,
    spec: ChunkSpec,
    pages: list[dict[str, object]],
    model: str,
    reasoning: str,
) -> tuple[ChunkExtraction, str | None, dict[str, object] | None]:
    content: list[dict[str, object]] = []
    for page in pages:
        content.extend(
            [
                {
                    "type": "input_text",
                    "text": f"SOURCE PAGE {page['page_number']}",
                },
                {
                    "type": "input_image",
                    "image_url": page["image_data_url"],
                    "detail": "high",
                },
            ]
        )
    content.append(
        {
            "type": "input_text",
            "text": chunk_prompt(source, spec, pages),
        }
    )
    response = OpenAI().responses.parse(
        model=model,
        reasoning={"effort": reasoning},
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content},
        ],
        text_format=ChunkExtraction,
    )
    if response.output_parsed is None:
        raise RuntimeError(f"{spec.key}: model returned no parsed extraction")
    usage = response.usage.model_dump(mode="json") if response.usage else None
    return response.output_parsed, response.id, usage


def validate_chunk(extraction: ChunkExtraction, spec: ChunkSpec) -> list[str]:
    errors: list[str] = []
    expected = list(range(spec.first_problem, spec.last_problem + 1))
    actual = [item.source_number for item in extraction.problems]
    if actual != expected:
        errors.append(f"expected problem numbers {expected}, received {actual}")
    if has_ascii_control_characters(extraction):
        errors.append("content contains an ASCII control character")
    for item in extraction.problems:
        if not item.problem.body and not item.problem.subparts:
            errors.append(f"problem {item.source_number} has no content")
        if any(not isinstance(block, ProblemTextBlock) for block in item.problem.body):
            errors.append(f"problem {item.source_number} contains a non-text body block")
    allowed_numbers = set(expected)
    allowed_pages = set(spec.pages)
    for flag in extraction.review_flags:
        if not set(flag.source_numbers) <= allowed_numbers:
            errors.append(f"review flag refers outside {spec.key}'s problem range")
        if not set(flag.source_pages) <= allowed_pages:
            errors.append(f"review flag refers outside {spec.key}'s page range")
        if flag.category == ReviewCategory.CORRECTION and not all(
            [flag.original_text, flag.corrected_text, flag.context]
        ):
            errors.append("correction flag lacks original, corrected, or context text")
    return list(dict.fromkeys(errors))


def checkpoint_path(build_root: Path, source: SourceExam, spec: ChunkSpec) -> Path:
    return build_root / source.id / "chunks" / f"{spec.key}.json"


def load_checkpoint(
    path: Path,
    source: SourceExam,
    spec: ChunkSpec,
    model: str,
    reasoning: str,
) -> ChunkExtraction | None:
    if not path.is_file():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        extraction = ChunkExtraction.model_validate(value["model_extraction"])
    except (OSError, ValueError, KeyError):
        return None
    if (
        value.get("prompt_version") != PROMPT_VERSION
        or value.get("source_sha256") != source.sha256
        or value.get("model") != model
        or value.get("reasoning_effort") != reasoning
        or value.get("pages") != list(spec.pages)
        or value.get("problem_range") != [spec.first_problem, spec.last_problem]
        or validate_chunk(extraction, spec)
    ):
        return None
    return extraction


def save_checkpoint(
    path: Path,
    source: SourceExam,
    spec: ChunkSpec,
    extraction: ChunkExtraction,
    model: str,
    reasoning: str,
    response_id: str | None,
    usage: dict[str, object] | None,
) -> None:
    write_json(
        path,
        {
            "schema_version": 1,
            "prompt_version": PROMPT_VERSION,
            "source_pdf": str(source.pdf_path),
            "source_sha256": source.sha256,
            "source_download_sha256": source.download_sha256,
            "pages": list(spec.pages),
            "problem_range": [spec.first_problem, spec.last_problem],
            "model": model,
            "reasoning_effort": reasoning,
            "response_id": response_id,
            "usage": usage,
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "validation_errors": [],
            "model_extraction": extraction.model_dump(mode="json"),
        },
    )


def assemble(
    source: SourceExam,
    chunks: dict[str, ChunkExtraction],
) -> tuple[ExamRecord, list[ReviewFlag]]:
    numbered = [
        problem
        for spec in CHUNKS
        for problem in chunks[spec.key].problems
    ]
    expected = list(range(1, (source.problem_count or 0) + 1))
    actual = [item.source_number for item in numbered]
    if actual != expected:
        raise RuntimeError(f"merged source-number sequence is invalid: {actual}")
    flags = [
        ReviewFlag(
            category=flag.category,
            problem_indices=flag.source_numbers,
            source_pages=flag.source_pages,
            message=flag.message,
            original_text=flag.original_text,
            corrected_text=flag.corrected_text,
            context=flag.context,
        )
        for spec in CHUNKS
        for flag in chunks[spec.key].review_flags
    ]
    exam = ExamRecord(
        id=source.id,
        subject=source.subject,
        subject_tag=source.subject_tag,
        year=None,
        month=None,
        part=None,
        pdf_url=source.pdf_url,
        content=[ProblemBlock(problem=item.problem) for item in numbered],
        document_type=DocumentType.PRACTICE_PROBLEMS,
        problem_count=source.problem_count,
    )
    errors = validate_exam(exam, source, flags)
    if errors:
        raise RuntimeError("merged extraction is invalid: " + "; ".join(errors))
    return exam, flags


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract a large numbered practice-problem collection in page chunks"
    )
    parser.add_argument("exam_id", nargs="?", default=DEFAULT_ID)
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument("--review-dir", type=Path, default=Path("exams"))
    parser.add_argument("--build-root", type=Path, default=Path("build/extraction"))
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--reasoning", choices=["low", "medium", "high"], default="high")
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--force", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    sources = load_sources(args.manifest)
    if args.exam_id not in sources:
        raise SystemExit(f"unknown manifest ID: {args.exam_id}")
    source = sources[args.exam_id]
    if source.document_type != DocumentType.PRACTICE_PROBLEMS:
        raise SystemExit(f"not a practice-problem collection: {args.exam_id}")
    if sha256_file(source.pdf_path) != source.sha256:
        raise SystemExit(f"source hash does not match manifest: {args.exam_id}")
    if source.problem_count != CHUNKS[-1].last_problem:
        raise SystemExit("manifest problem count does not match the configured chunks")

    page_evidence = render_pages(source, args.build_root / source.id, args.dpi)
    chunks: dict[str, ChunkExtraction] = {}
    missing: list[ChunkSpec] = []
    for spec in CHUNKS:
        checkpoint = checkpoint_path(args.build_root, source, spec)
        extraction = None if args.force else load_checkpoint(
            checkpoint, source, spec, args.model, args.reasoning
        )
        if extraction is None:
            missing.append(spec)
        else:
            chunks[spec.key] = extraction

    def run(spec: ChunkSpec) -> tuple[ChunkSpec, ChunkExtraction]:
        pages = [page_evidence[page - 1] for page in spec.pages]
        extraction, response_id, usage = call_model(
            source, spec, pages, args.model, args.reasoning
        )
        errors = validate_chunk(extraction, spec)
        if errors:
            raise RuntimeError(f"{spec.key}: " + "; ".join(errors))
        save_checkpoint(
            checkpoint_path(args.build_root, source, spec),
            source,
            spec,
            extraction,
            args.model,
            args.reasoning,
            response_id,
            usage,
        )
        return spec, extraction

    if missing:
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
            futures = {executor.submit(run, spec): spec for spec in missing}
            completed = 0
            for future in as_completed(futures):
                spec, extraction = future.result()
                chunks[spec.key] = extraction
                completed += 1
                print(f"progress={completed}/{len(missing)} completed={spec.key}")

    exam, flags = assemble(source, chunks)
    write_json(exam_json_path(source), exam)
    write_text(exam_html_path(source), render_html(exam))
    update_review_files(args.review_dir, {source.id: (source, flags)})
    print(
        f"completed={source.id} chunks={len(CHUNKS)} problems={source.problem_count} "
        f"review_flags={len(flags)} cached={len(CHUNKS) - len(missing)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
