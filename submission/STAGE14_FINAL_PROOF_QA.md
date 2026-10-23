# JPET Stage 14 Final Polish — submission author-check proof

Date: 2026-10-23. **Source and page-layout technical QA: PASS. Actual journal submission readiness: BLOCKED pending author declarations and consent.**

## Source
Baseline Stage14 PR #35 complete HEAD `cbe47a3777fdd193289eff0583f9d5d8d16e43d1`. New Draft PR #36 contains `manuscript/JPET_submission_author_check.tex` and PDF. Changed ONLY the first-page version/date line, Abstract heading structure (Introduction / Methods / Results / Conclusion; original scientific propositions preserved), and final declaration/acknowledgment block. Automated `scripts/stage14_jpet_submission_proof_qa.py` verifies entire intervening manuscript byte-for-byte unchanged, exact 20/20 references, immutable original proof-supplement/figure3 input, and prevents silent adoption of V2b funding/COI declarations.

The title carries the already-confirmed Ryota Matsuki / Independent Researcher, Matsuyama, Ehime, Japan / email / ORCID details. No employer affiliation is claimed.

## Exact technical verification

- Local `latexmk` three-pass build: success, 23 pages; external GitHub CI build: [#39914237814](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39914237814) full SUCCESS. Original initial regex-only script failure was fixed and is superseded.
- Canonical committed GitHub PDF: `manuscript/JPET_submission_author_check.pdf`, **23 pages**, **594,246 bytes**, Git blob SHA-1 **`1c564f78db81f01282430dff3fea6571f40adac0`**, raw PDF SHA-256 **`38a020b4827a6a7abb5a83d33c0228ebad2d41198ea5bf63d92a3d64987ba381`**.
- Canonical source `manuscript/JPET_submission_author_check.tex`: **61,568 bytes**, Git blob SHA-1 **`bd7c15e8b1ce8e18abfc633a821fc43529ab7cb0`**, raw SHA-256 **`900c12709d89e0b91a1dd00eeddfb00c9f03acb5565bcc206f33a985caa3adf4`**.
- Workflow artifact ID **12484386827**: actual extracted PDF's complete Git blob ID verified identical to committed GitHub PDF. Local and CI-generated PDFs have different bytes because of LaTeX toolchain differences; final distributed ZIP uses the **verified CI PDF**.
- All 23 GitHub CI PDF pages rendered; focus visual inspection on pp.1–2 (title, structured abstract, intro), pp.9–11 (theorem proof, Tables 1/2, Figure 3), pp.21–23 (funding/COI, data/code, ethics, AI disclosure, 20 references). Zero reported Overfull hboxes, undefined citations, missing references. Table 1 remains after the final proof sentence, not interleaved into it.
- Download package contains the exact approved-CI PDF, main LaTeX source, 2 input TeX files, 3 vector figure PDFs, author-check guide, cover-letter draft and SHA256 file manifest.

## Remaining, required author input

- V2b research funding / institutional support (prior unrelated JRS `none` does not establish V2b fact);
- V2b competing interests;
- Exact AI disclosure wording and any omitted acknowledgments; author review of proofs, numerical artifacts, citations and manuscript;
- Originality / no active overlapping submission, any necessary reproduction or institutional permissions, final author approval, and live Wiley Research Exchange-generated review PDF.
- The author-check PDF contains explicit italicized confirmation prompts. **It is not suitable for upload unchanged**. A dated, stable GitHub code commit URL is already in the data availability statement; JPET current requirements do not demand a DOI as a universal prerequisite.

**Stop rule:** no claims of submission readiness or click on Submit until statements are personally verified and incorporated, then a newly built PDF is inspected. No journal submission or merge occurred.
