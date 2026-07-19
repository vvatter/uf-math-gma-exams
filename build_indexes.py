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
    MONTH_ORDER,
    PAGE_UPDATED_ISO,
    PAGE_UPDATED_LABEL,
    PROJECT_SOURCE_URL,
    SourceExam,
    load_sources,
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


LEVELS = (
    ArchiveLevel("qualifying", "Qualifying", "-qualifying"),
    ArchiveLevel("first-year", "First-year", "-first-year"),
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


def page_start(title: str) -> list[str]:
    return [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        f"  <title>{escape(title)}</title>",
        f'  <link rel="stylesheet" href="{COMPUTER_MODERN_CSS}">',
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


def render_root_index(sources: Iterable[SourceExam]) -> str:
    source_list = list(sources)
    groups = grouped_sources(source_list)
    lines = page_start(ARCHIVE_TITLE)
    lines.extend(
        institution_header(
            ARCHIVE_TITLE,
            f"Browse accessible HTML versions of {len(source_list)} archived examinations by level and subject.",
        )
    )
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
            count = len(exams)
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
    lines.extend(page_end())
    return "\n".join(lines) + "\n"


def source_date_sort_key(source: SourceExam) -> tuple[object, ...]:
    return (
        -source.year,
        -MONTH_ORDER.get(source.month, 13),
        source.part or 0,
        source.id,
    )


def render_subject_index(subject_tag: str, sources: Iterable[SourceExam]) -> str:
    exams = list(sources)
    if not exams or any(source.subject_tag != subject_tag for source in exams):
        raise ValueError(f"invalid source group for {subject_tag}")
    exams.sort(key=source_date_sort_key)
    heading = subject_heading(exams[0])
    lines = page_start(heading)
    lines.extend(institution_header(heading))
    lines.append(
        '    <div class="table-wrap" role="region" tabindex="0" '
        f'aria-label="{escape(heading, quote=True)}">'
    )
    lines.append("      <table>")
    noun = "exam" if len(exams) == 1 else "exams"
    lines.append(f"        <caption>{len(exams)} {noun}, newest first</caption>")
    lines.extend(
        [
            "        <thead>",
            "          <tr>",
            '            <th scope="col">Date</th>',
            '            <th scope="col">Part</th>',
            '            <th scope="col">Accessible HTML</th>',
            '            <th scope="col">Archived PDF</th>',
            "          </tr>",
            "        </thead>",
            "        <tbody>",
        ]
    )
    for source in exams:
        month_number = MONTH_ORDER.get(source.month, 13)
        date_label = f"{source.month.title()} {source.year}"
        part = (
            f"Part {source.part}"
            if source.part is not None
            else '<span aria-hidden="true">&mdash;</span><span class="sr-only">Not applicable</span>'
        )
        html_name = source.pdf_path.with_suffix(".html").name
        lines.extend(
            [
                "          <tr>",
                f'            <th scope="row"><time datetime="{source.year}-{month_number:02d}">{escape(date_label)}</time></th>',
                f"            <td>{part}</td>",
                f'            <td><a href="{escape(html_name, quote=True)}">Read exam</a></td>',
                f'            <td><a href="{escape(source.pdf_path.name, quote=True)}">View PDF</a></td>',
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
    pages = {site_root / "index.html": render_root_index(source_list)}
    for subject_tag, exams in groups.items():
        pages[exams[0].pdf_path.parent / "index.html"] = render_subject_index(
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
