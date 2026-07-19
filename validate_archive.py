#!/usr/bin/env python3
"""Validate the complete committed PDF, JSON, Markdown, and review archive."""

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

from extract_exams import (
    REVIEW_FILES,
    ExamRecord,
    ReviewFlag,
    exam_json_path,
    exam_markdown_path,
    load_sources,
    render_markdown,
    review_bucket,
    sha256_file,
    validate_exam,
)


REVIEW_IDENTITY_FIELDS = (
    "exam_id",
    "problem_numbers",
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
    if exam.instructions:
        yield "instructions", exam.instructions
    for problem in exam.problems:
        yield f"problem {problem.number}", problem.text
        pending = [
            (f"problem {problem.number} subpart {item.label}", item)
            for item in problem.subparts
        ]
        while pending:
            location, subpart = pending.pop(0)
            yield location, subpart.text
            pending[0:0] = [
                (f"{location} / {item.label}", item) for item in subpart.subparts
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
    expressions: list[dict[str, object]], script: Path | None = None
) -> list[str]:
    script = script or Path(__file__).resolve().with_name("validate_mathjax.mjs")
    input_text = "".join(
        json.dumps(expression, ensure_ascii=False) + "\n" for expression in expressions
    )
    try:
        result = subprocess.run(
            ["node", str(script)],
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
        return [f"MathJax validator could not run; use npm ci: {detail}"]
    errors = [
        f"{item['exam_id']}: {item['location']}: MathJax: {item['message']} "
        f"in {item['tex']!r}"
        for item in failures
    ]
    if result.returncode not in (0, 1) and not errors:
        detail = result.stderr.strip() or f"exit status {result.returncode}"
        errors.append(f"MathJax validator could not run; use npm ci: {detail}")
    return errors


def validate_archive(manifest: Path, review_dir: Path) -> tuple[list[str], dict[str, int]]:
    sources = load_sources(manifest)
    errors: list[str] = []
    flags_by_exam: dict[str, list[ReviewFlag]] = {}
    review_counts: dict[str, int] = {}
    expressions: list[dict[str, object]] = []

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
        if document.get("review_type") != bucket:
            errors.append(f"{path}: review_type does not match its filename")
        identities = Counter(review_identity(item) for item in items)
        if any(count > 1 for count in identities.values()):
            errors.append(f"{path}: contains duplicate review records")
        for index, item in enumerate(items):
            exam_id = item.get("exam_id")
            if exam_id not in sources:
                errors.append(f"{path}: item {index} refers to an unknown exam")
                continue
            try:
                flag = ReviewFlag.model_validate(item)
            except ValidationError as error:
                errors.append(f"{path}: item {index} is invalid: {error}")
                continue
            if review_bucket(flag.category) != bucket:
                errors.append(f"{path}: item {index} belongs in another review file")
            if item.get("source_pdf") != str(sources[exam_id].pdf_path):
                errors.append(f"{path}: item {index} has the wrong source PDF")
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
        markdown_path = exam_markdown_path(source)
        for path, label in (
            (json_path, "canonical JSON"),
            (markdown_path, "Markdown rendering"),
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
        expressions.extend(math_expressions(exam))
        if (
            markdown_path.exists()
            and markdown_path.read_text(encoding="utf-8") != render_markdown(exam)
        ):
            errors.append(prefix + "Markdown does not match the canonical JSON")

    source_ids = set(sources)
    for suffix, label in ((".json", "JSON"), (".md", "Markdown")):
        for path in review_dir.rglob(f"*{suffix}"):
            if path.parent == review_dir and path.name.startswith("review-"):
                continue
            if path.stem not in source_ids:
                errors.append(f"{path}: orphaned canonical {label} file")

    errors.extend(validate_mathjax(expressions))

    stats = {
        "exams": len(sources),
        "corrections": review_counts.get("corrections", 0),
        "transformations": review_counts.get("transformations", 0),
        "serious": review_counts.get("serious", 0),
        "math_expressions": len(expressions),
    }
    return errors, stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the complete local exam archive")
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument("--review-dir", type=Path, default=Path("exams"))
    args = parser.parse_args()

    errors, stats = validate_archive(args.manifest, args.review_dir)
    if errors:
        for error in errors:
            print(f"error: {error}")
        print(f"failed: exams={stats['exams']} errors={len(errors)}")
        return 1
    print(
        f"valid: exams={stats['exams']} corrections={stats['corrections']} "
        f"transformations={stats['transformations']} serious={stats['serious']} "
        f"math_expressions={stats['math_expressions']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
