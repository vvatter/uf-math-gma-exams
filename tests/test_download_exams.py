from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from download_exams import (
    QUALIFYING_INDEX_URL,
    Subject,
    download_candidates,
    discover_exams,
    discover_subjects,
    exam_stem,
    label_suffix,
    normalize_pdf_url,
    parse_date,
    previous_download_metadata,
    refresh_local_metadata,
    subject_tag,
)


class NamingTests(unittest.TestCase):
    def test_subject_tags(self) -> None:
        self.assertEqual(subject_tag("First Year Numerical Analysis"), "numerical-analysis-first-year")
        self.assertEqual(subject_tag("PhD Numerical Analysis"), "numerical-analysis-phd")
        self.assertEqual(
            subject_tag("PhD Variational Analysis/Numerical Optimization"),
            "numerical-optimization-phd",
        )
        self.assertEqual(subject_tag("PhD Partial Differential Equations"), "pde-phd")
        self.assertEqual(subject_tag("Algebra Qualifying Exam"), "algebra-qualifying")
        self.assertEqual(
            subject_tag("Numerical Analysis Qualifying Exam"),
            "numerical-analysis-qualifying",
        )

    def test_qualifying_index_subjects(self) -> None:
        html = """
        <a href="/past-exams/qualifying-exams/algebra-qualifying-exam/">
          Algebra Qualifying Exam
        </a>
        <a href="/past-exams/qualifying-exams/topology-qualifying-exam/">
          Topology Qualifying Exam
        </a>
        """

        import download_exams

        original = download_exams.fetch_html
        download_exams.fetch_html = lambda _url: html
        try:
            subjects = discover_subjects(QUALIFYING_INDEX_URL)
        finally:
            download_exams.fetch_html = original

        self.assertEqual(
            [(item.title, item.tag) for item in subjects],
            [
                ("Algebra Qualifying Exam", "algebra-qualifying"),
                ("Topology Qualifying Exam", "topology-qualifying"),
            ],
        )

    def test_date_parser_preserves_source_month(self) -> None:
        self.assertEqual(parse_date("2026 January"), (2026, "january"))
        self.assertEqual(parse_date("2017 April"), (2017, "april"))

    def test_part_labels(self) -> None:
        self.assertEqual(label_suffix("Part 2", "Part 2"), "part-2")
        self.assertIsNone(label_suffix("Exam", "Link"))

    def test_exam_stem_places_year_before_month(self) -> None:
        self.assertEqual(
            exam_stem("algebra-first-year", 2025, "august", "part-1"),
            "algebra-first-year-2025-aug-part-1",
        )

    def test_legacy_pdf_urls_prefer_the_modern_https_path(self) -> None:
        legacy = "http://gma.math.ufl.edu/gma/wp-content/uploads/sites/130/exam.pdf"
        modern = "https://gma.math.ufl.edu/wp-content/uploads/sites/130/exam.pdf"

        self.assertEqual(normalize_pdf_url(legacy, "https://gma.math.ufl.edu/"), modern)
        self.assertEqual(download_candidates(legacy)[0], modern)

    def test_refresh_preserves_download_hash_and_updates_working_hash(self) -> None:
        content = b"%PDF-1.4\noptimized working bytes\n"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            pdf_path = root / "exam.pdf"
            manifest_path = root / "manifest.json"
            pdf_path.write_bytes(content)
            manifest_path.write_text(
                json.dumps(
                    {
                        "exams": [
                            {
                                "path": str(pdf_path),
                                "size": 100,
                                "sha256": "download-hash",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            self.assertEqual(refresh_local_metadata(manifest_path), (1, 1))
            item = json.loads(manifest_path.read_text(encoding="utf-8"))["exams"][0]

        self.assertEqual(item["download_size"], 100)
        self.assertEqual(item["download_sha256"], "download-hash")
        self.assertEqual(item["size"], len(content))
        self.assertEqual(item["sha256"], hashlib.sha256(content).hexdigest())

    def test_previous_acquisition_metadata_survives_rediscovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest_path = Path(temp) / "manifest.json"
            manifest_path.write_text(
                json.dumps(
                    {
                        "exams": [
                            {
                                "path": "exams/example.pdf",
                                "download_size": 123,
                                "download_sha256": "original-hash",
                                "resolved_url": "https://example.edu/exam.pdf",
                                "status": "downloaded",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            metadata = previous_download_metadata(manifest_path)["exams/example.pdf"]

        self.assertEqual(
            metadata,
            {
                "download_size": 123,
                "download_sha256": "original-hash",
                "resolved_url": "https://example.edu/exam.pdf",
                "status": "downloaded",
            },
        )


class TableTests(unittest.TestCase):
    def test_table_rows_produce_stable_names_and_collision_suffixes(self) -> None:
        html = """
        <table id="tablepress-1" class="tablepress">
          <thead><tr><th>Date</th><th>Part 1</th><th>Part 2</th></tr></thead>
          <tbody>
            <tr><td>2025 August</td>
              <td><a href="/wp-content/one.pdf">Part 1</a></td>
              <td><a href="/wp-content/two.pdf">Part 2</a></td>
            </tr>
            <tr><td>2025 August</td>
              <td><a href="/wp-content/other.pdf">Part 1</a></td><td></td>
            </tr>
          </tbody>
        </table>
        """
        subject = Subject(
            "First Year Algebra",
            "algebra-first-year",
            "https://gma.math.ufl.edu/past-exams/example/",
        )

        import download_exams

        original = download_exams.fetch_html
        download_exams.fetch_html = lambda _url: html
        try:
            exams = discover_exams(subject, download_exams.Path("exams"))
        finally:
            download_exams.fetch_html = original

        self.assertEqual(
            [exam.path for exam in exams],
            [
                "exams/algebra-first-year/algebra-first-year-2025-aug-part-1.pdf",
                "exams/algebra-first-year/algebra-first-year-2025-aug-part-2.pdf",
                "exams/algebra-first-year/algebra-first-year-2025-aug-part-1-2.pdf",
            ],
        )


if __name__ == "__main__":
    unittest.main()
