#!/usr/bin/env python3
"""Render exam JSON as tagged LaTeX and compile accessible PDFs."""

from __future__ import annotations

import argparse
from concurrent.futures import as_completed, ThreadPoolExecutor
from dataclasses import dataclass
import os
from pathlib import Path
import re
import signal
import shutil
import subprocess
import tempfile
from typing import Iterable

from extract_exams import (
    ExamRecord,
    InstructionsBlock,
    NumberingMode,
    Problem,
    ProblemTextBlock,
    ProblemBlock,
    SectionBlock,
    SourceExam,
    Subpart,
    TikzBlock,
    exam_figure_png_path,
    exam_json_path,
    exam_pdf_path,
    exam_tex_path,
    exam_title,
    iter_tikz_blocks,
    load_sources,
    write_text,
)


PROTOTYPE_IDS = (
    "algebra-phd-1988-sep",
    "analysis-phd-1997-jan",
    "combinatorics-phd-1991-may",
    "logic-phd-2006-aug",
    "numerical-analysis-phd-2021-aug",
)
PUBLIC_EXAM_ROOT = "https://gma.math.ufl.edu/exams"
MATH_SEGMENT = re.compile(r"(\\\((?:.|\n)*?\\\)|\\\[(?:.|\n)*?\\\])")
SINGLE_MATH_ATOM = re.compile(
    r"(?:[^\W_]|\\[A-Za-z]+|\\(?:mathbb|mathcal|mathbf|mathrm|mathsf|mathtt|mathit)\{[^\W_]\})",
    re.UNICODE,
)
PARAGRAPH_SENTINEL = "\ue000"
SMALL_NUMBERS = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)


@dataclass(frozen=True)
class BuildResult:
    exam_id: str
    tex_path: Path
    pdf_path: Path
    temporary_bytes: int


def escape_text(value: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "{": r"\{",
        "}": r"\}",
        "#": r"\#",
        "$": r"\$",
        "%": r"\%",
        "&": r"\&",
        "_": r"\_",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(character, character) for character in value)


def render_prose_segment(value: str) -> str:
    value = re.sub(r"\n\s*\n+", PARAGRAPH_SENTINEL, value)
    value = re.sub(r"[ \t\r\n]+", " ", value)
    value = escape_text(value)
    return value.replace(PARAGRAPH_SENTINEL, "\n\n\\par\n")


def normalize_math(value: str) -> str:
    value = re.sub(r"\\require\{amscd\}\s*", "", value)
    value = re.sub(
        r"([_^])\\(mathbb|mathcal|mathbf|mathrm|mathsf|mathtt|mathit)\s+([A-Za-z0-9])",
        lambda match: rf"{match.group(1)}{{\{match.group(2)}{{{match.group(3)}}}}}",
        value,
    )
    return value.strip()


def prevent_orphaned_math(rendered: list[str], math: str) -> None:
    """Keep a one-glyph inline expression with the word that introduces it."""
    if not SINGLE_MATH_ATOM.fullmatch(math) or not rendered:
        return
    prose = rendered[-1]
    if not prose.endswith(" "):
        return
    preceding = prose[:-1].rstrip()
    if preceding and (preceding[-1].isalnum() or preceding[-1] in ")]}"):
        rendered[-1] = prose[:-1] + "~"


def render_display_math(math: str) -> str:
    if r"\begin{CD}" in math:
        # luamml cannot currently translate amscd and can loop indefinitely.
        # Keep the tagged Formula and visual diagram, but skip nested MathML.
        return (
            "\n{\\tagpdfsetup{math/mathml/structelem=false,math/mathml/AF=false,math/alt/use=true}\n"
            "\\[\n"
            f"{math}\n"
            "\\]\n"
            "}\n"
        )
    return f"\n\\[\n{math}\n\\]\n"


def render_text(value: str) -> str:
    rendered: list[str] = []
    position = 0
    for match in MATH_SEGMENT.finditer(value):
        rendered.append(render_prose_segment(value[position : match.start()]))
        segment = match.group(0)
        math = normalize_math(segment[2:-2])
        if segment.startswith(r"\["):
            rendered.append(render_display_math(math))
        else:
            prevent_orphaned_math(rendered, math)
            rendered.append(r"\(" + math + r"\)")
        position = match.end()
    rendered.append(render_prose_segment(value[position:]))
    return "".join(rendered).strip()


def count_phrase(count: int, noun: str) -> str:
    amount = SMALL_NUMBERS[count] if count < len(SMALL_NUMBERS) else str(count)
    return f"This {noun} has {amount} {'part' if count == 1 else 'parts'}."


def render_subparts(subparts: list[Subpart], depth: int = 0) -> list[str]:
    if not subparts:
        return []
    lines = [r"\begin{examsubparts}"]
    for subpart in subparts:
        label = escape_text(subpart.label.strip())
        lines.append(rf"\item[\textnormal{{{label}}}]")
        if subpart.text.strip():
            lines.append(render_text(subpart.text))
        elif subpart.subparts:
            lines.append(count_phrase(len(subpart.subparts), "part"))
        lines.extend(render_subparts(subpart.subparts, depth + 1))
    lines.append(r"\end{examsubparts}")
    return lines


def render_problem(problem: Problem) -> list[str]:
    lines = [r"\item"]
    for body_block in problem.body:
        if isinstance(body_block, ProblemTextBlock):
            lines.append(render_text(body_block.text))
        else:
            lines.extend(render_tikz_block(body_block))
    if not problem.body and problem.subparts:
        lines.append(count_phrase(len(problem.subparts), "problem"))
    lines.extend(render_subparts(problem.subparts))
    return lines


def render_problem_run(problems: list[Problem], starting_after: int) -> list[str]:
    lines = [rf"\begin{{examproblems}}{{{starting_after}}}"]
    for problem in problems:
        lines.extend(render_problem(problem))
    lines.append(r"\end{examproblems}")
    return lines


def render_instruction(block: InstructionsBlock) -> list[str]:
    return [r"\begin{examinstructions}", render_text(block.text), r"\end{examinstructions}"]


def tikz_options(figure: TikzBlock, include_alt: bool) -> str:
    options = list(figure.options)
    if include_alt:
        options.insert(0, f"alt={{{escape_text(figure.alt)}}}")
    if not options:
        return ""
    return "[\n  " + ",\n  ".join(options) + "\n]"


def render_tikz_block(figure: TikzBlock) -> list[str]:
    return [
        r"\par\smallskip",
        r"\begin{center}",
        rf"\begin{{adjustbox}}{{max width=.8\linewidth,max totalheight={figure.height_lines}\baselineskip}}",
        rf"\begin{{tikzpicture}}{tikz_options(figure, include_alt=True)}",
        figure.code.rstrip(),
        r"\end{tikzpicture}",
        r"\end{adjustbox}",
        r"\end{center}",
        r"\smallskip",
    ]


def render_standalone_figure_tex(figure: TikzBlock) -> str:
    lines = [
        r"\documentclass[tikz,border=4mm]{standalone}",
        r"\usepackage{newcomputermodern}",
    ]
    if figure.libraries:
        lines.append(rf"\usetikzlibrary{{{','.join(figure.libraries)}}}")
    lines.extend(
        [
            r"\begin{document}",
            rf"\begin{{tikzpicture}}{tikz_options(figure, include_alt=False)}",
            figure.code.rstrip(),
            r"\end{tikzpicture}",
            r"\end{document}",
            "",
        ]
    )
    return "\n".join(lines)


def render_content_blocks(
    blocks: Iterable[InstructionsBlock | ProblemBlock], displayed_number: int
) -> tuple[list[str], int]:
    lines: list[str] = []
    pending: list[Problem] = []

    def flush() -> None:
        nonlocal displayed_number
        if not pending:
            return
        lines.extend(render_problem_run(pending, displayed_number))
        displayed_number += len(pending)
        pending.clear()

    for block in blocks:
        if isinstance(block, ProblemBlock):
            pending.append(block.problem)
            continue
        flush()
        lines.extend(render_instruction(block))
    flush()
    return lines, displayed_number


def render_tex(exam: ExamRecord) -> str:
    title = exam_title(exam)
    linked_title, title_suffix = title.split(",", maxsplit=1)
    title_suffix = "," + title_suffix
    escaped_title = escape_text(title)
    escaped_linked_title = escape_text(linked_title)
    escaped_title_suffix = escape_text(title_suffix)
    subject_url = f"{PUBLIC_EXAM_ROOT}/{exam.subject_tag}/"
    tikz_libraries = sorted(
        {library for figure in iter_tikz_blocks(exam) for library in figure.libraries}
    )
    lines = [
        r"\DocumentMetadata{",
        r"  pdfversion=2.0,",
        r"  pdfstandard=ua-2,",
        r"  lang=en-US,",
        r"  tagging=on,",
        r"  tagging-setup={math/setup=mathml-SE,tabsorder=structure}",
        r"}",
        r"\documentclass[11pt,letterpaper]{article}",
        r"\usepackage[margin=0.68in,includefoot]{geometry}",
        r"\usepackage{newcomputermodern}",
        r"\usepackage{amsmath,amscd,mathtools}",
        r"\usepackage{tikz,adjustbox}",
        r"\providecommand{\square}{\mdlgwhtsquare}",
        r"\usepackage[hidelinks]{hyperref}",
        r"\hypersetup{",
        rf"  pdftitle={{{escaped_title}}},",
        r"  pdfauthor={University of Florida Department of Mathematics},",
        r"  pdfsubject={Graduate mathematics examination},",
        r"  pdfdisplaydoctitle=true,",
        r"  bookmarksopen=true",
        r"}",
        r"\setcounter{secnumdepth}{0}",
        r"\setlength{\parindent}{0pt}",
        r"\setlength{\parskip}{0.28em}",
        r"\setlength{\emergencystretch}{3em}",
        r"\setlength{\leftmargini}{2.15em}",
        r"\setlength{\leftmarginii}{2.65em}",
        r"\setlength{\leftmarginiii}{3em}",
        r"\renewcommand{\labelenumi}{\textbf{\theenumi.}}",
        r"\pagestyle{empty}",
        r"\raggedbottom",
        r"\allowdisplaybreaks",
        r"\newenvironment{examproblems}[1]{%",
        r"  \begin{enumerate}%",
        r"  \setcounter{enumi}{#1}%",
        r"  \setlength{\topsep}{0.35em}%",
        r"  \setlength{\partopsep}{0pt}%",
        r"  \setlength{\itemsep}{0.48em}%",
        r"  \setlength{\parsep}{0.18em}%",
        r"}{\end{enumerate}}",
        r"\newenvironment{examsubparts}{%",
        r"  \begin{enumerate}%",
        r"  \setlength{\topsep}{0.18em}%",
        r"  \setlength{\partopsep}{0pt}%",
        r"  \setlength{\itemsep}{0.16em}%",
        r"  \setlength{\parsep}{0.1em}%",
        r"}{\end{enumerate}}",
        r"\newenvironment{examinstructions}{%",
        r"  \par\begingroup\itshape",
        r"}{%",
        r"  \par\endgroup\vspace{0.18em}",
        r"}",
        r"\makeatletter",
        r"\renewcommand\section{\@startsection{section}{1}{0pt}%",
        r"  {-1.25ex plus -.25ex minus -.1ex}%",
        r"  {0.55ex plus .1ex}%",
        r"  {\normalfont\large\bfseries}}",
        r"\renewcommand{\@maketitle}{%",
        r"  \newpage\null\vskip -1em%",
        r"  {\footnotesize\bfseries",
        r"    \href{https://www.ufl.edu/}{University of Florida}, \href{https://math.ufl.edu/}{Department of Mathematics}\par}%",
        r"  \vskip -0.5em%",
        r"  \tagstructbegin{tag=Title}%",
        rf"    {{\LARGE\bfseries\href{{{subject_url}}}{{{escaped_linked_title}}}{escaped_title_suffix}\par}}%",
        r"  \tagstructend%",
        r"  \vskip 0.25em%",
        r"  \tagmcbegin{artifact}%",
        r"    \hrule height 1pt%",
        r"  \tagmcend%",
        r"  \vskip 1em%",
        r"}",
        r"\makeatother",
        rf"\title{{{escaped_title}}}",
        r"\author{}",
        r"\date{}",
        r"\begin{document}",
        r"\maketitle",
        r"\thispagestyle{empty}",
    ]

    if tikz_libraries:
        package_index = lines.index(r"\usepackage{tikz,adjustbox}")
        lines.insert(
            package_index + 1,
            rf"\usetikzlibrary{{{','.join(tikz_libraries)}}}",
        )

    displayed_number = 0
    pending: list[InstructionsBlock | ProblemBlock] = []

    def flush_pending() -> None:
        nonlocal displayed_number
        if not pending:
            return
        rendered, displayed_number = render_content_blocks(pending, displayed_number)
        lines.extend(rendered)
        pending.clear()

    for block in exam.content:
        if not isinstance(block, SectionBlock):
            pending.append(block)
            continue
        flush_pending()
        lines.append(rf"\section{{{escape_text(block.heading.strip())}}}")
        if block.numbering == NumberingMode.RESTART:
            displayed_number = 0
        rendered, displayed_number = render_content_blocks(
            block.content, displayed_number
        )
        lines.extend(rendered)
    flush_pending()
    lines.extend((r"\end{document}", ""))
    return "\n".join(lines)


def directory_size(path: Path) -> int:
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def next_attempt_directory(parent: Path) -> Path:
    parent.mkdir(parents=True, exist_ok=True)
    attempt_numbers = [
        int(match.group(1))
        for item in parent.iterdir()
        if item.is_dir() and (match := re.fullmatch(r"attempt-(\d+)", item.name))
    ]
    attempt = parent / f"attempt-{max(attempt_numbers, default=0) + 1:03d}"
    attempt.mkdir()
    return attempt


def run_latexmk(
    command: list[str],
    workdir: Path,
    environment: dict[str, str],
    timeout_seconds: int,
) -> subprocess.CompletedProcess[str]:
    process = subprocess.Popen(
        command,
        cwd=workdir,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        start_new_session=True,
    )
    try:
        stdout, stderr = process.communicate(timeout=timeout_seconds)
    except subprocess.TimeoutExpired as error:
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            stdout, stderr = process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            stdout, stderr = process.communicate()
        error.stdout = stdout
        error.stderr = stderr
        raise
    return subprocess.CompletedProcess(command, process.returncode, stdout, stderr)


def compile_figure_png(
    source: SourceExam,
    figure: TikzBlock,
    workdir: Path,
    environment: dict[str, str],
    timeout_seconds: int,
) -> Path:
    stem = f"{source.id}.{figure.id}"
    figure_tex = workdir / f"{stem}.figure.tex"
    write_text(figure_tex, render_standalone_figure_tex(figure))
    command = [
        "latexmk",
        "-lualatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        figure_tex.name,
    ]
    result = run_latexmk(command, workdir, environment, timeout_seconds)
    figure_pdf = figure_tex.with_suffix(".pdf")
    if result.returncode != 0 or not figure_pdf.is_file():
        detail = "\n".join((result.stdout + "\n" + result.stderr).splitlines()[-80:])
        raise RuntimeError(f"LuaLaTeX failed for figure {stem}:\n{detail}")

    png_prefix = workdir / stem
    try:
        raster = subprocess.run(
            [
                "pdftocairo",
                "-png",
                "-singlefile",
                "-r",
                "300",
                "-transp",
                str(figure_pdf),
                str(png_prefix),
            ],
            capture_output=True,
            check=False,
            encoding="utf-8",
            timeout=timeout_seconds,
        )
    except FileNotFoundError as error:
        raise RuntimeError("figure rendering requires pdftocairo") from error
    figure_png = Path(f"{png_prefix}.png")
    if raster.returncode != 0 or not figure_png.is_file():
        detail = raster.stderr.strip() or raster.stdout.strip() or "no diagnostic output"
        raise RuntimeError(f"pdftocairo failed for figure {stem}: {detail}")
    output = exam_figure_png_path(source, figure)
    shutil.copy2(figure_png, output)
    return output


def compile_tex(
    source: SourceExam,
    figures: list[TikzBlock],
    temp_root: Path | None = None,
    timeout_seconds: int = 180,
) -> BuildResult:
    tex_path = exam_tex_path(source)
    pdf_path = exam_pdf_path(source)
    if temp_root is not None:
        temp_root = temp_root.expanduser().resolve()
        if not temp_root.is_dir():
            raise RuntimeError(f"temporary build root is not a directory: {temp_root}")
    build_parent = temp_root or Path(tempfile.gettempdir())
    tex_cache = build_parent / "uf-math-gma-tex-cache"
    tex_cache.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["TEXMFVAR"] = str(tex_cache)
    environment["TEXMFCACHE"] = str(tex_cache)

    exam_workdir = build_parent / "uf-math-gma-tex-work" / source.id
    workdir = next_attempt_directory(exam_workdir)
    working_tex = workdir / tex_path.name
    shutil.copy2(tex_path, working_tex)
    for figure in figures:
        compile_figure_png(
            source,
            figure,
            workdir,
            environment,
            timeout_seconds,
        )
    command = [
        "latexmk",
        "-lualatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        working_tex.name,
    ]
    try:
        result = run_latexmk(command, workdir, environment, timeout_seconds)
    except subprocess.TimeoutExpired as error:
        detail = "\n".join(
            ((error.stdout or "") + "\n" + (error.stderr or "")).splitlines()[-40:]
        )
        raise RuntimeError(
            f"LuaLaTeX timed out after {timeout_seconds}s for {source.id}; "
            f"build retained at {workdir}:\n{detail}"
        ) from error
    temporary_bytes = directory_size(workdir)
    working_pdf = workdir / f"{source.id}.pdf"
    if result.returncode != 0 or not working_pdf.is_file():
        detail = "\n".join((result.stdout + "\n" + result.stderr).splitlines()[-80:])
        raise RuntimeError(
            f"LuaLaTeX failed for {source.id}; build retained at {workdir}:\n{detail}"
        )
    shutil.copy2(working_pdf, pdf_path)
    shutil.rmtree(workdir)
    if not any(exam_workdir.iterdir()):
        exam_workdir.rmdir()
    return BuildResult(source.id, tex_path, pdf_path, temporary_bytes)


def build_exam(
    source: SourceExam,
    temp_root: Path | None = None,
    timeout_seconds: int = 180,
) -> BuildResult:
    exam = ExamRecord.model_validate_json(
        exam_json_path(source).read_text(encoding="utf-8")
    )
    write_text(exam_tex_path(source), render_tex(exam))
    return compile_tex(
        source,
        list(iter_tikz_blocks(exam)),
        temp_root,
        timeout_seconds,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exam_ids", nargs="*")
    parser.add_argument(
        "--prototype",
        action="store_true",
        help="build the five representative prototype exams",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="all_exams",
        help="build every exam in the manifest",
    )
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument(
        "--temp-root",
        type=Path,
        default=(Path(value) if (value := os.getenv("TEX_BUILD_ROOT")) else None),
        help="parent for disposable TeX build directories (or TEX_BUILD_ROOT)",
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout-seconds", type=int, default=180)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    selected_modes = sum((bool(args.exam_ids), args.prototype, args.all_exams))
    if selected_modes != 1:
        raise SystemExit("supply exam IDs, --prototype, or --all")
    if args.workers < 1:
        raise SystemExit("--workers must be at least 1")
    if args.timeout_seconds < 1:
        raise SystemExit("--timeout-seconds must be at least 1")
    sources = load_sources(args.manifest)
    if args.prototype:
        exam_ids = list(PROTOTYPE_IDS)
    elif args.all_exams:
        exam_ids = sorted(sources)
    else:
        exam_ids = list(dict.fromkeys(args.exam_ids))
    unknown = sorted(set(exam_ids) - set(sources))
    if unknown:
        raise SystemExit("unknown exam IDs: " + ", ".join(unknown))

    failures: dict[str, str] = {}
    built = 0
    completed = 0
    total = len(exam_ids)
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                build_exam,
                sources[exam_id],
                args.temp_root,
                args.timeout_seconds,
            ): exam_id
            for exam_id in exam_ids
        }
        for future in as_completed(futures):
            exam_id = futures[future]
            completed += 1
            try:
                future.result()
            except Exception as error:
                failures[exam_id] = str(error)
                print(f"failed: {exam_id}: {str(error).splitlines()[0]}")
            else:
                built += 1
            if completed % 10 == 0 or completed == total or exam_id in failures:
                print(
                    f"progress={completed}/{total} built={built} failed={len(failures)}",
                    flush=True,
                )

    print(f"completed={completed} built={built} failed={len(failures)}")
    if failures:
        print("failed_ids=" + ",".join(sorted(failures)))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
