from __future__ import annotations

from pathlib import Path
import unittest

from build_indexes import (
    ConcernEntry,
    archive_level,
    render_concerns_index,
    render_root_index,
    render_subject_index,
    subject_heading,
    subject_name,
)
from extract_exams import ConcernStatus, DocumentType, ProblemConcern, SourceExam


def source(
    subject_tag: str,
    subject: str,
    year: int,
    month: str,
    part: int | None = None,
) -> SourceExam:
    suffix = f"-part-{part}" if part is not None else ""
    exam_id = f"{subject_tag}-{year}-{month[:3]}{suffix}"
    return SourceExam(
        id=exam_id,
        subject=subject,
        subject_tag=subject_tag,
        year=year,
        month=month,
        part=part,
        pdf_url=f"https://example.edu/{exam_id}.pdf",
        pdf_path=Path("exams") / subject_tag / exam_id / f"{exam_id}.source.pdf",
        sha256="abc",
        download_sha256="abc",
    )


def practice_source(variant: str, part: int) -> SourceExam:
    exam_id = f"algebra-first-year-practice-{variant.lower()}-part-{part}"
    return SourceExam(
        id=exam_id,
        subject="First Year Algebra",
        subject_tag="algebra-first-year",
        year=None,
        month=None,
        part=part,
        pdf_url=f"https://example.edu/{exam_id}.pdf",
        pdf_path=Path("exams") / "algebra-first-year" / exam_id / f"{exam_id}.source.pdf",
        sha256="abc",
        download_sha256="abc",
        practice_variant=variant,
    )


def practice_collection() -> SourceExam:
    exam_id = "algebra-first-year-practice-problems"
    return SourceExam(
        id=exam_id,
        subject="First Year Algebra",
        subject_tag="algebra-first-year",
        year=None,
        month=None,
        part=None,
        pdf_url="https://example.edu/fypoolalg.pdf",
        pdf_path=Path("exams") / "algebra-first-year" / exam_id / f"{exam_id}.source.pdf",
        sha256="abc",
        download_sha256="abc",
        document_type=DocumentType.PRACTICE_PROBLEMS,
        problem_count=113,
    )


class IndexRenderingTests(unittest.TestCase):
    def test_level_and_subject_labels_are_derived_from_archive_metadata(self) -> None:
        qualifying = source(
            "algebra-qualifying", "Algebra Qualifying Exam", 2025, "august"
        )
        first_year = source(
            "numerical-analysis-first-year",
            "First Year Numerical Analysis",
            2024,
            "may",
        )
        phd = source("logic-phd", "PhD Logic", 2020, "january")

        self.assertEqual(archive_level(qualifying.subject_tag).key, "qualifying")
        self.assertEqual(subject_name(first_year), "Numerical Analysis")
        self.assertEqual(subject_heading(phd), "Logic PhD Exams")

    def test_root_index_orders_levels_then_subjects(self) -> None:
        exams = [
            source("topology-phd", "PhD Topology", 2020, "january"),
            source("algebra-phd", "PhD Algebra", 2020, "january"),
            source(
                "topology-first-year", "First Year Topology", 2020, "january"
            ),
            source(
                "analysis-qualifying", "Analysis Qualifying Exam", 2025, "august"
            ),
        ]

        rendered = render_root_index(
            exams, concern_count=2, concerned_exam_count=1
        )

        self.assertLess(
            rendered.index('id="level-1">Qualifying'),
            rendered.index('id="level-2">First-Year'),
        )
        self.assertLess(
            rendered.index('id="level-2">First-Year'),
            rendered.index('id="level-3">PhD'),
        )
        self.assertLess(
            rendered.index("exams/algebra-phd/index.html"),
            rendered.index("exams/topology-phd/index.html"),
        )
        self.assertIn('<span class="count">1 exam</span>', rendered)
        self.assertIn(
            '<a href="exams/algebra-phd/index.html">Algebra</a>\n'
            '            <span class="count">1 exam</span>',
            rendered,
        )
        self.assertIn('<nav aria-label="Exam archive">', rendered)
        self.assertIn(
            '<a href="concerns.html">Known or suspected errors</a>', rendered
        )
        self.assertIn(
            '<span class="count">2 concerns across 1 exam</span>', rendered
        )
        self.assertLess(
            rendered.index("    </nav>"),
            rendered.index('<p class="concerns-link">'),
        )
        self.assertLess(
            rendered.index('<p class="concerns-link">'),
            rendered.index("    <footer>"),
        )
        self.assertIn("margin: 3rem 0 1.5rem;", rendered)
        self.assertIn('href="#main-content">Skip to main content</a>', rendered)
        self.assertNotIn("gma.math.ufl.edu", rendered)
        self.assertIn(
            '<p class="page-updated">Page updated <time datetime="2026-07-20">'
            "July 20, 2026</time>.</p>",
            rendered,
        )

    def test_subject_index_is_semantic_and_newest_first(self) -> None:
        exams = [
            source("algebra-phd", "PhD Algebra", 2024, "august", 2),
            source("algebra-phd", "PhD Algebra", 2025, "january"),
            source("algebra-phd", "PhD Algebra", 2024, "august", 1),
        ]

        rendered = render_subject_index("algebra-phd", exams)

        self.assertIn("<h1>Algebra PhD Exams</h1>", rendered)
        self.assertIn('<div class="table-wrap" role="region" tabindex="0"', rendered)
        self.assertIn('<th scope="col">Date</th>', rendered)
        self.assertIn('<th scope="row"><time datetime="2025-01">', rendered)
        self.assertLess(
            rendered.index("algebra-phd-2025-jan/index.html"),
            rendered.index("algebra-phd-2024-aug-part-1/index.html"),
        )
        self.assertLess(
            rendered.index("algebra-phd-2024-aug-part-1/index.html"),
            rendered.index("algebra-phd-2024-aug-part-2/index.html"),
        )
        self.assertIn('href="../../index.html">All exam subjects</a>', rendered)
        self.assertIn(
            'href="algebra-phd-2025-jan/algebra-phd-2025-jan.source.pdf">View PDF</a>',
            rendered,
        )
        self.assertIn(".institution a { text-decoration: none; }", rendered)
        self.assertNotIn('class="breadcrumb"', rendered)
        self.assertNotIn("gma.math.ufl.edu", rendered)
        self.assertLess(rendered.index("Project source"), rendered.index("All exam subjects"))

    def test_subject_index_puts_undated_practice_exams_last(self) -> None:
        dated = source("algebra-first-year", "First Year Algebra", 2013, "january", 1)
        practice_a_1 = practice_source("A", 1)
        practice_a_2 = practice_source("A", 2)
        practice_b_1 = practice_source("B", 1)

        rendered = render_subject_index(
            "algebra-first-year",
            [practice_b_1, practice_a_2, dated, practice_a_1],
        )

        self.assertIn("newest first; undated practice exams last", rendered)
        self.assertIn('<th scope="col">Date or practice</th>', rendered)
        self.assertLess(rendered.index(dated.id), rendered.index(practice_a_1.id))
        self.assertLess(rendered.index(practice_a_1.id), rendered.index(practice_a_2.id))
        self.assertLess(rendered.index(practice_a_2.id), rendered.index(practice_b_1.id))
        self.assertNotIn('datetime="None-', rendered)

    def test_subject_index_features_collection_outside_exam_table(self) -> None:
        dated = source("algebra-first-year", "First Year Algebra", 2013, "january", 1)
        collection = practice_collection()

        rendered = render_subject_index(
            "algebra-first-year", [dated, collection]
        )

        featured = (
            '<a href="algebra-first-year-practice-problems/index.html">'
            "Practice Problems</a>"
        )
        self.assertIn(featured, rendered)
        self.assertIn('113<span class="sr-only"> problems</span>', rendered)
        self.assertLess(rendered.index(featured), rendered.index("<table>"))
        self.assertIn("<caption>1 exam, newest first</caption>", rendered)
        self.assertNotIn(
            "algebra-first-year-practice-problems/algebra-first-year-practice-problems.source.pdf",
            rendered,
        )

    def test_concerns_index_formats_numbers_and_sorts_subject_then_date(self) -> None:
        analysis = source("analysis-phd", "PhD Analysis", 1997, "january")
        older_algebra = source("algebra-phd", "PhD Algebra", 1995, "may")
        newer_algebra = source("algebra-phd", "PhD Algebra", 2001, "september")
        concern = ProblemConcern(
            status=ConcernStatus.SUSPECTED,
            explanation=r"The endpoint \(1\) may be inconsistent with the domain.",
        )

        rendered = render_concerns_index(
            [
                ConcernEntry(
                    source=analysis,
                    problem_index=16,
                    displayed_number=8,
                    section_heading="III.",
                    concern=concern,
                ),
                ConcernEntry(
                    source=older_algebra,
                    problem_index=2,
                    displayed_number=2,
                    section_heading=None,
                    concern=concern,
                ),
                ConcernEntry(
                    source=newer_algebra,
                    problem_index=4,
                    displayed_number=4,
                    section_heading=None,
                    concern=concern,
                ),
            ]
        )

        self.assertIn("<h1>Known or Suspected Errors</h1>", rendered)
        self.assertIn("mathjax@4/tex-chtml.js", rendered)
        self.assertIn("AI-assisted extraction", rendered)
        self.assertIn("have not been reviewed by a human", rendered)
        self.assertNotIn("University of Florida faculty", rendered)
        self.assertIn('<strong class="concern-number">8.</strong>', rendered)
        self.assertNotIn("#problem-16", rendered)
        self.assertIn("<strong>Warning: Suspected error.</strong>", rendered)
        self.assertIn(r"The endpoint \(1\) may be inconsistent", rendered)
        self.assertIn('role="note"', rendered)
        self.assertIn(
            ".concern-exam h2 { margin-bottom: .9rem; padding-bottom: 0; border-bottom: 0; }",
            rendered,
        )
        self.assertLess(
            rendered.index("Algebra PhD Exam, September 2001"),
            rendered.index("Algebra PhD Exam, May 1995"),
        )
        self.assertLess(
            rendered.index("Algebra PhD Exam, May 1995"),
            rendered.index("Analysis PhD Exam, January 1997"),
        )


if __name__ == "__main__":
    unittest.main()
