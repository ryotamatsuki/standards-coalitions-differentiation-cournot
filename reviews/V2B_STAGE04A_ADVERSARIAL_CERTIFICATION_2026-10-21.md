# Stage 4A — Independent Mathematical Adversarial Certification (V2b)

**Audit:** 2026-10-21, research-paper-workflow v2.9, formal Stage 4A.
**Canonical mathematical verdict: GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS, restricted to the EXACT RATIONAL WITNESS and an unspecified open neighborhood.**
**Next authorized substantive stage: Stage 6 novelty re-kill**, with the Stage-2 inaccessible-primary-source uncertainty clearly preserved. There is **NO** theory freeze, formal verification PASS, model-general theorem, source-priority certification, or manuscript authorization.

## A. What the reviewer knew and what was independent

This audit had access to the ChatGPT discussion and published Stage-4 claims, equations, parameter witness and previously reported computed results. Therefore **this was not a fully BLIND clean-room review** and MUST NOT be described as one. The reviewer did not call/import earlier production continuation or interval proof code in the new Stage-4A script. It reconstructed the SU 3×3 Cournot system, unilateral firm design gradients and welfare functions from the displayed economic primitives, and applied a **different root-certification method**:

- earlier Stage-4 certificate: interval sign-enclosure of Nash FOC rectangle faces (Poincare–Miranda) and adaptive interval subdivisions;
- **this Stage-4A certificate: parameter-uniform Krawczyk (interval-Newton-type) inclusion** for SU's 2×2 Nash system, separate scalar interval Newton for IS, symbolic differentiation of implied government welfare derivatives; 1,000 adjacent exact-rational policy depth intervals covering the entire continuum [0,1].
- A separate independently coded **direct 3×3 inverse-demand matrix evaluator** applies unilateral firm deviations (one firm changes x_i while competitors are held fixed), checking 400 numerical derivative profiles from 200 random SU design points.
- Both methods depend on SymPy mathematical expressions and mpmath's interval-arithmetic implementation. Thus **their arithmetic kernel/toolchain is not fully independent**. Proof-assistant certification and author/external-human verification remain pending and cannot be inferred from CI success.

Reproduction script: verification/v2b_stage04a_krawczyk_cleanroom.py.
GitHub Actions workflow: .github/workflows/v2b-stage04a-independent.yml.
Verified PASS CI run: https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39480815816 .
Observed from separate container invocation: 1,000 policy intervals accepted; 0 failures/subdivisions; negative derivative upper bounds, plus independent frozen benchmark gaps.

## B. Primitives and exact mathematical domain

Exact parameter witness:
(a-c,eta,rho,kappa)=(1,379/500,9/10,1701/2000).

At each history S in SW, SU, IS and policy g in [0,1], governments act first:
(1) A offers bilateral SU(AB) at depth g, B may refuse;
(2) C decides whether to apply;
(3) A/B unanimously approve; IS inherits exactly g;
(4) firms select residual product homogeneity x_i∈[0,1] and pay once-only kappa(1-x_i)^2/2;
(5) Cournot three products in each of three identical national markets, q_i>=0, fulfilled network expectations n^e=q.

U(q|n^e)=a 1'q - 0.5 q'Bq +eta q'H n^e,
B=rho H+(1-rho)X, H_ii=X_ii=1,
H_ij=g for same-standard edges and 0 otherwise,
X_ij=(x_i+x_j)/2 for i !=j.
National W_i=.5 q'Bq + 3 q_i^2 - kappa(1-x_i)^2/2.

## C. Theorem certificates: claim → attack → evidence → residual limitation

### V2B-4A-01: Stage 5 is well defined on ALL upstream histories

**Claim (restricted witness):** for every S, g∈[0,1], x∈[0,1]^3, exactly one nonnegative fulfilled-expectations Cournot q exists and q_i>0 for every i.

**Attack:** starting from consumer utility and Cournot unilateral quantity choice, compute M=I+B-eta H. H and X are PSD (for additive X, check its eight Boolean vertex matrices and use coordinate-affine convex decomposition). At witness M=I+.142H+.1X >=I. Diagonal A=2-eta=1.242; all cross coeffs are in [0,.242]. The standard q best-response map
T_i(q)=max(0, [1-sum_{j≠i}M_ij q_j]/A)
is a sup-norm contraction on cube [0,1/A]^3 with Lipschitz < 2*.242/1.242 ≈.3897. Entire cube's raw best response is strictly positive because 2*.242/A<1. Unique globally interior continuation, no zero-output active-set surprise, even for design x corners or g endpoints.

**Alternative equilibrium search:** global contraction rules out another q. No computational root branch is needed for this theorem.

**Certification:** PASS for restricted exact parameter witness. **NOT** universal for arbitrary eta/rho. Example outside the safe domain eta=.8, rho=.1, IS g=1,x=(0,0,0) yields M eigenvalue 2+2rho-3eta=-.2; broad positive-expectations existence assumptions cannot be made outside domain.

### V2B-4A-02: Stage 4 design Nash exists and is unique globally

**Claim:** for every S,g at the witness, unique pure firm Nash over x∈[0,1]^3; SU members choose equal u, outsider v; SW/IS all symmetric. Root paths interior.

**Attack:** with beta=.1, M>=I, q=M^-1 1, and ||M_i||=beta/sqrt2. Matrix inverse differentiation bounds for any i,j:
||partial_i q|| <= beta sqrt(3/2), ||partial_ij q|| <= beta² sqrt3; hence each |partial_ij²(3q_i²)|<=27beta²=.27. Firm payoff Hessian Jacobian has diagonal <=.27-kappa=-.5805 and off-diagonal absolute ≤.27; it is negative definite in symmetric part by strictly negative row dominance since .8505 >81*.1²=.81. Strict own concavity, compact convex action sets and Rosen diagonal strict concavity give pure Nash existence and uniqueness **over all asymmetries and boundaries**. A successful FOC root alone is not used as evidence of uniqueness.

**Attack of unilateral derivative:** 200 seeded random SU points (400 own-firm derivative comparisons for firms 1 & 3), recompute q through a fresh 3×3 matrix solve following x_i±1e-6 unilateral deviations; absolute discrepancy maximum ≈6.3163×10^-10 vs independently derived analytic firm FOC.

**Root identity and corners:** Krawczyk sign-bound root proof places SU (u,v) in strictly interior rectangles for every g; scalar IS interval Newton likewise. By Rosen the unique certified SU/IS roots are the only firm Nash candidates; other asymmetric or boundary designs cannot constitute Nash. SW is their g=0 restriction, with x_SW≈.718592707322.

**Certification:** PASS on stated exact witness. Not a general result for small kappa (V2a multiplicity examples and regions outside this strong Rosen bound are not transferred to V2b).

### V2B-4A-03: endogenously chosen design prevents every positive-depth union

**Claim:** for all real g∈(0,1], at the witness, A/B prefer SW to SU and C prefers remaining outside SU to IS:
M_SU(g)<W_SW and I_IS(g)<O_SU(g).

**Attack:** derive SU market quantities by independently solving the two distinct symmetric linear equations:
(A+m)Q_M + n Q_O=1; 2n Q_M + A Q_O=1,
where A=2-eta, m=(rho-eta)g+(1-rho)u and n=(1-rho)(u+v)/2.
Derive member/outsider unilateral design FOCs using the inverse 3×3 matrix and own-design-only M_i perturbation (NOT differentiate a symmetric joint choice).
Derive W_member and W_outsider from consumer CS=.5q'Bq plus own firm operating profit and once-paid real investment. Re-solve their equilibrium path implicitly; do NOT hold designs constant when differentiating policy.

For each of the 1,000 exact adjacent rational policy intervals G=[j/1000,(j+1)/1000], each:
(1) a *numerical* root guess merely centers a rational Nash box;
(2) the **parameter-uniform Krawczyk inclusion K(X,G) strictly inside X** certifies an actual SU Nash solution for every real g∈G (and invertible SU Jacobian);
(3) a scalar **interval Newton enclosure** does the same for IS's unique Nash design;
(4) interval differentiation and implicit comparative statics enclose the total dM_SU/dg and d(I_IS-O_SU)/dg and require their ENTIRE upper bounds strictly negative.

All 1,000 ranges succeeded: 0 failed sign/solution/invertibility intervals. Largest interval upper bounds (not pointwise estimates):
dM_SU/dg < -0.0079701929973;
d(I_IS-O_SU)/dg < -0.0150388833377.

At g=0, W_SW=M_SU=O_SU=I_IS. Integrating uniform strict derivatives proves the two global inequalities for every g>0. C strictly refuses positive-depth accession at Stage 2; and SU would make A/B strictly worse than Stage-1 rejection. Hence **no substantive positive-depth alliance in any sequentially rational path**. Formal SW vs SU/IS membership labels at g=0 can vary with indifferent action choices; no unique formal government SPNE is claimed.

**Certification:** PASS conditional on soundness of independently derived symbolic algebra and the shared mpmath interval arithmetic kernel. This is stronger than merely scanning finitely many g values.

### V2B-4A-04: frozen-design counterfactual has positive-depth IS and dominates ANY SU

**Claim:** when firms' design strategies are fixed to SW Nash x_SW while keeping the *same* government extensive game, utility, design-cost LEVEL, and government objectives, an accepted positive-depth IS exists and beats all SU and SW possibilities for proposer A.

**Attack:** isolate SW x root with rational bounds x∈[.71859270731,.71859270734], verified by opposite-sign exact-interval FOCs. Hold x constant in separate SU/IS primitive welfare formulas for every policy g. At g=1/20=.05, interval inequalities show:
I_frozen(.05)-O_frozen(.05) > .00023461662306 (C applies);
I_frozen(.05)-M_frozen(.05)>0 (A/B admit);
I_frozen(.05)-W_SW>0 (B accepts).
Cover all g∈[0,1] by 500 exact rational subintervals and bound W_A^SU(g) from above. Independent interval result:
sup_g M_frozen(g) < 2.423573565 < 2.4413970373 < I_frozen(.05).
Thus any global best Stage-1 agreement cannot be SW or a terminal SU and must be a positive-depth IS. The positive-depth IS feasible set is closed under weak acceptance at ties, and a maximizing policy exists by continuity and compactness. No specific globally maximizing g or unique formal SPNE is claimed.

**Certification:** PASS within benchmark definition. Do not relabel the fixed-design benchmark as exogenous infinite-kappa or optimal social-planner design; it is only the SW-design-frozen counterfactual.

### V2B-4A-05: nonempty open neighborhood (NOT broad generality)

Witness has strict slack in Rosen bound, positive market BR contraction margin, SU/IS negative derivative signs uniformly on compact g domain, and frozen strict policy preference gaps. Smooth continuation in parameters inside the strict domain implies a nonempty open neighborhood with the same qualitative substantive policy outcome reversal.

**Certification:** qualitative PASS, neighborhood radius not quantified, no arbitrary-function-form portability claim.

## D. Extra adversarial domain and failed-overclaim register

- Market corner q_i=0: feasible but never equilibrium at fixed witness; global contraction proof handles all q_i>=0.
- Firm corners x_i=0 or1, asymmetric choices and off-path designs: feasible, but not an equilibrium of Stage 4 by Rosen uniqueness + interior certified root.
- Government g=0: institutional labels indeterminate under indifference; economic outcome equivalent to SW. Do NOT call formal government SPNE unique.
- Government g=1 and interior, outsider refusal, C application followed by member veto, A offer and B refusal: all produce one of the already certified SW/SU/IS continuations, with unchanged g on IS.
- Other eta,rho with very strong positive network complementarity: unsupported by fixed-witness certificate, and can break M positivity. No extrapolation.
- Consumer U might only be weakly, not strictly, concave at some boundary x; price inverse and firm quantity equilibrium are nonetheless well-defined.
- Every numerical solver failure is a **NUMERICAL_FAILURE**, not an unprofitable deviation. In the successful certified ranges, the numerical root was a guess and could not generate PASS without rational-interval inclusion; no failed interval remained unresolved.
- **Unproven:** general all-parameter SPNE regime map, unique literal formal government SPNE, robustness to nonlinear demand or installed-base networks, substantive interpretation for all standards, novel contribution versus inaccessible full original predecessors.

## E. Preliminary formal-verification applicability decision (mandatory Stage 4A)

**FORMALIZATION APPLICABLE**. Formal-verification IMPLEMENTATION is NOT STARTED; **FORMAL VERIFICATION PASS is NOT claimed**. Before Stage 8 freeze, at Stage 7.5A close the formal gate.

Priority target map:
1. V2B-4A-01 / Market KKT and unique continuation: formalize exact rational off-diagonal bound and contraction/positivity on cube; inputs H/X PSD and Cournot utility may initially be assumed, then audited.
2. V2B-4A-02 / Firm Nash: formalize norm and Hessian bound 27beta², Rosen diagonal strict negativity, global Nash implication. Distinguish encoded own payoff from real utility primitives.
3. V2B-4A-03 / Whole continuum signed inequalities: **highest priority** formalize interval bounds at each rational g cell, Krawczyk inclusion/parametric root existence, and total derivative negative across union of closed intervals. Verify no conclusion-smuggling via unproved sign hypotheses.
4. V2B-4A-04 / Counterfactual margins: formalize exact rational SW design root enclosure and all 500 frozen SU upper cells; show existence of feasible IS beats union.
5. V2B-4A-05 / SPNE continuation: formally express implication from inequalities and defined government game; tie conventions and equivalence at g=0 cannot be silently elided.

Suggested proof assistant: Lean 4/mathlib; toolchain/library versions to be chosen and pinned at implementation. For interval computing, use a proof-producing rational/sign certificate or independently audited validated interval library. There is no formal assistant build, no kernel proof, no author verification by implication.

## F. Stage decision and next contract

**Stage 4A canonical verdict: GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS (restricted to explicit V2b exact witness/open neighborhood; shared interval-kernel caveat disclosed).**
The independent attack materially differs from the prior root-face method, directly reconstructs firm deviations and government accounting, covers every admissible coalition/policy after all upstream histories, and isolates nonunique literal tie labels. No material unknown continuation at the witness was treated as equilibrium.

**Next: Stage 6 — Novelty Re-Kill** on this now explicitly scoped mathematical result. User authorizes deferral of unavailable Gandal–Shy/Baake–Boom original full-text readings; mark their exact theorem-absorption mapping **UNRESOLVED** instead of claiming priority. Stage 6 must attempt structurally generic parent-theorem absorption and decide mathematical contribution versus preexisting application. No theory freeze or paper drafting until later gates.
