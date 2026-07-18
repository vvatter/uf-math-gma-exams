# UF Math GMA Exam Archive Dataset

> **Development disclosure:** This project is vibe-coded using **ChatGPT-5.6 Sol
> (xhigh)**. Its architecture, implementation, tests, extraction workflow, and
> documentation are being developed through human-directed collaboration with that
> model.

## Purpose

The University of Florida Department of Mathematics maintains the Graduate Mathematics
Association's collections of [First Year and PhD Exams](https://gma.math.ufl.edu/past-exams/first-year-and-phd-exams/)
and [Qualifying Exams](https://gma.math.ufl.edu/past-exams/qualifying-exams/). The
purpose of this project is to extract the information contained in every exam in those
archives so the questions, mathematical notation, and instructions can be presented in
more accessible forms.

The two collections apply to different cohorts:

- First Year and PhD Exams are for students who entered before Fall 2025.
- Qualifying Exams are for students who entered in Fall 2025 or later.

This Git repository also serves as the project archive. It contains the acquisition and
extraction code, the source PDFs after lossless optimization, one canonical JSON record
per exam, and a readable Markdown rendering of each JSON record. `manifest.json`
records the source URLs and preserves both the originally downloaded and current
working-file sizes and hashes.

## Scope

The project does not repair, tag, or otherwise remediate the archived source PDFs. It
may rewrite them with lossless PDF optimization to reduce storage, but it does not
intentionally change their visible content. Instead, it extracts the questions,
mathematical notation, and meaningful instructions into one JSON file per exam. New
accessible presentations will be generated from that dataset. Visual dependencies and
other genuine uncertainties are sent to a small serious-review queue, while corrections
and completed structural transformations are logged separately.

Each extracted JSON file and its readable Markdown rendering are stored beside the
source PDF in the same `exams/<subject-tag>/` directory. Matching stems make the three
files easy to compare during review. Each JSON record includes the current GMA PDF URL,
one instructions value, and structured problems with recursively nested subparts. Math
uses MathJax delimiters `\(...\)` and `\[...\]`.

If a linked PDF contains only a notice that the exam was unavailable, that notice is
stored in `instructions` and the problem list is empty. The JSON and Markdown still
document exactly what the archive provides at that URL.

The project is designed for a complete initial extraction followed by selective
reprocessing and a separate later verification pass. It does not spend a second model
call verifying every exam during the first run.

See [APPROACH.md](APPROACH.md) for the dataset schema, extraction rules, review policy,
and validation plan.

## Setup

Downloading uses only Python's standard library. Structured extraction requires Python
3.11 or newer, the packages declared in `pyproject.toml`, and an OpenAI API key with
access to `gpt-5.6-sol`. This project uses the base Python environment directly.

```sh
python3 -m pip install "openai>=2.0" "pydantic>=2.8" "PyMuPDF>=1.26"
export OPENAI_API_KEY="your-key"
```

## Download

```sh
python3 download_exams.py
```

The script discovers the current subject pages and their exam tables from both GMA
indexes on every run. It
stores files under `exams/<subject-tag>/` and writes `manifest.json` with the source URL,
subject, date, local path, original download size and SHA-256, current working size and
SHA-256, and download status for every PDF. Valid files already on disk are checked and
skipped, so rerunning the command is safe.

After losslessly optimizing local PDFs, refresh their working sizes and hashes without
using the network:

```sh
python3 download_exams.py --refresh-local-metadata
```

Use `--dry-run` to inspect the current catalog without downloading PDFs:

```sh
python3 download_exams.py --dry-run
```

## Extract

Run the representative five-exam pilot with:

```sh
python3 extract_exams.py --pilot
```

The pilot covers a scan, multipart questions, formula-heavy pages, Logic's local
numbering, two instruction tiers, and essential figures. Canonical records are written
beside their source PDFs under `exams/<subject-tag>/`, using the same filename stem and
`.json` and `.md` extensions. Human-review findings are collected in
`exams/review-serious.json`. Corrections and completed transformations are recorded in
`exams/review-corrections.json` and `exams/review-transformations.json`. Model responses,
token usage, rendered source pages, and validation failures remain under ignored
`build/extraction/` checkpoints.

The command resumes valid completed records by default. Use `--force` only when a
record should be re-extracted after a prompt or policy change. Specific manifest IDs
can be supplied instead of `--pilot`:

```sh
python3 extract_exams.py logic-phd-2006-aug topology-phd-2025-may
```

## Naming

A single-file sitting is named as follows:

```text
numerical-analysis-phd-2026-jan.pdf
```

When a table provides multiple files for the same sitting, the label is retained:

```text
algebra-first-year-2025-aug-part-1.pdf
algebra-first-year-2025-aug-part-2.pdf
```

First Year and PhD are normally appended to the subject tag. Two subject names have
explicit overrides:

- `Variational Analysis/Numerical Optimization` becomes `numerical-optimization-phd`.
- `Partial Differential Equations` becomes `pde-phd`.

Qualifying subjects use tags such as `algebra-qualifying`,
`analysis-qualifying`, `numerical-analysis-qualifying`, and
`topology-qualifying`.

January, May, August, and September are the expected exam months. If the source table
contains another valid month, the script preserves it, reports it in the manifest, and
uses its ordinary three-letter abbreviation rather than guessing a replacement.

## Download Options

```text
--output DIR       PDF root directory (default: exams)
--manifest FILE   JSON manifest path (default: manifest.json)
--index-url URL    Source index URL; repeat to replace the two default indexes
--workers N        Concurrent PDF downloads (default: 4)
--overwrite        Download valid existing files again
--dry-run          Discover and name files without downloading
--refresh-local-metadata
                   Preserve download hashes and refresh local working hashes
```

## Extraction Options

```text
--pilot             Extract the five representative pilot exams
--review-dir DIR    Review-log directory (default: exams)
--build-root DIR    Checkpoint root directory (default: build/extraction)
--model MODEL       Extraction model (default: gpt-5.6-sol)
--reasoning LEVEL   Reasoning effort: low, medium, or high (default: high)
--dpi N             Source-page rendering resolution (default: 200)
--workers N         Concurrent model calls (default: 2)
--force             Archive and re-extract completed records
```
