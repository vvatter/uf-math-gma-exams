from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
import tempfile
import unittest

import pymupdf

from extract_exams import (
    ExamRecord,
    InstructionsBlock,
    NumberingMode,
    PROMPT_VERSION,
    Problem,
    ProblemBlock,
    ReviewCategory,
    ReviewFlag,
    SectionBlock,
    SYSTEM_PROMPT,
    SourceExam,
    Subpart,
    clean_native_text,
    exam_json_path,
    exam_markdown_path,
    extract_one,
    has_ascii_control_characters,
    part_from_manifest,
    render_markdown,
    select_exam_ids,
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
        content=[ProblemBlock(problem=problem) for problem in problems],
    )


class ExtractionSchemaTests(unittest.TestCase):
    def test_prompt_normalizes_mathematician_names_and_eponyms(self) -> None:
        normalized_prompt = " ".join(SYSTEM_PROMPT.split())

        self.assertEqual(PROMPT_VERSION, "exam-extraction-v10")
        self.assertIn("Gödel rather than Goedel", normalized_prompt)
        self.assertIn("Hahn–Banach", SYSTEM_PROMPT)
        self.assertIn("Preserve a hyphen that is actually part", SYSTEM_PROMPT)
        self.assertIn("not source corrections", SYSTEM_PROMPT)

    def test_outputs_are_adjacent_to_source_pdf(self) -> None:
        item = source()

        self.assertEqual(exam_json_path(item), Path("exams/example.json"))
        self.assertEqual(exam_markdown_path(item), Path("exams/example.md"))

    def test_problem_number_is_derived_not_accepted_as_data(self) -> None:
        with self.assertRaises(ValueError):
            Problem.model_validate(
                {"number": 1, "text": "Prove it.", "subparts": []}
            )

    def test_all_selection_skips_completed_before_applying_limit(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            items = [
                replace(
                    source("analysis-phd"),
                    id=f"analysis-phd-{year}-jan",
                    year=year,
                    pdf_path=directory / f"analysis-phd-{year}-jan.pdf",
                )
                for year in (1988, 1989, 1990)
            ]
            exam_json_path(items[0]).write_text("{}", encoding="utf-8")
            sources = {item.id: item for item in items}

            selection = select_exam_ids(
                sources,
                [],
                pilot=False,
                all_exams=True,
                subject_tags=None,
                limit=1,
                force=False,
            )
            forced_selection = select_exam_ids(
                sources,
                [],
                pilot=False,
                all_exams=True,
                subject_tags=None,
                limit=None,
                force=True,
            )

        self.assertEqual(selection.ids, ("analysis-phd-1989-jan",))
        self.assertEqual(selection.skipped_completed, 1)
        self.assertEqual(selection.deferred_by_limit, 1)
        self.assertEqual(forced_selection.ids, tuple(item.id for item in items))
        self.assertEqual(forced_selection.skipped_completed, 0)

    def test_subject_selection_is_repeatable_and_validated(self) -> None:
        analysis = replace(
            source("analysis-phd"),
            id="analysis-phd-1988-jan",
            pdf_path=Path("exams/analysis-phd-1988-jan.pdf"),
        )
        logic = replace(
            source("logic-phd"),
            id="logic-phd-2006-aug",
            pdf_path=Path("exams/logic-phd-2006-aug.pdf"),
        )
        sources = {item.id: item for item in (analysis, logic)}

        selection = select_exam_ids(
            sources,
            [],
            pilot=False,
            all_exams=False,
            subject_tags=["logic-phd", "analysis-phd"],
            limit=None,
            force=True,
        )

        self.assertEqual(
            selection.ids,
            ("analysis-phd-1988-jan", "logic-phd-2006-aug"),
        )
        with self.assertRaisesRegex(ValueError, "unknown subject tags: imaginary-phd"):
            select_exam_ids(
                sources,
                [],
                pilot=False,
                all_exams=False,
                subject_tags=["imaginary-phd"],
                limit=None,
                force=False,
            )

    def test_notice_only_record_validates_and_renders(self) -> None:
        item = source()
        exam = exam_for(item, [])
        exam.content = [
            InstructionsBlock(text="This exam was not provided to the archive.")
        ]

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

    def test_ascii_control_characters_are_invalid(self) -> None:
        item = source()
        exam = exam_for(item, [Problem(text="Let \x07 be a measure.", subparts=[])])

        self.assertIn(
            "content contains an ASCII control character",
            validate_exam(exam, item, []),
        )

    def test_native_text_evidence_drops_ascii_control_characters(self) -> None:
        self.assertEqual(clean_native_text("  A\x07B\nC\x01  "), "AB\nC")

    def test_control_character_detection_walks_models(self) -> None:
        clean = exam_for(source(), [Problem(text="Clean.", subparts=[])])
        corrupt = exam_for(source(), [Problem(text="Bad \x1dmu.", subparts=[])])

        self.assertFalse(has_ascii_control_characters(clean))
        self.assertTrue(has_ascii_control_characters(corrupt))

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
            exam = exam_for(item, [Problem(text="Prove it.", subparts=[])])
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

    def test_valid_checkpoint_is_promoted_without_another_model_call(self) -> None:
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
            extraction = {
                "content": [
                    {
                        "type": "problem",
                        "problem": {"text": "Prove it.", "subparts": []},
                    }
                ],
                "review_flags": [],
            }
            saved_path = root / "build" / item.id / "extraction.json"
            saved_path.parent.mkdir(parents=True)
            saved_path.write_text(
                json.dumps(
                    {
                        "source_sha256": item.sha256,
                        "review_flags": [],
                        "validation_errors": ["obsolete validator error"],
                        "model_extraction": extraction,
                    }
                ),
                encoding="utf-8",
            )

            exam, flags, cached = extract_one(
                item, root / "build", "unused-model", "high", 200, False
            )
            checkpoint = json.loads(saved_path.read_text(encoding="utf-8"))
            json_exists = pdf_path.with_suffix(".json").exists()
            markdown_exists = pdf_path.with_suffix(".md").exists()

        self.assertTrue(cached)
        self.assertEqual(exam.content[0].problem.text, "Prove it.")
        self.assertEqual(flags, [])
        self.assertEqual(checkpoint["validation_errors"], [])
        self.assertIn("revalidated_at", checkpoint)
        self.assertTrue(json_exists)
        self.assertTrue(markdown_exists)

    def test_manifest_part_label(self) -> None:
        self.assertEqual(part_from_manifest({"source_label": "Part 2"}), 2)
        self.assertIsNone(part_from_manifest({"source_label": "Exam"}))

    def test_recursive_subparts_validate(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                Problem(
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
            "**1.** Bipartite graphs:\n"
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
                    text=r"Let \(G\) be a group.",
                    subparts=[Subpart(label="(a)", text="Prove it.", subparts=[])],
                )
            ],
        )
        exam.content.insert(0, InstructionsBlock(text="Answer one problem."))

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
        exam = exam_for(item, [Problem(text="Prove it.", subparts=[])])

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
                    text="",
                    subparts=[
                        Subpart(label="(a)", text="First.", subparts=[]),
                        Subpart(label="(b)", text="Second.", subparts=[]),
                    ],
                )
            ],
        )

        self.assertIn(
            "**1.** This problem has two parts.\n* (a) First.\n* (b) Second.",
            render_markdown(exam),
        )

    def test_sections_control_derived_problem_numbers(self) -> None:
        item = source()
        exam = exam_for(item, [Problem(text="Preamble problem.", subparts=[])])
        exam.content.extend(
            [
                SectionBlock(
                    heading="II. Set Theory",
                    numbering=NumberingMode.RESTART,
                    content=[
                        InstructionsBlock(text="Prove both statements."),
                        ProblemBlock(problem=Problem(text="First theorem.", subparts=[])),
                        ProblemBlock(problem=Problem(text="Second theorem.", subparts=[])),
                    ],
                ),
                SectionBlock(
                    heading="SECTION III",
                    numbering=NumberingMode.CONTINUE,
                    content=[
                        ProblemBlock(problem=Problem(text="Final theorem.", subparts=[]))
                    ],
                ),
            ]
        )

        self.assertEqual(validate_exam(exam, item, []), [])
        self.assertIn(
            "**1.** Preamble problem.\n\n"
            "## II. Set Theory\n\n"
            "*Prove both statements.*\n\n"
            "**1.** First theorem.\n\n"
            "**2.** Second theorem.\n\n"
            "## SECTION III\n\n"
            "**3.** Final theorem.",
            render_markdown(exam),
        )

    def test_empty_section_is_invalid(self) -> None:
        item = source()
        exam = ExamRecord(
            id=item.id,
            subject=item.subject,
            subject_tag=item.subject_tag,
            year=item.year,
            month=item.month,
            part=item.part,
            pdf_url=item.pdf_url,
            content=[
                SectionBlock(
                    heading="Part I",
                    numbering=NumberingMode.RESTART,
                    content=[InstructionsBlock(text="Read carefully.")],
                )
            ],
        )

        self.assertIn("contains no problems", "\n".join(validate_exam(exam, item, [])))

    def test_correction_requires_review_evidence(self) -> None:
        item = source()
        exam = exam_for(item, [Problem(text="Prove it.", subparts=[])])
        flag = ReviewFlag(
            category=ReviewCategory.CORRECTION,
            problem_indices=[1],
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
                problem_indices=[1],
                source_pages=[1],
                message="Corrected typo.",
                original_text="teh",
                corrected_text="the",
                context="Immediate context.",
            ),
            ReviewFlag(
                category=ReviewCategory.NUMBERING_TRANSFORMATION,
                problem_indices=[1, 2],
                source_pages=[1],
                message="Renumbered two sections globally.",
                original_text=None,
                corrected_text=None,
                context=None,
            ),
            ReviewFlag(
                category=ReviewCategory.VISUAL_CONTENT,
                problem_indices=[2],
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
