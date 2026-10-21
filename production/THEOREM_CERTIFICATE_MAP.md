# Stage9 theorem-to-certificate and reviewer-verifiability map
**Current technical freeze:** V2B-THEORY-FREEZE-2026-10-21-v2-CERT-REPAIR (v1 economic primitives untouched; repaired nonlinear proof certificates). **STATUS:** audit map of already certified claims, NOT a new mathematical theorem. Original canonical φ=x; φ=x² is a separately certified diagnostic, never a silent replacement of V2b.

## Theorem objects and current proof level

| Freeze theorem | Source primitives / bridge equations | Exact quantified outcome | Inspectable artifacts | Proof and formal status |
|---|---|---|---|---|
| T1 market continuation | Utility U; p=a1−Bq+ηHn^e; fixed n^e under firm deviations; M=I+B−ηH; Mq=1 | ∀ S∈{SW,SU,IS}, ∀g∈[0,1], ∀x∈[0,1]^3 at exact θ0, unique positive q | Frozen §2; reviews/V2B_STAGE04A_ADVERSARIAL_CERTIFICATION_2026-10-21.md; alt quadratic Stage4 report | Analytic contraction/positive quantity proof. **NOT** Lean-checked |
| T2 firm design Nash | q=M⁻¹1; Π_i=3q_i²−κ(1−x_i)²/2; F_i=6q_i q_{i,x_i}+κ(1−x_i); q_{x_i}=−M⁻¹M_{x_i}q | ∀ S,g at θ0, one global pure x Nash in full asymmetric cube | v2b_stage04a_krawczyk_cleanroom.py; v2b_alt_quadratic_rosen_interval.py, v2b_exact_rational_interval.py | Rosen analytic/interval Jacobian and root inclusion, separately for each φ. **NOT** Lean-checked |
| T3 government no positive agreement | Reduced W_A^SU(g), W_C^SU(g), W_i^IS(g), W^SW; implicit x'(g) | ∀g>0 at θ0, member SU<S W and IS<C outsider SU under **AB-first unchanged-g consent** | v2b_stage04a_krawczyk_cleanroom.py; v2b_alt_quadratic_policy_interval.py; two CI runs | Computational rational interval Krawczyk/face signs across ENTIRE continuum; NOT a finite grid or FULL Lean |
| T4 frozen design policy counterfactual | x fixed at SW-Nash across all histories; same national W, same costs and menu | ∃ positive g, IS acceptable to C and AB, dominates SW and all terminal SU policies. φ=x: g=.05; φ=x²: g=.005 | v2b_stage04a_krawczyk_cleanroom.py; v2b_alt_quadratic_policy_interval.py | Global interval bounds on SU and frozen C entry; tiny C gain φ=x² ~9.1×10⁻⁷. Lean **only rational proxy** sign for φ=x² g=.005 |
| T5 welfare-positive hypothetical IS | CS=½q'Bq; country CS+3q_i²−cost_i, sum_i W_i | φ∈{x,x²}, g=.05 IS after firm reoptimization strictly Pareto dominates SW; NOT implemented | v2b_stage06_pareto_holdout.py; v2b_alt_quadratic_policy_interval.py; v2b_stage07_welfare_institutions.py; generated table (canonical only) | Strict pointwise interval bounds. Lean **only rational proxy** comparison for φ=x² |
| T6 nearby parameter neighborhoods | strict signed all-g bounds + unique Nash + continuity | Existence of a nonempty **unquantified** parameter neighborhood for each φ in the same model | Stage4A+Stage7.5A proof reports | **CONDITIONAL:** no explicit radius, no general φ class; state as qualitative scope inference only |
| T7 rejected overclaims | Institutional and functional failure boundaries | Same-depth g=.05 frozen acceptance under φ=x² is strictly false; no universal φ or bargaining agenda claim | Stage7.5 pre-reg, v2b_stage075_nonlinear_design_diagnostic.py, Lean frozen rejection sign | **REJECTED** as stronger statements; preserve failures |

### Government backward-induction bridge (Stage10 readers must see)

C chooses between W_C^SU(g) and W_C^IS(g) at **unchanged g**; no C application yields SU. B chooses between the SW continuation and joining A's SU plan; A chooses any g∈[0,1] and anticipates C response. Since each x^*(S,g) is unique, every upstream history maps to well-defined continuation welfare, avoiding equilibrium-selection artifacts. Strict T3 signs imply no positive-depth coalition. At g=0, nominal union labels may vary by indifference; outcome equivalence is not uniqueness of formal SPNE.

### Benchmarks and method boundaries

- P=linear φ(x)=x is the canonical source of welfare table; the more nonlinear φ=x² is the ONLY evaluated genuine functional-robustness alternative.
- Original pre-registered nonlinear *same-g* φ=x² g=.05 fixed-design C entry is FAIL. Frozen g=.005 C benefit is tiny POSITIVE, not evidence same-depth robustness.
- Gandal–Shy (2001) government standards recognition uses Bertrand fixed Salop variety; no formal union can mean compatible mutual recognition, unlike V2b SW. Broad standards-investment and coalition technology paradoxes are existing research. Academic priority not universally certified.
- Lean4 formal file uses fixed RATIONAL design proxies, not actual Nash roots quantified inside Lean. Class = **PROOF-CRITICAL POINTWISE ARITHMETIC CORE**; all-g and Rosen claims rely on separate interval proofs.
- User approval accepts the research scope, not independent personal rederivation of proof code.
- Never present standalone code execution PASS, a tabulated payoff or a mathematical bound as proof of empirical effectiveness of an actual interoperability consortium.

## Stage10 exhibit architecture (NOT manuscript construction)

- One figure explaining timing A→B→C→AB consent→firms x→Cournot q, using separate labels for SU and IS and the inherited compatibility g.
- One conditional equilibrium national/world welfare table, generated by production/scripts/generate_welfare_table.py.
- One graphical government welfare vs g exhibit only if numerical continuation is independently rechecked against full-g interval sign certificates; **NOT YET GENERATED**.
- One theorem-to-primitive bridge exhibit making clear \(\partial_g W_{\rm member} = W_g + W_x x'\), and how C's outside option enters admission.
- Small appendix source-status table for Baake–Boom / Cabral–Salant original-vs-WP priority uncertainty. No Gandal private PDF re-distribution.

## Stage13 computational-proof correction record

2026-10-21: PR #4 exposed non-outward float coefficients and Rosen float summation in the nonlinear p=2 certifier. PR #5 reissues exact coefficient interval compiler and interval Gershgorin sums. Stage4A rerun https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39571673076 PASSED. The original p=2 g=.05 frozen C rejection remains failed and the g=.005 participation margin remains tiny. Stage14 is still blocked by unresolved full Cheng-Huang propositions and author-dependent submissions. Old v1 freeze survives as a separate Git document.
