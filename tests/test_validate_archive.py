from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

import pymupdf

from build_indexes import build_indexes
from extract_exams import (
    REVIEW_FILES,
    ExamRecord,
    Problem,
    ProblemTextBlock,
    ProblemBlock,
    exam_html_path,
    exam_json_path,
    load_sources,
    render_html,
    sha256_file,
)
from validate_archive import validate_archive, validate_mathjax


def make_problem(text: str, subparts: list[object]) -> Problem:
    body = [ProblemTextBlock(text=text)] if text else []
    return Problem(body=body, subparts=subparts)


class ArchiveValidationTests(unittest.TestCase):
    def make_archive(self, root: Path) -> tuple[Path, Path, Path]:
        review_dir = root / "exams"
        subject_dir = review_dir / "algebra-phd"
        exam_id = "algebra-phd-2025-may"
        exam_dir = subject_dir / exam_id
        exam_dir.mkdir(parents=True)
        pdf_path = exam_dir / f"{exam_id}.source.pdf"
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
                            "id": exam_id,
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
            id=exam_id,
            subject="PhD Algebra",
            subject_tag="algebra-phd",
            year=2025,
            month="may",
            part=None,
            pdf_url="https://example.edu/exam.pdf",
            content=[ProblemBlock(problem=make_problem(text="Prove it.", subparts=[]))],
        )
        source = next(iter(load_sources(manifest_path).values()))
        exam_json_path(source).write_text(
            exam.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        html_path = exam_html_path(source)
        html_path.write_text(render_html(exam), encoding="utf-8")
        for bucket, (filename, purpose) in REVIEW_FILES.items():
            (review_dir / filename).write_text(
                json.dumps(
                    {
                        "schema_version": 2,
                        "review_type": bucket,
                        "purpose": purpose,
                        "items": [],
                    }
                ),
                encoding="utf-8",
            )
        build_indexes(manifest_path)
        return manifest_path, review_dir, html_path

    def test_complete_archive_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest, review_dir, _html = self.make_archive(Path(temp))
            errors, stats = validate_archive(manifest, review_dir)

        self.assertEqual(errors, [])
        self.assertEqual(stats["exams"], 1)

    def test_html_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest, review_dir, html = self.make_archive(Path(temp))
            html.write_text("changed\n", encoding="utf-8")
            errors, _stats = validate_archive(manifest, review_dir)

        self.assertTrue(any("HTML does not match" in error for error in errors))

    def test_subject_index_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest, review_dir, _html = self.make_archive(Path(temp))
            subject_index = review_dir / "algebra-phd" / "index.html"
            subject_index.write_text("changed\n", encoding="utf-8")
            errors, _stats = validate_archive(manifest, review_dir)

        self.assertTrue(any("archive index does not match" in error for error in errors))

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
