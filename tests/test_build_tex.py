from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from build_tex import (
    escape_text,
    next_attempt_directory,
    render_standalone_figure_tex,
    render_tex,
    render_text,
)
from extract_exams import (
    ConcernStatus,
    ExamRecord,
    InstructionsBlock,
    NumberingMode,
    Problem,
    ProblemConcern,
    ProblemTextBlock,
    ProblemBlock,
    SectionBlock,
    Subpart,
    TikzBlock,
)


def make_problem(text: str, subparts: list[Subpart]) -> Problem:
    body = [ProblemTextBlock(text=text)] if text else []
    return Problem(body=body, subparts=subparts)


class TexRenderingTests(unittest.TestCase):
    def exam(self) -> ExamRecord:
        return ExamRecord(
            id="algebra-phd-1988-sep",
            subject="PhD Algebra",
            subject_tag="algebra-phd",
            year=1988,
            month="september",
            part=None,
            pdf_url="https://example.edu/exam.pdf",
            content=[
                InstructionsBlock(text="Do two problems."),
                SectionBlock(
                    heading="I. Algebra & Geometry",
                    numbering=NumberingMode.RESTART,
                    content=[
                        ProblemBlock(
                            problem=make_problem(
                                text=(
                                    "Let \\(A\\) be a ring.\n\\[\n"
                                    "\\require{amscd}\\begin{CD}A @>>> B\\end{CD}\n\\]"
                                ),
                                subparts=[
                                    Subpart(label="(a)", text="Prove it.", subparts=[])
                                ],
                            )
                        )
                    ],
                ),
            ],
        )

    def test_plain_text_escaping_does_not_touch_math(self) -> None:
        self.assertEqual(escape_text("A&B_1"), r"A\&B\_1")
        self.assertEqual(
            render_text(r"For A&B, use \(x_1&x_2\)."),
            r"For A\&B, use \(x_1&x_2\).",
        )

    def test_single_glyph_math_stays_with_its_introducing_word(self) -> None:
        self.assertEqual(render_text(r"Let \(x\) be fixed."), r"Let~\(x\) be fixed.")
        self.assertEqual(
            render_text(r"Choose \(\mathbb{R}\) as the field."),
            r"Choose~\(\mathbb{R}\) as the field.",
        )
        self.assertEqual(
            render_text(r"The first case. \(x\) is positive."),
            r"The first case. \(x\) is positive.",
        )
        self.assertEqual(
            render_text(r"Let \(x_1\) be fixed."), r"Let \(x_1\) be fixed."
        )

    def test_math_font_arguments_are_grouped_in_scripts(self) -> None:
        self.assertEqual(
            render_text(r"Integrate \(\int_\mathbb R f(x)\,dx\)."),
            render_text(r"Integrate \(\int_{\mathbb{R}} f(x)\,dx\)."),
        )

    def test_renderer_enables_pdf_ua_2_mathml_and_cleans_mathjax_require(self) -> None:
        rendered = render_tex(self.exam())

        self.assertIn("pdfstandard=ua-2", rendered)
        self.assertIn("math/setup=mathml-SE", rendered)
        self.assertIn(r"\usepackage{newcomputermodern}", rendered)
        self.assertIn(r"\providecommand{\square}{\mdlgwhtsquare}", rendered)
        self.assertIn(r"\section{I. Algebra \& Geometry}", rendered)
        self.assertIn(r"\begin{examinstructions}", rendered)
        self.assertIn(r"\renewcommand{\labelenumi}{\textbf{\theenumi.}}", rendered)
        self.assertIn(
            r"University of Florida}, \href{https://math.ufl.edu/}{Department of Mathematics}",
            rendered,
        )
        self.assertIn(r"\hrule height 1pt", rendered)
        self.assertIn(r"\tagmcbegin{artifact}", rendered)
        self.assertIn(r"\newpage\null\vskip -1em", rendered)
        self.assertIn(r"\vskip -0.5em", rendered)
        self.assertIn(r"\vskip 0.25em", rendered)
        self.assertIn(r"\vskip 1em", rendered)
        self.assertIn(r"\pagestyle{empty}", rendered)
        self.assertIn(
            r"\href{https://gma.math.ufl.edu/exams/algebra-phd/}{Algebra PhD Exam}, September 1988",
            rendered,
        )
        self.assertNotIn(
            r"\href{https://gma.math.ufl.edu/exams/algebra-phd/}{Algebra PhD Exam, September 1988}",
            rendered,
        )
        self.assertIn(r"\item[\textnormal{(a)}]", rendered)
        self.assertIn(r"\begin{CD}A @>>> B\end{CD}", rendered)
        self.assertIn(r"math/mathml/structelem=false", rendered)
        self.assertNotIn(r"\require{amscd}", rendered)

    def test_renderer_titles_undated_practice_exams_without_a_date(self) -> None:
        exam = self.exam().model_copy(
            update={
                "id": "algebra-first-year-practice-b-part-2",
                "subject": "First Year Algebra",
                "subject_tag": "algebra-first-year",
                "year": None,
                "month": None,
                "part": 2,
                "practice_variant": "B",
            }
        )

        rendered = render_tex(exam)

        self.assertIn(r"\title{Algebra First-Year Practice Exam B, Part 2}", rendered)
        self.assertNotIn("None", rendered)

    def test_empty_problem_stem_gets_presentation_only_summary(self) -> None:
        exam = self.exam()
        exam.content = [
            ProblemBlock(
                problem=make_problem(
                    text="",
                    subparts=[
                        Subpart(label="(a)", text="First.", subparts=[]),
                        Subpart(label="(b)", text="Second.", subparts=[]),
                    ],
                )
            )
        ]

        self.assertIn("This problem has two parts.", render_tex(exam))

    def test_problem_concern_is_tagged_colored_and_precedes_source_text(self) -> None:
        exam = self.exam()
        problem = make_problem(text=r"Prove the claim for \(p\).", subparts=[])
        problem.concerns = [
            ProblemConcern(
                status=ConcernStatus.SUSPECTED,
                explanation=r"The claim appears to fail when \(p=2\).",
            )
        ]
        exam.content = [ProblemBlock(problem=problem)]

        rendered = render_tex(exam)

        self.assertIn(r"\definecolor{ProblemConcern}{HTML}{7A1F1F}", rendered)
        self.assertIn(r"\tagstructbegin{tag=Aside}", rendered)
        self.assertIn(r"\textbf{Warning: Suspected error.}", rendered)
        self.assertLess(
            rendered.index("Warning: Suspected error."),
            rendered.index("Prove the claim"),
        )

    def test_tikz_figure_is_vector_tagged_and_has_standalone_png_source(self) -> None:
        exam = self.exam()
        figure = TikzBlock(
            id="labeled-square",
            alt="A square with four labeled vertices.",
            libraries=["arrows.meta"],
            options=["line cap=round"],
            height_lines=10,
            code=r"\draw (0,0) rectangle (1,1);",
        )
        exam.content = [
            ProblemBlock(
                problem=Problem(
                    body=[
                        ProblemTextBlock(text="Consider the diagram."),
                        figure,
                    ],
                    subparts=[],
                )
            )
        ]

        rendered = render_tex(exam)
        standalone = render_standalone_figure_tex(figure)

        self.assertIn(r"\usetikzlibrary{arrows.meta}", rendered)
        self.assertIn(r"alt={A square with four labeled vertices.}", rendered)
        self.assertIn(r"max width=.8\linewidth,max totalheight=10\baselineskip", rendered)
        self.assertIn(r"\draw (0,0) rectangle (1,1);", rendered)
        self.assertIn(r"\documentclass[tikz,border=4mm]{standalone}", standalone)
        self.assertNotIn("alt={", standalone)

    def test_build_attempts_do_not_reuse_partial_auxiliary_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            first = next_attempt_directory(parent)
            (first / "partial.aux").write_text("incomplete", encoding="utf-8")
            second = next_attempt_directory(parent)

            self.assertEqual(first.name, "attempt-001")
            self.assertEqual(second.name, "attempt-002")
            self.assertFalse((second / "partial.aux").exists())


if __name__ == "__main__":
    unittest.main()
