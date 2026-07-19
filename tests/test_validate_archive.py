from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

import pymupdf

from extract_exams import REVIEW_FILES, ExamRecord, Problem, render_markdown, sha256_file
from validate_archive import validate_archive, validate_mathjax


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

    def test_mathjax_catches_renderer_errors(self) -> None:
        errors = validate_mathjax(
            [
                {
                    "exam_id": "valid",
                    "location": "problem 1",
                    "tex": r"\left\{x\,\middle|\,x>0\right\}",
                    "display": False,
                },
                {
                    "exam_id": "valid-cd",
                    "location": "problem 2",
                    "tex": r"\begin{CD}A @>>> B\end{CD}",
                    "display": True,
                },
                {
                    "exam_id": "invalid",
                    "location": "problem 1",
                    "tex": r"\mathrel{\middle|}",
                    "display": False,
                },
                {
                    "exam_id": "undefined",
                    "location": "problem 2",
                    "tex": r"\notarealmacro{x}",
                    "display": False,
                },
            ]
        )

        self.assertEqual(len(errors), 2)
        self.assertIn("invalid: problem 1", "\n".join(errors))
        self.assertIn(r"Extra \middle", "\n".join(errors))
        self.assertIn(r"Undefined control sequence \notarealmacro", "\n".join(errors))


if __name__ == "__main__":
    unittest.main()
