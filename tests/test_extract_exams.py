from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
import tempfile
import unittest

import pymupdf

from extract_exams import (
    ExamRecord,
    PROMPT_VERSION,
    Problem,
    ReviewCategory,
    ReviewFlag,
    SYSTEM_PROMPT,
    SourceExam,
    Subpart,
    exam_json_path,
    exam_markdown_path,
    extract_one,
    part_from_manifest,
    render_markdown,
    sha256_file,
    update_review_files,
    validate_exam,
)


def source(subject_tag: str = "algebra-first-year") -> SourceExam:
    return SourceExam(
        id=f"{subject_tag}-2025-may-part-1",
        subject="First Year Algebra" if subject_tag != "logic-phd" else "PhD Logic",
        subject_tag=subject_tag,
        year=2025,
        month="may",
        part=1,
        pdf_url="https://gma.math.ufl.edu/wp-content/uploads/sites/130/exam.pdf",
        pdf_path=Path("exams/example.pdf"),
        sha256="abc",
        download_sha256="abc",
    )


def exam_for(item: SourceExam, problems: list[Problem]) -> ExamRecord:
    return ExamRecord(
        id=item.id,
        subject=item.subject,
        subject_tag=item.subject_tag,
        year=item.year,
        month=item.month,
        part=item.part,
        pdf_url=item.pdf_url,
        instructions=None,
        problems=problems,
    )


class ExtractionSchemaTests(unittest.TestCase):
    def test_prompt_normalizes_mathematician_names_and_eponyms(self) -> None:
        normalized_prompt = " ".join(SYSTEM_PROMPT.split())

        self.assertEqual(PROMPT_VERSION, "exam-extraction-v6")
        self.assertIn("Gödel rather than Goedel", normalized_prompt)
        self.assertIn("Hahn–Banach", SYSTEM_PROMPT)
        self.assertIn("Preserve a hyphen that is actually part", SYSTEM_PROMPT)
        self.assertIn("not source corrections", SYSTEM_PROMPT)

    def test_outputs_are_adjacent_to_source_pdf(self) -> None:
        item = source()

        self.assertEqual(exam_json_path(item), Path("exams/example.json"))
        self.assertEqual(exam_markdown_path(item), Path("exams/example.md"))

    def test_notice_only_record_validates_and_renders(self) -> None:
        item = source()
        exam = exam_for(item, [])
        exam.instructions = "This exam was not provided to the archive."

        self.assertEqual(validate_exam(exam, item, []), [])
        self.assertEqual(
            render_markdown(exam),
            "# Algebra, first year exam, May 2025, Part 1\n\n"
            "*This exam was not provided to the archive.*\n",
        )

    def test_empty_record_without_notice_is_invalid(self) -> None:
        item = source()
        exam = exam_for(item, [])

        self.assertIn(
            "record contains neither problems nor a notice",
            validate_exam(exam, item, []),
        )

    def test_cached_extraction_records_approved_working_hash_change(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            pdf_path = root / "exam.pdf"
            with pymupdf.open() as document:
                document.new_page()
                document.save(pdf_path)
            item = replace(
                source(),
                pdf_path=pdf_path,
                sha256=sha256_file(pdf_path),
                download_sha256="download-hash",
            )
            exam = exam_for(item, [Problem(number=1, text="Prove it.", subparts=[])])
            pdf_path.with_suffix(".json").write_text(
                exam.model_dump_json(indent=2), encoding="utf-8"
            )
            checkpoint_path = root / "build" / item.id / "extraction.json"
            checkpoint_path.parent.mkdir(parents=True)
            checkpoint_path.write_text(
                json.dumps({"source_sha256": "download-hash", "review_flags": []}),
                encoding="utf-8",
            )

            _, _, cached = extract_one(
                item, root / "build", "unused-model", "high", 200, False
            )
            checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))

        self.assertTrue(cached)
        self.assertEqual(checkpoint["source_sha256"], item.sha256)
        self.assertEqual(checkpoint["source_sha256_history"], ["download-hash"])
        self.assertEqual(checkpoint["source_download_sha256"], "download-hash")

    def test_manifest_part_label(self) -> None:
        self.assertEqual(part_from_manifest({"source_label": "Part 2"}), 2)
        self.assertIsNone(part_from_manifest({"source_label": "Exam"}))

    def test_recursive_subparts_validate(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                Problem(
                    number=1,
                    text=r"Let \(G\) be a group.",
                    subparts=[
                        Subpart(
                            label="(a)",
                            text="Prove the claim.",
                            subparts=[Subpart(label="i.", text="First case.", subparts=[])],
                        )
                    ],
                )
            ],
        )

        self.assertEqual(validate_exam(exam, item, []), [])

    def test_markdown_renders_nested_subparts(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                Problem(
                    number=4,
                    text="Bipartite graphs:",
                    subparts=[
                        Subpart(
                            label="(a)",
                            text="Determine when the graph is",
                            subparts=[
                                Subpart(label="(1)", text="planar;", subparts=[]),
                                Subpart(label="(2)", text="Eulerian.", subparts=[]),
                            ],
                        )
                    ],
                )
            ],
        )

        self.assertIn(
            "**4.** Bipartite graphs:\n"
            "* (a) Determine when the graph is\n"
            "    * (1) planar;\n"
            "    * (2) Eulerian.",
            render_markdown(exam),
        )

    def test_markdown_is_rendered_from_exam_record(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                Problem(
                    number=1,
                    text=r"Let \(G\) be a group.",
                    subparts=[Subpart(label="(a)", text="Prove it.", subparts=[])],
                )
            ],
        )
        exam.instructions = "Answer one problem."

        self.assertEqual(
            render_markdown(exam),
            "# Algebra, first year exam, May 2025, Part 1\n\n"
            "*Answer one problem.*\n\n"
            "**1.** Let \\(G\\) be a group.\n"
            "* (a) Prove it.\n",
        )

    def test_qualifying_exam_markdown_title(self) -> None:
        item = replace(
            source(),
            id="algebra-qualifying-2026-jan-part-1",
            subject="Algebra Qualifying Exam",
            subject_tag="algebra-qualifying",
            year=2026,
            month="january",
        )
        exam = exam_for(item, [Problem(number=1, text="Prove it.", subparts=[])])

        self.assertTrue(
            render_markdown(exam).startswith(
                "# Algebra, qualifying exam, January 2026, Part 1\n"
            )
        )

    def test_markdown_supplies_stub_for_parts_without_a_stem(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                Problem(
                    number=4,
                    text="",
                    subparts=[
                        Subpart(label="(a)", text="First.", subparts=[]),
                        Subpart(label="(b)", text="Second.", subparts=[]),
                    ],
                )
            ],
        )

        self.assertIn(
            "**4.** This problem has two parts.\n* (a) First.\n* (b) Second.",
            render_markdown(exam),
        )

    def test_logic_requires_global_sequence(self) -> None:
        item = source("logic-phd")
        exam = exam_for(
            item,
            [
                Problem(number=1, text="First.", subparts=[]),
                Problem(number=3, text="Third.", subparts=[]),
            ],
        )

        self.assertIn("logic problem numbers are not globally sequential", validate_exam(exam, item, []))

    def test_logic_instructions_must_cover_final_numbers(self) -> None:
        item = source("logic-phd")
        exam = exam_for(
            item,
            [
                Problem(number=1, text="First.", subparts=[]),
                Problem(number=2, text="Second.", subparts=[]),
            ],
        )
        exam.instructions = "Problem 1 concerns Set theory."

        self.assertIn(
            "logic instructions do not map every final problem to a topic",
            validate_exam(exam, item, []),
        )

    def test_numbering_gap_requires_review_flag(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                Problem(number=1, text="First.", subparts=[]),
                Problem(number=3, text="Third.", subparts=[]),
            ],
        )

        self.assertIn(
            "nonsequential problem numbers lack a numbering review flag",
            validate_exam(exam, item, []),
        )

    def test_correction_requires_review_evidence(self) -> None:
        item = source()
        exam = exam_for(item, [Problem(number=1, text="Prove it.", subparts=[])])
        flag = ReviewFlag(
            category=ReviewCategory.CORRECTION,
            problem_numbers=[1],
            source_pages=[1],
            message="Corrected typo.",
            original_text="teh",
            corrected_text="the",
            context=None,
        )

        self.assertIn(
            "correction flag lacks original, corrected, or context text",
            validate_exam(exam, item, [flag]),
        )

    def test_review_files_split_flags_and_preserve_project_records(self) -> None:
        item = source()
        flags = [
            ReviewFlag(
                category=ReviewCategory.CORRECTION,
                problem_numbers=[1],
                source_pages=[1],
                message="Corrected typo.",
                original_text="teh",
                corrected_text="the",
                context="Immediate context.",
            ),
            ReviewFlag(
                category=ReviewCategory.NUMBERING_TRANSFORMATION,
                problem_numbers=[1, 2],
                source_pages=[1],
                message="Renumbered two sections globally.",
                original_text=None,
                corrected_text=None,
                context=None,
            ),
            ReviewFlag(
                category=ReviewCategory.VISUAL_CONTENT,
                problem_numbers=[2],
                source_pages=[1],
                message="Diagram omitted.",
                original_text=None,
                corrected_text=None,
                context=None,
            ),
        ]
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            serious_path = directory / "review-serious.json"
            serious_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "items": [
                            {
                                "exam_id": item.id,
                                "origin": "project",
                                "status": "open",
                            },
                            {
                                "exam_id": item.id,
                                "origin": "extraction",
                                "status": "old",
                            },
                        ],
                    }
                ),
                encoding="utf-8",
            )

            update_review_files(directory, {item.id: (item, flags)})
            correction = json.loads(
                (directory / "review-corrections.json").read_text(encoding="utf-8")
            )["items"]
            transformation = json.loads(
                (directory / "review-transformations.json").read_text(encoding="utf-8")
            )["items"]
            serious = json.loads(serious_path.read_text(encoding="utf-8"))["items"]

        self.assertEqual(correction[0]["category"], "correction")
        self.assertEqual(correction[0]["status"], "logged")
        self.assertEqual(transformation[0]["category"], "numbering-transformation")
        self.assertEqual([record.get("origin") for record in serious], ["project", "extraction"])
        self.assertEqual(serious[1]["category"], "visual-content")
        self.assertEqual(serious[1]["status"], "open")


if __name__ == "__main__":
    unittest.main()
