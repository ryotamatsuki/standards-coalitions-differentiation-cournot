# Stage 14: JPET author-check proof — final editorial package

**Status: SCIENCE/TYPESETTING PASS in local build; final journal upload BLOCKED by author-specific declarations.** This file is a checklist and does not assert completion of author declarations.

## Manuscript preparation completed

- Canonical candidate: `manuscript/JPET_submission_author_check.tex`, in [Draft PR #36](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/pull/36), based strictly on Stage14 PR #35 exact science snapshot `cbe47a3777fdd193289eff0583f9d5d8d16e43d1`.
- Prior Stage 13R-M version label and `Not for submission` removed from the **typeset first page**, verified historical byline/independent research affiliation/ORCID kept unchanged.
- The JPET author guideline's **structured abstract** requirement is met with four explicit labels, Introduction / Methods / Results / Conclusion. The existing abstract's scientific statements and all economic claims are identical; 156 words without labels.
- Main scientific source after the abstract and before the Declarations block is **byte-identical** to Stage14 PR #35. Every mathematical lemma/theorem/proof, parameter figure/table, numerical finding, and all 20 references remain unchanged. The data/code statement points to a real immutable GitHub **commit SHA** (not a fictitious DOI). The theoretical study has no empirical dataset; its computational certificates and source files remain available from the repository at the pinned source revision.
- Relevant journal author requirements checked from the [current official Wiley JPET page](https://onlinelibrary.wiley.com/page/journal/14679779/homepage/forauthors.html), including the Research Exchange/Wiley Authors route and the paired `.tex` and PDF uploads, plus all `\\input` files.

## Truthfulness gates — action required from author

**The working PDF intentionally preserves these statements for author confirmation:**

1. **Funding:** confirm whether V2b received *any* external grant, employer-provided research support, funded computational resources or other relevant institutional support. The fact that an unrelated JRS paper declared no funding cannot prove this for V2b. If there was none, replace the italicized funding reviewer line with: `The author received no specific external funding for this research.`
2. **Competing interests:** confirm any relevant employment, research, consulting and financial interests for **this study**, not an earlier paper. If none, replace the italicized conflict line with `The author declares no competing interests.`
3. **AI assistance/acknowledgments:** a substantive OpenAI ChatGPT disclosure is drafted based on the actual reported literature, code, algebra, testing and manuscript work. Verify every use and claim about checks, whether other tools/versions were used, and whether acknowledgments are missing. Remove the italicized author-check instruction *only after personally approving the statement*.
4. **Pre-submission portal confirmations:** confirm originality and no simultaneous journal submission, necessary third-party permissions, accurate employment/affiliation identification and institutional restrictions, article/abstract/subject metadata in the live portal, and the exact **publisher-generated PDF**.

Author-approved declaration text must be inserted into the manuscript **before** submitting. Never upload an author-check proof carrying the italicized prompts.

## Live Wiley file designations

- Main `JPET_submission_author_check.tex` — select **Main Document – LaTeX .tex File**.
- The exact compiled `JPET_submission_author_check.pdf` after approvals — select **Main Document – LaTeX PDF**.
- `stage13r_proof_supplement.tex` and `stage13r_figure3_tikz.tex` — required **LaTeX Supplementary Files**.
- All three standalone figure PDF exports are supplied for upload as requested; use appropriate figure/supporting-file types, do not label them theorem proof certificates unless they are.
- The draft cover letter and Japanese approval checklist are author-review materials, not a substitute for direct portal statements.

**LaTeX compile:** `latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode JPET_submission_author_check.tex`.

**No manuscript or submission uploaded to Wiley.** Do not click final Submit without express author instruction.
