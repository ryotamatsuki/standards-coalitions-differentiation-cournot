# Stage13 — FINAL integration/exposition/reviewer-verifiability gate
**Date:** 2026-10-22 JST. **Verdict: GO TO STAGE14 SUBMISSION QA, NOT journal submission approval.** This is an AI-assisted editorial/technical review, not an actual external review or a JPET decision.

## Verified current artifact identity
- **Frozen input:** Stage12 Journal Positioning PR29; Stage11 repaired 21-page current manuscript on PR28 at `e9e534863f54e19e438a1ace26bf91ff1dedfb2d`.
- **New integrated article:** `manuscript/stage13_jpet_integrated.tex`. Git blob `2412d3b868614260d1ad110ff5e97c6c1eaaab64` checked against locally integrated source before CI.
- **Mathematical supplement:** `manuscript/stage13_proof_supplement.tex`, unedited copy from the **latest GitHub** Stage11 `manuscript/stage11_proof_supplement.tex` (includes SU two-variable Krawczyk / IS scalar interval Newton and the lift to full three-firm Nash); unchanged mathematical certificate.
- **Numerical Figure3:** `manuscript/stage13_figure3_tikz.tex`, unedited copy of Stage11 v0.5r1 vetted numerical candidate diagram; not certified phase partition.
- **Canonical compiled Stage13 PDF:** `manuscript/stage13_jpet_integrated.pdf` **20 pages / 524131 bytes**, Git blob `e55fd8e5d9a55c958757d113c32fae131d1b1604`, committed on Stage13 branch by independent GitHub Actions.
- **Build run:** https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39799741413 — **SUCCESS**, job `build` all steps success: `latexmk` ran successive pdflatex passes; final pass log contains no undefined references/citations or overfull line diagnostics; 20pp reported and output artifact uploaded, then PDF committed to branch. Historical first attempt `39799323104` failed **only** because host runner lacked `pdfinfo` after successful LaTeX; workflow now checks successful `Output written on ... (20 pages)` in native TeX log. This operational failure was repaired and is not silently called PASS.
- Original Stage11 TeX/PDF, Stage12 journal reports, main, and Theory Freeze have NOT been edited on this branch.

## Workflow v2.9 Stage13 closeout checklist (actual revised manuscript)
| Mandatory criterion | Evidence | Decision |
|---|---|---|
| Exposition profile | THEORY-FIRST Original Article for JPET; no fake empirical methods | PASS |
| Introduction search-cost: question, stakes, primitives, finding, method, closest novelty, limitations | §§1–2; direct local + all-depth result before further details | PASS |
| Section purity and reader arrival | model §2; Nash §3; incidence §4; local/global theorem §5; institution §6; supporting thresholds §7; predecessor comparison §8; conclusion §9 | PASS |
| CORE/HELPFUL/APPENDIX/DELETE and repetition | `STAGE13_EXPOSITION_STREAMLINING_REPORT.md` documents individual sections; repetitive hedges and contributions compressed | PASS |
| Five-exhibit thought experiment | 3 figures, 2 tables each with distinct reading purpose and verified source, as in `STAGE13_FIGURE_TABLE_RECONCILIATION.md` | PASS |
| Reviewer-verifiability full proof chain | `STAGE13_REVIEWER_VERIFIABILITY_REPORT.md`: primitives→Cournot→unilateral Nash→national incidence→voting→strict all-g certificate→optimal proposal; SU/IS reductions explained | PASS |
| Exhibit caption scope and algorithm | Figure3 star separately center-certified, broad `kappa,eta` map candidly exploratory; gray=no agreement found in sampled search, not proof | PASS |
| Certificate integrity | Stage11 immutable 1000 interval source, upper signs, global frozen SU envelope; no universal bargaining or 2D all-depth theorem claimed | PASS |
| Math notation/references | GitHub LaTeX all passes; 2 theorems, 2 lemmas, 2 propositions; no unresolved references in final compilation log | PASS |
| PDF and legibility | local preview 20p, Figure3/Table1+Table2 pp10–11 visually inspected; remote builds same integrated article with authoritative latest supplement | PASS for integration / final journal print proof remains Stage14 |
| Original scientific content | no additional government primitives, transfer rule, renegotiation game, arbitrary demand proof, numerical result, or publication-priority upgrade | PASS |
| Submission declarations | author data/ORCID/funding/COI/AI/data availability still intentionally placeholders | PENDING Stage14, not Stage13 proof blocker |
| Journal submission itself | not initiated or authorized | SEPARATE Stage14 final gate |

## Status / boundary
The correct **final source of truth is the GitHub Stage13 PDF built with the latest complete Stage11 proof supplement**. The local preview archive created earlier may contain a reconstructed proof supplement with immaterial wording differences and must NOT be used to make byte-identity claims about the canonical GitHub PDF. For Stage14 submission preparation use the new branch files and successful workflow artifact; historic Stage11 file remains for provenance.

**Stage13 = GO (exposition/verification/exhibit integration completed and independent GitHub build SUCCESS). Proceed to Stage14 journal-authoring and final submission QA, not direct portal upload.** Any new substantive mathematical contradiction should reopen the earliest affected proof stage, not be patched by prose.
