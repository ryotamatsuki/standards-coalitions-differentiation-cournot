# V2b / JPET — final pre-submission Lean 4 mathematical audit, Stages 1 and 2

**Date:** 2026-10-24. **Scope:** only mathematical verification of the existing linear residual-design model. This is not a revision to the paper or proof assumptions. Independent Draft PR #38, based on PR #37 exact frozen HEAD `34af29b70f35dd22da2a69873c6832708f9d7c79`.

## Model and source identity

Authoritative paper: `manuscript/JPET_submission_final.tex`, Git blob SHA-1 `2e485def8e126c1312fb74ba05b6a7b8bd9e52d9`. The model uses `X_ij=(x_i+x_j)/2`, not the earlier nonlinear `(x_i^2+x_j^2)/2`. Prior `formal/V2bWelfareCore.lean` formalizes **only fixed rational proxy welfare comparisons in the nonlinear model** and is not a formal proof of this manuscript's Nash/game theorem.

### Stage 1 — formal analytic/auditable components

Source `formal/jpet_audit/JPETAnalyticCore.lean` (pinned Lean 4 v4.24.0 + Mathlib v4.24.0):
- Starting from **primitive fulfilled-expectations inverse price** and the firm's own Cournot FOC, infer the A row of `(I+B−ηH)q=d1`; at fragmentation show symmetric inversion `q=d/L`, with an explicit nonzero denominator.
- Starting from `nationalWelfare = domestic consumer surplus + home-world profit − one-time design cost`, formalize differentiation of the sum with `HasDerivAt`. Prove the exact `D−(C(2u'+v')+V(u'+v'))` identity from the 3 CS contributions, a private own-profit/cost envelope assumption, and 2 rival-profit contributions. The equality is **derived**, not installed as an axiom.
- Algebraic symmetry/three-edge incidence: `m'=μ, o'=ν, i'=2μ+ν, (i-o)'=2μ` given permutation-symmetric link derivatives.

Source `formal/jpet_audit/JPETPrimitiveBridge.lean`:
- Derive **unilateral design quantity sensitivities** by solving the FULL THREE-ROW symmetric `M q_{x_A}=-M_{x_A}q` system (two distinct row types), with `P=α-t, L=α+2t`; no cartel-path derivative substituted.
- Verify closed-form C = βd²(η+2t)/L³, V = 3βd²(α−2t)/(P L³), and D from direct consumer plus resident world-operating-profit effects as symbolic rational identities for real primitives with explicitly nonzero denominators.

**CAVEAT:** The Lean source does **not** yet automatically derive the full three-equation firm Nash Jacobian `J`, invert it as a parameterized smooth economic map, prove Rosen full-cube Nash uniqueness, or independently prove via Lean's differentiability rules that every specific CS/firm-profit partial-derivative formula equals the algebraic candidate (the original appendix supplies these analytic steps). In particular, `C,V,D` formula checks are not evidence of a complete kernel-side reconstruction of private Nash best replies.

### Stage 2 — formal conclusion and external-certificate bridge

Source `JPETAnalyticCore.lean`:
- From `0<D<L`, `ν_F>-D`, `ν_N>-2(D-L)`, derive **the signed frozen/endogenous local welfare and accession slopes**.
- Define inherited-depth integration as `i≥s ∧ i≥m ∧ i≥o`, stand-alone bilateral acceptance as `m≥s`, and prove negative member and outsider gaps preclude both even if a *directly proposed* grand agreement satisfies `i>s`.
- Conditional global theorem: given certified strict real payoff-gap upper bounds uniformly in g, all positive-depth offers are refused.

Source `formal/jpet_audit/JPETLocalCalculus.lean`:
- Using genuine Mathlib calculus and `HasDerivAt`, establish a **strict-right-neighborhood** sign theorem at zero. Under explicitly stated seven actual-payoff derivative identities and zero-baseline conditions, derive the local Theorem 1 **level** comparisons, not merely signs at g=0.
- Using the mean-value theorem / strict antitonicity on `[0,1]`, show that continuous actual payoffs with derivatives strictly negative on `(0,1)` imply negative member and outsider payoff gaps for every g>0. Lean then derives the governmental veto conditions.

**CAVEAT:** The strict signs of the actual all-depth payoff derivatives are **imported as hypotheses** from the Python Krawczyk/interval-Newton certification. Lean does **not** recheck the interval arithmetic or conclude all-depth certificate validity from unchecked data. The frozen-design government-optimal global envelope, four-dimensional **open** primitive neighborhood, full Rosen uniqueness, full SPNE and Lean's formalization of non-linear design-map robustness are **not** kernel-certified. This project's result should be described as **formal analytic and theorem-interface audit**, not FULL MAIN THEOREM VERIFIED IN LEAN.

### Independent verification discipline

- No edits to manuscript, mathematical lemmas/theorems, proof-supplement TeX, three figures, Python certificates, research assumptions, or Theory Freeze. CI rejects changing anything outside `formal/jpet_audit/` and `.github/workflows/jpet-lean-final-audit.yml`.
- No `sorry`, `admit`, `axiom` or unproved custom proof in formal sources.
- Pinned Mathlib and Lean v4.24.0; actual kernel build required to record a PASS. Earlier failed runs due source import order and Lean noncomputable-Real syntax/field simplification are engineering fixes, **not new mathematical counterexamples**.
- No journal submission, merge, external message, reference changes, AI disclosure changes or broader novelty audit.

## Result and stop decision

**Lean KERNEL COMPILE PASS for all three audit modules:** [GitHub Actions #40044618574](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/40044618574), whose Lean kernel-check step completed **successfully**. Its overall workflow status was failure solely because the frozen-source whitelist had not yet permitted this NEW audit report file itself. The whitelist was restricted to this report plus the isolated Lean source and workflow in commit `2d00dbe2c767ed67c94def705143817fb549dce6`, and a complete end-to-end CI re-run is required for final overall GREEN.

- `JPETAnalyticCore.lean`: 9 kernel-proved theorem declarations (Cournot row, symmetric output, welfare sum derivative, primitive component incidence, edge incidence, local slopes, accession/direct-grand vote, conditional full-depth gap), plus model definitions.
- `JPETPrimitiveBridge.lean`: 4 universally quantified real-algebra identities with explicit domain restrictions (unilateral Cournot sensitivity matrix rows; C; V; D).
- `JPETLocalCalculus.lean`: 5 true calculus/governmental implications (positive right derivative sign; negative right derivative sign; actual local payoff-level comparison; whole-menu derivative negativity -> rejection).
- No `sorry`, `admit` or project-specific `axiom` statements. Each file actually executed under `lake env lean` with Lean 4.24.0 and mathlib v4.24.0.
- All three theorem groups **PASS** at their explicitly stated hypotheses; the entire full economic game and numerical interval certificates are **not** formally verified inside Lean.

**Audit outcome: PASS for the precisely bounded analytic/core and conditional theorem-interface checks. FULL MAIN THEOREM LEAN VERIFICATION remains NOT CLAIMED.**

A full Lean proof of all Python interval cells and the unrestricted Nash/coalition theorem is beyond the authorized bounded Stage 1–2 scope; any omitted dependencies are explicitly listed above, not silently changed into assumptions of the economics theorem.
