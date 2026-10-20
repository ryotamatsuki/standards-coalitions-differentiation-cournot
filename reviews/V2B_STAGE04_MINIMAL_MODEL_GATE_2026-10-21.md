# Stage 4 — Minimal Model Mathematical Gate: V2b
Date 2026-10-21. Workflow v2.9. **Verdict: GO for the exact-rational restricted witness and its unquantified open neighborhood, conditional on the recorded computer-assisted proof's implementation soundness; Stage 4A next.** No full parameter-space SPNE classification, Stage 4A pass, novelty certification, or theory freeze.

## 1. Primitive and extensive-form domain
Three symmetric countries A,B,C, each with one firm selling in **each of three identical national Cournot markets**, government maximizing domestic CS plus home-firm three-market operating income minus once-paid real design expenditure. No harmonization costs, transfers or market-access legislation. Government sequence: A offers bilateral union depth g in [0,1] to B; B accepts/rejects (reject -> SW); C applies or stays out; A and B unanimously approve accession (reject -> SU); accepted IS inherits **exactly the initial g**. Firms then simultaneously choose x_i in [0,1] before Cournot nonnegative quantities. Accept/apply/approve at government indifference, particularly g=0. Formal g=0 coalition labels may vary although economic allocations coincide.

Rational exact witness (a-c,eta,rho,kappa)=(1,379/500,9/10,1701/2000). Per-market utility at fixed expected networks n^e:
U(q|n^e)=a 1'q - (1/2)q'Bq + eta q'H n^e.
B=rho H+(1-rho)X; H_ii=X_ii=1; H_ij=g for common-standard pairs, 0 otherwise; X_ij=(x_i+x_j)/2 for i!=j. At fulfilled expectations n^e=q, the market equilibrium's matrix is M=I+B-eta H. Operating global profit is 3q_i^2, cost once per firm kappa(1-x_i)^2/2. National W_i=(q'Bq)/2+3q_i^2-kappa(1-x_i)^2/2. Do not apply earlier V1 z_i>=g constraints or V1 numerical threshold results to V2b.

## 2. Claim V2B-4-01: globally well-defined stage-5 continuation (at witness)
Conditional consumer demand is concave because H is a block equicorrelation PSD matrix and X is PSD by convexity in x plus checking its 8 Boolean-vertex matrices; B is PSD. Note boundary B can be singular: demand STRICT concavity is not claimed.

At the witness M=I+.142H+.1X is >=I in Loewner order. M_ii=A=2-eta=1.242. Every offdiag M_ij belongs to [0,1-eta]=[0,.242]. Cournot simultaneous best responses on cube [0,d/A]^3 are a sup-norm contraction with factor <=2*.242/1.242<1. The unconstrained best response is strictly positive everywhere on that cube because 2*.242/1.242<1. Therefore one unique strictly positive Cournot + fulfilled-network-expectation continuation exists for **every** coalition S, policy g∈[0,1], and design x∈[0,1]^3. Formula q=M^-1 d1 is valid globally on the entire history domain at this witness, including design boundaries. A production-network multiplicity or zero-sales corner is not silently filtered.

## 3. Claim V2B-4-02: global stage-4 firm Nash uniqueness (at witness)
With beta=1-rho=.1, q=M^-1 d1, M_i=partial M/partial x_i has operator norm beta/sqrt2. The eigenvalue bound M>=I implies ||q||<=sqrt3 d, ||partial_i q||<=beta sqrt(3/2)d, and ||partial_i partial_j q||<=beta^2 sqrt3 d. Consequently each entry of the operating-profit Hessian for R_i=3q_i^2 obeys |partial_ij^2 R_i| <= 27 beta^2 d^2=.27. Firm payoff R_i-kappa(1-x_i)^2/2 is strictly concave in its own x_i; symmetric part of the gradient Jacobian is negative definite by strict row diagonal dominance when kappa>81 beta^2 d^2=.81. The witness kappa=.8505 satisfies it with slack .0405. Compact convex strategy sets and strict own concavity imply Nash existence; Rosen diagonal strict concavity implies uniqueness over ALL asymmetric strategies/boundaries, not just symmetric candidate roots. SW and IS unique Nash must be symmetric; SU must have x_1=x_2.

SU root interior globally: a Poincare–Miranda inward-face sign certificate supplies a Nash root in (u,v)∈(.7,.8)^2 for each g; uniqueness identifies that root. IS scalar root is between .6 and .95 for every g (its firm gradient is positive at .6 and negative at .95 uniformly). SW x≈.718592707322. Thus no design endpoint arises in any stage-4 equilibrium at the witness.

## 4. Claim V2B-4-03: endogenous design defeats all substantive integration
Denote M(g)=W_A^SU=W_B^SU, O(g)=W_C^SU, I(g)=W_i^IS evaluated at each regime's unique Stage-4 Nash. The previously committed adaptive RATIONAL INTERVAL CERTIFICATE checks signed Nash root faces, Jacobian invertibility, implicit design comparative statics, and interval derivative bounds uniformly for **every real g∈[0,1]**. Its critical outputs:
  dM(g)/dg<0 and d[I(g)-O(g)]/dg<0 across whole interval.
At g=0, M(0)=O(0)=I(0)=W^SW. Integrating the two strict signs gives M(g)<W^SW and I(g)<O(g) for all g>0. Thus C will not voluntarily join positive-depth IS; A/B cannot obtain greater payoff through positive-depth SU than rejection and SW. No SPNE yields substantive positive-depth harmonization under the game's consent sequence. Literal SW versus zero-depth SU or IS labeling is tie-convention dependent.

The interval proof is **computer-assisted**, not formally checked in Lean or independently reimplemented. Its source is verification/v2b_interval_reversal_certificate.py; a GitHub Actions test previously passed (run 39472853173). The displayed result does not generalize beyond the exact witness and its continuity-open neighborhood.

## 5. Claim V2B-4-04: frozen-SW-design counterfactual yields positive IS
The fixed-design counterfactual restricts x_i=x_i^SW after EVERY government history, leaving identical government strategy spaces, fixed-depth inheritance, market utility, physical design cost LEVEL, and national welfare accounting unchanged. It is a separate counterfactual extensive game, not a Nash continuation of the original endogenous-design game.

The certified SW root lies in [.71859270731,.71859270734]. At g=.05=1/20, an interval evaluation proves I_frozen(g)>O_frozen(g) (C applies), I_frozen(g)>M_frozen(g) (A/B approve), and I_frozen(g)>W^SW (B accepts). An outward-rounded bound covering every frozen SU policy g∈[0,1] has sup M_frozen(g)<2.433100, while I_frozen(.05)>2.441397. Consequently an admissible positive-depth IS contract is more profitable for proposer A than *any* SU or SW history. Weak acceptance at indifference gives compact feasible IS set and hence a globally maximizing positive-depth IS outcome. Numerically the cap for C acceptance is about .07743519; that approximate optimizer is NOT required for the proof.

This is a reversal in substantive coalition **OUTCOME** between two explicitly different games, not a contradiction of earlier scholars' propositions or an all-parameter comparative statics theorem.

## 6. Stage-4 independent-from-production diagnostics (not Stage 4A)
A fresh script verification/v2b_stage04_primitive_reconstruction.py reconstructs all H/X/B/M and W matrices **directly from definitions**, without importing V2b continuation helpers. It solves three firm FOCs with its own 3D root, checks unilateral scalar profits against bounded optimization for SW/SU/IS across policies, verifies X and M eigenvalues at vertices, and compares analytic payoff gradients with direct finite differences. Separately executed local check: 900 random (firm, design, regime) derivative comparisons, maximum absolute discrepancy ~7.09e-10.

Direct high-stakes values:
- SW x=.718592707322, W=2.422078421718.
- Endogenous SU g=.05, members x≈.7215948 and outsider x≈.7201967: M≈2.421604947547 (below SW), O≈2.440259596858.
- Endogenous IS g=.05: I≈2.439013049624 < O, so C will not join.
- Frozen designs at same g=.05: I≈2.441397037364 > frozen O≈2.441162420695, > SW and > any frozen SU.
- Direct SU policy derivative at g=0 with x frozen ≈+0.006767924; firm design feedback ≈-0.015069744; fully endogenous derivative ≈-0.008301820 (independent finite differences reproduce).
- Finite g-grid and scalar optimizer check Nash branch feasibility; **only** the separately committed interval cert establishes global continuum inequalities. Solver convergence failures are never counted as unprofitable deviations.

## 7. Complete deviations / corners / tie record
- B rejection yields SW with unique design/market continuation. Endogenous any positive g: C chooses not to apply, B rejects the unprofitable SU (or A avoids a positive-depth agreement); positive-depth IS infeasible from C's best response.
- Frozen at feasible positive g=.05: C applies, A and B approve, B accepts over SW; Stage 1 global maximizer is in positive IS feasible subset because its payoff exceeds ALL SU and SW alternatives.
- C nonapplication or application and A/B rejection after any g: unique SU continuation; C admission: unique IS continuation with identical g. All are covered by firm/marginal signed root and demand positivity conditions.
- At g=0 network, substitution and all government payoffs coincide across formal S labels. Accept/reject and apply/nonapply indifference can lead multiple **literal** SPNE labels, but not different substantive economic regime. No uniqueness of formal government strategy profile claimed.
- Every firm x_i=0/1 is a feasible deviation (not constrained by government g). Rosen strict concavity and full root-face certificate rule out alternative asymmetric/boundary design Nash. Every market q_i=0 is feasible but never a Cournot equilibrium at the witness by uniform positivity; no implicit filtering.
- Any nonconvergence is UNRESOLVED by workflow policy; no failure reported by the independent routine for tested sample histories. This is NOT a claim that a finite numerical sweep exhausts all histories.

## 8. Quantifier and proof-maturity ledger
V2B-4-01: for **all S,g,x** at the **fixed rational witness**, UNIQUE strictly positive quantity equilibrium — analytical contraction/PSD proof + diagnostic.
V2B-4-02: for **all S,g** at the **fixed rational witness**, UNIQUE pure firm design Nash, all firms interior — uniform Rosen + signed face proof + diagnostic.
V2B-4-03: for **all strictly positive real g∈(0,1]** at fixed witness, endogenous C rejects IS and A/B prefer SW to SU; global substantive SPNE no-integration — computer-assisted rational-interval inequality certificate, implementation-dependent.
V2B-4-04: **there exists** a feasible positive-depth frozen-design IS dominating all SU/SW alternatives — continuous SU upper interval bound and strict payoff gaps; best possible frozen g not analytically determined.
V2B-4-05: **there exists** a nonempty unquantified open parameter neighborhood with same sign/payoff inequalities — strict margins, compactness and smooth unique continuation. Not genericity.
Prior-art originality: **UNRESOLVED**; formal-verification applicability and independent hostile review are **PENDING at Stage 4A**; portability to arbitrary product-design functions or nonlinear network benefits **NOT CLAIMED**.

## 9. Formal gate result and next contract
**Stage 4 canonical verdict: GO, restricted to V2b's verified fixed-witness/open-neighborhood coalition-outcome reversal.** Does not authorize theory freeze, manuscript, journal priority claim or broad SPNE regime classification.

**Next: Stage 4A clean-room adversarial mathematical certification.** Before reading the original interval source, reconstruct stage-5 FOCs and national welfare from primitives, derive a truly distinct quantified method to check sign inequalities across the entire g-domain, attack Rosen Hessian bound, Poincare–Miranda root containment, indifference strategies and frozen benchmark. The independent reviewer must record actual source exposure, discrepancies and solver-failure taxonomy, and make a formal-verification applicability decision. If any proof-critical gap remains, fail closed and reopen Stage 4; do not call a second execution of the same CI independent adversarial certification.

Stage-2 Gandal–Shy full-text priority remains unresolved by user-directed deferral; no absence-of-source novelty inference.
