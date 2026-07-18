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

The initial public dataset remains intentionally small:

```json
{
  "schema_version": 1,
  "id": "algebra-first-year-2025-may-part-1",
  "subject": "First Year Algebra",
  "subject_tag": "algebra-first-year",
  "year": 2025,
  "month": "may",
  "part": 1,
  "pdf_url": "https://gma.math.ufl.edu/wp-content/uploads/sites/130/FY-Algebra-1_2025_05.pdf",
  "instructions": "Answer four questions. Indicate which four problems should be graded.",
  "problems": [
    {
      "number": 1,
      "text": "Let \\(p\\) be a prime and let \\(G\\) be a nontrivial finite \\(p\\)-group.",
      "subparts": [
        {
          "label": "(a)",
          "text": "Prove that \\(Z(G)\\) is nontrivial.",
          "subparts": []
        },
        {
          "label": "(b)",
          "text": "Prove that every nontrivial finite \\(p\\)-group has a normal subgroup of index \\(p\\).",
          "subparts": []
        }
      ]
    }
  ]
}
```

`part` is `null` when the exam is not divided. `instructions` is `null` when the
source provides no meaningful instructions.

A rare linked PDF may contain only a notice that the exam was not provided. Such a
record preserves the notice in `instructions` and uses an empty `problems` array. This
is a valid representation of the archive item, not an extraction failure or a synthetic
exam.

There is deliberately no field for:

- original top-level problem labels separate from the normalized `number`;
- sections;
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

Each exam has at most one instructions string. It preserves meaningful rules such as:

- how many problems to answer;
- which ranges or groups must be represented;
- whether full proofs or short responses are expected;
- requirements about clarity, detail, showing work, conclusions, and legibility;
- allowed materials or methods, when relevant;
- notation that applies to the whole exam.

Instructions are not rewritten merely for clarity. Their wording and sentence-level
detail are preserved as closely as possible. Only the minimum edits needed to combine
instruction blocks, remove excluded logistics, or update references after problem
renumbering are allowed. Boilerplate about names, answer sheets, page use, dates, and
grading boxes is removed, but authored requirements about the expected response are
retained.

When the source gives different directions for problem ranges, the directions are
combined into one coherent string. For example:

```text
For Problems 1–5, show all work and support all statements. For Problems 6–15,
give complete definitions, statements, or short proofs.
```

Point values are removed from individual problems. If point values are the source's
only indication that two groups require different levels of response, that distinction
is expressed in the custom instructions without retaining the scores.

## Problem Numbering

Ordinary exams retain their top-level problem numbers. Unexpected gaps or cross-problem
references are flagged for review rather than silently repaired.

Some single PDFs contain internal parts or sections that restart their problem numbers. In
that case, the problems receive one consecutive global sequence, the final ranges and their
source parts are explained in the instructions, and the transformation is logged for review.
For example, Part I Problems 1–5 followed by Part II Problems 1–5 become global Problems
1–10, with the instructions identifying Problems 1–5 as Part I and Problems 6–10 as Part II.

Logic exams are a common instance of this rule. Their section-local labels are replaced
with one global sequence. Section names are folded into the instructions rather than
stored as problem metadata. For example:

```text
Complete seven problems, including at least one from each topic. Problems 1–3
concern General Logic, Problems 4–6 concern Model Theory, Problems 7–9 concern
Set Theory, and Problems 10–12 concern Computability.
```

The generated ranges must be derived from the final problem numbering so they cannot
drift out of agreement with the problem list.

## Multipart Problems

Each top-level problem is one JSON object. Subparts do not remain embedded in its
`text`. They are ordered objects in the problem's `subparts` array:

```json
{
  "number": 4,
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
includes the original text, corrected text, immediate context, and problem number. If
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

The initial corpus run performs one Sol extraction per exam. It does not immediately
send every result through a second model pass. Raw responses and page evidence are
retained as build checkpoints; only schema-valid canonical exam JSON enters the
dataset.

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

- `numbering-transformation`: section-local or restarted labels were replaced by one
  global problem sequence;
- `instruction-rewrite`: multiple instruction blocks were materially consolidated or
  rewritten to agree with final problem numbers.

Transformation records have `status: logged`. They document what the extractor did and
do not by themselves require intervention.

`review-serious.json` contains unresolved cases that actually require a person before
publication. A typical record is:

```json
{
  "exam_id": "topology-phd-2025-may",
  "problem_numbers": [12],
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
  cannot be represented cleanly in the single instructions field;
- `cross-reference`: a problem refers to another problem and renumbering may matter;
- `transcription`: words or mathematics remain uncertain after initial extraction;
- `numbering`: source numbering is missing, duplicated, or otherwise unclear;
- `instructions`: selection or response rules may not agree with the final numbering.

For visual content, the automatic pass transcribes the surrounding problem text but
does not invent a description or reconstruction. The review record identifies the exam,
problem, and source page so a person can restore the missing information appropriately.

For shared context that cannot be put into the exam instructions, the automatic pass
does not invent a new data structure. It flags the case so a reviewer can decide
whether to duplicate the context into the affected problems or express its scope in the
instructions.

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
4. Top-level problem numbers are unique.
5. Logic problem numbers are globally sequential and their generated topic ranges agree
   with the problem list.
6. Every problem and subpart has a `subparts` array, and every subpart has a nonempty
   original `label` field.
7. MathJax delimiters are balanced and the TeX can be parsed by the target renderer.
8. Every model-reported correction, transformation, or uncertainty appears in its
   corresponding review file.
9. Every source PDF has either one dataset JSON or an explicit extraction failure.
10. No exam with an open serious-review item is marked ready for publication.

Initial extraction results remain provisional until the later verification phase. A
representative pilot and the full first pass will establish additional checks before
publication begins.

## Presentation Is Downstream

The dataset is the source of truth for future outputs. The extraction command also
creates a Markdown view of each accepted JSON record. Its title contains the subject,
followed by “first year exam” or “PhD exam,” month, year, and part when present.
Instructions are italicized, problem numbers are bold, and labeled subparts are compact
nested bullets. Markdown is always regenerated from JSON and is never independently
edited or returned by the model.

When a source problem has labeled subparts but no independent stem, the Markdown
renderer adds a presentation-only sentence such as “This problem has 3 parts.” The
sentence is derived from the subpart array and is not added to the canonical JSON or
represented as source-authored text.

A WordPress renderer can create semantic headings, ordered problem lists, labeled nested
subpart lists, and accessible MathJax output.

A PDF generator can produce a newly typeset accessible PDF from the same record.

Neither renderer should need to inspect the original PDF. Source pages are consulted
only while resolving a review item or auditing extraction quality.
