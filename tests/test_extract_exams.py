from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
import tempfile
import unittest

import pymupdf

from extract_exams import (
    ConcernStatus,
    DocumentType,
    ExamRecord,
    InstructionsBlock,
    NumberingMode,
    PROMPT_VERSION,
    Problem,
    ProblemConcern,
    ProblemTextBlock,
    ProblemBlock,
    ReviewCategory,
    ReviewFlag,
    SectionBlock,
    SYSTEM_PROMPT,
    SourceExam,
    Subpart,
    TikzBlock,
    clean_native_text,
    exam_html_path,
    exam_json_path,
    exam_pdf_path,
    exam_tex_path,
    exam_title,
    extract_one,
    has_ascii_control_characters,
    part_from_manifest,
    render_html,
    select_exam_ids,
    sha256_file,
    update_review_files,
    validate_exam,
)


def make_problem(text: str, subparts: list[Subpart]) -> Problem:
    body = [ProblemTextBlock(text=text)] if text else []
    return Problem(body=body, subparts=subparts)


def source(subject_tag: str = "algebra-first-year") -> SourceExam:
    exam_id = f"{subject_tag}-2025-may-part-1"
    return SourceExam(
        id=exam_id,
        subject="First Year Algebra" if subject_tag != "logic-phd" else "PhD Logic",
        subject_tag=subject_tag,
        year=2025,
        month="may",
        part=1,
        pdf_url="https://gma.math.ufl.edu/wp-content/uploads/sites/130/exam.pdf",
        pdf_path=Path("exams") / subject_tag / exam_id / f"{exam_id}.source.pdf",
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
        practice_variant=item.practice_variant,
        document_type=item.document_type,
        problem_count=item.problem_count,
    )


class ExtractionSchemaTests(unittest.TestCase):
    def test_practice_problem_collection_title_and_count(self) -> None:
        item = replace(
            source(),
            id="algebra-first-year-practice-problems",
            year=None,
            month=None,
            part=None,
            document_type=DocumentType.PRACTICE_PROBLEMS,
            problem_count=2,
        )
        problems = [make_problem("First.", []), make_problem("Second.", [])]
        exam = exam_for(item, problems)

        self.assertEqual(exam_title(item), "Algebra First-Year Exam, Practice Problems")
        self.assertEqual(validate_exam(exam, item, []), [])
        exam.problem_count = 3
        self.assertIn(
            "document, date, practice variant, or part metadata does not match source",
            validate_exam(exam, item, []),
        )

    def test_undated_practice_exam_title(self) -> None:
        item = replace(
            source(),
            id="algebra-first-year-practice-a-part-1",
            year=None,
            month=None,
            practice_variant="A",
        )

        self.assertEqual(
            exam_title(item),
            "Algebra First-Year Practice Exam A, Part 1",
        )

    def test_only_practice_exams_may_be_undated(self) -> None:
        practice = replace(
            source(),
            id="algebra-first-year-practice-a-part-1",
            year=None,
            month=None,
            practice_variant="A",
        )
        problem = make_problem("Prove it.", [])
        self.assertEqual(validate_exam(exam_for(practice, [problem]), practice, []), [])

        undated = replace(practice, practice_variant=None)
        errors = validate_exam(exam_for(undated, [problem]), undated, [])
        self.assertIn("a record without a date must be a practice exam", errors)

        dated_practice = replace(source(), practice_variant="A")
        errors = validate_exam(
            exam_for(dated_practice, [problem]), dated_practice, []
        )
        self.assertIn("practice exams cannot have a year or month", errors)

    def test_prompt_normalizes_mathematician_names_and_eponyms(self) -> None:
        normalized_prompt = " ".join(SYSTEM_PROMPT.split())

        self.assertEqual(PROMPT_VERSION, "exam-extraction-v17")
        self.assertIn("Gödel rather than Goedel", normalized_prompt)
        self.assertIn("Hahn–Banach", SYSTEM_PROMPT)
        self.assertIn("Preserve a hyphen that is actually part", SYSTEM_PROMPT)
        self.assertIn("not source corrections", SYSTEM_PROMPT)
        self.assertIn(
            "does not require a visual-content flag", normalized_prompt
        )
        self.assertIn(
            "Do not flag a clear cross-problem reference merely because it exists",
            normalized_prompt,
        )
        self.assertIn("MATHEMATICAL CONCERNS", SYSTEM_PROMPT)
        self.assertIn("Never mark a concern confirmed", normalized_prompt)

    def test_outputs_use_canonical_exam_directory_names(self) -> None:
        item = source()

        directory = Path("exams/algebra-first-year/algebra-first-year-2025-may-part-1")
        self.assertEqual(
            exam_json_path(item),
            directory / "algebra-first-year-2025-may-part-1.json",
        )
        self.assertEqual(exam_html_path(item), directory / "index.html")
        self.assertEqual(
            exam_tex_path(item),
            directory / "algebra-first-year-2025-may-part-1.tex",
        )
        self.assertEqual(
            exam_pdf_path(item),
            directory / "algebra-first-year-2025-may-part-1.pdf",
        )

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
                    pdf_path=(
                        directory
                        / f"analysis-phd-{year}-jan"
                        / f"analysis-phd-{year}-jan.source.pdf"
                    ),
                )
                for year in (1988, 1989, 1990)
            ]
            exam_json_path(items[0]).parent.mkdir(parents=True)
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

    def test_bulk_selection_omits_practice_problem_collections(self) -> None:
        dated = source()
        collection = replace(
            source(),
            id="algebra-first-year-practice-problems",
            year=None,
            month=None,
            part=None,
            document_type=DocumentType.PRACTICE_PROBLEMS,
            problem_count=113,
        )
        sources = {item.id: item for item in (dated, collection)}

        selection = select_exam_ids(
            sources,
            [],
            pilot=False,
            all_exams=True,
            subject_tags=None,
            limit=None,
            force=True,
        )

        self.assertEqual(selection.ids, (dated.id,))
        with self.assertRaisesRegex(
            ValueError, "require extract_practice_problems.py"
        ):
            select_exam_ids(
                sources,
                [collection.id],
                pilot=False,
                all_exams=False,
                subject_tags=None,
                limit=None,
                force=True,
            )

    def test_subject_selection_is_repeatable_and_validated(self) -> None:
        analysis = replace(
            source("analysis-phd"),
            id="analysis-phd-1988-jan",
            pdf_path=Path(
                "exams/analysis-phd-1988-jan/analysis-phd-1988-jan.source.pdf"
            ),
        )
        logic = replace(
            source("logic-phd"),
            id="logic-phd-2006-aug",
            pdf_path=Path("exams/logic-phd-2006-aug/logic-phd-2006-aug.source.pdf"),
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
        self.assertIn(
            "This exam was not provided to the archive.",
            render_html(exam),
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
        exam = exam_for(item, [make_problem(text="Let \x07 be a measure.", subparts=[])])

        self.assertIn(
            "content contains an ASCII control character",
            validate_exam(exam, item, []),
        )

    def test_native_text_evidence_drops_ascii_control_characters(self) -> None:
        self.assertEqual(clean_native_text("  A\x07B\nC\x01  "), "AB\nC")

    def test_control_character_detection_walks_models(self) -> None:
        clean = exam_for(source(), [make_problem(text="Clean.", subparts=[])])
        corrupt = exam_for(source(), [make_problem(text="Bad \x1dmu.", subparts=[])])

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
            exam = exam_for(item, [make_problem(text="Prove it.", subparts=[])])
            exam_json_path(item).write_text(
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
                        "problem": {
                            "body": [{"type": "text", "text": "Prove it."}],
                            "subparts": [],
                        },
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
            json_exists = exam_json_path(item).exists()
            html_exists = exam_html_path(item).exists()

        self.assertTrue(cached)
        self.assertEqual(exam.content[0].problem.body[0].text, "Prove it.")
        self.assertEqual(flags, [])
        self.assertEqual(checkpoint["validation_errors"], [])
        self.assertIn("revalidated_at", checkpoint)
        self.assertTrue(json_exists)
        self.assertTrue(html_exists)

    def test_tikz_figure_renders_as_accessible_html(self) -> None:
        item = source()
        alt = "A square with vertices labeled clockwise."
        problem = Problem(
            body=[
                ProblemTextBlock(text="Consider the following diagram."),
                TikzBlock(
                    id="labeled-square",
                    alt=alt,
                    options=["line cap=round"],
                    height_lines=10,
                    code=r"\draw (0,0) rectangle (1,1);",
                ),
            ],
            subparts=[],
        )
        exam = exam_for(item, [problem])

        html = render_html(exam)

        self.assertIn('<figure class="problem-figure">', html)
        self.assertIn(f'alt="{alt}"', html)
        self.assertIn(f'src="{item.id}.labeled-square.png"', html)
        self.assertIn('style="max-height: 10lh"', html)
        self.assertIn("max-width: 80%", html)
        self.assertIn("max-height: 6lh", html)

    def test_tikz_wrapper_is_rejected_from_canonical_json(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                Problem(
                    body=[
                        TikzBlock(
                            id="bad-wrapper",
                            alt="A diagram.",
                            code=r"\begin{tikzpicture}\draw (0,0)--(1,1);\end{tikzpicture}",
                        )
                    ],
                    subparts=[],
                )
            ],
        )

        self.assertIn(
            "problem index 1 TikZ code contains a document or picture wrapper",
            validate_exam(exam, item, []),
        )

    def test_manifest_part_label(self) -> None:
        self.assertEqual(part_from_manifest({"source_label": "Part 2"}), 2)
        self.assertIsNone(part_from_manifest({"source_label": "Exam"}))

    def test_recursive_subparts_validate(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                make_problem(
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

    def test_html_renders_nested_subparts(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                make_problem(
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

        rendered = render_html(exam)
        self.assertEqual(rendered.count('<ol class="subparts">'), 2)
        self.assertIn('<span class="subpart-label">(a)</span>', rendered)
        self.assertIn('<span class="subpart-label">(1)</span>', rendered)
        self.assertIn('<span class="subpart-label">(2)</span>', rendered)
        self.assertIn("Determine when the graph is", rendered)
        self.assertIn("planar;", rendered)
        self.assertIn("Eulerian.", rendered)

    def test_html_is_semantic_escaped_and_accessible(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                make_problem(
                    text=r"Let \(G < H\) and prove the claim.",
                    subparts=[
                        Subpart(
                            label="(a)",
                            text="Handle the first case.",
                            subparts=[
                                Subpart(label="i.", text="Give details.", subparts=[])
                            ],
                        )
                    ],
                )
            ],
        )
        exam.content.insert(0, InstructionsBlock(text="Answer one problem."))

        rendered = render_html(exam)

        self.assertTrue(rendered.startswith("<!doctype html>\n<html lang=\"en\">"))
        self.assertIn('<meta charset="utf-8">', rendered)
        self.assertIn('<main id="main-content">', rendered)
        self.assertIn(
            "<h1>Algebra First-Year Exam, May 2025, Part 1</h1>", rendered
        )
        self.assertIn(
            '<p class="institution"><a href="https://www.ufl.edu/">University of Florida</a>, '
            '<a href="https://math.ufl.edu/">Department of Mathematics</a></p>',
            rendered,
        )
        self.assertIn('<ol class="problems" start="1">', rendered)
        self.assertIn('<ol class="subparts">', rendered)
        self.assertIn('<span class="subpart-label">(a)</span>', rendered)
        self.assertIn('<span class="subpart-label">i.</span>', rendered)
        self.assertIn(r"Let \(G &lt; H\) and prove the claim.", rendered)
        self.assertIn("computer-modern@0.1.3/cmu-serif.css", rendered)
        self.assertIn("mathjax@4.1.3/tex-chtml.js", rendered)
        self.assertNotIn("gma.math.ufl.edu", rendered)
        self.assertIn(
            '<a href="https://github.com/vvatter/uf-math-gma-exams">Project source</a>',
            rendered,
        )
        self.assertIn('<a href="../../../index.html">All exam subjects</a>', rendered)
        self.assertIn(
            '<a href="../index.html">Algebra First-Year Exams</a>', rendered
        )
        self.assertIn(
            '<a href="algebra-first-year-2025-may-part-1.source.pdf">Original PDF</a>',
            rendered,
        )
        self.assertLess(rendered.index("Project source"), rendered.index("All exam subjects"))
        self.assertIn(
            '<p class="page-updated">Page updated <time datetime="2026-07-20">'
            "July 20, 2026</time>.</p>",
            rendered,
        )
        self.assertNotIn('target="_blank"', rendered)
        self.assertNotIn("border-left", rendered)
        self.assertIn("footer { display: none; }", rendered)
        self.assertIn("body { font-size: 11pt; line-height: 1.28;", rendered)
        self.assertIn(".institution { margin-bottom: .2rem; font-size: 9pt; }", rendered)
        self.assertIn('.institution a { text-decoration: none; }', rendered)

    def test_html_places_problem_concern_before_source_text(self) -> None:
        item = source()
        problem = make_problem(
            text=r"Let \(p\) be prime and prove the assertion.", subparts=[]
        )
        problem.concerns = [
            ProblemConcern(
                status=ConcernStatus.SUSPECTED,
                explanation=r"The assertion appears to fail when \(p=2\).",
            )
        ]

        rendered = render_html(exam_for(item, [problem]))

        self.assertIn('<li class="problem" id="problem-1">', rendered)
        self.assertIn('<div class="problem-concern" role="note">', rendered)
        self.assertIn("<strong>Warning: Suspected error.</strong>", rendered)
        self.assertIn("color: #7a1f1f", rendered)
        self.assertLess(
            rendered.index("Warning: Suspected error."),
            rendered.index(r"Let \(p\) be prime"),
        )

    def test_problem_concerns_must_be_nonempty_and_unique(self) -> None:
        item = source()
        problem = make_problem(text="Prove it.", subparts=[])
        problem.concerns = [
            ProblemConcern(status=ConcernStatus.SUSPECTED, explanation=" "),
            ProblemConcern(status=ConcernStatus.SUSPECTED, explanation=" "),
        ]

        errors = validate_exam(exam_for(item, [problem]), item, [])

        self.assertIn("problem index 1 has an empty concern", errors)
        self.assertIn("problem index 1 has duplicate concerns", errors)

    def test_problem_concern_rejects_unwrapped_unicode_math(self) -> None:
        item = source()
        problem = make_problem(text="Prove it.", subparts=[])
        problem.concerns = [
            ProblemConcern(
                status=ConcernStatus.SUSPECTED,
                explanation="The source asserts σ_n ≥ 0.",
            )
        ]

        errors = validate_exam(exam_for(item, [problem]), item, [])

        self.assertTrue(
            any("Unicode math outside MathJax delimiters" in error for error in errors)
        )

    def test_html_preserves_section_numbering_and_instruction_math(self) -> None:
        item = source()
        exam = exam_for(item, [make_problem(text="Preamble problem.", subparts=[])])
        exam.content.extend(
            [
                SectionBlock(
                    heading="II. Set Theory",
                    numbering=NumberingMode.RESTART,
                    content=[
                        InstructionsBlock(
                            text="Use this identity.\n\\[\na^2+b^2=c^2\n\\]"
                        ),
                        ProblemBlock(problem=make_problem(text="First theorem.", subparts=[])),
                        ProblemBlock(problem=make_problem(text="Second theorem.", subparts=[])),
                    ],
                ),
                SectionBlock(
                    heading="SECTION III",
                    numbering=NumberingMode.CONTINUE,
                    content=[
                        ProblemBlock(problem=make_problem(text="Final theorem.", subparts=[]))
                    ],
                ),
            ]
        )

        rendered = render_html(exam)

        self.assertIn('<section aria-labelledby="section-1">', rendered)
        self.assertIn('<h2 id="section-1">II. Set Theory</h2>', rendered)
        self.assertEqual(rendered.count('<ol class="problems" start="1">'), 2)
        self.assertIn('<ol class="problems" start="3">', rendered)
        self.assertIn('<div class="instructions">', rendered)
        self.assertIn(
            '<div class="display-math">\\[\na^2+b^2=c^2\n\\]</div>', rendered
        )

    def test_qualifying_exam_html_title(self) -> None:
        item = replace(
            source(),
            id="algebra-qualifying-2026-jan-part-1",
            subject="Algebra Qualifying Exam",
            subject_tag="algebra-qualifying",
            year=2026,
            month="january",
        )
        exam = exam_for(item, [make_problem(text="Prove it.", subparts=[])])

        self.assertIn(
            "<h1>Algebra Qualifying Exam, January 2026, Part 1</h1>",
            render_html(exam),
        )

    def test_html_supplies_stub_for_parts_without_a_stem(self) -> None:
        item = source()
        exam = exam_for(
            item,
            [
                make_problem(
                    text="",
                    subparts=[
                        Subpart(label="(a)", text="First.", subparts=[]),
                        Subpart(label="(b)", text="Second.", subparts=[]),
                    ],
                )
            ],
        )

        rendered = render_html(exam)
        self.assertIn("This problem has two parts.", rendered)
        self.assertIn('<span class="subpart-label">(a)</span>', rendered)
        self.assertIn('<span class="subpart-label">(b)</span>', rendered)

    def test_instruction_only_section_is_valid(self) -> None:
        item = source()
        exam = exam_for(item, [make_problem(text="First theorem.", subparts=[])])
        exam.content.append(
            SectionBlock(
                heading="II",
                numbering=NumberingMode.RESTART,
                content=[InstructionsBlock(text="Prove the first theorem.")],
            )
        )

        self.assertEqual(validate_exam(exam, item, []), [])
        rendered = render_html(exam)
        self.assertIn('<h2 id="section-1">II</h2>', rendered)
        self.assertIn("Prove the first theorem.", rendered)
        exam.content[-1].content = []
        self.assertIn("section 'II' is empty", validate_exam(exam, item, []))

    def test_correction_requires_review_evidence(self) -> None:
        item = source()
        exam = exam_for(item, [make_problem(text="Prove it.", subparts=[])])
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
