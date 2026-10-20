# V2b Stage 7.5A — Embedded Formal Verification Gate, exact-rational welfare core
**Verified:** 2026-10-21. **Toolchain:** Lean 4 v4.24.0, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b. NO mathlib dependency; Lean Init library only. Pinned version in root lean-toolchain. Clean GitHub Actions run https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39517673634: PASS, with prior failed first attempt https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39517506979 preserved. First failure: unconfigured reducibility of huge Rat expressions under ordinary 'decide'; fixed using 'decide +kernel', not by adding premises or deleting any theorem.

## Formal applicability, targets and exact status

**Formalization is APPLICABLE**: the paper depends on strict rational welfare inequalities, some as small as approximately 9.1e-7, and universal whole-policy sign certificates. Neither inconvenience nor the cost of fully encoding a continuous Cournot game suffices to label this N/A.

**Targeted proof-critical CORE has a PASS, NOT the entire economic-model theorem.** Selected formal target: four strict pointwise welfare-sign inequalities in the pre-registered nonlinear model using explicit rational product design PROXIES. Build was checked with Lean kernel, zero project axioms/holes. Project-wide proof-maturity statement: **FORMAL VERIFICATION PASS — BOUNDED POINTWISE ARITHMETIC CORE ONLY**; **FULL MAIN THEOREM / TRUE-NASH ROOT-ENCLOSURE / all-g SPNE: NOT FORMALLY CERTIFIED** and still rely on Stage4A mathematical certificates. Whether the bounded core adequately closes the gate for Stage8 must be considered together with statement fidelity, all-g interval proof, and author's contribution review; it does not by itself imply Stage7.5A GO.

## Exact theorem and statement-fidelity map

Source: formal/V2bWelfareCore.lean. Variables in type Rat rather than Real; rational primitives eta=379/500, rho=9/10, kappa=1701/2000, a=2−eta and beta=1−rho. For frozen design use xSWproxy=610737479601/10^12; for international endogenous proxy xISproxy=617707153937/10^12. Models include 3 markets of Cournot profit, CS with product substitution matrix, and cost paid ONCE as kappa*(1−x)^2/2.

| Paper certificate / risk | Lean theorem | Lean-scope statement proven | NOT certified by this theorem |
|---|---|---|---|
| ALT-4A-03 frozen C at small positive g | frozen_c_participation_small | suOutsider(1/200,xSWproxy)<international(1/200,xSWproxy) | The xSWproxy is NOT itself proved to be SW Nash; not all x in Nash root bracket or all g |
| Original failed same-g test | frozen_c_participation_failed_at_original_depth | international(1/20,xSWproxy)<suOutsider(1/20,xSWproxy) | Firm optimization at g=.05 or any neighborhood |
| ALT-4A-03 frozen IS beats SW | frozen_international_better_than_sw | international(0,xSWproxy)<international(1/200,xSWproxy) | All SU deviations, or a fully solved government offer game |
| ALT-4A-04 hypothetic Pareto gain | endogenous_proxy_pareto_gain | international(0,xSWproxy)<international(1/20,xISproxy) | True IS Nash x*(g), off-path government policy, social planner or complete SPNE |

These exact proxies lie extremely near approximate Nash roots computed independently, but **no Lean theorem proves the root inclusion / error bound**. Stage4A rational interval enclosures and globally unique Nash proofs are the separate mathematical bridge; do NOT say Lean itself has checked those. The four Lean inequalities are 0-variable exact rational numerical statements, not general universal differential calculus. This is a bounded arithmetic recheck of the smallest and most fragile welfare comparisons, useful against floating-rounding and arithmetic transposition errors; it is not a proof of the model.

## Axiom and placeholder audit

The Clean GitHub CI checks for proof commands 'sorry', 'admit', 'axiom'. The source uses none; no project-specific axioms or packaged preproved results. The command '#print axioms' was executed for each of the four names and returns only the Lean built-in standard logical axioms **propext, Classical.choice, Quot.sound**. Crucially, **sorryAx is NOT present**, nor is a trusted externally generated statement inserted as a theorem. Lean compiles the proofs using 'by decide +kernel' rather than trusting the interpreter output as an assumed proposition. Build command: $HOME/.elan/bin/lean formal/V2bWelfareCore.lean, toolchain 4.24.0. Toolchain pin: lean-toolchain. No mathlib external package, no linter or translation system.

## Non-formalized model scope and critical dependencies

- Consumer demand and inverse-demand derivation, network expectations, equilibrium correspondence and strategies are **not** formalized.
- Stage5 full nonnegative quantities domain, boundary/active-set reasoning and 3-market Cournot are mathematical inputs to the formula, not independently verified inside Lean.
- Stage4 globally unique 3-firm Nash and algebraic root isolations are **not** checked by Lean. The p=1/p=2 separate Stage4A interval proofs supply those assertions; they are shared SymPy/mpmath implementation and not proof-assistant kernels.
- The world and national welfare model includes explicit formulas in Lean; equality to primitive consumer and firm optimization is **audited externally**, not proved from scratch in Lean.
- Government participation under every real g, C veto and positive-depth no-alliance SPNE results are **not** formalized. These are outside the bounded formal core.
- The mapping of proxy inequality to the true Nash outcome **depends on independently checked small-interval bounds**, whose proof is not imported into Lean.
- No Lean formalization exists for p=1 additive design, the full open-neighborhood parameters or continuous φ class. Formal core is only p=2.

## Final authorization boundary

**Formal verification recorded as PASS only for the SELECTED pointwise exact-rational welfare core.** This satisfies the narrow proof-critical-core build requirement. It does NOT confer FULL CLAIM formal verification or resolve missing author intellectual-accountability evidence. Before any theory freeze, Stage7.5A adjudication must decide whether this bounded assurance plus separate interval full-game certification is sufficient for current explicitly narrow theoretical claims and must complete the author contribution record. Any change to the rational proxies, welfare formulas or headline quantifiers invalidates this certificate until Lean CI reruns; any change to true Nash bounds or government protocol requires earlier mathematical recertification.

Two non-overlapping axes: Lean arithmetic correctness = bounded PASS; actual entire economic equilibrium and institutional validity = Stage4A computer-assisted proofs and Stage7/7.5A portability audit, not Lean.
