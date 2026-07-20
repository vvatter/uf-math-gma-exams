from __future__ import annotations

import unittest

from extract_exams import Problem, ProblemTextBlock
from extract_practice_problems import (
    CHUNKS,
    ChunkExtraction,
    NumberedProblem,
    validate_chunk,
)


class PracticeProblemExtractionTests(unittest.TestCase):
    def test_chunks_cover_one_through_113_exactly_once(self) -> None:
        numbers = [
            number
            for chunk in CHUNKS
            for number in range(chunk.first_problem, chunk.last_problem + 1)
        ]

        self.assertEqual(numbers, list(range(1, 114)))
        spanning = next(chunk for chunk in CHUNKS if chunk.key == "pages-03-04")
        self.assertEqual(spanning.pages, (3, 4))
        self.assertLessEqual(spanning.first_problem, 42)
        self.assertGreaterEqual(spanning.last_problem, 42)

    def test_chunk_validator_rejects_a_numbering_gap(self) -> None:
        spec = CHUNKS[-1]
        problem = Problem(
            body=[ProblemTextBlock(text="Prove it.")],
            subparts=[],
        )
        extraction = ChunkExtraction(
            problems=[
                NumberedProblem(source_number=111, problem=problem),
                NumberedProblem(source_number=113, problem=problem),
            ],
            review_flags=[],
        )

        errors = validate_chunk(extraction, spec)

        self.assertTrue(any("expected problem numbers" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
