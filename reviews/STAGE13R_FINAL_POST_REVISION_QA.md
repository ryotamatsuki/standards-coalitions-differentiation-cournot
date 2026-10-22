# Stage13R-L current manuscript QA — 23 October 2026

**Current literature-integrated canonical draft in PR #33:** `manuscript/stage13rl_jpet_revised.tex`, compiled `manuscript/stage13rl_jpet_revised.pdf` (**22 pages**); source parent PR #32 HEAD `4532486e4929ba3d228229d76264c059ee3a6852`.

**New successful source QA and PDF build:** [GitHub Actions #39863273352](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39863273352), 20/20 reference-to-citation mapping PASS, all 45 scientific proof/formula environments unchanged, same proof supplement, zero undefined or duplicate citations and zero overfull boxes. The compiled PDF was saved **only to the independent literature branch**, not PR #32 or main.

**Exact current output identity (CI artifact ID `12462472951` / branch's committed blobs):**

| Current file | Size (bytes) | Git Blob SHA-1 |
|---|---:|---|
| `manuscript/stage13rl_jpet_revised.pdf` | **572,923** | `2593ef595fb52ff4be3ec7d7228b9f9dc4ac085f` |
| `manuscript/stage13r_figure1.pdf` (inherited unchanged) | 97,582 | `9977c9a04ce0a59c5bcd561e855cc81322dd9d0a` |
| `manuscript/stage13r_figure2.pdf` (inherited unchanged) | 150,696 | `44d631aaf5c3a02929370e065cd9672b3fa8a2ab` |
| `manuscript/stage13r_figure3.pdf` (inherited unchanged) | 107,883 | `60da45c9356e540f2f0a304958bf25eb8f5ec6e2` |

**Visually inspected updated pages:** 1–3, 9–10, 13–14, 19–22. Theorem 4 still starts page 9, Table 2 is on page 10 before its complete explanation, Table 3 is on page 19 and the subsequent formula/where definition is uninterrupted. Full bibliography is on pages 21–22, complete and readable. Nine new references and eleven originals have actual support in Model, Related Literature, Introduction or unchanged proof supplement.

**Author-held Stage14 blockers unchanged:** verified author metadata/ORCID and declarations (funding, COI, AI use, acknowledgment/ethics), deposited immutable source/code archive, actual portal-generated PDF and explicit approval. No paper submission or merge is authorized.

The detailed new source/version and QA ledger is [`STAGE13RL_REFERENCE_INTEGRATION_AND_QA.md`](STAGE13RL_REFERENCE_INTEGRATION_AND_QA.md).

---

## Historical Stage13R QA (before the additional nine references)

**The following older 21-page PDF sizes, hashes and run numbers describe the earlier Stage13R artifact only; they are retained to preserve the audit trail and are NOT the current literature-integrated manuscript.**

# Stage13R JPET hostile-referee revision — final post-revision quality assurance

**Date:** 2026-10-23 JST. **Input:** 18-item adversarial review, Draft PR #31 (Stage13 20-page working manuscript). **Implemented output:** Stage13R Draft PR #32; `manuscript/stage13r_jpet_revised.tex`, `manuscript/stage13r_proof_supplement.tex`, and `manuscript/stage13r_figure3_tikz.tex`. Prior Stage13 manuscript, numerical/scientific code, frozen theory, main unchanged.

**Editorial repair outcome: CONDITIONAL GO for final author verification; NOT journal submission authorization.**
The seventeen scholarly/editorial/technical issue responses (#01–#17) are implemented, with the immutable release link remaining a publication-stage dependency under #17. #18 is implemented as a production/declaration checklist and a non-fabricated manuscript template, but cannot be declared complete until the real author supplies and approves the statements. #17's production code/index is implemented; an immutable submitted public release is still an author-controlled publication task. There are **no unresolved identified manuscript-level prose, math-bridge, figure caption or LaTeX build failures**, but the separately defined author/archival/portal submission gate remains open.

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
| 13R-16 | Table 2 fixed-placement float and intact explanatory sentence on page 10; Table 3 fixed in Appendix E, equation/where bridge intact on page 19; Theorem 4 starts on page 9 | **PDF VISUAL + READING-ORDER PASS** |
| 13R-17 | `replication/STAGE13R_REPRODUCIBILITY.md` pins source commit, numerical vs exact scope, code/hashes, versions, commands, expected outputs; final deposited version link must be inserted when author publishes archive | EVIDENCE INDEX PASS; RELEASE PENDING |
| 13R-18 | `submission/STAGE13R_AUTHOR_INPUTS_AND_PACKAGE_BLOCKERS.md` and conspicuous in-manuscript confirmation placeholders; generates Figure1--3 separately as vector PDFs | TECHNICAL PACKAGING PASS; **AUTHOR DECLARATIONS PENDING** |

## Final post-layout QA: source, build, placement, and exact PDF identity

**Current manuscript revision:** the source layout fixes entered at commits `ea18f8cbc5f7329cc1ef08f8f0159feb6e40f4d3` and `30af5cd9102c647c7a2742d0740c696cb1ee8353` on Draft PR #32. The final dedicated build tested source commit **`30af5cd9102c647c7a2742d0740c696cb1ee8353`**, GitHub Actions run **39857593056**, whose entire job, four PDF compiles, strict reference/Overfull test, artifact upload, and branch PDF synchronization all returned **SUCCESS**.

- Execution and log: https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39857593056
- Generated run artifact: `stage13r-jpet-revised-paper-and-vector-figures`, ID **12460496115**; the downloaded archive contains the 21-page main PDF, 3 standalone vector figure PDFs, and the LaTeX build log.
- Exact binary-check target: live Draft PR #32 branch head **`44d0c30959cfb542e38d796b40307155e389da1c`** *before the QA-only metadata update*. The four PDF Git blob identities below match that branch's Git tree byte for byte, using the exact downloaded successful-run artifact (`SHA1("blob " + bytesize + "\\0" + filebytes)`). Revisions to this QA markdown after that commit do not alter the PDF blobs. Verify any later scientific/TeX/figure source changes against a new build.

| Checked-in PDF | Exact size (bytes) | Git Blob SHA-1, artifact and branch verified |
|---|---:|---|
| `manuscript/stage13r_jpet_revised.pdf` | **559,425** | `ad0d9477caab52c6a8f252511cc527c7c3f05c3a` |
| `manuscript/stage13r_figure1.pdf` | **97,582** | `9977c9a04ce0a59c5bcd561e855cc81322dd9d0a` |
| `manuscript/stage13r_figure2.pdf` | **150,696** | `44d631aaf5c3a02929370e065cd9672b3fa8a2ab` |
| `manuscript/stage13r_figure3.pdf` | **107,883** | `60da45c9356e540f2f0a304958bf25eb8f5ec6e2` |

**PDF-level visual and reading-order inspection, completed on the rebuilt article:**

1. **Theorem 4:** `\\Needspace{10\\baselineskip}` in the main TeX keeps the theorem heading and initial substantive lines together. The printed theorem begins at the top of **page 9**; it no longer leaves "There" stranded at the bottom of page 8.
2. **Table 2 (13R-16):** `\\begin{table}[H]` in the main TeX anchors the welfare table between its complete introductory paragraph and its complete explanation. Page **10** reads "At g=0.05, integration improves every country's welfare relative to fragmentation under either design treatment" continuously **after** the table; no intervening float splits that sentence. Both text extraction and page image were reviewed.
3. **Table 3 (certificate):** `\\begin{table}[H]` in the Appendix E source anchors the certificate at the end of Appendix E on **page 19**, ahead of the Appendix F header. Page **19** presents equation (43) immediately followed by its polynomial "where" definition with **no intervening table**, unlike the old float.
4. Standalone vector Figures 1–3 compile successfully; Figure 3 retains the explicitly exploratory "IS candidate" / "No offer found" scope. There were no changes to coefficient data, Nash conditions, certified intervals, primitive-space theorem scope, or scientific computation code.
5. CI parsing of LaTeX output reports **no unresolved citations/references, multiply defined natbib entries, or overfull boxes**. Pages 9, 10, 18 and 19 were separately rendered/inspected; manuscript length remains **21 pages**.

**Status of two additional layout/QA findings from the subsequent independent review:** RESOLVED. The earlier sizes (560196 and 559422 bytes) and earlier blob IDs are superseded; they must not be cited as proof of identity for the revised article.

## Submission blockers — do not fake PASS
1. Author-verified full name, research affiliation, correspondence email, ORCID.
2. Funding, conflicts, acknowledgments, ethics statement with actual facts; AI tool names/tasks and genuine author-review declaration.
3. Immutable public archived code/data release URL (and final manuscript/certificate commit SHA), checked against final public artifact; repository branch alone is not asserted an archived DOI.
4. Actual JPET portal policy check and submission-generated review PDF inspection, and final express author approval.
5. No external JPET editorial or referee decision has been made, no manuscript submitted.

**Gate:** Stage13R scholarly/editorial revisions and build/graphics QA **COMPLETE**; final submission **BLOCKED ON AUTHOR-ONLY DISCLOSURES / ARCHIVAL RELEASE / STAGE14 PORTAL QA**. No new model extension necessary.
