from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

import pymupdf

from extract_exams import REVIEW_FILES, ExamRecord, Problem, render_markdown, sha256_file
from validate_archive import validate_archive


class ArchiveValidationTests(unittest.TestCase):
    def make_archive(self, root: Path) -> tuple[Path, Path, Path]:
        review_dir = root / "exams"
        subject_dir = review_dir / "algebra-phd"
        subject_dir.mkdir(parents=True)
        pdf_path = subject_dir / "algebra-phd-2025-may.pdf"
        with pymupdf.open() as document:
            document.new_page()
            document.save(pdf_path)
        digest = sha256_file(pdf_path)
        manifest_path = root / "manifest.json"
        manifest_path.write_text(
            json.dumps(
                {
                    "exams": [
                        {
                            "path": str(pdf_path),
                            "subject": "PhD Algebra",
                            "subject_tag": "algebra-phd",
                            "year": 2025,
                            "month": "may",
                            "download_url": "https://example.edu/exam.pdf",
                            "sha256": digest,
                            "download_sha256": digest,
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        exam = ExamRecord(
            id=pdf_path.stem,
            subject="PhD Algebra",
            subject_tag="algebra-phd",
            year=2025,
            month="may",
            part=None,
            pdf_url="https://example.edu/exam.pdf",
            instructions=None,
            problems=[Problem(number=1, text="Prove it.", subparts=[])],
        )
        pdf_path.with_suffix(".json").write_text(
            exam.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        markdown_path = pdf_path.with_suffix(".md")
        markdown_path.write_text(render_markdown(exam), encoding="utf-8")
        for bucket, (filename, purpose) in REVIEW_FILES.items():
            (review_dir / filename).write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "review_type": bucket,
                        "purpose": purpose,
                        "items": [],
                    }
                ),
                encoding="utf-8",
            )
        return manifest_path, review_dir, markdown_path

    def test_complete_archive_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest, review_dir, _markdown = self.make_archive(Path(temp))
            errors, stats = validate_archive(manifest, review_dir)

        self.assertEqual(errors, [])
        self.assertEqual(stats["exams"], 1)

    def test_markdown_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest, review_dir, markdown = self.make_archive(Path(temp))
            markdown.write_text("changed\n", encoding="utf-8")
            errors, _stats = validate_archive(manifest, review_dir)

        self.assertTrue(any("Markdown does not match" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
