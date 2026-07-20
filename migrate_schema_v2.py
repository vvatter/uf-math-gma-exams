#!/usr/bin/env python3
"""Prepare and mechanically migrate the archive to ordered schema version 2."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from extract_exams import (
    REVIEW_FILES,
    LegacyExamRecord,
    exam_json_path,
    load_sources,
    migrate_legacy_exam,
    write_json,
)


AFFECTED_CATEGORIES = {"instruction-rewrite", "numbering-transformation"}
DEFAULT_AFFECTED_PATH = Path("build/schema-v2/affected-exams.json")


def legacy_records(manifest: Path) -> dict[str, LegacyExamRecord]:
    records: dict[str, LegacyExamRecord] = {}
    for source in load_sources(manifest).values():
        path = exam_json_path(source)
        raw = json.loads(path.read_text(encoding="utf-8"))
        if raw.get("schema_version") == 1:
            records[source.id] = LegacyExamRecord.model_validate(raw)
    return records


def affected_ids(review_dir: Path) -> list[str]:
    document = json.loads(
        (review_dir / REVIEW_FILES["transformations"][0]).read_text(encoding="utf-8")
    )
    return sorted(
        {
            item["exam_id"]
            for item in document["items"]
            if item.get("category") in AFFECTED_CATEGORIES
        }
    )


def convert_review_files(
    review_dir: Path, records: dict[str, LegacyExamRecord]
) -> None:
    for bucket, (filename, _purpose) in REVIEW_FILES.items():
        path = review_dir / filename
        document = json.loads(path.read_text(encoding="utf-8"))
        for item in document["items"]:
            if "problem_indices" in item:
                item.pop("problem_numbers", None)
                continue
            numbers = item.pop("problem_numbers", [])
            record = records.get(item["exam_id"])
            if record is None:
                raise RuntimeError(
                    f"cannot convert review reference for {item['exam_id']}: "
                    "legacy JSON is unavailable"
                )
            positions = {
                problem.number: index
                for index, problem in enumerate(record.problems, start=1)
            }
            missing = [number for number in numbers if number not in positions]
            if missing:
                raise RuntimeError(
                    f"cannot convert review reference for {item['exam_id']}: "
                    f"unknown problem numbers {missing}"
                )
            item["problem_indices"] = [positions[number] for number in numbers]
        document["schema_version"] = 2
        write_json(path, document)


def migrate_unaffected(
    manifest: Path,
    records: dict[str, LegacyExamRecord],
    affected: set[str],
) -> int:
    sources = load_sources(manifest)
    migrated = 0
    for exam_id, legacy in records.items():
        if exam_id in affected:
            continue
        expected = list(range(1, len(legacy.problems) + 1))
        actual = [problem.number for problem in legacy.problems]
        if actual != expected:
            raise RuntimeError(
                f"{exam_id}: mechanical migration cannot represent numbering {actual}"
            )
        exam = migrate_legacy_exam(legacy)
        write_json(exam_json_path(sources[exam_id]), exam)
        migrated += 1
    return migrated


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument("--review-dir", type=Path, default=Path("exams"))
    parser.add_argument("--affected-output", type=Path, default=DEFAULT_AFFECTED_PATH)
    args = parser.parse_args()

    records = legacy_records(args.manifest)
    if not records:
        print("No schema-version-1 records remain; nothing to migrate.")
        return 0
    if args.affected_output.exists():
        affected = json.loads(
            args.affected_output.read_text(encoding="utf-8")
        )["exam_ids"]
    else:
        affected = affected_ids(args.review_dir)
    write_json(
        args.affected_output,
        {
            "schema_version": 1,
            "purpose": "Schema-v2 exams requiring fresh extraction from source PDFs",
            "exam_ids": affected,
        },
    )
    convert_review_files(args.review_dir, records)
    migrated = migrate_unaffected(args.manifest, records, set(affected))
    print(
        f"affected={len(affected)} mechanically_migrated={migrated} "
        f"legacy_remaining={len(records) - migrated}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
