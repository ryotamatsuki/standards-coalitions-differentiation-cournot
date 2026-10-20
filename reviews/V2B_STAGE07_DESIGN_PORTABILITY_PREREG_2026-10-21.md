# Pre-registration: Stage 7 bounded design-function robustness diagnostic (2026-10-21)

**Filed BEFORE new simulation.** Diagnostic only: canonical V2b formulas and validated claims remain unchanged. Stage 7.5 requires checking whether the positive-Pareto-but-blocked agreement survives at least one credible non-cosmetic alternative. No arbitrary rescue tuning.

## Single specified alternative

Keep all country roles, A/B-first fixed-depth consent with C application and unanimous AB admission, national welfare, continuous compatibility H, network coefficient eta, three-market Cournot, once-only design cost kappa(1-x_i)^2/2, and exact rational witness (a-c,eta,rho,kappa)=(1,379/500,9/10,1701/2000).

**Only** replace the residual characteristic transfer function in the utility substitution matrix:
- Canonical V2b: X_ij=(x_i+x_j)/2 (i≠j).
- **Diagnostic nonlinear characteristic:** X_ij=(x_i²+x_j²)/2 (i≠j), X_ii=1.

Economic motivation: a firm's nonstandard design proximity may be nonlinear in its observable design effort x_i; marginal increases near x_i=0 have smaller substitutability effects. This changes the firm's marginal strategic returns, and is **not merely renaming x** because design cost stays quadratic in original x. It leaves X PSD: define z_i=x_i²∈[0,1] and reuse additive-kernel PSD result, and leaves H independent from X.

## Ex ante success / failure definitions (DO NOT CHANGE)
Re-solve Stage 5 at all x and Stage 4 Nash from this new M(x), checking unilateral deviations numerically rather than inserting x² into old equilibrium solution. At the ORIGINAL parameter witness:
1. Local relevant sign predictions at g=0: endogenous derivative W_A,SU'(0)<0 AND frozen-at-SW-differentiation W_A,SU'(0)>0; the latter yields C local gain positive by symmetry. Check using finite perturbations or implicit differentiation of correct new FOCs.
2. At specified g=0.05: endogenous SU member W_A,SU<W_SW and C outsider gain O_SU>I_IS; **yet** hypothetical IS W_IS>W_SW (strict Pareto gain); frozen x at SW Nash has I_IS>O_SU and I_IS>W_SW.
3. Scan g∈[0,1] including endpoints for diagnostic signs (e.g., 201 points). This can flag counterexamples but **CANNOT** certify the all-g SPNE claim.
4. Check three-firm unilateral pure-strategy best replies on x∈[0,1] at key policy points, report solver and Nash multiplicity uncertainty honestly.

**Positive Stage 7.5 diagnostic:** all key inequalities 1–2 survive and no g-scan contradiction, with explicit numerical-not-theorem disclaimer. Formal all-g universal robustness and firm Nash globality remain Stage 7.5A.

**Negative Stage 7.5 diagnostic:** any inequality 1–2 fails. Do not change cost coefficient, test a different nonlinear power, or otherwise parameter-shop to rescue the claim in this experiment. Report MODEL-SPECIFIC until separately authorized.

The institution's agenda is deliberately held fixed here; the separately observed contrast with a direct three-party offer remains an INSTITUTION-SPECIFIC result, not a defect of the test.
