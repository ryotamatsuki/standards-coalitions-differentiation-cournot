# V2b Stage25 Figure/Table Architecture Gate — v0.2 correction
**Date:** 2026-10-22 JST | **Status:** actual LaTeX/PDF v0.2 completed locally; manuscript still NOT submission-ready.

## Why needed
Stage10 of `ryotamatsuki/research-paper-workflow` v2.9 requires a figure/table architecture prior to Stage11. The v0.1 English draft contained only a numeric table and lacked deliberate figure selection. This omission is now corrected in the **actual 16-page v0.2 LaTeX source/PDF**, not merely in a future plan.

## Exhibit map
| Exhibit | Exact location | Economic purpose | Claim boundary |
|---|---|---|---|
| Figure 1: government proposal + backward-induction continuation | p.5 / Model & timing | A proposes AB(depth g), B votes anticipating accession, C & incumbents vote on inherited g, terminal SW/SU/IS; firm Nash x(H) then Cournot q(H,x) define payoffs | schematic of stated extensive form; not a newly solved equilibrium or proof of real-world ISO fixed-depth protocols |
| Figure 2: national welfare controlled comparison | p.7 / incidence mechanism | Frozen firms yield D>0 and positive member/outsider slopes; same govt game + Nash redesign x'_g=-J^-1 F_g yields D-L<0 and negative slopes; outsider accession derivative 2mu | ONLY local sign under Stage22 inequalities; not global bargaining invariance |
| Table 1: result hierarchy and scope | p.10 / Main theorem section | Contrast local A, certified OPEN-region global A, direct-grand B, lambda_c local threshold C1, rho=1 eta=6/7 face + rho<1 strip C2 | main/auxiliary distinction, no universal generality |
| Table 2: numerical government payoffs at g=.05 | p.10 / numerical illustration | Frozen (m-s,i-o,i-s) = (+.000272382,+.000234617,+.019318616); Endogenous (-.000473474,-.001246547,+.016934628) | REUSED independent Stage23 evaluator, uncalibrated, NOT a replacement for all-g certificates |

## Visual and numerical QA
- Both figures are editable embedded TikZ vector objects; both tables are editable LaTeX/booktabs structures; cross-references added in relevant prose.
- Recompiled twice using pdflatex. 16-page final PDF, zero undefined-ref or overfull-box warnings.
- Rendered and visually inspected pp. 5, 7, 10. Initial crossed dashed edge on Figure1 and dividing line on Figure2 were repaired, and Table1 labels shortened/spacing improved before final QA.
- No new diagram claims or fabricated curves. No amendment to theory, proofs, original parameter region, or Stage22 theory freeze.

## Identified v0.2 artifact SHA256
- LaTeX: `79fc7b1e2237daf50189e7c63607f2d19e42d207b92687b3013a84b45410dc2b`
- PDF: `b97e778232b2107ba0ac913f298b8193f07369aa7c5db487eee3245dcf6e3236`
- Prepared user-deliverable ZIP: `/mnt/data/stage25/stage25_jpet_initial_draft_v02_with_figures.zip`.

**Important source-of-truth qualification:** The complete v0.2 TeX/PDF are locally created downloadable conversation artifacts, **not yet synchronized to GitHub by the connector**. This GitHub record is the durable figure architecture/QA provenance only. Do not claim repo contains the entire updated TeX/PDF. No main merge.

## Next
Use full v0.2 artifacts for Stage11 manuscript-level hostile referee / explanation & proof-traceability audit; final JPET Stage12 routing remains provisional.