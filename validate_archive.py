#!/usr/bin/env python3
"""Validate the complete committed PDF, JSON, HTML, and review archive."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
from typing import Iterator

import pymupdf
from pydantic import ValidationError

from prepare_mathjax import MathJaxSetupError, prepare_mathjax

from build_indexes import expected_index_pages
from extract_exams import (
    REVIEW_FILES,
    ExamRecord,
    InstructionsBlock,
    NumberingMode,
    ProblemTextBlock,
    ProblemBlock,
    ReviewFlag,
    SectionBlock,
    exam_html_path,
    exam_figure_png_path,
    exam_json_path,
    load_sources,
    iter_problems,
    iter_tikz_blocks,
    render_html,
    review_bucket,
    sha256_file,
    validate_exam,
)


REVIEW_IDENTITY_FIELDS = (
    "exam_id",
    "problem_indices",
    "category",
    "source_pdf",
    "source_pages",
    "message",
    "original_text",
    "corrected_text",
    "context",
    "origin",
)
MATH_PATTERN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.DOTALL)


def review_identity(item: dict[str, object]) -> str:
    identity = {field: item.get(field) for field in REVIEW_IDENTITY_FIELDS}
    return json.dumps(identity, ensure_ascii=False, sort_keys=True)


def located_text(exam: ExamRecord) -> Iterator[tuple[str, str]]:
    problem_index = 0
    displayed_number = 0
    for block in exam.content:
        if isinstance(block, InstructionsBlock):
            yield "instructions", block.text
            continue
        if isinstance(block, ProblemBlock):
            items = [(None, block)]
        else:
            if block.numbering == NumberingMode.RESTART:
                displayed_number = 0
            items = [(block.heading, item) for item in block.content]
        for section_heading, item in items:
            prefix = f"section {section_heading} / " if section_heading else ""
            if isinstance(item, InstructionsBlock):
                yield prefix + "instructions", item.text
                continue
            problem_index += 1
            displayed_number += 1
            problem = item.problem
            location = f"{prefix}problem {displayed_number} (index {problem_index})"
            for concern_index, concern in enumerate(problem.concerns, start=1):
                yield f"{location} concern {concern_index}", concern.explanation
            for body_index, body_block in enumerate(problem.body, start=1):
                if isinstance(body_block, ProblemTextBlock):
                    yield f"{location} text block {body_index}", body_block.text
            pending = [
                (f"{location} subpart {part.label}", part)
                for part in problem.subparts
            ]
            while pending:
                subpart_location, subpart = pending.pop(0)
                yield subpart_location, subpart.text
                pending[0:0] = [
                    (f"{subpart_location} / {part.label}", part)
                    for part in subpart.subparts
                ]


def math_expressions(exam: ExamRecord) -> Iterator[dict[str, object]]:
    for location, content in located_text(exam):
        for match in MATH_PATTERN.finditer(content):
            inline, display = match.groups()
            yield {
                "exam_id": exam.id,
                "location": location,
                "tex": inline if inline is not None else display,
                "display": display is not None,
            }


def validate_mathjax(
    expressions: list[dict[str, object]],
    script: Path | None = None,
    cache_root: Path | None = None,
) -> list[str]:
    script = script or Path(__file__).resolve().with_name("validate_mathjax.mjs")
    try:
        cache_root = cache_root or prepare_mathjax()
    except MathJaxSetupError as error:
        return [f"MathJax validator could not be prepared: {error}"]
    input_text = "".join(
        json.dumps(expression, ensure_ascii=False) + "\n" for expression in expressions
    )
    try:
        result = subprocess.run(
            [
                "node",
                str(script),
                str(cache_root / "src" / "bundle"),
                str(cache_root / "font"),
            ],
            input=input_text,
            capture_output=True,
            check=False,
            encoding="utf-8",
        )
    except FileNotFoundError:
        return ["MathJax validation requires Node.js; the node executable was not found"]
    try:
        output = json.loads(result.stdout)
        failures = output["failures"]
    except (KeyError, TypeError, ValueError):
        detail = result.stderr.strip() or result.stdout.strip() or "no diagnostic output"
        return [f"MathJax validator could not run: {detail}"]
    errors = [
        f"{item['exam_id']}: {item['location']}: MathJax: {item['message']} "
        f"in {item['tex']!r}"
        for item in failures
    ]
    if result.returncode not in (0, 1) and not errors:
        detail = result.stderr.strip() or f"exit status {result.returncode}"
        errors.append(f"MathJax validator could not run: {detail}")
    return errors


def validate_archive(
    manifest: Path,
    review_dir: Path,
    exam_ids: set[str] | None = None,
) -> tuple[list[str], dict[str, int]]:
    all_sources = load_sources(manifest)
    errors: list[str] = []
    unknown_ids = sorted((exam_ids or set()) - set(all_sources))
    errors.extend(f"unknown requested exam: {exam_id}" for exam_id in unknown_ids)
    sources = {
        exam_id: source
        for exam_id, source in all_sources.items()
        if exam_ids is None or exam_id in exam_ids
    }
    flags_by_exam: dict[str, list[ReviewFlag]] = {}
    review_counts: dict[str, int] = {}
    concern_count = 0
    expressions: list[dict[str, object]] = []
    index_pages: dict[Path, str] = {}

    if exam_ids is None:
        try:
            index_pages = expected_index_pages(all_sources.values(), manifest.parent)
        except ValueError as error:
            errors.append(f"archive indexes cannot be generated: {error}")
        for path, expected in index_pages.items():
            if not path.exists():
                errors.append(f"{path}: archive index is missing")
            elif path.read_text(encoding="utf-8") != expected:
                errors.append(f"{path}: archive index does not match the manifest")

    for bucket, (filename, _purpose) in REVIEW_FILES.items():
        path = review_dir / filename
        if not path.exists():
            errors.append(f"{path}: review file is missing")
            continue
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
            items = document["items"]
        except (KeyError, OSError, ValueError) as error:
            errors.append(f"{path}: review file is invalid: {error}")
            continue
        review_counts[bucket] = len(items)
        if document.get("schema_version") != 2:
            errors.append(f"{path}: schema_version is not 2")
        if document.get("review_type") != bucket:
            errors.append(f"{path}: review_type does not match its filename")
        identities = Counter(review_identity(item) for item in items)
        if any(count > 1 for count in identities.values()):
            errors.append(f"{path}: contains duplicate review records")
        for index, item in enumerate(items):
            exam_id = item.get("exam_id")
            if exam_id not in all_sources:
                errors.append(f"{path}: item {index} refers to an unknown exam")
                continue
            try:
                flag = ReviewFlag.model_validate(item)
            except ValidationError as error:
                errors.append(f"{path}: item {index} is invalid: {error}")
                continue
            if review_bucket(flag.category) != bucket:
                errors.append(f"{path}: item {index} belongs in another review file")
            if item.get("source_pdf") != str(all_sources[exam_id].pdf_path):
                errors.append(f"{path}: item {index} has the wrong source PDF")
            if exam_id in sources:
                flags_by_exam.setdefault(exam_id, []).append(flag)

    for source in sources.values():
        prefix = f"{source.id}: "
        if not source.pdf_path.exists():
            errors.append(prefix + "source PDF is missing")
            continue
        if sha256_file(source.pdf_path) != source.sha256:
            errors.append(prefix + "source PDF hash does not match the manifest")
        try:
            with pymupdf.open(source.pdf_path) as document:
                page_count = document.page_count
        except (OSError, RuntimeError, ValueError) as error:
            errors.append(prefix + f"source PDF cannot be opened: {error}")
            continue
        if page_count < 1:
            errors.append(prefix + "source PDF has no pages")

        json_path = exam_json_path(source)
        html_path = exam_html_path(source)
        for path, label in (
            (json_path, "canonical JSON"),
            (html_path, "HTML rendering"),
        ):
            if not path.exists():
                errors.append(prefix + f"{label} is missing")
        if not json_path.exists():
            continue

        try:
            exam = ExamRecord.model_validate_json(json_path.read_text(encoding="utf-8"))
        except (OSError, ValidationError, ValueError) as error:
            errors.append(prefix + f"canonical JSON is invalid: {error}")
            continue
        flags = flags_by_exam.get(source.id, [])
        for flag in flags:
            if any(page < 1 or page > page_count for page in flag.source_pages):
                errors.append(prefix + "review flag refers to an unknown source page")
        errors.extend(prefix + error for error in validate_exam(exam, source, flags))
        concern_count += sum(len(problem.concerns) for problem in iter_problems(exam))
        for figure in iter_tikz_blocks(exam):
            figure_path = exam_figure_png_path(source, figure)
            if not figure_path.is_file():
                errors.append(prefix + f"figure PNG is missing: {figure_path.name}")
                continue
            try:
                with pymupdf.open(figure_path) as image:
                    if image.page_count != 1:
                        errors.append(prefix + f"figure PNG is invalid: {figure_path.name}")
            except (OSError, RuntimeError, ValueError) as error:
                errors.append(prefix + f"figure PNG cannot be opened: {error}")
        expressions.extend(math_expressions(exam))
        if (
            html_path.exists()
            and html_path.read_text(encoding="utf-8") != render_html(exam)
        ):
            errors.append(prefix + "HTML does not match the canonical JSON")

    if exam_ids is None:
        canonical_paths = {
            ".json": {exam_json_path(source) for source in sources.values()},
            ".html": {exam_html_path(source) for source in sources.values()},
        }
        for suffix, label in (
            (".json", "JSON"),
            (".html", "HTML"),
        ):
            for path in review_dir.rglob(f"*{suffix}"):
                if path.parent == review_dir and path.name.startswith("review-"):
                    continue
                if path in index_pages:
                    continue
                if path not in canonical_paths[suffix]:
                    errors.append(f"{path}: orphaned canonical {label} file")

    errors.extend(validate_mathjax(expressions))

    stats = {
        "exams": len(sources),
        "corrections": review_counts.get("corrections", 0),
        "transformations": review_counts.get("transformations", 0),
        "serious": review_counts.get("serious", 0),
        "concerns": concern_count,
        "math_expressions": len(expressions),
        "indexes": len(index_pages),
    }
    return errors, stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the complete local exam archive")
    parser.add_argument("exam_ids", nargs="*", help="validate only these manifest IDs")
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument("--review-dir", type=Path, default=Path("exams"))
    args = parser.parse_args()

    errors, stats = validate_archive(
        args.manifest,
        args.review_dir,
        set(args.exam_ids) if args.exam_ids else None,
    )
    if errors:
        for error in errors:
            print(f"error: {error}")
        print(f"failed: exams={stats['exams']} errors={len(errors)}")
        return 1
    print(
        f"valid: exams={stats['exams']} corrections={stats['corrections']} "
        f"transformations={stats['transformations']} serious={stats['serious']} "
        f"concerns={stats['concerns']} math_expressions={stats['math_expressions']} "
        f"indexes={stats['indexes']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
