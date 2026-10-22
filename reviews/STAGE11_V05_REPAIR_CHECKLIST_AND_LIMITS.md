# Stage 11 v0.5 — Independent hostile-review repair closure checklist (2026-10-22 JST)

**Repair parent:** Stage11 PR #27, commit `54ac8389f2c45d56b2e587a62c62f226cc121f95`. **Target:** JPET-oriented V2b original-architecture English research manuscript, not formally submission-authorized. main and Theory Freeze untouched.

## What was corrected, not just proposed

| Stage11 finding / must-fix gate | Repaired article/source | Verification and honest bound | Status |
|---|---|---|---|
| M1: v0.4 false SW cells (7 F and 4 N) | `manuscript/figure3_v05_tikz.tex`, `manuscript/stage25_jpet_v05.tex` figure text/caption | A 41×41 recomputation with geometric near-zero g proposals, sign-change root bracketing, actual unilateral Nash, feasibility-vote tests, and government payoffs finds all 11 accepted IS witnesses; the corrected 41×41 array has F: SW765/IS916, N: SW1047/IS634, SU0. | **REPAIRED for documented counterexamples** |
| M1: prevent false certainty across other cells | Same | Main article explicitly calls gray cells **no profitable accepted offer found by numerical candidate search** and disclaims any fully certified 2D SW/IS boundary, including absence of optimal SU; original v0.4 optimal-phase theorem-like claim withdrawn. | **PASS as appropriately scoped numerical illustration**, not interval proof |
| M1: hidden SU more attractive than colored IS | Local v0.5 rerun ledger and dominance evaluator (distributed in accompanying ZIP) | 1,550 IS cells rerun with sampled/locally optimized bilateral envelope; 0 numerical reversals, smallest IS--SU computed payoff gap 0.0000396774360. Not a theorem of globally optimal g. | **Numerical stress PASS; exact certificate NOT ATTEMPTED** |
| M1: benchmark | Stage22/Stage11 historical exact all-depth replay + separate v0.5 reevaluation | At (.8505,.758) F IS / N SW, with source theorem and consent bounds unchanged. | **PASS** |
| M2: consumer domain & full Nash | `manuscript/stage11_proof_supplement.tex` §§full cube | PSD vertex/convexity, fixed-point positive quantities, unilateral q derivatives, Rosen sufficient strict bound, finite deviations, strict reference margin, full cube uniqueness and interior certificate connection. | **PASS proof bridge** |
| M2: exact all-depth derivative proof & optimal offer | Supplement §all depth | Named 1000 interval enclosures, parameterized Krawczyk inclusion, implicit derivatives, explicit strict bounds, integration from g=0, compact *closed feasible IS* set, frozen candidate dominated SU global envelope; archival exact code/run commit. | **PASS proof traceability** |
| M2: network face & active strip | `manuscript/stage11_proof_supplement.tex` §network | Explicit P(theta,g), explicit accepted h, cleared sign-polynomial and restricted Taylor/quadratic argument with scope | **PASS self-contained proof sketch/full bridges; unrestricted rho never claimed** |
| M3: economic identity of x | `manuscript/stage25_jpet_v05.tex` §2 | x residual similarity, 1−x costly differentiation investment, x and g not conflated, stylized linear pairwise aggregation disclosed | **PASS** |
| M3: bargaining implementation | Article §2 voting and §6, supplement | Sequential publicly observed C,A,B votes; mandatory yes on indifference including off-path; inherited g; direct grand rejection option separately SW | **PASS** |
| M3: focused priority & economic value | Introduction/related literature | Generic standards stumbling block and regulatory-endogenous-design known; *controlled Nash-to-national-consent and all-depth same-game comparison* is contribution; no independent new regionalism claim | **PASS within literature limits** |
| Post-edit compilation/layout | Manuscript and supplement, corrected Figure3 | Local pdflatex twice; **20 pages, zero warnings/undefined refs/overfull boxes**. Full contact sheet and Figure3 page inspected. CI GitHub workflow added for branch-built PDF; only call CI passed when run confirms. | **PASS locally; CI result separate** |
| Formal Stage11 closure, then Stage12 | This checklist | No new primitives or proof claim; final Stage11 re-review of *this exact revised source and PDF* still required before advancing to formal Stage12 | **Stage11 re-review required** |

## 11-error numerical regression details

Frozen originally-SW but now positive IS at eta=.7555 and kappa in {.93625,.945,.95375,.9625,.97125,.98,.98875}; endogenous originally-SW but positive IS at (eta,kappa) in {(.760,.945),(.760,.95375),(.76075,.86625),(.7615,.79625)}.

At kappa=.93625, eta=.7555 (frozen), g=.0001: i−s ≈ 3.8135571435e−5, i−o ≈ 3.9470471e−10, i−m ≈ 3.81347486e−5. At kappa=.945, eta=.760 (endogenous), g=.0001: i−s ≈3.7070680e−5, i−o ≈1.3949686e−10. Both reproduce PR27 independent 80-digit diagnostics up to ordinary double-precision roundoff.

## Mathematical proof and traceability provenance

Historical exact-interval outputs are in `verification/stage11/canonical_global_replay.log`, `pareto_replay.log`, `adjustment_cost_replay.log`, and `network_face_replay.log` at immutable audit commit `54ac8389f2c45d56b2e587a62c62f226cc121f95`. The underlying scripts and environment manifest are preserved at that revision. The supplement re-states the mathematical targets, parameter domain, 1000-interval Krawczyk algorithm, result margins and required deduction to government outcomes. The corrected 2D numeric map is **NOT** that interval certificate.

Local user-downloadable reproducible ZIP `V2b_Stage11_Repaired_v05_full_package.zip` includes complete TeX/PDF, both figure formats, original v0.5 repaired computational code, 3362-case ledger, historical v0.4 classifier helper, and JSON checks. The GitHub branch contains the **manuscript-facing corrected source** and this audit checklist; direct GitHub PDF build is managed by the branch-only Actions workflow.

## Unresolved scope (do NOT falsely mark PASS)

1. **No exact theorem-level partition of the entire (kappa,eta) figure rectangle.** Manuscript removes that claim; the center-and-open-set theorem remains supported by separate exact replay.
2. **Certain BFG/CH and Klimenko full supplements remain inaccessible in historical priority comparisons.** No direct absorber was identified in inspected results; missing access is not priority proof. Unbounded new literature search not a required Stage11 repair.
3. **Author review and final journal submission checks** (bibliography/citation and AI disclosure, ORCID, funding/conflicts) are separate downstream gates. No external JPET acceptance implied.

**Provisional repair verdict: M1–M3 substantively addressed without model extension; retain Stage11 re-review gate and do not claim full global phase certification or stage12/submission GO.**
