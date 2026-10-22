# V2b Stage13 — exposition streamlining and JPET manuscript integration
**Date:** 2026-10-22 JST. **Primary journal:** Journal of Public Economic Theory (JPET); **article type:** Original Article, general theory / THEORY-FIRST. **Gate:** Stage13 integration / not Stage14 author submission QA. **Input:** Stage12 PR #29 target GO, current 21p Stage11 v0.5 at `e9e534863f54e19e438a1ace26bf91ff1dedfb2d`; source `manuscript/stage25_jpet_v05.tex`. Output is **separate file** `manuscript/stage13_jpet_integrated.tex` including `stage13_proof_supplement.tex`, `stage13_figure3_tikz.tex`. Frozen previous TeX/PDF and Stage11 scientific code are left untouched.

## Decision: INTEGRATED — stylistic/structural compression only
- The early Introduction already explicitly states the research question, why public consent matters, 3-country Cournot/firm-design setting, local national-incidence sign reversal, all-depth government-outcome reversal, the closest Takarada/Kawabata/Grossman predecessors, and inherited-depth restriction. Cut the **repeated penultimate contribution paragraph**, retain a short forward roadmap. No need for a new result or generic standards literature survey.
- Remove redundant commentary immediately after local result and all-depth proof. Keep the proof, the open-neighborhood quantifier and the `g∈[0,1]` certificate bounds fully visible.
- Numerical examples remain **uncalibrated**; remove an unnecessary speculative percentage and preserve three precisely defined welfare gap columns. Recast Figure3 exposition in a shorter 2-paragraph methodological caution. **Blue means found accepted IS more attractive than tested bilateral envelope; gray means no superior accepted proposal found.** It is *not* a 2D rigorous SW boundary or universal no-SU theorem.
- Replace defensive rhetorical introduction of the institutional counterfactual with the direct-grand alternative's different rejection option; retain Proposition 5 and full proof. This is the limit of main theorem, not a separate first-to-discover regionalism claim.
- Shorten end-of-literature repetitions; retain closest sources and their differing decision makers. Do not add unverified strong priority assertions.
- Main/Appendix footnote about program output becomes ordinary cross-reference to verified differential-incidence bridge, not research-process instruction.
- **Proof-critical bridge retained:** `Mq=d1`, unilateral `F_i`, `x_g=-J^{-1}F_g`, national `W_A,x=(-C,-C-V,-C-V)`, correct **positive V contribution** to loss, edge-count outsider consent, strict certified all-depth derivative bounds, frozen accepted IS and global SU bound, plus closed feasible-depth optimality argument.
- **Scientific artifacts unchanged:** `manuscript/stage13_proof_supplement.tex` is a **byte-preserving copy** of the latest `manuscript/stage11_proof_supplement.tex` on Stage12 parent; similarly `stage13_figure3_tikz.tex` copies the verified Figure 3 source. This is not a new numerical classification, theorem, or model. The Stage11 r1 source (21p) is the authoritative preceding version.

## Article architecture and section classification
| Unit | Role | Stage13 treatment |
|---|---|---|
| Abstract / §1 question, mechanism, exact scope | CORE | retain, trim repeated afterthought; excludes novelty first-claim and universal treaty failure |
| §2 country, firm, network and timing | CORE | retain full primitives and votes; inherited g and no-regotiation scope unchanged |
| §3 Cournot and unilateral design Nash | CORE | retain FOCs, national continuation definition |
| §4 incidence/edge-count lemmas | CORE | retain equations for D, L, V and causal Figure2 |
| §5 local and all-depth reversal | CORE | retain both theorem statements and complete proof architecture |
| §5 numerical Table2 | CORE | retain signed national welfare gap comparison |
| §5 Figure3 | HELPFUL (closely qualified) | retained, two-panel candidate map; no exact phase-curve claim |
| §6 different bargaining routes, direct grand | CORE | keep as strict limitation of institutional interpretation |
| §7 lambda critical, network rho=1/near-face | HELPFUL | keep one compact main paragraph/proposition, algebra in Appendix |
| §8 closest prior art | CORE | keep 3 grouped conceptual relations, remove late repeated contribution pitch |
| §9 Conclusion | CORE | already concise, no new empirical or political claims |
| Appendices A–D / full exact-support supplement | APPENDIX BUT PROOF-CRITICAL | retain all nontrivial bridges, full Nash uniqueness / PSD / interval Newton and Krawczyk / face and strip proof; not cut for brevity |
| Working author declarations | APPENDIX PLACEHOLDER | retained distinctly provisional; author must supply actual statements in Stage14 |

## Introduction search-cost and reader-arrival (verified local preview, actual section locations)
- Economic question & why: page 1, §1.
- Main local reversal and all-depth outcome summary: pages 1–2, §1.
- Government/firm strategy primitives and country welfare: §2 (pages 2–5).
- First nationwide incidence derivation and mechanism: §4 (pages 6–8).
- Headline local and globally depth-optimized theorems: §5 (pages 8–10).
- Numerical regime comparison/Table2: page 10; Figure3 and §6 institutional counterfactual: page 11.
- Supporting cost/network cases: §7; close literature: §8; long technical supplement: Appendix.
These are observational page landmarks, not journal-wide mandatory page cutoffs. An independent GitHub build may alter page pagination; no explicit hard length cap for JPET was inferred from a comparison journal.

## Scope and sign check
- Derived national loss: `L=C(2u'+v')+V(u'+v')`, **plus**, unchanged.
- Full government optimality only at certified center/open region, original inherited-depth proposal/vote order. Direct grand Pareto improvement does not remove the institutional limitation.
- `lambda_c` is local consent slope threshold, not full governmental phase boundary.
- `rho=1, eta=6/7` is non-strategic face, with only restricted rho<1 active-strip extension; not Figure3 `rho=.9` general theorem.
- All 3 figures and 2 tables retained after five-exhibit necessity assessment (separate report). No hidden new policy costs, tariffs, first-best, transfers, renegotiation solution, or empirical calibration.

**Exposition verdict: PASS for content/claim scope.** Final publication suitability, author identity/ORCID, official JPET portal declarations, and standalone supporting-info packaging belong to Stage14. Stage13 independent PDF build/visual/cross-ref QA must also PASS before the gate is treated as closed.
