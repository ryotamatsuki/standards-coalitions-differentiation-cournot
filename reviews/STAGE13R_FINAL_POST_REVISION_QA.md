# Stage13R JPET hostile-referee revision — final post-revision quality assurance

**Date:** 2026-10-23 JST. **Input:** 18-item adversarial review, Draft PR #31 (Stage13 20-page working manuscript). **Implemented output:** Stage13R Draft PR #32; `manuscript/stage13r_jpet_revised.tex`, `manuscript/stage13r_proof_supplement.tex`, and `manuscript/stage13r_figure3_tikz.tex`. Prior Stage13 manuscript, numerical/scientific code, frozen theory, main unchanged.

**Editorial repair outcome: CONDITIONAL GO for final author verification; NOT journal submission authorization.**
16? No: 17 scholarly/editorial/technical issues (#01 through #17) are implemented. #18 is implemented as a production/declaration checklist and a non-fabricated manuscript template, but cannot be declared complete until the real author supplies and approves the statements. #17's production code/index is implemented; an immutable submitted public release is still an author-controlled publication task. There are **no unresolved identified manuscript-level prose, math-bridge, figure caption or LaTeX build failures**, but the separately defined author/archival/portal submission gate remains open.

## Full item-by-item disposition (nothing silently omitted)
| Referee issue | Final manuscript or workflow response | QA result |
|---|---|---|
| 13R-01 | §1/§2 clearly distinguish government g, firm x, substitute-demand B, network H/eta, rho and destination-market expectations | EDIT PASS |
| 13R-02 | Frozen cost K(z), private differentiation saving, domestic CS/home-firm profit mechanism, Table2 backward induction | EDIT PASS |
| 13R-03 | Explicit stand-alone m-s versus outsider accession i-o and B's anticipated continuation | EDIT PASS |
| 13R-04 | Replace scientifically incorrect 'same government payoffs' with identical primitives/objectives/votes and **different induced reduced payoffs** | EDIT PASS |
| 13R-05 | Main all-depth theorem proof separated into (1) full Nash, (2) consent/optimal depth with conservative interval bounds, (3) open-neighborhood persistence; supplementary certificate table | EDIT PASS |
| 13R-06 | Appendix A unilateral quantity derivative and cross-firm profit bridge; correct plus sign in induced loss | EDIT PASS |
| 13R-07 | Private design equilibrium heading; Appendix F unambiguous delta welfare gap notation and maintained full Nash | EDIT PASS |
| 13R-08 | Rosen (1965), Rump (2010) cited at applicable Nash and interval-proof steps, duplicates caught and eliminated | EDIT+RENDER PASS |
| 13R-09 | Face-cutoff derivative and explicit inward interior-Nash continuation from rho=1 face; restricted application | EDIT PASS |
| 13R-10 | Direct Takarada2020 Proposition 2, 5--6 comparison, core vs specified government procedure and original controlled firm continuation | EDIT PASS |
| 13R-11 | Compress generic novelty defenses and repeated proof-process prose; preserve scope | EDIT PASS |
| 13R-12 | Replace entire Abstract with research question, institution, central mechanism, results and limitation | EDIT PASS |
| 13R-13 | Simplify network-boundary discussion, closest literature, direct-grand boundary and Conclusion | EDIT PASS |
| 13R-14 | Figure3 in-panel labels **IS candidate / No offer found**; caption/text explicitly withdraw 2D exact partition; graph polygons unchanged | RENDER+SCOPE PASS |
| 13R-15 | Shorten Figure1 explanatory caption; keep original causal sequence and Figure2 | EDIT+RENDER PASS |
| 13R-16 | Main results table crossrefs to theorem/proposition labels and two-step Table2 national-acceptance explanation | EDIT+RENDER PASS |
| 13R-17 | `replication/STAGE13R_REPRODUCIBILITY.md` pins source commit, numerical vs exact scope, code/hashes, versions, commands, expected outputs; final deposited version link must be inserted when author publishes archive | EVIDENCE INDEX PASS; RELEASE PENDING |
| 13R-18 | `submission/STAGE13R_AUTHOR_INPUTS_AND_PACKAGE_BLOCKERS.md` and conspicuous in-manuscript confirmation placeholders; generates Figure1--3 separately as vector PDFs | TECHNICAL PACKAGING PASS; **AUTHOR DECLARATIONS PENDING** |

## Reproducibility of *final checked-in* graphics and PDF
Latest successful GitHub Actions job: **39843182651**:
https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39843182651

- All steps SUCCESS: wrapper generator, integrated LaTeX compile, three standalone figure PDF compiles, strict checking for Overfull hbox, duplicate/undefined citations/refs, publication of workflow artifacts and branch binary sync.
- Actual 21-page updated manuscript `manuscript/stage13r_jpet_revised.pdf`; PDF size **560,196 bytes**.
- Independently downloaded the **exact final successful run artifact ZIP** and checked byte-identical Git Blob SHA for all 4 PDFs against the live Draft PR #32 head tree:

| File | Size | Verified Git Blob SHA |
|---|---:|---|
| `manuscript/stage13r_jpet_revised.pdf` | 560196 | `19285a8cea5adfc50aa63a0e0390e3d1fd844350` |
| `manuscript/stage13r_figure1.pdf` | 103981 | `a8c50e73ff5efe473e64a6170d34d0cfa1e43fac` |
| `manuscript/stage13r_figure2.pdf` | 150696 | `c4f2039906205c0133c9b5f3eba4947542afc141` |
| `manuscript/stage13r_figure3.pdf` | 103857 | `db5ff551a10bf71a0e079549e17f6ab4c0b03463` |

- Parsed final `stage13r_jpet_revised.log`: no Overfull hbox, undefined citation/reference, or duplicated natbib citation; CI independently enforced this.
- Page rendering was visually inspected, including first page, numerical Figure3 page 11, appendix certificate, and declarations/last bibliography. Main source has 3 figures, 2 tables and exactly one `\end{document}`.
- The workflow had **initial failures** (duplicate stale source fragment, incomplete draft paragraph, then binary push races); each was repaired and the latest *full* run passed, rather than treating past failures as PASS.
- Scientific model and underlying code are unchanged. No new theorem claim; numerical Figure3 is **exploratory** only.

## Submission blockers — do not fake PASS
1. Author-verified full name, research affiliation, correspondence email, ORCID.
2. Funding, conflicts, acknowledgments, ethics statement with actual facts; AI tool names/tasks and genuine author-review declaration.
3. Immutable public archived code/data release URL (and final manuscript/certificate commit SHA), checked against final public artifact; repository branch alone is not asserted an archived DOI.
4. Actual JPET portal policy check and submission-generated review PDF inspection, and final express author approval.
5. No external JPET editorial or referee decision has been made, no manuscript submitted.

**Gate:** Stage13R scholarly/editorial revisions and build/graphics QA **COMPLETE**; final submission **BLOCKED ON AUTHOR-ONLY DISCLOSURES / ARCHIVAL RELEASE / STAGE14 PORTAL QA**. No new model extension necessary.
