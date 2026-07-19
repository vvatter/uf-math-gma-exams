# Dataset Extraction Approach

## Goal

The Graduate Mathematics Association exam archives maintained by the University of
Florida Department of Mathematics contain decades of First Year and PhD examination
material for students who entered before Fall 2025, plus Qualifying Exams for students
who entered in Fall 2025 or later. The project will extract the information contained
in every exam into a clean, consistent dataset so it can be presented in more
accessible forms. Those presentations may be WordPress posts, newly generated PDFs, or
both.

This is not archival transcription and not PDF remediation. We aim to preserve the
questions, mathematical meaning, and instructions while discarding document furniture
that has no continuing value.

The Git repository is also the durable project archive. It tracks the acquisition and
extraction code, documentation and tests, losslessly optimized source PDFs, canonical
JSON records, generated Markdown views, and `manifest.json` provenance. The original
download size and hash remain in the manifest even when optimization changes the stored
PDF bytes. Regenerable page renders, model checkpoints, and other build artifacts remain
outside Git under `build/`.

## Unit of Work

Every linked PDF is one exam record and produces one adjacent JSON file plus one
Markdown view generated from that JSON. A PDF labeled Part 1 and a PDF labeled Part 2
are separate exams for this purpose. If a part was never published, no placeholder or
synthetic record is created.

Files that repeat questions from another exam are extracted independently. The dataset
does not deduplicate questions or create shared question records.

The PDF, canonical JSON, and generated Markdown are stored together for efficient
review. They share a filename stem and differ only by extension:

```text
exams/algebra-first-year/algebra-first-year-2025-may-part-1.pdf
exams/algebra-first-year/algebra-first-year-2025-may-part-1.json
exams/algebra-first-year/algebra-first-year-2025-may-part-1.md
```

An exam without a part has no part suffix:

```text
exams/numerical-analysis-phd/numerical-analysis-phd-2025-aug.json
exams/numerical-analysis-phd/numerical-analysis-phd-2025-aug.md
```

The filename stem is the stable exam identifier.

## Canonical Metadata

The catalog link determines:

- subject;
- subject tag;
- month;
- year;
- part, when present;
- the current canonical URL of the PDF on the GMA website.

This metadata is authoritative. The extractor must not obtain or revise the date from
the PDF contents. A full date printed in a PDF is discarded, and an internal date that
conflicts with the linked date is ignored.

The title displayed later can be generated from the subject, month, year, and part. It
does not need to be transcribed or stored separately.

## Core JSON

Schema version 2 stores document content as an ordered block sequence:

```json
{
  "schema_version": 2,
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
            "text": "Let \\(\\sum_{n=0}^{\\infty}c_nx^n\\) be a power series.",
            "subparts": []
          }
        }
      ]
    }
  ]
}
```

`part` is `null` when the linked exam is not a separately cataloged part. The `content`
array may contain `instructions`, `problem`, and `section` blocks. A section preserves
its displayed heading and contains instruction and problem blocks in source order;
sections are not nested.

A rare linked PDF may contain only a notice that the exam was not provided. Such a
record contains one instruction block and no problem blocks. This is a valid
representation of the archive item, not an extraction failure or a synthetic exam.

There is deliberately no field for:

- stored top-level problem numbers;
- original noninteger top-level labels;
- points;
- page numbers;
- full dates;
- names or signatures;
- the original title;
- layout coordinates.

`pdf_url` is the current canonical HTTPS URL used by the downloader, not necessarily
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
manifest-approved hash. This allows cached JSON and Markdown to survive byte-level PDF
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

When a labeled section line also contains a direction, the label or named title becomes
the section heading and the direction becomes its first instruction block. A labeled
direction with no following problems is an ordinary instruction block when it governs
other listed problems. If the line itself states a mathematical task, it becomes a
problem inside that section.

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
no printed integer problem label. It continues the preceding derived sequence and is
logged as a numbering transformation. This keeps the problem schema minimal while
making the added presentation number explicit in the audit record.

## Multipart Problems

Each problem block contains one problem object. Subparts do not remain embedded in its
`text`. They are ordered objects in the problem's `subparts` array:

```json
{
  "text": "Determine which of the following are irreducible.",
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

Nested subparts are supported by the Markdown renderer as nested bullet levels. This
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
paragraphs.

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
manually against source pages and generated Markdown before the complete run.

The pilot added an ASCII-control-character invariant after exposing corrupt mathematical
text that earlier MathJax matching could not see. That check found four more records for
fresh extraction, bringing the final source-based set to 131. Two especially malformed
documents required the narrowly scoped encoding-repair fallback described above.

The finished archive contains 129 section blocks across 48 exams, and 92 exams contain
more than one positioned instruction block. All 528 records use schema version 2. The
complete archive validator passed 23,154 MathJax expressions with no control characters
remaining. Superseded version-1 files are not retained in the canonical dataset; Git
history and ignored build history provide the audit trail.

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

`review-serious.json` contains unresolved cases that actually require a person before
publication. A typical record is:

```json
{
  "exam_id": "topology-phd-2025-may",
  "problem_indices": [12],
  "category": "visual-content",
  "source_pdf": "exams/topology-phd/topology-phd-2025-may.pdf",
  "source_pages": [2],
  "message": "Problem 12 depends on a pictured curve in a solid torus.",
  "status": "open"
}
```

Serious-review categories initially include:

- `visual-content`: a figure, diagram, graph, or table carries information;
- `shared-context`: notation or material applies to only a subset of problems and
  its scope remains unclear even with ordered instruction blocks;
- `cross-reference`: a problem refers to another problem and renumbering may matter;
- `transcription`: words or mathematics remain uncertain after initial extraction;
- `numbering`: source numbering is missing, duplicated, or otherwise unclear;
- `instructions`: selection or response rules may not agree with the final numbering.

For visual content, the automatic pass transcribes the surrounding problem text but
does not invent a description or reconstruction. The review record identifies the exam,
problem, and source page so a person can restore the missing information appropriately.

For shared context whose scope cannot be represented confidently with a positioned
instruction block, the automatic pass does not guess. It flags the case so a reviewer
can resolve the intended scope.

Serious items have `status: open`. They do not stop corpus extraction, but they prevent
the affected exam from being treated as ready for accessible publication. Logged
corrections and transformations do not block publication.

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
2. Its identifier, directory, subject metadata, date, and part agree with the catalog
   manifest and filename.
3. It contains at least one nonempty problem, or a nonempty notice when the linked PDF
   contains no exam questions.
4. Every section has a nonempty heading, a restart/continue policy, and at least one
   problem; instruction blocks may occur anywhere but cannot be empty.
5. Problem numbers are derived from content order and section policy rather than stored,
   so contradictory sequences cannot enter the data.
6. Every problem and subpart has a `subparts` array, and every subpart has a nonempty
   original `label` field.
7. ASCII control characters and dollar-sign math delimiters are absent, MathJax
   delimiters are balanced, and every expression completes real MathJax TeX-to-CHTML
   rendering without an error.
8. Every model-reported correction, transformation, or uncertainty appears in its
   corresponding review file.
9. Every source PDF has either one dataset JSON or an explicit extraction failure.
10. No exam with an open serious-review item is marked ready for publication.

Initial extraction results remain provisional until the later verification phase. The
archive validator additionally checks every PDF hash, JSON and Markdown pair, absolute
review index, source reference in the review logs, review page number, and expression
using the pinned MathJax version before publication begins. It accepts exam IDs for a
focused validation run and no IDs for the complete archive.

## Presentation Is Downstream

The dataset is the source of truth for future outputs. The extraction command also
creates a Markdown view of each accepted JSON record. Its title contains the subject,
followed by “first year exam” or “PhD exam,” month, year, and part when present.
Instructions are italicized, problem numbers are bold, and labeled subparts are compact
nested bullets. Section headings and displayed problem numbers are derived from ordered
blocks and restart/continue policy. Markdown is always regenerated from JSON and is
never independently edited or returned by the model.

When a source problem has labeled subparts but no independent stem, the Markdown
renderer adds a presentation-only sentence such as “This problem has three parts.” The
sentence is derived from the subpart array and is not added to the canonical JSON or
represented as source-authored text.

A WordPress renderer can create semantic headings, ordered problem lists, labeled nested
subpart lists, and accessible MathJax output.

A PDF generator can produce a newly typeset accessible PDF from the same record.

Neither renderer should need to inspect the original PDF. Source pages are consulted
only while resolving a review item or auditing extraction quality.
