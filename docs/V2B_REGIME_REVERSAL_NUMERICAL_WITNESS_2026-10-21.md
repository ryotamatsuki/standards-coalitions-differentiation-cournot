# V2b: conditional coalition-regime reversal under endogenous differentiation

**Date:** 2026-10-21. **Status:** independent numeric witness plus analytic local-derivative identity; **NOT a global SPNE theorem or theory freeze**.

## 1. Primitives and stage 4
As in V2b, firms compete in three equally sized countries. Each national consumer has quadratic utility with fulfilled network expectations:
\[
U(q\mid n^e)=a\mathbf1^\top q-\frac12 q^\top Bq+\eta q^\top Hn^e,\quad
B=\rho H+(1-\rho)X,\quad H_{ii}=X_{ii}=1,
\]
where \(H_{ij}=g\) for a pair sharing a standard and 0 otherwise; \(X_{ij}=(x_i+x_j)/2\).
Cournot interior quantities solve \(Mq=\mathbf1\), \(M=I+(\rho-\eta)H+(1-\rho)X\), \(a-c=1\).
Stage-4 firm objective is \(3q_i^2-\kappa(1-x_i)^2/2\).
Government welfare is \(W_i=\frac12q^\top Bq+3q_i^2-\kappa(1-x_i)^2/2\).
Stages 1–3: A proposes an AB SU with depth g, B accepts/rejects, C applies or remains outsider, A and B unanimously accept/refuse. **IS inherits the same g.** Rejected B -> SW. Costs of adoption zero. At g=0, institutional membership is observationally SW-equivalent and labels depend on tie conventions.

## 2. Stage-4 uniqueness sufficient condition: independently explain, do not just invoke
For each \(x_i\in[0,1]\), \(X\) is positive semidefinite (it is multi-affine in x, and all eight Boolean-vertex matrices are PSD). \(H\) is PSD. Define \(\beta=1-\rho\), \(d=a-c\), \(\mu=1-3\max\{\eta-\rho,0\}>0\). Then
\[
M=I+(\rho-\eta)H+\beta X\succeq\mu I.
\]
At every smooth interior Cournot profile, \(\|q\|_2\leq\sqrt3d/\mu\) and
\(\|\partial M/\partial x_i\|_2=\beta/\sqrt2\).
Implicit differentiation gives \(\|\partial q/\partial x_i\|_2\leq \beta\sqrt{3/2}d/\mu^2\) and
\(\|\partial^2q/\partial x_i\partial x_j\|_2\leq\beta^2\sqrt3d/\mu^3\).
Hence each Hessian entry of \(3q_i^2\) is bounded in absolute value by \(27\beta^2d^2/\mu^4\), and the game-profit Jacobian symmetric part is negative definite when
\[
\kappa>81\beta^2d^2/\mu^4.
\]
This establishes strict concavity in own strategies and Rosen-style diagonal strict concavity, yielding a unique Stage-4 pure Nash equilibrium (assuming the full Cournot interior-demand result and all stated smoothness conditions). The preceding coefficient is conservative. In the particular witness \(\eta<\rho\), so \(\mu=1\).

## 3. Main numerical witness WITHIN the uniqueness sufficient region

Set
\[
\eta=0.758,\quad \rho=0.900,\quad \kappa=0.8505,\quad d=1.
\]
The sufficient threshold equals \(81(1-\rho)^2=0.8100<0.8505=\kappa\). The positive-demand safe restriction \(0\leq\eta<\min\{1,4\rho/3\}\) is satisfied.

At SW, the unique symmetric Stage-4 continuation has
\[
x^{SW}=0.718592707322,\qquad W^{SW}=2.422078421718.
\]

### A. Endogenous x (full V2b)
Write \(M(g)=W_A^{SU}(g)=W_B^{SU}(g)\), \(O(g)=W_C^{SU}(g)\), and \(I(g)=W_i^{IS}(g)\) with the unique Stage-4 continuation.

Numerical audit of **1,001** uniformly spaced g values on [0.001,1] finds:
- \(\max[I(g)-O(g)]\approx -0.000016774<0\). C does not want to join at any sampled positive g.
- \(\max[M(g)-W^{SW}]\approx -0.000008325<0\). A/B do not want to form SU at any sampled positive g.
- At g=1: \(I-O\approx-0.125082032\), \(M-W^{SW}\approx-0.027102173\).
- At g=0.0001: \(I-O\approx-1.6621\times10^{-6}\) and \(M-W^{SW}\approx-8.3042\times10^{-7}\).

Thus **the numerical candidate is no substantive integration / SW-equivalent g=0**. Do NOT claim global optimality on the full continuum from a finite grid alone; a rigorous no-positive-g proof is still required.

### B. Frozen x benchmark
Hold \(x_i=x^{SW}\) fixed regardless of S,g, but keep all other primitives unchanged. This is a counterfactual, not a Nash Stage-4 policy.

The C participation condition \(I(g)\geq O(g)\) is met for small positive g and binds at:
\[
g_C=0.077435193151,\qquad I(g_C)=O(g_C)=2.451454610408.
\]
At the cap \(I(g_C)>W^{SW}\) and \(I(g_C)>M(g_C)\). The unconstrained IS welfare rises in the admissible interval. The frozen benchmark **therefore admits positive-depth IS**.

At g=0.07743519, the true endogenous SU member/outsider design choices are \(x_{1,2}\approx0.7232099\), \(x_3\approx0.72106734\). Under IS the true endogenous design is \(x_i\approx0.73008549\). Such reactions tighten C's accession constraint; this is why fixing x predicts too much standards integration.

The *policy regime* changes between a positive-depth IS in the frozen counterfactual and a SW-equivalent outcome in the endogenous case **as a robust numerical candidate**, not a fully certified theorem.

## 4. Exact local derivative identity from permutation symmetry

Let \(\widetilde W_i(t_{AB},t_{AC},t_{BC})\) be a differentiable reduced-form government payoff after unique firm continuation, where each t denotes the cross-compatibility on one edge; each link contributes additively to the utility/kernel and all firms/countries are ex ante symmetric.

Write \(m=\left.\partial_g W_A^{SU}(g)\right|_{g=0}\) when only edge AB is activated, and \(o=\left.\partial_g W_C^{SU}(g)\right|_{g=0}\) for the outsider. By symmetry the effect on a given country from an incident edge is m and from an unconnected edge is o. IS activates all three edges, so
\[
\left.\partial_g W_i^{IS}\right|_0=2m+o,\qquad
\boxed{\left.\partial_g[I(g)-O(g)]\right|_0=2m}.
\]
This equality applies both to firms reoptimizing and firms frozen, as long as the reduced-form continuation is differentiable and symmetry holds. It does NOT itself establish the global policy outcome.

Numerically, at the witness:
- Frozen: \(M'(0)\approx+0.00676792\), \([I-O]'(0)\approx+0.01353584\).
- Endogenous: \(M'(0)\approx-0.00830182\), \([I-O]'(0)\approx-0.01660364\).

**Mechanism:** endogenous residual product homogeneity raises pairwise substitutability after standard adoption, flipping the initial private incentive for a regional standards union and C's incentive to join a global standard at the same time. This mechanism survives a sufficient condition proving unique Stage-4 continuation.

## 5. Independent checks

Source: \`verification/v2b_regime_reversal_numeric.py\` (Scipy/NumPy). Repeatable tests:
- Check Stage-4 sufficient uniqueness inequality and inner-product equilibrium;
- Independently calculate SW/SU/IS Stage-4 choices from profit derivatives;
- Scan all g in [0.001,1] with 1,001 points;
- Find frozen counterfactual accession cap with Brent root search;
- Verify numerical one-firm unilateral best responses across [0,1] at g=0, cap, 0.5, 1.

### Open proof blockers
1. Analytically prove \(I(g)<O(g)\) AND \(M(g)<W^{SW}\) for **all real** g∈(0,1] at witness; finite sampling is not a certificate.
2. Prove frozen benchmark's optimal policy g is exactly the C cap, with no other admissible intervals or profit maxima.
3. Clarify precise tie-handling at g=0 (SW-equivalent may have formal SU/IS membership).
4. Verify every analytical bound, including the global-demand interior assumptions, in a clean theorem/proof file.
5. Search whether an open set in (eta,rho,kappa) maintains strict reversal; use continuity and no-positive-g inequalities.
6. Compare theorem-level contributions with compatibility/differentiation coalition literature before novelty claims.

No theory freeze, submission claims, or source-to-source copying from terminated C-ESD.
