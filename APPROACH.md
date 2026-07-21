# Dataset Extraction Approach

## Goal

The Graduate Mathematics Association exam archives maintained by the University of
Florida Department of Mathematics contain decades of First Year and PhD examination
material for students who entered before Fall 2025, plus Qualifying Exams for students
who entered in Fall 2025 or later. Four undated Algebra First-Year practice exams and a
113-question Algebra First-Year practice-problem collection from the department's
qualifying-exam syllabi page are included as well. The project will
extract the information contained in every exam into a clean, consistent dataset so it
can be presented in more accessible forms. Those presentations may be WordPress posts,
newly generated PDFs, or both.

This is not archival transcription and not PDF remediation. We aim to preserve the
questions, mathematical meaning, and instructions while discarding document furniture
that has no continuing value.

The Git repository is also the durable project archive. It tracks the acquisition and
extraction code, documentation and tests, losslessly optimized source PDFs, canonical
JSON records, generated HTML views, and `manifest.json` provenance. Each
exam has its own directory, which also provides stable locations for newly typeset TeX
and accessible PDF output. The original download size and hash remain in the manifest
even when optimization changes the stored PDF bytes. Regenerable page renders, model
checkpoints, TeX auxiliary files, and other build artifacts remain outside Git.

## Unit of Work

Every linked exam PDF is one exam record and produces one JSON file plus an HTML view
generated from that JSON. The separate practice-problem PDF is one collection record
with 113 ordered problem blocks. A PDF labeled Part 1 and a PDF labeled Part 2
are separate exams for this purpose. If a part was never published, no placeholder or
synthetic record is created.

Files that repeat questions from another exam are extracted independently. The dataset
does not deduplicate questions or create shared question records.

The source PDF, canonical JSON, and generated HTML are stored
together for efficient review. The exam directory name is the stable identifier. The
archived original is always `<exam-id>.source.pdf`; `index.html` is the web presentation;
and the data and typeset files retain the exam ID:

```text
exams/algebra-first-year/algebra-first-year-2025-may-part-1/
  algebra-first-year-2025-may-part-1.source.pdf
  algebra-first-year-2025-may-part-1.json
  index.html
  algebra-first-year-2025-may-part-1.tex
  algebra-first-year-2025-may-part-1.pdf
  algebra-first-year-2025-may-part-1.<figure-id>.png  # only when needed
```

The TeX and second PDF are generated accessible presentations; they are not renamed
copies of the archived source. An exam without a part has no part suffix:

```text
exams/numerical-analysis-phd/numerical-analysis-phd-2025-aug/
  numerical-analysis-phd-2025-aug.source.pdf
  numerical-analysis-phd-2025-aug.json
  index.html
```

The directory name and manifest `id` field are the stable exam identifier.

Undated practice records replace the date component with a stable A/B variant:

```text
exams/algebra-first-year/algebra-first-year-practice-a-part-1/
  algebra-first-year-practice-a-part-1.source.pdf
  algebra-first-year-practice-a-part-1.json
  index.html
  algebra-first-year-practice-a-part-1.tex
  algebra-first-year-practice-a-part-1.pdf
```

The practice-problem collection is also undated but is distinguished by document type
and declared problem count rather than by an invented variant:

```text
exams/algebra-first-year/algebra-first-year-practice-problems/
  algebra-first-year-practice-problems.source.pdf
  algebra-first-year-practice-problems.json
  index.html
  algebra-first-year-practice-problems.tex
  algebra-first-year-practice-problems.pdf
```

## Canonical Metadata

The catalog link determines:

- subject;
- subject tag;
- month;
- year;
- part, when present;
- the current official URL of the PDF.

This metadata is authoritative. The extractor must not obtain or revise the date from
the PDF contents. A full date printed in a PDF is discarded, and an internal date that
conflicts with the linked date is ignored.

The department's supplemental practice page instead determines the A/B variant and
Part 1 or Part 2. Those records intentionally store `null` for both `year` and `month`;
the extractor must not infer a date from the PDF or filesystem metadata. No other record
may omit its date, and a dated record may not have a practice variant.
The source filenames encode these dimensions independently: `prac1a` and `prac1b` are
Part 1, while `prac2a` and `prac2b` are Part 2; the final `a` or `b` is the practice
variant.

The same page identifies the practice-problem collection. Its canonical and manifest
records use `document_type: "practice-problems"`, `problem_count: 113`, null date and
part fields, and no practice variant. Validation requires the ordered content to contain
exactly the declared number of problems.

The title displayed later can be generated from the document type, subject, date or
practice variant, and part. It does not need to be transcribed or stored separately.

## Core JSON

Schema version 3 stores document content as an ordered block sequence and gives each
problem an ordered body of text and manually verified TikZ figure blocks:

```json
{
  "schema_version": 3,
  "id": "analysis-first-year-2015-jan-part-2",
  "subject": "First Year Analysis",
  "subject_tag": "analysis-first-year",
  "year": 2015,
  "month": "january",
  "part": 2,
  "pdf_url": "https://gma.math.ufl.edu/wp-content/uploads/sites/130/FY_Analysis-2_2015_01.pdf",
  "content": [
    {
      "type": "instructions",
      "text": "Do exactly 2 problems from Part A and 2 problems from Part B."
    },
    {
      "type": "section",
      "heading": "Part A",
      "numbering": "restart",
      "content": [
        {
          "type": "problem",
          "problem": {
            "body": [
              {
                "type": "text",
                "text": "Let \\(\\sum_{n=0}^{\\infty}c_nx^n\\) be a power series."
              }
            ],
            "concerns": [],
            "subparts": []
          }
        }
      ]
    }
  ]
}
```

`part` is `null` when the linked exam is not a separately cataloged part. `year` and
`month` are normally required together. They are both `null` only for an undated
practice record or practice-problem collection. An undated practice exam has
`practice_variant` set to `"A"` or `"B"`. The `content` array may contain `instructions`,
`problem`, and `section` blocks. A section preserves
its displayed heading and normally contains instruction and problem blocks in source
order; sections are not nested. A labeled group that only directs the reader back to
previously listed problems is represented as an instruction-only section with the
source-appropriate restart/continue policy.

A rare linked PDF may contain only a notice that the exam was not provided. Such a
record contains one instruction block and no problem blocks. This is a valid
representation of the archive item, not an extraction failure or a synthetic exam.

The practice-problem collection adds `document_type: "practice-problems"` and
`problem_count: 113`; ordinary exams use the default document type and do not declare a
problem count. Its top-level problem numbers are still derived from content order rather
than stored in the canonical problem objects.

A problem's optional `concerns` array records a legible source question that appears to
contain a mathematical error, missing hypothesis, undefined object, or other substantive
problem. Each record has a `status` of `suspected` or `confirmed` and a concise
`explanation`. Model extraction may create only `suspected` concerns; `confirmed` is
reserved for an explicit human decision.

There is deliberately no field for:

- stored top-level problem numbers;
- original noninteger top-level labels;
- points;
- page numbers;
- full dates;
- names or signatures;
- the original title;
- layout coordinates.

`pdf_url` is the current official HTTPS URL used by the downloader, not necessarily
the literal legacy URL found in the page markup. The acquisition manifest remains the
source for local paths, hashes, redirects, and other download provenance.

The manifest distinguishes the bytes originally downloaded from the local working PDF.
`download_sha256` and `download_size` preserve acquisition provenance. `sha256` and
`size` describe the current working file and may change after intentional lossless PDF
optimization. Refreshing working metadata is an explicit local operation; it does not
replace the original download hash.

The archived PDFs were optimized one at a time with
`ocrmypdf -O1 --skip-text --quiet --jobs 1`. An optimized temporary file replaces the
downloaded file only when it is smaller, and the original access and modification times
are restored. OCRmyPDF is an optional archive-maintenance tool, not part of extraction.

When an approved working hash differs from an existing extraction checkpoint, the old
working hash is retained in `source_sha256_history` and the checkpoint adopts the new
manifest-approved hash. This allows cached JSON and HTML to survive byte-level PDF
optimization without erasing provenance or making another model call.

## Instructions

An exam may have as many instruction blocks as the source requires. A block remains at
its source position: before the first problem, inside a section, or between problem
groups. It preserves meaningful rules such as:

- how many problems to answer;
- which ranges or groups must be represented;
- whether full proofs or short responses are expected;
- requirements about clarity, detail, showing work, conclusions, and legibility;
- allowed materials or methods, when relevant;
- notation that applies to the whole exam.

Instructions are not rewritten merely for clarity, combined into a preamble, or moved
away from the material they govern. Their wording and sentence-level detail are
preserved as closely as possible. Boilerplate about names, answer sheets, page use,
dates, and grading boxes is removed, but authored requirements about the expected
response are retained. References are changed only when a noninteger source label must
be normalized.

When a labeled section line also contains a direction before following problems, the
label or named title becomes the section heading and the direction becomes its first
instruction block. The same representation is used when the direction governs
previously listed problems and the section has no problems of its own. If the line
itself states a mathematical task, it becomes a problem inside that section.

Point values are removed from individual problems. If point values are the source's
only indication that two groups require different levels of response, that distinction
is expressed in the custom instructions without retaining the scores.

## Problem Numbering

Problems do not store a `number` field. Their order in the JSON determines their
displayed number. Instructions do not increment the counter. A section has one binary
numbering policy:

- `restart` resets the displayed counter to 1 for its first problem;
- `continue` advances from the preceding displayed problem number.

This preserves ordinary restarted numbering in parts and topic sections without
flattening it or rewriting instructions. Review records refer to `problem_indices`,
which are absolute one-based problem positions in document reading order and therefore
remain unambiguous when displayed numbers repeat.

The schema intentionally does not represent noninteger top-level labels. Actual corpus
cases such as `A–C`, `C1–C8`, `1A–4C`, and `5, 5′, 6, 6′` are normalized to derived
consecutive numbers in reading order. Each such change receives a
`numbering-transformation` record, and any instruction reference changed as a result
receives an `instruction-rewrite` record. Unexpected ambiguity is serious review rather
than silent normalization.

The corpus also contains one standalone mathematical task under a section heading with
no printed integer problem label. Its section restarts the derived sequence, so the task
is displayed as Problem 1 and logged as a numbering transformation. This keeps the
problem schema minimal while making the added presentation number explicit in the audit
record.

## Problem Bodies And Figures

Every problem has a `body` array followed by a `subparts` array. Normal extraction
places the complete problem stem in one text block. Text and figures can be interleaved
when a visual must appear at a specific point:

```json
{
  "body": [
    {
      "type": "text",
      "text": "Compute the homology of the space shown."
    },
    {
      "type": "tikz",
      "id": "filled-torus",
      "alt": "Diagram of a torus with two filled openings.",
      "libraries": [],
      "options": ["line cap=round", "x=1cm", "y=1cm"],
      "height_lines": 6,
      "code": "\\draw (0,0) -- (1,1);"
    }
  ],
  "subparts": []
}
```

TikZ is manual, reviewed restoration rather than model output. The `code` value contains
only the body of `tikzpicture`; `documentclass`, document wrappers, and the
`tikzpicture` environment itself are generated downstream. `libraries` and `options`
record only what that figure needs, `height_lines` sets its PDF and HTML height limit
and defaults to six, and each figure ID is unique within its exam.

The LaTeX renderer places the TikZ directly in the tagged PDF as vector content and
passes `alt` to its `Figure` structure. The same build creates a transparent 300 DPI PNG
for HTML. HTML uses a semantic `figure` and `img` with the same alt text. PDF and HTML presentations preserve
aspect ratio, do not enlarge the art, and cap it at 80% of the text width and the
figure's `height_lines` value. The generated PNG is named
`<exam-id>.<figure-id>.png`.

## Multipart Problems

Each problem block contains one problem object. Subparts do not remain embedded in its
body text. They are ordered objects in the problem's `subparts` array:

```json
{
  "body": [
    {
      "type": "text",
      "text": "Determine which of the following are irreducible."
    }
  ],
  "subparts": [
    {
      "label": "(a)",
      "text": "\\(X^3-X^2+X+2\\) in \\(\\mathbb{Q}[X]\\)",
      "subparts": []
    },
    {
      "label": "A.",
      "text": "A differently styled source part",
      "subparts": []
    },
    {
      "label": "1.",
      "text": "A numerically styled source part",
      "subparts": []
    }
  ]
}
```

The label is preserved exactly as a field: `(a)`, `A.`, `1.`, `i.`, and other authored
forms are not normalized. Labels are not repeated in the `text` value. `subparts` is an
empty array when there are none. If a subpart itself contains labeled parts, the same
structure recurses through its own `subparts` array.

Nested subparts are supported by the HTML renderer as nested semantic lists. This
occurs in the source corpus and is covered by a rendering regression test. Labels still
count as subpart structure when they are printed inline: if `(a)` contains `(1)`, `(2)`,
and `(3)`, those three items are nested beneath `(a)` rather than left inside its text.

## Mathematical Transcription

The extractor preserves the mathematical task, not the visual typesetting. Ordinary
prose uses Unicode text. MathJax is the target math renderer. Dataset strings use
`\(...\)` for inline math and `\[...\]` for displayed math. Because backslashes are
escaped in serialized JSON, those delimiters appear as `\\(...\\)` and `\\[...\\]` in
the JSON file.

A mathematical identifier remains math even when it is only one letter inside a prose
sentence. For example, “no two adjacent \(a\)’s” stores the `a` in inline math while
leaving the apostrophe and surrounding punctuation in prose. This is a model judgment;
a deterministic check cannot distinguish every variable from an English article
without producing false positives.

Display math is reserved for standalone formulas. A short centered instruction such as
“Find \(\max_{X\in I} f(X)\)” is represented as its own prose paragraph using inline
math rather than being promoted to a display equation solely because of its source
layout. Meaningful paragraph boundaries are retained with blank lines; definitions,
standalone formulas, instructions, and concluding tasks are not merged into adjacent
paragraphs. Generated presentations italicize instruction prose while keeping displayed
mathematics upright.

Mathematicians' names use their standard spelling and diacritics when the identity is
unambiguous, such as `Gödel` rather than `Goedel`. Established eponymous names use an en
dash between different people's names, as in `Hahn–Banach`, `Radon–Nikodym`,
`Gram–Schmidt`, and `Borsuk–Ulam`. A hyphen that belongs within one person's surname is
preserved. These are controlled presentation normalizations rather than source
corrections, so they do not create correction-review records. An ambiguous identity or
name form is preserved as printed and sent to serious review rather than guessed.

The model may:

- join lines and remove line-break hyphenation;
- normalize whitespace;
- replace visual math typesetting with equivalent MathJax-compatible TeX;
- remove point values and administrative text;
- correct a typographical error only under the rule below.

The model may not:

- paraphrase or summarize a problem;
- modernize wording merely for style;
- change notation without necessity;
- add definitions, hints, assumptions, or solutions;
- silently resolve a mathematically meaningful ambiguity.

**Correction rule:** Preserve the source reading unless the intended correction is
uniquely determined by the immediate mathematical context.

Every typographical correction is added to `exams/review-corrections.json`. The record
includes the original text, corrected text, immediate context, and problem index. If
more than one correction is plausible, the source reading remains in the dataset and
the uncertainty is placed in `exams/review-serious.json` instead.

## Mathematical Concerns

When the source is legible but its mathematics appears false, underdetermined,
internally inconsistent, or dependent on a missing definition or hypothesis, the source
wording remains unchanged and the problem receives a canonical concern. The explanation
states the issue cautiously and does not propose a repair unless the immediate
mathematical context uniquely determines one. A transcription uncertainty remains a
serious-review item instead; it is not converted into a mathematical concern merely
because one possible reading would be false.

Concerns are publication data rather than unresolved extraction tasks. HTML and LaTeX
place a dark-red, boldly labeled warning before the affected problem, so the warning is
encountered before a reader attempts the question and does not depend on color alone.
The root `concerns.html` page collects every concern, groups them under linked exam
titles, and prefixes each warning with its displayed problem number. The same content is
included in accessible PDFs and their reading order.

## Vision-First Extraction

The source collection includes scans, broken encodings, and difficult mathematical
typesetting. Native PDF text and OCR may be supplied as supporting evidence, but neither
is authoritative.

`gpt-5.6-sol` with high reasoning is the extraction model. It receives rendered page
images plus the catalog metadata and returns schema-constrained JSON. The prompt tells
it explicitly to ignore printed titles and dates, remove unwanted administrative text,
preserve problem wording, and transcribe mathematics for MathJax.

Native PDF text is sanitized to remove ASCII control characters before it is offered as
untrusted evidence. `--vision-only` omits native text for documents where that evidence
is counterproductive. If a model response nevertheless contains control characters, a
narrow Sol recovery pass receives the escaped extraction and repairs only its encoding
and MathJax delimiters. Both response IDs and usage records remain in the checkpoint.

The normal path performs one Sol extraction per exam; it does not send every result
through a second model pass. Raw responses and page evidence are retained as build
checkpoints; only schema-valid canonical exam JSON enters the dataset.

The large practice-problem collection uses nine independently resumable calls rather
than one oversized request. Pages 3 and 4 are one chunk because Problem 42 begins on
page 3 and ends on page 4; every other source page is its own chunk. Temporary source
numbers are allowed only in chunk responses so ordinary code can require the exact
ranges 1–14, 15–29, 30–55, 56–66, 67–77, 78–88, 89–98, 99–110, and 111–113. The merge
then removes those temporary numbers and creates the canonical ordered problem blocks.
An experiment that extracted pages 3 and 4 both jointly and separately found the same
30–55 sequence and no mathematical disagreements, but the page-3-only response wrongly
treated the incomplete Problem 42 as complete. The joint chunk is therefore the
authoritative configuration.

## Corpus-Wide Iteration

The first complete pass is expected to reveal document classes and failure modes that
were not anticipated in advance. A result in which roughly 70 percent of exams are good
and 30 percent need a revised approach and re-extraction would be normal, not a pipeline
failure.

The workflow therefore favors a complete, checkpointed initial pass over repeated
per-exam refinement:

1. Extract the entire corpus once with a versioned schema and prompt.
2. Review deterministic failures and the serious-review queue; audit the correction and
   transformation logs for recurring patterns.
3. Identify recurring failure classes rather than patching isolated JSON by hand.
4. Revise the prompt, parser, schema, or postprocessing rule as appropriate.
5. Re-extract only the affected exams, preserving the original checkpoints.
6. After extraction and selective reprocessing are complete, run a separate verification
   pass across the resulting dataset.

The later verification pass is a distinct project phase. Its model prompt, evidence,
and acceptance rules will be designed after the initial corpus has shown what actually
needs verification.

### Schema Version 2 Migration

The ordered-block schema was tested as a corpus migration rather than as 127 individual
reports. Of the 528 version-1 records, 401 flat records were converted mechanically.
The 127 records previously associated with instruction or numbering transformations
were selected for fresh extraction from their PDFs. An eight-exam pilot was compared
manually against source pages and generated HTML before the complete run.

The pilot added an ASCII-control-character invariant after exposing corrupt mathematical
text that earlier MathJax matching could not see. That check found four more records for
fresh extraction, bringing the final source-based set to 131. Two especially malformed
documents required the narrowly scoped encoding-repair fallback described above.

The finished archive contains 134 section blocks across 48 exams, and 92 exams contain
more than one positioned instruction block. The complete version-2 archive validator
passed 23,161 MathJax expressions with no control characters remaining. Superseded
version-1 files are not retained in the canonical dataset; Git history and ignored
build history provide the audit trail.

### Schema Version 3 Figure Support

Version 3 replaced each problem's single `text` field with an ordered `body` array. The
528 version-2 records were migrated mechanically: every nonempty stem became one text
block, with no change to its string value, and empty stems remained empty bodies. This
made exact figure placement possible without changing problem numbering or subpart
structure. Manually reviewed TikZ blocks can now be inserted beside the text they
illustrate, and all presentations remain deterministic products of the same JSON.

## Review Logs

Extraction writes three files with different operational meanings:

```text
exams/review-corrections.json
exams/review-transformations.json
exams/review-serious.json
```

`review-corrections.json` logs every uniquely determined source correction. Each record
includes the original and corrected readings plus their immediate context. These records
have `status: logged`.

`review-transformations.json` logs completed, intentional structural changes. Current
transformation categories are:

- `numbering-transformation`: noninteger labels or an unnumbered standalone task were
  assigned derived consecutive numbers;
- `instruction-rewrite`: an instruction reference was minimally changed to agree with
  normalized noninteger labels.

Transformation records have `status: logged`. They document what the extractor did and
do not by themselves require intervention.

`review-serious.json` contains unresolved source, transcription, visual, or structural
cases that actually require a person before publication. Apparent mathematical flaws in
otherwise legible questions are canonical concerns, not serious-review records. A
typical serious-review record is:

```json
{
  "exam_id": "topology-phd-2025-may",
  "problem_indices": [12],
  "category": "visual-content",
  "source_pdf": "exams/topology-phd/topology-phd-2025-may/topology-phd-2025-may.source.pdf",
  "source_pages": [2],
  "message": "Problem 12 depends on a pictured curve in a solid torus.",
  "status": "open"
}
```

Serious-review categories initially include:

- `visual-content`: a figure, diagram, graph, or table carries information that was
  not completely and unambiguously transcribed;
- `shared-context`: notation or material applies to only a subset of problems and
  its scope remains unclear even with ordered instruction blocks;
- `cross-reference`: a reference to another problem has a broken or ambiguous target;
- `transcription`: words or mathematics remain uncertain after initial extraction;
- `numbering`: source numbering is missing, duplicated, or otherwise unclear;
- `instructions`: selection or response rules may not agree with the final numbering.

For unresolved visual content, the automatic pass transcribes the surrounding problem
text but does not invent a description or reconstruction. A table that can be represented
completely and unambiguously as MathJax or structured text is transcribed and does not
require a serious-review record. Otherwise, the review record identifies the exam,
problem, and source page so a person can restore the missing information appropriately.

For shared context whose scope cannot be represented confidently with a positioned
instruction block, the automatic pass does not guess. It flags the case so a reviewer
can resolve the intended scope.

Serious items have `status: open`. They do not stop corpus extraction, but they prevent
the affected exam from being treated as ready for accessible publication. Logged
corrections, transformations, and clearly disclosed mathematical concerns do not block
publication.

## Content Removed

The dataset normally omits:

- logos, branding, and department names;
- printed titles that duplicate catalog metadata;
- full dates and days of the month;
- page numbers, headers, and footers;
- names, signature fields, grading grids, and answer-space instructions;
- point values;
- blank pages and writing space;
- scan noise and handwritten marks that are not part of a question.

## Deterministic Validation

Before an exam JSON is accepted, ordinary code checks that:

1. The file matches the versioned JSON schema.
2. Its identifier, directory, subject metadata, document type, date or practice variant,
   and part agree
   with the catalog manifest and exam directory name. Year and month must occur together;
   only an explicitly labeled practice exam or practice-problem collection may omit both.
3. It contains at least one nonempty problem, or a nonempty notice when the linked PDF
   contains no exam questions.
4. Every section has a nonempty heading, a restart/continue policy, and at least one
   instruction or problem block. A section may contain instructions without containing
   problems. Instruction blocks may occur anywhere but cannot be empty.
5. Problem numbers are derived from content order and section policy rather than stored,
   so contradictory sequences cannot enter the data.
6. Every problem has a `body` and `subparts` array; text blocks are nonempty; TikZ blocks
   have unique IDs, nonempty alt text and code, and no document or environment wrappers;
   every subpart has a nonempty original `label` field.
7. Every concern has a valid status and a nonempty, nonduplicated explanation; Unicode
   mathematical symbols cannot appear outside MathJax delimiters.
8. Every canonical TikZ block has a readable generated PNG beside its exam outputs.
9. ASCII control characters and dollar-sign math delimiters are absent, MathJax
   delimiters are balanced, and every expression completes real MathJax TeX-to-CHTML
   rendering without an error.
10. Every model-reported correction, transformation, or uncertainty appears in its
   corresponding review file.
11. Every source PDF has either one dataset JSON or an explicit extraction failure; a
    practice-problem collection also contains exactly its declared problem count.
12. No exam with an open serious-review item is marked ready for publication.

Initial extraction results remain provisional until the later verification phase. The
archive validator additionally checks every PDF hash, JSON, HTML, and site-index
set, absolute review index, source reference in the review logs, review page number, and expression
using the pinned MathJax version before publication begins. It accepts exam IDs for a
focused validation run and no IDs for the complete archive. Its verified, on-demand
MathJax cache contains only the TeX input, CommonHTML output, lightweight DOM adapter,
and required font metrics, avoiding a full npm installation and `node_modules` tree.

## Presentation Is Downstream

The dataset is the source of truth for generated outputs. The extraction command creates
an HTML view of each accepted JSON record. Its title contains the subject,
followed by “First-Year Exam,” “PhD Exam,” or “Qualifying Exam,” month, year, and part
when present. An undated practice title instead includes “Practice Exam A” or “Practice
Exam B” and its part, without a fabricated date. The collection title is “Algebra
First-Year Exam, Practice Problems.”
Instructions are italicized, problem numbers are bold, and labeled subparts are compact
nested lists. Restored figures use PNG assets and carry the canonical alt text.
Section headings and displayed problem numbers are derived from ordered
blocks and restart/continue policy. HTML is always regenerated from JSON and is never
independently edited or returned by the model.

When a source problem has labeled subparts but no independent stem, the HTML and TeX
renderers add a presentation-only sentence such as “This problem has three parts.” The
sentence is derived from the subpart array and is not added to the canonical JSON or
represented as source-authored text.

The static HTML renderer creates semantic headings, ordered problem lists, labeled
nested subpart lists, keyboard-visible links, responsive equations, accessible MathJax
output, and print styles. It uses a narrow reading column and Computer Modern webfonts.
The source-PDF and subject-index links are omitted when the page is printed.

Canonical concerns render immediately before their problems as semantic notes with a
bold warning label. The warning's dark-red color is supplementary rather than its only
identifying feature.

A second deterministic renderer creates a root archive index and one index inside every
subject directory, plus a root concerns index. The root page orders levels as
Qualifying, First-Year, and PhD, then orders subjects alphabetically within each level.
Subject tables order dated exams from newest to oldest, put undated practice exams at
the bottom, and link to the accessible HTML and archived PDF. The Algebra First-Year
index features the 113-question collection above that table rather than counting it as
another exam. `concerns.html` orders subjects alphabetically, orders exams newest first
within each subject, and groups numbered warnings under a single linked exam title. The
index pages use semantic navigation, scoped table headings, visible keyboard
focus, responsive overflow, and the same institutional identity and typography as the
exam pages. The complete archive validator compares every generated index against
`manifest.json` and the canonical concern records.

Website navigation is self-contained. Generated pages do not link to the retiring GMA
website; source URLs remain in canonical data only as provenance. Every page footer puts
the project-source link first and includes a subdued semantic update date. Subject pages
then link to the main archive, while exam pages link to the main archive, their named
subject archive, and the committed `<exam-id>.source.pdf`. The site-wide update date is an explicit
renderer constant so regeneration remains deterministic and does not make every page
appear changed merely because validation ran on another day.

The same semantic HTML can be adapted for WordPress publication.

A deterministic LaTeX renderer generates a second, newly typeset presentation from the
same JSON. It uses LuaLaTeX from TeX Live 2026, Unicode Computer Modern fonts, ordinary
LaTeX headings and lists, and current LaTeX tagging support to produce tagged PDF 2.0
targeting PDF/UA-2. Ordinary mathematics receives nested MathML structure. The visual
design follows the HTML presentation: a single-line institutional header, a large
left-aligned title with a thin rule, italic instructions, bold problem numbers, compact
problem spacing, paper-conscious margins, and no printed page numbers.
The institutional names are invisible-style links to the university and department
websites. Only the subject-and-level portion of the title is likewise linked, without
color or border, to the future
`https://gma.math.ufl.edu/exams/<subject-tag>/` archive location; the date and part
remain outside the link.

The TeX renderer also prevents a simple one-glyph inline expression from becoming a
line-start orphan when it immediately follows a word. It emits a nonbreaking space
before atoms such as `\(x\)`, `\(\alpha\)`, and `\(\mathbb{R}\)`, while leaving longer
expressions normally breakable. This is presentation-only preprocessing and does not
modify the canonical data or the other generated formats.

The source and generated PDFs remain distinct. `<exam-id>.source.pdf` is the optimized
archive copy; `<exam-id>.pdf` is compiled from `<exam-id>.tex`. TeX compilation occurs in a
configurable temporary root, which may be a RAM drive. A reusable LuaLaTeX font cache is
kept outside the repository. Successful build directories are deleted immediately,
including all auxiliary files. Failed and interrupted attempts remain in numbered
per-exam directories for diagnosis, while retries use a fresh directory to avoid
reading a truncated auxiliary or MathML file.

Generated accessible PDFs must not be passed through OCRmyPDF or Ghostscript
optimization. Testing OCRmyPDF 16.10.2 with
`-O1 --skip-text --quiet --jobs 1` removed the structure tree and link annotations,
downgraded the file from PDF 2.0 to PDF 1.7, changed extracted text, and failed both
PDF/UA-2 and Well-Tagged PDF validation. Lossless optimization of the archived
`<exam-id>.source.pdf` inputs remains a separate, pre-extraction operation. A `qpdf`
object-stream rewrite preserved accessibility and rendered output in testing, but its
approximately 3% size reduction did not justify making it a build dependency.

Automatic LuaLaTeX MathML generation does not currently handle `amscd` reliably. The
renderer therefore disables nested MathML only around an `amscd` display, while keeping
the diagram visually typeset and represented as a tagged formula. All other formulas
retain MathML structure. This narrow compatibility fallback is covered by a renderer
test and the resulting prototypes are checked against both veraPDF's PDF/UA-2 and
Well-Tagged PDF profiles.

Neither renderer should need to inspect the original PDF. Source pages are consulted
only while resolving a review item or auditing extraction quality.
