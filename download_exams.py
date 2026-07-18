#!/usr/bin/env python3
"""Discover and download the GMA first-year, PhD, and qualifying exam archives."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import time
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen


FIRST_YEAR_PHD_INDEX_URL = (
    "https://gma.math.ufl.edu/past-exams/first-year-and-phd-exams/"
)
QUALIFYING_INDEX_URL = "https://gma.math.ufl.edu/past-exams/qualifying-exams/"
DEFAULT_INDEX_URLS = (FIRST_YEAR_PHD_INDEX_URL, QUALIFYING_INDEX_URL)
ALLOWED_HOST = "gma.math.ufl.edu"
USER_AGENT = "Mozilla/5.0 (compatible; GMAExamArchiveHelper/1.0)"
EXPECTED_MONTHS = {"january", "may", "august", "september"}
MONTH_ABBREVIATIONS = {
    "january": "jan",
    "february": "feb",
    "march": "mar",
    "april": "apr",
    "may": "may",
    "june": "jun",
    "july": "jul",
    "august": "aug",
    "september": "sep",
    "october": "oct",
    "november": "nov",
    "december": "dec",
}
SUBJECT_OVERRIDES = {
    "variational analysis/numerical optimization": "numerical-optimization-phd",
    "partial differential equations": "pde-phd",
}
DATE_RE = re.compile(r"\b(?P<year>(?:19|20)\d{2})\s+(?P<month>[A-Za-z]+)\b")
PART_RE = re.compile(r"\bpart\s*([0-9]+)\b", re.IGNORECASE)


class DiscoveryError(RuntimeError):
    """Raised when the live pages do not satisfy the expected archive structure."""


@dataclass(frozen=True)
class Link:
    url: str
    text: str


@dataclass(frozen=True)
class Subject:
    title: str
    tag: str
    url: str


@dataclass
class Exam:
    subject: str
    subject_tag: str
    subject_url: str
    year: int
    month: str
    source_label: str
    source_url: str
    download_url: str
    path: str
    status: str = "pending"
    resolved_url: str | None = None
    size: int | None = None
    sha256: str | None = None
    download_size: int | None = None
    download_sha256: str | None = None
    error: str | None = None


@dataclass
class Cell:
    kind: str
    text: str
    links: list[Link]


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[Link] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a" and self._href is None:
            values = dict(attrs)
            self._href = values.get("href")
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href is not None:
            self.links.append(Link(self._href, clean_text(" ".join(self._text))))
            self._href = None
            self._text = []


class TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[list[Cell]] = []
        self._table_depth = 0
        self._target_depth: int | None = None
        self._row: list[Cell] | None = None
        self._cell_kind: str | None = None
        self._cell_text: list[str] = []
        self._cell_links: list[Link] = []
        self._link_href: str | None = None
        self._link_text: list[str] = []

    @property
    def in_target_table(self) -> bool:
        return self._target_depth is not None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        values = dict(attrs)
        if tag == "table":
            self._table_depth += 1
            classes = set((values.get("class") or "").split())
            table_id = values.get("id") or ""
            if self._target_depth is None and (
                table_id.startswith("tablepress-") or "tablepress" in classes
            ):
                self._target_depth = self._table_depth
            return
        if not self.in_target_table:
            return
        if tag == "tr":
            self._row = []
        elif tag in {"td", "th"} and self._row is not None:
            self._cell_kind = tag
            self._cell_text = []
            self._cell_links = []
        elif tag == "a" and self._cell_kind is not None:
            self._link_href = values.get("href")
            self._link_text = []

    def handle_data(self, data: str) -> None:
        if self._cell_kind is not None:
            self._cell_text.append(data)
        if self._link_href is not None:
            self._link_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self.in_target_table and tag == "a" and self._link_href is not None:
            self._cell_links.append(
                Link(self._link_href, clean_text(" ".join(self._link_text)))
            )
            self._link_href = None
            self._link_text = []
        elif self.in_target_table and tag in {"td", "th"} and self._cell_kind == tag:
            assert self._row is not None
            self._row.append(
                Cell(
                    kind=self._cell_kind,
                    text=clean_text(" ".join(self._cell_text)),
                    links=self._cell_links,
                )
            )
            self._cell_kind = None
            self._cell_text = []
            self._cell_links = []
        elif self.in_target_table and tag == "tr" and self._row is not None:
            if self._row:
                self.rows.append(self._row)
            self._row = None
        elif tag == "table":
            if self._target_depth == self._table_depth:
                self._target_depth = None
            self._table_depth = max(0, self._table_depth - 1)


def clean_text(value: str) -> str:
    return " ".join(value.replace("\xa0", " ").split())


def slugify(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")


def subject_tag(title: str) -> str:
    normalized = clean_text(title)
    lowered = normalized.lower()
    if lowered.startswith("first year "):
        level = "first-year"
        subject = normalized[len("First Year ") :]
    elif lowered.startswith("phd "):
        level = "phd"
        subject = normalized[len("PhD ") :]
    elif lowered.endswith(" qualifying exam"):
        level = "qualifying"
        subject = normalized[: -len(" Qualifying Exam")]
    else:
        raise DiscoveryError(f"unrecognized subject title: {title!r}")
    override = SUBJECT_OVERRIDES.get(subject.lower())
    return override or f"{slugify(subject)}-{level}"


def normalize_page_url(url: str, base_url: str) -> str:
    absolute = urljoin(base_url, url)
    parsed = urlparse(absolute)
    return urlunparse(parsed._replace(fragment=""))


def normalize_pdf_url(url: str, base_url: str) -> str:
    absolute = normalize_page_url(url, base_url)
    parsed = urlparse(absolute)
    if parsed.hostname != ALLOWED_HOST:
        raise DiscoveryError(f"refusing PDF link outside {ALLOWED_HOST}: {absolute}")
    if not parsed.path.lower().endswith(".pdf"):
        raise DiscoveryError(f"linked exam is not a PDF URL: {absolute}")
    path = parsed.path.replace("/gma/wp-content/", "/wp-content/", 1)
    return urlunparse(parsed._replace(scheme="https", path=path))


def download_candidates(url: str) -> list[str]:
    parsed = urlparse(url)
    candidates: list[str] = []
    if "/gma/wp-content/" in parsed.path:
        modern_path = parsed.path.replace("/gma/wp-content/", "/wp-content/", 1)
        candidates.append(urlunparse(parsed._replace(scheme="https", path=modern_path)))
    candidates.append(urlunparse(parsed._replace(scheme="https")))
    if parsed.scheme == "http":
        candidates.append(url)
    return list(dict.fromkeys(candidates))


def fetch(url: str, timeout: int = 60) -> tuple[bytes, str, str | None]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"})
    with urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get_content_type()
        charset = response.headers.get_content_charset()
        return response.read(), response.geturl(), charset or (
            "utf-8" if content_type == "text/html" else None
        )


def fetch_html(url: str) -> str:
    data, resolved_url, charset = fetch(url)
    try:
        return data.decode(charset or "utf-8")
    except UnicodeDecodeError as error:
        raise DiscoveryError(f"could not decode {resolved_url}: {error}") from error


def discover_subjects(index_url: str) -> list[Subject]:
    parser = AnchorParser()
    parser.feed(fetch_html(index_url))
    index_path = urlparse(index_url).path.rstrip("/") + "/"
    subjects: list[Subject] = []
    seen: set[str] = set()
    for link in parser.links:
        if not (
            re.match(r"^(?:First Year|PhD)\s+\S", link.text, re.IGNORECASE)
            or re.match(r"^\S.*\sQualifying Exam$", link.text, re.IGNORECASE)
        ):
            continue
        url = normalize_page_url(link.url, index_url)
        parsed = urlparse(url)
        if parsed.hostname != ALLOWED_HOST or not parsed.path.startswith(index_path):
            continue
        if parsed.path.rstrip("/") == index_path.rstrip("/") or url in seen:
            continue
        seen.add(url)
        subjects.append(Subject(link.text, subject_tag(link.text), url))
    if not subjects:
        raise DiscoveryError(f"no subject pages found at {index_url}")
    duplicate_tags = {item.tag for item in subjects if sum(s.tag == item.tag for s in subjects) > 1}
    if duplicate_tags:
        raise DiscoveryError(f"subject tags are not unique: {sorted(duplicate_tags)}")
    return subjects


def parse_date(value: str) -> tuple[int, str]:
    match = DATE_RE.search(clean_text(value))
    if not match:
        raise DiscoveryError(f"could not parse exam date: {value!r}")
    month = match.group("month").lower()
    if month not in MONTH_ABBREVIATIONS:
        raise DiscoveryError(f"unrecognized month in exam date: {value!r}")
    return int(match.group("year")), month


def label_suffix(anchor_label: str, column_label: str) -> str | None:
    labels = [clean_text(anchor_label), clean_text(column_label)]
    for label in labels:
        match = PART_RE.search(label)
        if match:
            return f"part-{match.group(1)}"
    generic = {"", "exam", "link", "download", "pdf"}
    for label in labels:
        if label.lower() not in generic and label.lower() != "date":
            return slugify(label)
    return None


def unique_path(path: Path, url: str, reserved: dict[Path, str]) -> Path:
    if path not in reserved or reserved[path] == url:
        reserved[path] = url
        return path
    counter = 2
    while True:
        candidate = path.with_name(f"{path.stem}-{counter}{path.suffix}")
        if candidate not in reserved or reserved[candidate] == url:
            reserved[candidate] = url
            return candidate
        counter += 1


def exam_stem(
    subject_tag: str, year: int, month: str, suffix: str | None = None
) -> str:
    stem = f"{subject_tag}-{year}-{MONTH_ABBREVIATIONS[month]}"
    return f"{stem}-{suffix}" if suffix else stem


def discover_exams(subject: Subject, output_root: Path) -> list[Exam]:
    parser = TableParser()
    parser.feed(fetch_html(subject.url))
    if not parser.rows:
        raise DiscoveryError(f"no exam table found for {subject.title}: {subject.url}")
    headers: list[str] = []
    exams: list[Exam] = []
    seen_urls: set[str] = set()
    reserved: dict[Path, str] = {}
    for row in parser.rows:
        if row and all(cell.kind == "th" for cell in row):
            headers = [cell.text for cell in row]
            continue
        if not row or not DATE_RE.search(row[0].text):
            continue
        year, month = parse_date(row[0].text)
        row_links = [
            (column, link)
            for column, cell in enumerate(row[1:], start=1)
            for link in cell.links
            if urlparse(urljoin(subject.url, link.url)).path.lower().endswith(".pdf")
        ]
        for column, link in row_links:
            source_url = normalize_page_url(link.url, subject.url)
            download_url = normalize_pdf_url(link.url, subject.url)
            if download_url in seen_urls:
                continue
            seen_urls.add(download_url)
            column_label = headers[column] if column < len(headers) else ""
            suffix = label_suffix(link.text, column_label)
            stem = exam_stem(subject.tag, year, month, suffix)
            destination = unique_path(
                output_root / subject.tag / f"{stem}.pdf", download_url, reserved
            )
            exams.append(
                Exam(
                    subject=subject.title,
                    subject_tag=subject.tag,
                    subject_url=subject.url,
                    year=year,
                    month=month,
                    source_label=link.text or column_label or "Exam",
                    source_url=source_url,
                    download_url=download_url,
                    path=str(destination),
                )
            )
    if not exams:
        raise DiscoveryError(f"no PDF exam links found for {subject.title}: {subject.url}")
    return exams


def discover_catalog(
    index_urls: list[str], output_root: Path
) -> tuple[list[Subject], list[Exam]]:
    subjects = [
        subject
        for index_url in index_urls
        for subject in discover_subjects(index_url)
    ]
    duplicate_tags = {
        subject.tag
        for subject in subjects
        if sum(item.tag == subject.tag for item in subjects) > 1
    }
    if duplicate_tags:
        raise DiscoveryError(
            f"subject tags are not unique across indexes: {sorted(duplicate_tags)}"
        )
    exams = [
        exam
        for subject in subjects
        for exam in discover_exams(subject, output_root)
    ]
    return subjects, exams


def file_metadata(path: Path) -> tuple[int, str]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as source:
        header = source.read(1024)
        if b"%PDF-" not in header:
            raise DiscoveryError(f"existing file is not a PDF: {path}")
        digest.update(header)
        size += len(header)
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
    return size, digest.hexdigest()


def download_exam(exam: Exam, overwrite: bool, retries: int = 3) -> Exam:
    destination = Path(exam.path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and not overwrite:
        try:
            exam.size, exam.sha256 = file_metadata(destination)
            if exam.download_size is None:
                exam.download_size = exam.size
            if exam.download_sha256 is None:
                exam.download_sha256 = exam.sha256
            if exam.status not in {"downloaded", "existing"}:
                exam.status = "existing"
            return exam
        except DiscoveryError:
            pass

    errors: list[str] = []
    temporary = destination.with_suffix(destination.suffix + ".part")
    for candidate in download_candidates(exam.source_url):
        for attempt in range(1, retries + 1):
            try:
                request = Request(
                    candidate,
                    headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,*/*"},
                )
                digest = hashlib.sha256()
                size = 0
                header = b""
                with urlopen(request, timeout=90) as response, temporary.open("wb") as target:
                    resolved = response.geturl()
                    if not (urlparse(resolved).hostname or "").endswith("ufl.edu"):
                        raise DiscoveryError(f"unexpected redirect host: {resolved}")
                    while chunk := response.read(1024 * 1024):
                        if len(header) < 1024:
                            header += chunk[: 1024 - len(header)]
                        target.write(chunk)
                        digest.update(chunk)
                        size += len(chunk)
                if b"%PDF-" not in header:
                    raise DiscoveryError(f"response is not a PDF: {candidate}")
                os.replace(temporary, destination)
                exam.status = "downloaded"
                exam.resolved_url = resolved
                exam.size = size
                exam.sha256 = digest.hexdigest()
                exam.download_size = size
                exam.download_sha256 = exam.sha256
                exam.error = None
                return exam
            except (HTTPError, URLError, TimeoutError, OSError, DiscoveryError) as error:
                temporary.unlink(missing_ok=True)
                errors.append(f"{candidate} (attempt {attempt}): {error}")
                if attempt < retries:
                    time.sleep(attempt)
    exam.status = "failed"
    exam.error = " | ".join(errors)
    return exam


def manifest_data(
    index_urls: list[str],
    subjects: list[Subject],
    exams: list[Exam],
    dry_run: bool,
) -> dict[str, object]:
    counts: dict[str, int] = {}
    for exam in exams:
        counts[exam.status] = counts.get(exam.status, 0) + 1
    unexpected = sorted({exam.month for exam in exams if exam.month not in EXPECTED_MONTHS})
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "index_urls": index_urls,
        "dry_run": dry_run,
        "summary": {
            "subjects": len(subjects),
            "pdfs": len(exams),
            "status_counts": counts,
            "unexpected_months": unexpected,
        },
        "subjects": [
            {
                **asdict(subject),
                "pdf_count": sum(exam.subject_tag == subject.tag for exam in exams),
            }
            for subject in subjects
        ],
        "exams": [asdict(exam) for exam in exams],
    }


def write_manifest(path: Path, data: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".part")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def previous_download_metadata(
    path: Path,
) -> dict[str, dict[str, int | str | None]]:
    if not path.exists():
        return {}
    raw = json.loads(path.read_text(encoding="utf-8"))
    return {
        item["path"]: {
            "download_size": item.get("download_size", item.get("size")),
            "download_sha256": item.get("download_sha256", item.get("sha256")),
            "resolved_url": item.get("resolved_url"),
            "status": item.get("status"),
        }
        for item in raw.get("exams", [])
    }


def refresh_local_metadata(path: Path) -> tuple[int, int]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    checked = 0
    for item in raw.get("exams", []):
        pdf_path = Path(item["path"])
        if not pdf_path.exists():
            continue
        item.setdefault("download_size", item.get("size"))
        item.setdefault("download_sha256", item.get("sha256"))
        size, sha256 = file_metadata(pdf_path)
        if (item.get("size"), item.get("sha256")) != (size, sha256):
            changed += 1
        item["size"] = size
        item["sha256"] = sha256
        checked += 1
    raw["local_metadata_refreshed_at"] = datetime.now(timezone.utc).isoformat()
    write_manifest(path, raw)
    return checked, changed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Discover and download the GMA first-year, PhD, and qualifying exam archive."
    )
    parser.add_argument(
        "--index-url",
        action="append",
        dest="index_urls",
        help="source index URL; repeat to use multiple indexes (defaults to both GMA archives)",
    )
    parser.add_argument("--output", type=Path, default=Path("exams"))
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--refresh-local-metadata", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.workers < 1:
        raise SystemExit("--workers must be at least 1")
    if args.refresh_local_metadata:
        if args.overwrite or args.dry_run:
            raise SystemExit("--refresh-local-metadata cannot be combined with download options")
        if not args.manifest.exists():
            raise SystemExit(f"manifest not found: {args.manifest}")
        checked, changed = refresh_local_metadata(args.manifest)
        print(f"Refreshed {checked} local PDFs; {changed} working files changed.")
        return 0
    index_urls = args.index_urls or list(DEFAULT_INDEX_URLS)
    try:
        subjects, exams = discover_catalog(index_urls, args.output)
    except DiscoveryError as error:
        raise SystemExit(f"discovery failed: {error}") from error

    previous = previous_download_metadata(args.manifest)
    for exam in exams:
        prior = previous.get(exam.path)
        if prior:
            download_size = prior["download_size"]
            download_sha256 = prior["download_sha256"]
            resolved_url = prior["resolved_url"]
            status = prior["status"]
            if isinstance(download_size, int):
                exam.download_size = download_size
            if isinstance(download_sha256, str):
                exam.download_sha256 = download_sha256
            if isinstance(resolved_url, str):
                exam.resolved_url = resolved_url
            if status in {"downloaded", "existing"}:
                exam.status = str(status)

    print(f"Discovered {len(exams)} PDFs across {len(subjects)} subjects.")
    unexpected = sorted({exam.month for exam in exams if exam.month not in EXPECTED_MONTHS})
    if unexpected:
        print("Unexpected source-table months preserved: " + ", ".join(unexpected))

    if not args.dry_run:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(download_exam, exam, args.overwrite): index
                for index, exam in enumerate(exams)
            }
            completed = 0
            for future in as_completed(futures):
                index = futures[future]
                exams[index] = future.result()
                completed += 1
                if completed % 25 == 0 or completed == len(exams):
                    print(f"Processed {completed}/{len(exams)} PDFs.")

    data = manifest_data(index_urls, subjects, exams, args.dry_run)
    write_manifest(args.manifest, data)
    counts = data["summary"]["status_counts"]  # type: ignore[index]
    print(f"Manifest: {args.manifest}")
    print("Statuses: " + ", ".join(f"{key}={value}" for key, value in sorted(counts.items())))
    return 1 if counts.get("failed", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
