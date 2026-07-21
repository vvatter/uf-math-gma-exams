#!/usr/bin/env python3
"""Generate accessible archive and subject indexes from the exam manifest."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Iterable

from extract_exams import (
    COMPUTER_MODERN_CSS,
    MATHJAX_SCRIPT,
    MONTH_ORDER,
    PAGE_UPDATED_ISO,
    PAGE_UPDATED_LABEL,
    PROJECT_SOURCE_URL,
    DocumentType,
    ExamRecord,
    ProblemConcern,
    SourceExam,
    exam_json_path,
    exam_title,
    iter_problem_locations,
    load_sources,
    render_html_text,
    subject_archive_title,
    subject_display_name,
    write_text,
)


ARCHIVE_TITLE = "Graduate Mathematics Exam Archive"


@dataclass(frozen=True)
class ArchiveLevel:
    key: str
    heading: str
    tag_suffix: str


@dataclass(frozen=True)
class ConcernEntry:
    source: SourceExam
    problem_index: int
    displayed_number: int
    section_heading: str | None
    concern: ProblemConcern


LEVELS = (
    ArchiveLevel("qualifying", "Qualifying", "-qualifying"),
    ArchiveLevel("first-year", "First-Year", "-first-year"),
    ArchiveLevel("phd", "PhD", "-phd"),
)


def archive_level(subject_tag: str) -> ArchiveLevel:
    for level in LEVELS:
        if subject_tag.endswith(level.tag_suffix):
            return level
    raise ValueError(f"subject tag has no recognized archive level: {subject_tag}")


def subject_name(source: SourceExam) -> str:
    return subject_display_name(source.subject, source.subject_tag)


def subject_heading(source: SourceExam) -> str:
    return subject_archive_title(source.subject, source.subject_tag)


def grouped_sources(sources: Iterable[SourceExam]) -> dict[str, list[SourceExam]]:
    groups: dict[str, list[SourceExam]] = defaultdict(list)
    for source in sources:
        groups[source.subject_tag].append(source)
    for subject_tag, exams in groups.items():
        labels = {subject_name(exam) for exam in exams}
        if len(labels) != 1:
            raise ValueError(f"inconsistent subject names for {subject_tag}: {labels}")
    return dict(groups)


def page_start(title: str, include_mathjax: bool = False) -> list[str]:
    lines = [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        f"  <title>{escape(title)}</title>",
        f'  <link rel="stylesheet" href="{COMPUTER_MODERN_CSS}">',
    ]
    if include_mathjax:
        lines.append(f'  <script defer src="{MATHJAX_SCRIPT}"></script>')
    lines.extend(
        [
            "  <style>",
            "    * { box-sizing: border-box; }",
            "    html { color-scheme: light; background: #fff; }",
            "    body {",
            "      margin: 0;",
            "      color: #191918;",
            '      font-family: "CMU Serif", Georgia, serif;',
            "      font-size: 1.125rem;",
            "      font-weight: 500;",
            "      line-height: 1.55;",
            "    }",
            "    a { color: #174f78; text-decoration-thickness: .08em; text-underline-offset: .15em; }",
            "    a:hover { color: #8a321d; }",
            "    a:focus-visible, .table-wrap:focus-visible {",
            "      outline: 3px solid #d28b18;",
            "      outline-offset: 3px;",
            "    }",
            "    .skip-link {",
            "      position: absolute;",
            "      top: .5rem;",
            "      left: .5rem;",
            "      z-index: 1;",
            "      padding: .55rem .75rem;",
            "      background: #fff;",
            "      transform: translateY(-180%);",
            "    }",
            "    .skip-link:focus { transform: none; }",
            "    main {",
            "      width: 100%;",
            "      max-width: 64rem;",
            "      margin: 0 auto;",
            "      padding: 3.5rem 2rem 4rem;",
            "    }",
            "    .site-header {",
            "      margin-bottom: 2.25rem;",
            "      padding-bottom: 1.25rem;",
            "      border-bottom: 2px solid #242421;",
            "    }",
            "    .institution { margin: 0 0 .4rem; font-size: 1rem; font-weight: 700; }",
            "    h1, h2 { line-height: 1.18; }",
            "    h1 { margin: 0; font-size: 2.2rem; }",
            "    h2 {",
            "      margin: 2.8rem 0 .65rem;",
            "      padding-bottom: .3rem;",
            "      border-bottom: 1px solid #b8b8b2;",
            "      font-size: 1.45rem;",
            "    }",
            "    p { margin: 0 0 1rem; }",
            "    .lede { max-width: 48rem; font-size: 1.18rem; }",
            "    .concerns-link {",
            "      display: flex;",
            "      flex-wrap: wrap;",
            "      gap: .35rem .75rem;",
            "      align-items: baseline;",
            "      margin: 3rem 0 1.5rem;",
            "    }",
            "    .concerns-link a { font-weight: 700; }",
            "    .concern-notice { max-width: 52rem; margin-bottom: 2rem; }",
            "    .concern-exam h2 { margin-bottom: .9rem; padding-bottom: 0; border-bottom: 0; }",
            "    .concern-list { margin: 0; padding: 0; list-style: none; }",
            "    .concern { margin: 0 0 1.35rem; }",
            "    .concern p { margin-bottom: .45rem; }",
            "    .concern-warning { color: #7a1f1f; }",
            "    .featured-resource {",
            "      display: flex;",
            "      flex-wrap: wrap;",
            "      gap: .35rem .75rem;",
            "      align-items: baseline;",
            "      margin: 0 0 2rem;",
            "      padding: 0 0 .75rem;",
            "      border-bottom: 1px solid #d8d8d2;",
            "    }",
            "    .featured-resource a { font-weight: 700; }",
            "    .subject-list {",
            "      display: grid;",
            "      grid-template-columns: repeat(2, minmax(0, 1fr));",
            "      column-gap: 2.5rem;",
            "      margin: 0;",
            "      padding: 0;",
            "      list-style: none;",
            "    }",
            "    .subject-list li {",
            "      display: flex;",
            "      justify-content: space-between;",
            "      gap: 1rem;",
            "      align-items: baseline;",
            "      border-bottom: 1px solid #d8d8d2;",
            "    }",
            "    .subject-list a {",
            "      padding: .7rem 0;",
            "      font-weight: 700;",
            "    }",
            "    .count { padding: .7rem 0; color: #555550; font-weight: 500; white-space: nowrap; }",
            "    .table-wrap { max-width: 100%; overflow-x: auto; }",
            "    table { width: 100%; min-width: 39rem; border-collapse: collapse; }",
            "    caption { padding: 0 0 .75rem; text-align: left; font-style: italic; }",
            "    th, td { padding: .65rem .75rem; border-bottom: 1px solid #d8d8d2; text-align: left; }",
            "    thead th { border-bottom: 2px solid #242421; font-weight: 700; }",
            "    tbody th { font-weight: 500; }",
            "    tbody tr:hover { background: #f5f5f2; }",
            "    .sr-only {",
            "      position: absolute;",
            "      width: 1px;",
            "      height: 1px;",
            "      padding: 0;",
            "      margin: -1px;",
            "      overflow: hidden;",
            "      clip: rect(0, 0, 0, 0);",
            "      white-space: nowrap;",
            "      border: 0;",
            "    }",
            "    footer {",
            "      margin-top: 3.25rem;",
            "      padding-top: 1rem;",
            "      border-top: 1px solid #b8b8b2;",
            "      font-size: 1rem;",
            "    }",
            "    footer ul { display: flex; flex-wrap: wrap; gap: .5rem 1.25rem; margin: 0; padding: 0; list-style: none; }",
            "    .page-updated { margin: .65rem 0 0; color: #5f5f5a; font-size: .9rem; }",
            "    @media (max-width: 42rem) {",
            "      body { font-size: 1.05rem; }",
            "      main { padding: 2rem 1.15rem 3rem; }",
            "      h1 { font-size: 1.8rem; }",
            "      .subject-list { grid-template-columns: 1fr; }",
            "    }",
            "    @media print {",
            "      @page { margin: .55in; }",
            "      body { font-size: 10pt; line-height: 1.3; color: #000; }",
            "      main { max-width: none; padding: 0; }",
            "      .skip-link, footer { display: none; }",
            "      .site-header { margin-bottom: .7rem; padding-bottom: .35rem; border-bottom-width: 1px; }",
            "      .institution { margin-bottom: .2rem; font-size: 9pt; }",
            "      .institution a { text-decoration: none; }",
            "      h1 { font-size: 17pt; }",
            "      h2 { margin: .9rem 0 .35rem; font-size: 12pt; }",
            "      .subject-list { grid-template-columns: repeat(2, minmax(0, 1fr)); }",
            "      .subject-list a, .count { padding: .25rem 0; }",
            "      .concerns-link { margin: 1rem 0 .55rem; }",
            "      .concern { margin-bottom: .55rem; break-inside: avoid; }",
            "      .concern-warning { color: #651818; }",
            "      table { min-width: 0; }",
            "      th, td { padding: .25rem .4rem; }",
            "      a { color: inherit; }",
            "    }",
            "  </style>",
            "</head>",
            "<body>",
            '  <a class="skip-link" href="#main-content">Skip to main content</a>',
            '  <main id="main-content">',
        ]
    )
    return lines


def institution_header(title: str, lede: str | None = None) -> list[str]:
    lines = [
        '    <header class="site-header">',
        '      <p class="institution"><a href="https://www.ufl.edu/">University of Florida</a>, '
        '<a href="https://math.ufl.edu/">Department of Mathematics</a></p>',
        f"      <h1>{escape(title)}</h1>",
    ]
    if lede:
        lines.append(f'      <p class="lede">{escape(lede)}</p>')
    lines.append("    </header>")
    return lines


def page_end(additional_links: tuple[tuple[str, str], ...] = ()) -> list[str]:
    lines = [
        "    <footer>",
        "      <ul>",
        f'        <li><a href="{PROJECT_SOURCE_URL}">Project source</a></li>',
    ]
    for href, label in additional_links:
        lines.append(
            f'        <li><a href="{escape(href, quote=True)}">{escape(label)}</a></li>'
        )
    lines.extend(
        [
            "      </ul>",
            f'      <p class="page-updated">Page updated <time datetime="{PAGE_UPDATED_ISO}">{PAGE_UPDATED_LABEL}</time>.</p>',
            "    </footer>",
            "  </main>",
            "</body>",
            "</html>",
        ]
    )
    return lines
def concern_entries(sources: Iterable[SourceExam]) -> list[ConcernEntry]:
    entries: list[ConcernEntry] = []
    for source in sources:
        path = exam_json_path(source)
        if not path.is_file():
            continue
        exam = ExamRecord.model_validate_json(path.read_text(encoding="utf-8"))
        for problem_index, displayed_number, section_heading, problem in iter_problem_locations(
            exam
        ):
            entries.extend(
                ConcernEntry(
                    source=source,
                    problem_index=problem_index,
                    displayed_number=displayed_number,
                    section_heading=section_heading,
                    concern=concern,
                )
                for concern in problem.concerns
            )
    return entries


def concern_sort_key(entry: ConcernEntry) -> tuple[object, ...]:
    level_order = next(
        index
        for index, level in enumerate(LEVELS)
        if entry.source.subject_tag.endswith(level.tag_suffix)
    )
    return (
        subject_name(entry.source).casefold(),
        entry.source.year is None,
        -(entry.source.year or 0),
        -MONTH_ORDER.get(entry.source.month or "", 13),
        level_order,
        entry.source.practice_variant or "",
        entry.source.part or 0,
        entry.source.id,
        entry.problem_index,
    )


def render_root_index(
    sources: Iterable[SourceExam],
    concern_count: int = 0,
    concerned_exam_count: int = 0,
) -> str:
    source_list = list(sources)
    exam_sources = [
        source for source in source_list if source.document_type == DocumentType.EXAM
    ]
    collection_count = len(source_list) - len(exam_sources)
    groups = grouped_sources(source_list)
    lede = f"Browse accessible HTML versions of {len(exam_sources)} archived examinations"
    if collection_count:
        collection_noun = "collection" if collection_count == 1 else "collections"
        lede += f" and {collection_count} practice-problem {collection_noun}"
    lede += " by level and subject."
    lines = page_start(ARCHIVE_TITLE)
    lines.extend(
        institution_header(
            ARCHIVE_TITLE,
            lede,
        )
    )
    concern_noun = "concern" if concern_count == 1 else "concerns"
    exam_noun = "exam" if concerned_exam_count == 1 else "exams"
    lines.append('    <nav aria-label="Exam archive">')
    for index, level in enumerate(LEVELS, start=1):
        level_groups = [
            (tag, exams)
            for tag, exams in groups.items()
            if archive_level(tag) == level
        ]
        level_groups.sort(key=lambda item: subject_name(item[1][0]).casefold())
        lines.append(f'      <section aria-labelledby="level-{index}">')
        lines.append(f'        <h2 id="level-{index}">{level.heading}</h2>')
        lines.append('        <ul class="subject-list">')
        for subject_tag, exams in level_groups:
            count = sum(
                source.document_type == DocumentType.EXAM for source in exams
            )
            noun = "exam" if count == 1 else "exams"
            lines.extend(
                [
                    "          <li>",
                    f'            <a href="exams/{escape(subject_tag, quote=True)}/index.html">{escape(subject_name(exams[0]))}</a>',
                    f'            <span class="count">{count} {noun}</span>',
                    "          </li>",
                ]
            )
        lines.append("        </ul>")
        lines.append("      </section>")
    lines.append("    </nav>")
    lines.extend(
        [
            '    <p class="concerns-link">',
            '      <a href="concerns.html">Known or suspected errors</a>',
            f'      <span class="count">{concern_count} {concern_noun} across {concerned_exam_count} {exam_noun}</span>',
            "    </p>",
        ]
    )
    lines.extend(page_end())
    return "\n".join(lines) + "\n"


def render_concerns_index(entries: Iterable[ConcernEntry]) -> str:
    ordered = sorted(entries, key=concern_sort_key)
    grouped: dict[str, list[ConcernEntry]] = defaultdict(list)
    for entry in ordered:
        grouped[entry.source.id].append(entry)

    lines = page_start("Known or Suspected Errors", include_mathjax=True)
    lines.extend(
        institution_header(
            "Known or Suspected Errors",
            "These notices identify possible mathematical problems in archived source exams.",
        )
    )
    lines.extend(
        [
            '    <div class="concern-notice">',
            "      <p>The source questions remain unchanged. These concerns were identified during AI-assisted extraction and have not been reviewed by a human.</p>",
            "    </div>",
        ]
    )
    for exam_index, exam_entries in enumerate(grouped.values(), start=1):
        source = exam_entries[0].source
        exam_href = f"exams/{source.subject_tag}/{source.id}/index.html"
        heading_id = f"concern-exam-{exam_index}"
        lines.extend(
            [
                f'    <section class="concern-exam" aria-labelledby="{heading_id}">',
                f'      <h2 id="{heading_id}"><a href="{escape(exam_href, quote=True)}">{escape(exam_title(source))}</a></h2>',
                '      <ul class="concern-list">',
            ]
        )
        for entry in exam_entries:
            status = (
                "Suspected error."
                if entry.concern.status.value == "suspected"
                else "Confirmed error."
            )
            content = render_html_text(entry.concern.explanation, 10)
            warning = (
                f'<strong class="concern-number">{entry.displayed_number}.</strong> '
                f"<strong>Warning: {status}</strong>"
            )
            if content and content[0].lstrip().startswith("<p>"):
                content[0] = content[0].replace("<p>", f"<p>{warning} ", 1)
            else:
                content.insert(0, f"          <p>{warning}</p>")
            lines.extend(
                [
                    '        <li class="concern">',
                    '          <div class="concern-warning" role="note">',
                    *content,
                    "          </div>",
                    "        </li>",
                ]
            )
        lines.extend(["      </ul>", "    </section>"])
    lines.extend(page_end((("index.html", "All exam subjects"),)))
    return "\n".join(lines) + "\n"


def source_date_sort_key(source: SourceExam) -> tuple[object, ...]:
    if source.practice_variant is not None:
        return (1, source.practice_variant, source.part or 0, source.id)
    return (
        0,
        -(source.year or 0),
        -MONTH_ORDER.get(source.month or "", 13),
        source.part or 0,
        source.id,
    )


def render_subject_index(subject_tag: str, sources: Iterable[SourceExam]) -> str:
    source_list = list(sources)
    if not source_list or any(source.subject_tag != subject_tag for source in source_list):
        raise ValueError(f"invalid source group for {subject_tag}")
    collections = [
        source
        for source in source_list
        if source.document_type == DocumentType.PRACTICE_PROBLEMS
    ]
    exams = [
        source for source in source_list if source.document_type == DocumentType.EXAM
    ]
    exams.sort(key=source_date_sort_key)
    heading = subject_heading(source_list[0])
    lines = page_start(heading)
    lines.extend(institution_header(heading))
    for collection in collections:
        if collection.problem_count is None:
            raise ValueError(f"practice collection has no problem count: {collection.id}")
        lines.extend(
            [
                '    <p class="featured-resource">',
                f'      <a href="{escape(collection.id, quote=True)}/index.html">Practice Problems</a>',
                f'      <span class="count">({collection.problem_count}<span class="sr-only"> problems</span>)</span>',
                "    </p>",
            ]
        )
    lines.append(
        '    <div class="table-wrap" role="region" tabindex="0" '
        f'aria-label="{escape(heading, quote=True)}">'
    )
    lines.append("      <table>")
    noun = "exam" if len(exams) == 1 else "exams"
    has_practice = any(source.practice_variant is not None for source in exams)
    has_parts = any(source.part is not None for source in exams)
    ordering = (
        "newest first; undated practice exams last"
        if has_practice
        else "newest first"
    )
    lines.append(f"        <caption>{len(exams)} {noun}, {ordering}</caption>")
    lines.extend(
        [
            "        <thead>",
            "          <tr>",
            (
                '            <th scope="col">Date or practice</th>'
                if has_practice
                else '            <th scope="col">Date</th>'
            ),
        ]
    )
    if has_parts:
        lines.append('            <th scope="col">Part</th>')
    lines.extend(
        [
            '            <th scope="col">Accessible HTML</th>',
            '            <th scope="col">Archived PDF</th>',
            "          </tr>",
            "        </thead>",
            "        <tbody>",
        ]
    )
    for source in exams:
        if source.practice_variant is not None:
            row_heading = f"Practice {escape(source.practice_variant)}"
        elif source.year is not None and source.month is not None:
            month_number = MONTH_ORDER.get(source.month, 13)
            date_label = f"{source.month.title()} {source.year}"
            row_heading = (
                f'<time datetime="{source.year}-{month_number:02d}">'
                f"{escape(date_label)}</time>"
            )
        else:
            raise ValueError(f"exam has neither a date nor a practice variant: {source.id}")
        html_path = f"{source.id}/index.html"
        pdf_path = f"{source.id}/{source.id}.source.pdf"
        lines.extend(
            [
                "          <tr>",
                f'            <th scope="row">{row_heading}</th>',
            ]
        )
        if has_parts:
            part = (
                f"Part {source.part}"
                if source.part is not None
                else '<span aria-hidden="true">&mdash;</span><span class="sr-only">Not applicable</span>'
            )
            lines.append(f"            <td>{part}</td>")
        lines.extend(
            [
                f'            <td><a href="{escape(html_path, quote=True)}">Read exam</a></td>',
                f'            <td><a href="{escape(pdf_path, quote=True)}">View PDF</a></td>',
                "          </tr>",
            ]
        )
    lines.extend(["        </tbody>", "      </table>", "    </div>"])
    lines.extend(page_end((("../../index.html", "All exam subjects"),)))
    return "\n".join(lines) + "\n"


def expected_index_pages(
    sources: Iterable[SourceExam], site_root: Path
) -> dict[Path, str]:
    source_list = list(sources)
    groups = grouped_sources(source_list)
    entries = concern_entries(source_list)
    concerned_exam_count = len({entry.source.id for entry in entries})
    pages = {
        site_root / "index.html": render_root_index(
            source_list,
            concern_count=len(entries),
            concerned_exam_count=concerned_exam_count,
        ),
        site_root / "concerns.html": render_concerns_index(entries),
    }
    for subject_tag, exams in groups.items():
        pages[exams[0].pdf_path.parent.parent / "index.html"] = render_subject_index(
            subject_tag, exams
        )
    return pages


def build_indexes(manifest: Path, check: bool = False) -> list[str]:
    sources = load_sources(manifest)
    pages = expected_index_pages(sources.values(), manifest.parent)
    errors: list[str] = []
    for path, content in pages.items():
        if check:
            if not path.exists():
                errors.append(f"{path}: index is missing")
            elif path.read_text(encoding="utf-8") != content:
                errors.append(f"{path}: index does not match the manifest")
        else:
            write_text(path, content)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Build accessible exam archive indexes")
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument(
        "--check", action="store_true", help="check generated indexes without rewriting them"
    )
    args = parser.parse_args()
    errors = build_indexes(args.manifest, check=args.check)
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1
    action = "validated" if args.check else "generated"
    count = len(load_sources(args.manifest))
    print(f"{action}: archive index for {count} exams")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
