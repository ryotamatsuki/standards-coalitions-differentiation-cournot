# Stage13 — RIO draft metadata, author sign-off and submission declarations
**Date:** 2026-10-21 JST. **Status:** DRAFT / NO AUTHOR ATTESTATION / NOT FOR PORTAL SUBMISSION.
Journal: Review of Industrial Organization; original research article (Stage12 provisional). See `journal/STAGE12_RIO_REQUIREMENTS_LEDGER_2026-10-21.md`.

## Known items integrated into current manuscript

- Title: `International Standards Coalitions and Endogenous Product Design`; uniform across paper and Stage12 report.
- Abstract: approximately **186 English words** (current revised `paper/main.tex`; final quantitative count must be rechecked at Stage14) within Stage12 recorded 150–250 range.
- Five indexing keywords present; provisional JEL `L13, L15, L50, F15`; final journal/portal classification rules not verified.
- `paper/sections/07_discussion.tex` now contains *Methods and research-assistance disclosure* acknowledging substantive AI assistance in literature, language, analytic checks and software preparation; not a fabricated human verification claim.
- `production/scripts/generate_consent_table.py` and canonical `generate_welfare_table.py` deterministically produce both quantitative tables. `make table` and `make table-check` enforce sources and regression anchors.
- Formal proof limitation remains explicit: Lean only rational proxies, interval code for actual Nash/all-g.
- Stage8 theory identity and nine frozen Git blobs unchanged.

## Required author facts / attestations — explicitly pending

| Requirement | State | Reason / next action |
|---|---|---|
| Exact author name, order and authoritative institutional affiliation | AUTHOR-CONFIRMATION REQUIRED | Not inferred from GitHub username, public employer, profile or location |
| Corresponding author validated email, ORCID if available | AUTHOR-CONFIRMATION REQUIRED | No personal contact invented in manuscript |
| Human intellectual contribution and content sign-off | AUTHOR-CONFIRMATION REQUIRED | Earlier author scope approval is not verification of every Stage13 prose/math change |
| Funding and acknowledgments | AUTHOR-CONFIRMATION REQUIRED | Do not say no funding without actual declaration |
| Competing interests | AUTHOR-CONFIRMATION REQUIRED | Do not say none without author attestation |
| CRediT / contribution specification | AUTHOR-CONFIRMATION REQUIRED | AI/LLM not assigned authorship |
| Research data / generated-only computer evidence | DRAFT | No empirical data collected; source programs/coefficients, archive version and exact public repository release must be confirmed for data statement |
| Code availability / reproducibility location | DRAFT | Public repo exists; freeze/tag and run logs need immutable release and submission-time match |
| Substantive generative AI disclosure | DRAFT IN MANUSCRIPT | Verify all tools, models, dates and adopted outputs from actual project provenance with author; Springer/RIO portal fields Stage14 |
| Single-/double-anonymous review and manuscript identities | UNVERIFIED | Keep `\author{}` empty in anonymous-looking working paper; not a final author decision. Inspect authenticated RIO portal |
| Initial submission LaTeX files, title page, supplements, references.bib package | PENDING STAGE14 | Main compiles in CI; real journal upload file grouping, naming and class rules to be checked live |
| Cover letter, reviewer recommendations, declarations fields, APC/charges and preprints | PENDING STAGE14 | No invented portal/form requirements |

## Draft disclosure wording for author approval (do not submit unreviewed)

Generative AI systems assisted with manuscript drafting and editing, literature triage and comparison, software preparation, and exploratory mathematical checks. The mathematical claims rely on the stated symbolic and interval-computation routines and source-linked proofs; a limited Lean program checks only pointwise rational proxy comparisons. The authors remain responsible for the work's scientific validity, source accuracy, and final interpretation. The precise tool inventory and author verification record will be reviewed before submission.

The manuscript paragraph already discloses these points without claiming human independent verification. Journal-specific final location and wording remain for Stage14.

**Blocking status:** Not submission-ready; author declarations, current portal fields, and complete primary-source novelty audit (Cheng–Huang 2025 main propositions) remain unresolved.