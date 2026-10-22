# Stage 13R-L — journal-reference integration, source/version ledger, and final manuscript QA

**Date:** 2026-10-23 JST. **Decision:** Literature/editorial changes and final PDF verification **PASS**. This is NOT approval to submit, a mathematical novelty reassessment, or a change to the Theory Freeze.

## Provenance and working scope
- Parent: Draft PR #32 `revision/stage13r-jpet-full-response-20261023`, exact baseline HEAD **`4532486e4929ba3d228229d76264c059ee3a6852`** at Stage13R-L start.
- Bibliographic selection authority: `literature/STAGE13R_REFERENCE_SELECTION_20261023.md` at the same `4532486...` commit. Actual source document read in full.
- Previous manuscript: `manuscript/stage13r_jpet_revised.tex` (21-page version), unchanged.
- New isolated target: Draft PR **#33**, branch `literature/stage13rl-reference-integration-20261023`, comparing **against PR #32's branch**, without merging/force-updating either branch or main.
- Integrated document: `manuscript/stage13rl_jpet_revised.tex`; separately built `manuscript/stage13rl_jpet_revised.pdf`. This is the **new editorial working version**; the original Stage13R source and all scientific scripts remain on disk/repository unchanged.
- Source integration commit: `07af7dc1ba9ba30a47eea6257d6d6aa03446d5a6`; verified CI source commit `14100c014f60fe5af26a1dc871b5a7d9b4c24c8c`. The resulting binary PDF was committed on the same isolated PR branch, whose PDF-validated head is `ff99a825058cd693ccb72b2afe1542a1ef777ff7`, prior to adding this QA record.

## Exactly 9 selected additions — claim, actual prose location, verified bibliographic version
| Added cite key / first author | Where inserted and what the citation supports | Evidence access/limits and version |
|---|---|---|
| `KatzShapiro1985`, Katz & Shapiro (1985) | **Model**, following quadratic utility: fixed expected network demand during quantity deviations and fulfilled expectations at equilibrium | *AER* 75(3):424–440, JSTOR 1814809. Publisher index and selection history; **not** claimed as derivation of our exact utility, `M`, cost, three-government game |
| `BranderSpencer2015`, Brander & Spencer (2015) | **Model** costly residual differentiation and **Related Literature** strategic-trade paragraph: rivalry softening via costly horizontal differentiation | *Research in Economics* 69(2):157–165, DOI 10.1016/j.rie.2015.02.007. NBER abstract + published bibliographic info; **not** 2022 entry/price-rank theorem and not same cost function |
| `TakaradaKawabata2025`, Takarada & Kawabata (2025) | **Related Literature**, government-cooperation paragraph: outsider incentives and regional-to-multilateral mutual-recognition barriers | **Nagoya City University Discussion Paper 701, February 2025**, author PDF. Not described as peer-reviewed or the same physical compatibility regime; no publication-only proposition numbers imported |
| `EconomidesFlyer1998`, Economides & Flyer (1998) | **Related Literature**, private network coalition paragraph: coalition incentives trade off network scale and product rivalry | `Equilibrium Coalition Structures in Markets for Network Goods`, *Annales d'Économie et de Statistique* 49/50:361–380, JSTOR stable 20076121, published original PDF/abstract; not mixed with distinct working-paper title |
| `BaakeBoom2001`, Baake & Boom (2001) | **Related Literature**, private decisions paragraph: attributes/quality versus compatibility are already distinct in the firm-level literature | *IJIO* 19(1–2):267–284, DOI 10.1016/S0167-7187(99)00029-6, publication record/abstract and prior source comparison; full proposition coverage not asserted |
| `BarrettYang2001`, Barrett & Yang (2001) | **Related Literature**, international standards paragraph: rational incompatibility with an international standard is not intrinsically new | *JIE* 54(1):171–191, DOI 10.1016/S0022-1996(00)00082-9, journal abstract/record and historic WP; no WP proposition transplanted into article |
| `CabralSalant2014`, Cabral & Salant (2014) | **Related Literature**, private investment paragraph: standards may change firms' R&D incentives | *IJIO* 36:48–56, DOI 10.1016/j.ijindorg.2013.07.006; 2014 journal abstract plus 2009 preprint context, no 2009 proposition citation as 2014 |
| `LambertiniRossini1998`, Lambertini & Rossini (1998) | **Related Literature**, same paragraph: common standards coexist with firms' technology/quality decisions | **University of Bologna, Department of Economics, Working Paper 263 (1998)**. University repository DOI 10.6092/unibo/amsacta/774; not falsely given a journal/2004 publication status |
| `ZhouSpencerVertinsky2002`, Zhou, Spencer & Vertinsky (2002) | **Related Literature**, strategic-trade paragraph: policy interacts with endogenous quality and export-market returns | *JIE* 56(1):205–232, DOI 10.1016/S0022-1996(01)00118-0. Journal abstract/introduction, not represented as a national accession theorem |

Original **11** retained without removal: `Buccella2023`, `Cheng2025`, `Costinot2008`, `GandalShy2001`, `Grossman2021`, `Kawabata2021`, `Klimenko2009`, `Rosen1965`, `Rump2010`, `Simcoe2012`, `Takarada2020`. All original bibliography text preserved and reordered by first author's surname; `Rosen1965` and `Rump2010` appear in the **unchanged proof supplement**. Complete list now **20/20 individually cited**, not padded by unrelated papers. All bibliographic entries in the actual `thebibliography` environment, not an unused `.bib` file.

## Editorial integration tests
- Introduction retains the early government-equilibrium headline and closest-standards comparison; no new list-of-names preamble.
- Model ties `KatzShapiro1985` to the **expectations convention** and `BranderSpencer2015` to **costly differentiation** at the two actual model definitions.
- Related Literature is three connected paragraphs, proceeding (a) government coordination and outsider rejection, (b) firm coalitions and quality/compatibility, (c) endogenous investment and national welfare incidence. Familiar mechanisms are conceded; the distinct headline is a **same-protocol controlled frozen-versus-redesign government-optimal outcome** on certified benchmark/open set under inherited depth.
- Abstract, Conclusion, main theorem claims and Figure3's **exploratory** scope remain intact. No claim of universal protocol-robust coalition reversal.
- **Not added automatically:** Brander–Spencer (2022) (separate entry/competition ranking not invoked), Maggi–Mrázová (2024 public author text vs unverified 2026 full revision), Cellini–Lambertini (2004) (additional investment comparison beyond current concise scope), and further coalition/standardization papers listed in the selection memo. Omission does **not** resolve any outstanding full-theorem novelty/absorption uncertainty.

## Exact independent CI and source-difference checks
- Verified **success** GitHub Actions run **39863273352**: https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39863273352.
- CI source SHA `14100c014f60fe5af26a1dc871b5a7d9b4c24c8c`. Workflow `.github/workflows/stage13rl-references-build.yml` writes binary PDF **only** to the independent `literature/stage13rl-reference-integration-20261023` branch.
- `scripts/stage13rl_citation_scope_qa.py` assertions succeeded: original 11 + selected nine = 20, **all 20 have in-text/appendix cites**, no undefined/duplicate keys; surname sort; 45 original source equation/align/theorem/proposition/lemma/proof/split environments **byte-identical**; complete proof supplement byte-identical to parent commit; same `\\Needspace` guard, same frozen Table2 and certificate Table3 `[H]` placements. No scientific computation code changed or re-run for prose edits.
- Full `latexmk` build succeeded; LaTeX log check found no unresolved refs, undefined citations, multiply-defined natbib items or Overfull `\\hbox` warnings.
- PDF is **22 pages**, rather than prior 21. No font or scientific content was compressed merely to preserve the old page count.

### Exact output verification

Downloaded the ZIP generated by **the successful run** (`stage13rl-jpet-literature-integrated-pdf`, artifact **12462472951**, sha256 ZIP digest `dba5cfc34d9a5fc562d80f55cc753c5b9276bcc4aee37db540f46fa6f6bf8d89`). Extracted the actual PDF and compared its Git blob identity to the saved PDF in the subsequent PR #33 head Git tree.

| Current artifact | Bytes | Full Git Blob SHA-1 | Comparison result |
|---|---:|---|---|
| **`manuscript/stage13rl_jpet_revised.pdf`** | **572,923** | `2593ef595fb52ff4be3ec7d7228b9f9dc4ac085f` | PASS: downloaded CI bytes = committed binary |
| `manuscript/stage13r_figure1.pdf` | 97,582 | `9977c9a04ce0a59c5bcd561e855cc81322dd9d0a` | PASS: unchanged from parent |
| `manuscript/stage13r_figure2.pdf` | 150,696 | `44d631aaf5c3a02929370e065cd9672b3fa8a2ab` | PASS: unchanged from parent |
| `manuscript/stage13r_figure3.pdf` | 107,883 | `60da45c9356e540f2f0a304958bf25eb8f5ec6e2` | PASS: unchanged from parent |

**PDF visual verification:** Rendered **pages 1, 2, 3, 9, 10, 13, 14, 19, 20, 21, 22** from the exact build artifact. Opening Model citations and the three Related Literature paragraphs remain readable. All bibliography pages **21–22** were visually inspected. Theorem 4 begins on **page 9** as a coherent block; Table 2 appears on **page 10** before its complete explanatory sentence; Table 3 appears on **page 19** before the following appendix section and does not interrupt a formula from its immediate "where" definition. No new orphaned paragraph, broken float or overlapping reference text was observed.

## Remaining issues (outside literature integration)
1. The author must approve and supply publication name/affiliation, ORCID/contact, verified funding, conflict, acknowledgments, research ethics and accurate generative-AI disclosure; the present manuscript still has explicit author-verification placeholders.
2. Archive a final immutable public code/data/replay release (DOI or stable immutable link) and record the article/certificate commit versions; Git branch history alone is not advertised as a deposited archive.
3. Recheck the live JPET portal/author instructions, all upload files, generated review PDF and receive the author's explicit submission approval. **No journal submission or merge performed.**
4. Full-text novelty questions about inaccessible/unverified supplements and later paper versions remain separately scoped; neither citation inclusion nor the absence of an additional citation is a blanket novelty certification.

**Stage 13R-L gate: PASS for reference integration, academic English coherence, PDF layout, and artifact reproducibility. Stage14/submission gate: NOT YET COMPLETE.**
