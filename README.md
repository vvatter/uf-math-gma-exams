# UF Math GMA Exam Archive Dataset

> **Development disclosure:** This project is vibe-coded using **ChatGPT-5.6 Sol
> (xhigh)**. Its architecture, implementation, tests, extraction workflow, and
> documentation are being developed through human-directed collaboration with that
> model. The model also wrote this disclosure.

## Purpose

The University of Florida Department of Mathematics maintains the Graduate Mathematics
Association's collections of [First Year and PhD Exams](https://gma.math.ufl.edu/past-exams/first-year-and-phd-exams/)
and [Qualifying Exams](https://gma.math.ufl.edu/past-exams/qualifying-exams/). The
purpose of this project is to extract the information contained in every exam in those
archives so the questions, mathematical notation, and instructions can be presented in
more accessible forms. The archive also includes four undated Algebra First-Year
practice exams and a 113-question Algebra First-Year practice-problem collection
published on the department's
[qualifying-exam syllabi page](https://math.ufl.edu/qualifying-exam-syllabi/).

The two collections apply to different cohorts:

- First Year and PhD Exams are for students who entered before Fall 2025.
- Qualifying Exams are for students who entered in Fall 2025 or later.

This Git repository also serves as the project archive. It contains the acquisition and
extraction code, the source PDFs after lossless optimization, one canonical JSON record
per exam or practice-problem collection, and accessible HTML, TeX, and accessible PDF
renderings of each JSON record.
Manually reconstructed figures are stored as canonical TikZ blocks;
their generated PNG assets live beside the other exam files.
Each exam has its own directory so newly typeset TeX and PDF presentations can live
beside those files without confusing them with the archived source. The archived source
uses `<exam-id>.source.pdf`, so downloaded files retain meaningful, unique names.
`manifest.json`
records the stable exam IDs and source URLs and preserves both the originally downloaded
and current working-file sizes and hashes.

## Scope

The project does not repair, tag, or otherwise remediate the archived source PDFs. It
may rewrite them with lossless PDF optimization to reduce storage, but it does not
intentionally change their visible content. Instead, it extracts the questions,
mathematical notation, and meaningful instructions into one JSON file per exam or
practice-problem collection. New
accessible presentations will be generated from that dataset. Visual dependencies and
other genuine source uncertainties are sent to a small serious-review queue. Legible
questions with known or suspected mathematical problems retain their source wording and
carry a warning in the canonical record and generated presentations. Corrections and
completed structural transformations are logged separately.

Each document is stored under `exams/<subject-tag>/<document-id>/`. The archived original is
`<exam-id>.source.pdf`; the JSON uses the exam ID as its filename; and the accessible
HTML is `index.html`. The same directory reserves `<exam-id>.tex` and
`<exam-id>.pdf` for the newly typeset source and accessible PDF. This makes every version
easy to compare during review without allowing the source and generated PDFs to share a
name. Each JSON
record includes its current official PDF URL and an ordered sequence of instructions,
problems, and optional named sections. A problem body is an ordered sequence of text and
manually verified TikZ figures, followed by structured, recursively nested subparts. A
problem may also carry one or more known or suspected mathematical concerns. Math uses
MathJax delimiters `\(...\)` and `\[...\]`.

If a linked PDF contains only a notice that the exam was unavailable, that notice is
stored as an instruction block and there are no problem blocks. The JSON and HTML still
document exactly what the archive provides at that URL.

The HTML is static and semantic: it uses headings, ordered problem lists, nested subpart
lists, figure elements with alternative text, visible keyboard focus, responsive
display mathematics, and print styles. It loads Computer Modern webfonts and accessible
MathJax from versioned CDN URLs rather than bundling either dependency into every page.

The generated root `index.html` organizes the archive by level in the order Qualifying,
First-Year, and PhD. Within each level it links to a separate index for every subject.
Subject indexes list dated exams newest first, place undated practice exams last, and
link to both the accessible HTML and the archived source PDF. Each exam page links back
to its subject index, making the generated
files usable as a conventional static website as well as a repository archive.
The root also links to `concerns.html`, a consolidated list of known or suspected
mathematical errors grouped by exam. Exam titles link to the corresponding accessible
HTML, and each warning begins with its displayed problem number.
Generated pages do not link to the retiring GMA website. Its URLs remain in the dataset
and manifest only as source provenance; public PDF links use the optimized copies
committed to this repository.

The repository root includes `.nojekyll`, so GitHub Pages can publish these committed
static files directly from the `main` branch and repository root without transforming
them through Jekyll.

Problem numbers are not stored redundantly. Their order in the JSON determines their
displayed numbers. A section records whether numbering restarts at 1 or continues from
the preceding problems, so repeated source numbers remain faithful without making
review references ambiguous. Review logs use absolute one-based problem positions.

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

Archive validation also requires Node.js 20 or newer. Install the exact MathJax version
recorded in `package-lock.json` with:

```sh
npm ci
```

Newly typeset accessible PDFs require a full TeX Live 2026 installation. The current
reference build uses LuaHBTeX 1.24.0 and `latexmk`; full MacTeX 2026 includes the
required LaTeX tagging support, fonts, mathematics packages, TikZ, and `adjustbox`.
Exams with manually reconstructed figures also require Poppler's `pdftocairo` command
to generate transparent PNGs for HTML.

## Download

```sh
python3 download_exams.py
```

The script discovers the current subject pages and their exam tables from both GMA
indexes on every run and adds the department's four undated Algebra practice PDFs and
the 113-question practice-problem collection. It
stores each downloaded PDF as
`exams/<subject-tag>/<exam-id>/<exam-id>.source.pdf` and writes `manifest.json` with the exam ID, source URL,
subject, date or practice variant, local path, original download size and SHA-256,
current working size and SHA-256, and download status for every PDF. Valid files already
on disk are checked and skipped, so rerunning the command is safe.

After losslessly optimizing local PDFs, refresh their working sizes and hashes without
using the network:

```sh
python3 download_exams.py --refresh-local-metadata
```

Use `--dry-run` to inspect the current catalog without downloading PDFs:

```sh
python3 download_exams.py --dry-run
```

## Optional PDF Optimization

The PDFs committed to this archive were processed individually with OCRmyPDF's
lossless optimization level 1:

```sh
ocrmypdf -O1 --skip-text --quiet --jobs 1 input.pdf output.pdf
```

The temporary output replaces the downloaded PDF only when it is smaller. The batch
process preserves the source file's access and modification times. Because optimization
changes the file bytes, run `python3 download_exams.py --refresh-local-metadata`
afterward. The manifest keeps the original download size and hash while recording the
optimized file's current size and hash separately.

## Extract

Run the representative eight-exam pilot with:

```sh
python3 extract_exams.py --pilot
```

The pilot covers scans, multipart questions, formula-heavy pages, restarted and
continuing section numbering, noninteger source labels, instruction blocks between
sections, and essential figures. Canonical records are written
inside their exam directories using `<exam-id>.json` and `index.html`.
Human-review findings are collected in
`exams/review-serious.json`. Corrections and completed transformations are recorded in
`exams/review-corrections.json` and `exams/review-transformations.json`. Model responses,
token usage, rendered source pages, and validation failures remain under ignored
`build/extraction/` checkpoints. Review records are merged after each completed exam,
so an interrupted bulk run retains both its canonical output and its review findings.
Mathematical concerns in legible source questions are stored directly on the affected
problem rather than in `review-serious.json`; the generated HTML, TeX, PDF, and
`concerns.html` all expose the same warning.

The 113-question Algebra collection has a dedicated resumable extractor because a
single model request would be unnecessarily large:

```sh
python3 extract_practice_problems.py
```

It makes nine Sol calls at 200 DPI. Pages 1, 2, and 5–10 are processed individually;
pages 3 and 4 are processed together because Problem 42 crosses that page boundary.
Every chunk must return its exact configured problem-number range, and the deterministic
merge must contain Problems 1–113 exactly once before canonical JSON or HTML is written.
Successful chunk checkpoints remain under
`build/extraction/algebra-first-year-practice-problems/chunks/`, so interrupted runs
resume without repeating completed calls. Use `--force` only to replace every saved
chunk with a fresh extraction.

The command resumes valid completed records by default. Use `--force` only when a
record should be re-extracted after a prompt or policy change. Superseded JSON,
HTML, and checkpoints are archived under ignored
`build/extraction/<exam-id>/history/`.
Specific manifest IDs can be supplied instead of `--pilot`:

```sh
python3 extract_exams.py logic-phd-2006-aug topology-phd-2025-may
```

Extract every exam that does not yet have a canonical JSON record:

```sh
python3 extract_exams.py --all
```

Subject selections are repeatable and can be limited to operational batches. Bulk
selections run oldest first within each subject and skip completed JSON records before
applying the limit:

```sh
python3 extract_exams.py --subject analysis-phd --limit 10
python3 extract_exams.py --subject logic-phd --subject topology-phd
```

With bulk selection, `--force` includes completed records and re-extracts them. Without
`--force`, rerunning the same command continues with the remaining exams.

Regenerate every HTML presentation after a deterministic renderer change, without
making model calls or changing the canonical JSON:

```sh
python3 extract_exams.py --render-all
```

## Build Accessible PDFs

Generate the five representative TeX and PDF prototypes with:

```sh
python3 build_tex.py --prototype
```

Specific exam IDs can be built individually or together:

```sh
python3 build_tex.py algebra-phd-1988-sep logic-phd-2006-aug
```

Build the complete archive with four concurrent LuaLaTeX workers:

```sh
python3 build_tex.py --all --workers 4
```

Each exam has a three-minute compilation timeout by default. A bulk run retains failed
workspaces, reports their IDs, and continues building the rest of the archive. Use
`--timeout-seconds` to change that limit.

The renderer writes `<exam-id>.tex` beside the canonical JSON and compiles it with
LuaLaTeX into `<exam-id>.pdf`. The output is tagged PDF 2.0 targeting PDF/UA-2, with
MathML structure for ordinary mathematics, Unicode Computer Modern fonts, semantic
headings and lists, document metadata, and a structure-based tab order.
The institutional names link to the university and department websites. Only the
subject-and-level portion of the exam title links to the future subject archive at
`https://gma.math.ufl.edu/exams/<subject-tag>/`. These links retain black text and have
no visible border or other printed decoration.

Manually restored visual content is stored in the problem body as the inner code and
options of a `tikzpicture`, together with a stable figure ID and plain-language
alternative text. An optional `height_lines` value controls the PDF and HTML height
limit and defaults to six. Standalone-document wrappers are deliberately excluded from JSON.
The PDF renderer inserts the TikZ directly as vector content and supplies its alt text
to LaTeX's tagged `Figure` structure. The same build compiles an isolated copy and uses
`pdftocairo` to create `<exam-id>.<figure-id>.png`; HTML uses a semantic `figure` with an
`img` carrying the same alt text. HTML and PDF
figures are never enlarged and are limited to 80% of the text width and the figure's
configured line-height limit while preserving aspect ratio.

As a TeX-only line-breaking refinement, a one-glyph inline expression such as `\(x\)`,
`\(\alpha\)`, or `\(\mathbb{R}\)` is kept with an immediately preceding word. Longer
expressions remain normally breakable, and canonical JSON and HTML are not
changed.

Compilation takes place outside the archive, so TeX auxiliary files never enter an exam
directory. Use `--temp-root` or `TEX_BUILD_ROOT` to select a fast temporary volume or a
RAM drive:

```sh
python3 build_tex.py --prototype --temp-root /Volumes/RAMDisk
TEX_BUILD_ROOT=/Volumes/RAMDisk python3 build_tex.py logic-phd-2006-aug
```

The selected root contains a reusable font cache and numbered per-exam build attempts.
A successful attempt is removed immediately after its PDF is copied back. A failed or
interrupted attempt is retained for diagnosis, and the next run uses a fresh numbered
directory so incomplete auxiliary files cannot contaminate it.

Do not run the generated accessible PDFs through OCRmyPDF or Ghostscript optimization.
A test with OCRmyPDF 16.10.2 using the archive's usual
`-O1 --skip-text --quiet --jobs 1` options reduced file size but removed the PDF tag
tree and all link annotations, downgraded PDF 2.0 to PDF 1.7, changed extracted text,
and caused both PDF/UA-2 and Well-Tagged PDF validation to fail. That command remains
appropriate only for the archived `<exam-id>.source.pdf` files, before extraction.

A tested `qpdf` object-stream recompression preserved PDF 2.0, tags, links, extracted
text, rendered pixels, and both validation profiles, but reduced the 93 KB prototype by
only about 3%. It is not part of the required build workflow.

Generate the archive homepage and all subject indexes from `manifest.json` with:

```sh
python3 build_indexes.py
```

Check that committed index pages still match the manifest without rewriting them:

```sh
python3 build_indexes.py --check
```

Every generated page begins its footer with a link to the project source and includes a
small semantic page-update date. Exam footers also link to the main index, their subject
index, and the archived `<exam-id>.source.pdf`. The shared date is maintained by
`PAGE_UPDATED_ISO` and `PAGE_UPDATED_LABEL` in `extract_exams.py`; update both when the
published presentation or archive contents change.

Validate every local PDF hash, canonical JSON record, generated HTML and index
page, review record, and MathJax expression with:

```sh
python3 validate_archive.py
```

Supply exam IDs to validate only a focused pilot or retry set:

```sh
python3 validate_archive.py logic-phd-2009-jan topology-phd-1994-aug
```

## Naming

A single-file sitting is stored as follows:

```text
exams/numerical-analysis-phd/numerical-analysis-phd-2026-jan/numerical-analysis-phd-2026-jan.source.pdf
```

When a table provides multiple files for the same sitting, the label is retained in each
exam directory name:

```text
exams/algebra-first-year/algebra-first-year-2025-aug-part-1/algebra-first-year-2025-aug-part-1.source.pdf
exams/algebra-first-year/algebra-first-year-2025-aug-part-2/algebra-first-year-2025-aug-part-2.source.pdf
```

Generated TeX and accessible PDF filenames retain the stable exam ID, for example
`algebra-first-year-2025-aug-part-1.tex` and
`algebra-first-year-2025-aug-part-1.pdf`, within that exam directory.

Undated practice exams use an explicit A/B variant instead of inventing a year or month:

```text
exams/algebra-first-year/algebra-first-year-practice-a-part-1/
exams/algebra-first-year/algebra-first-year-practice-a-part-2/
exams/algebra-first-year/algebra-first-year-practice-b-part-1/
exams/algebra-first-year/algebra-first-year-practice-b-part-2/
```

They are titled “Algebra First-Year Practice Exam A” or “Practice Exam B,” with the part
appended, and appear after all dated exams in the Algebra First-Year subject index.
In the department filenames, the digit identifies the part (`prac1*` is Part 1 and
`prac2*` is Part 2), while the trailing letter identifies Practice A or B.

The undated problem collection uses its own stable directory:

```text
exams/algebra-first-year/algebra-first-year-practice-problems/
```

It is titled “Algebra First-Year Exam, Practice Problems” and appears as the featured
“Practice Problems (113)” link above the dated and A/B practice-exam table.

First Year and PhD are normally appended to the subject tag. Two subject names have
explicit overrides:

- `Variational Analysis/Numerical Optimization` becomes `numerical-optimization-phd`.
- `Partial Differential Equations` becomes `pde-phd`.

Qualifying subjects use tags such as `algebra-qualifying`,
`analysis-qualifying`, `numerical-analysis-qualifying`, and
`topology-qualifying`.

January, May, August, and September are the expected exam months. If the source table
contains another valid month, the script preserves it, reports it in the manifest, and
uses its ordinary three-letter abbreviation rather than guessing a replacement. The
four practice exams and the practice-problem collection intentionally have neither a
month nor a year.

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
--pilot             Extract the eight representative pilot exams
--all               Extract every exam without a canonical JSON record
--subject TAG       Extract missing exams for a subject; repeatable
--affected [FILE]   Extract IDs from a schema-migration affected list
--limit N           Limit a bulk selection after completed records are skipped
--review-dir DIR    Review-log directory (default: exams)
--build-root DIR    Checkpoint root directory (default: build/extraction)
--model MODEL       Extraction model (default: gpt-5.6-sol)
--reasoning LEVEL   Reasoning effort: low, medium, or high (default: high)
--dpi N             Source-page rendering resolution (default: 200)
--workers N         Concurrent model calls (default: 2)
--force             Archive under build/ and re-extract completed records
--vision-only       Omit native PDF text and use rendered page images only
--skip-current      With --affected, skip current-prompt successful checkpoints
```

The dedicated practice-problem extractor accepts the same model, reasoning, DPI,
worker, manifest, review-directory, and build-root controls. Its optional positional ID
defaults to `algebra-first-year-practice-problems`; `--force` discards chunk reuse.
