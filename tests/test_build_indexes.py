from __future__ import annotations

from pathlib import Path
import unittest

from build_indexes import (
    archive_level,
    render_root_index,
    render_subject_index,
    subject_heading,
    subject_name,
)
from extract_exams import SourceExam


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

        rendered = render_root_index(exams)

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


if __name__ == "__main__":
    unittest.main()
