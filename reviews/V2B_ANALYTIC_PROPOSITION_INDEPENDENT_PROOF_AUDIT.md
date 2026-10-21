# V2b Stage13A — independent analytic proposition proof audit

Date: 2026-10-21 JST. Audited source: PR #9 `07b275fd5693d8160234bf2e318e24e2fa4878c2`, descending from PRs #5–#8. This is an AI-assisted independent computational/reasoning audit, not external human peer review. Historical reports, manuscript, frozen sources and failed nonlinear checks are preserved.

## Decision and critical finding

**CONDITIONAL GO for a corrected full-paper development package; REVISE the literal Theorem C display.** All principal component identities checked independently agree with PR #9. However, its research report equation (9) has an incorrect minus sign inside the definition of the induced loss. Its checker tests the component derivatives but never assembles that displayed loss. Thus successful execution of the old checker did not validate the complete proposition.

The original expression is retained in its original file. The correct loss is

\[
\mathcal L=\frac{\beta d^2(\eta+2s)}{L^3}(2u'+v')
+\frac{3\beta d^2(\alpha-2s)}{P L^3}(u'+v').
\]

With the printed minus sign it is approximately −0.004637305 at the baseline, implying the wrong member slope +0.011405229. The corrected sum is +0.015069744, giving the previously reported negative slope −0.008301820. Therefore **the literal displayed C formula is FAILED; the corrected C formula and conditional theorem are PROVED — ANALYTIC**. This does not invalidate the older frozen all-depth theorem or change the model.

## 1. Source and independent calculation discipline

Read `paper/sections/01_model.tex`, `02_equilibrium.tex`, `03_main_results.tex`, `A_proofs.tex`, both Theory Freezes, PR #5 repair, PR #6 editorial rejection, PR #7 reappraisal, PR #8 structural audit, and PR #9 research report. The PR stack is research history, not independent proof evidence.

The new program `verification/v2b_stage13a_independent_audit.py` imports **no previous V2b program**. It solves a fully asymmetric Cournot system by scalar Cramer cofactors with three independent edges, takes unilateral derivatives before imposing symmetry, reconstructs the Jacobian and policy forcing, and checks the assembled welfare identity. This differs from PR #9's symmetric inverse-projector/matrix-derivative implementation. A second reviewer independently repeated the scalar calculation; see `V2B_STAGE13A_MATH_SECOND_REVIEW.md`.

For the new regional certificate every endpoint and intermediate operation is a Python `Fraction` interval. No float, mpmath printer, or inexact coefficient is used in sign certification. Floats appear only in labelled output summaries and numerical diagnostics. The `Interval` class rejects float coercion. Exact interval lower/upper endpoints are saved in `verification/stage13a/independent_results.json`.

## 2. A1 — Cournot equilibrium and welfare foundations

Write \(\alpha=2-\eta,\ \beta=1-\rho,\ \delta=\rho-\eta\), with \(d>0,0<\rho<1,0\leq\eta<1,\kappa>0\). Conditional inverse demand is \(p=a1-Bq+\eta Hn^e\), where \(B_{ii}=1\). Holding expected network use fixed during an output deviation gives \(p_i-c-q_i=0\). Only afterwards impose \(n^e=q\). Thus

\[
Mq=d1,\qquad M=I+B-\eta H,
\quad M_{ii}=\alpha,\quad M_{ij}=\delta H_{ij}+\tfrac\beta2(x_i+x_j).
\]

If \(M\) is nonsingular and \(M^{-1}1>0\), the interior candidate is \(q=dM^{-1}1\). Own output payoff has second derivative −2 given fixed expectations. These conditions identify an interior solution; nonsingularity alone does not exclude other nonnegative boundary fixed points. A convenient general sufficient condition for **unique nonnegative fulfilled-expectations equilibrium** is \(M\succ0\): the associated strictly convex quadratic program/LCP then has a unique solution; positivity of \(M^{-1}1\) makes it interior. No adaptive stability of actual network expectations is asserted.

For \(\delta\geq0,\eta>0\), all off-diagonal coefficients lie in \([0,1-\eta]\), and \(\alpha-2(1-\eta)=\eta>0\). The fixed-point map \(T_i=\max\{0,(d-\sum_{j\ne i}M_{ij}q_j)/\alpha\}\) maps \([0,d/\alpha]^3\) to itself, is a strict contraction and has strictly positive untruncated numerators. This is a uniform sufficient condition on the full design/policy cube, not a necessary condition. It includes the baseline. For \(\delta<0\), use the matrix/LCP criteria rather than silently importing this nonnegative-coefficient argument.

**Demand PSD is more general than the old baseline claim.** All 56 principal minors at the eight vertices of the affine three-dimensional design cube for X are nonnegative (exact check). Hence X is PSD on that cube. H is PSD: in SU its eigenvalues are \(1-g,1+g,1\); in IS they are \(1-g,1-g,1+2g\). Consequently \(B=\rho H+(1-\rho)X\succeq0\) for all admissible parameters and histories. At \(g=1,x=(1,1,1)\), B is rank one, so strict positive definiteness is false on the whole cube. At interior designs X is PD (an interior convex combination gives positive weight to X(0)=I), so B is PD there. PSD does not itself prove Cournot interiority.

At fulfilled expectations the margin remains q_i, worldwide operating profit is \(3q_i^2\), and the once-paid cost is \(\kappa(1-x_i)^2/2\). Consumer surplus is \(q^TBq/2\); the network term is already present through conditional willingness to pay, and must not be added again.

## 3. A2 — unilateral design Nash, not a symmetric joint derivative

The correct pseudo-gradient is \(F_i=6q_iq_{i,x_i}+\kappa(1-x_i)\). The matrix identity \(q_{x_i}=-M^{-1}M_{x_i}q\) follows by differentiating the market equations, but the independent code instead differentiates scalar cofactor quotients. Interior stationarity requires F_i=0; at x_i=0 a maximizing endpoint requires F_i<=0, and at x_i=1 requires F_i>=0. F_i=0 alone is neither a global best response nor a Nash proof.

In IS, at a symmetric candidate y, let \(t=\delta g+\beta y\). Then

\[
Q=\frac d{\alpha+2t},\qquad
F(y,g)=\kappa(1-y)-\frac{6\beta\alpha d^2}{(\alpha-t)(\alpha+2t)^3}=0.
\]

SW is the same equation at g=0, giving z. These are unilateral Nash equations evaluated at a symmetric profile, not derivatives of the joint path profit.

In SU let \(c=\delta g+\beta u,\ n=\beta(u+v)/2,\ T=\alpha(\alpha+c)-2n^2\). Then

\[
Q_M=d(\alpha-n)/T,\quad Q_O=d(\alpha+c-2n)/T,
\]
\[
F_M=\kappa(1-u)-3\beta Q_M\{[\alpha/(2T)+1/(2(\alpha-c))]Q_O+(\alpha-n)Q_M/T\}=0,
\]
\[
F_O=\kappa(1-v)-6\beta Q_O[(\alpha+c)Q_M-nQ_O]/T=0.
\]

These equal the PR #9 expressions; independent reviewer recomputation confirms the individual deviation is taken first. General interior feasibility here requires nonzero denominators and strictly positive displayed quantities, with the full Cournot uniqueness condition above.

**Useful full-asymmetric sufficient condition.** When \(\delta\geq0,\eta>0\), the inverse norm bound is \(1/\eta\), \(\|q\|_\infty\leq d/\alpha\), \(\|M_{x_i}\|_\infty\leq\beta\). Every operating-profit Hessian entry has magnitude at most
\[
H_0=18\beta^2d^2/(\eta^2\alpha^2).
\]
If \(\kappa>3H_0\), the symmetric pseudo-gradient Jacobian is strictly negative diagonally dominant everywhere. Thus own profits are strictly concave, a pure Nash exists by compactness/concavity, and Rosen strict monotonicity gives at most one Nash on the **entire asymmetric cube**, including boundary strategies. Interior existence is a separate root or boundary argument. This condition is sufficient, conservative, and not necessary. Symmetry then yields equal IS designs and equal SU member designs; it must not be assumed to exclude asymmetric equilibria.

## 4. A3 / Proposition A — symmetric comparative statics

Suppose the symmetric stationary profile is an interior Nash with smooth continuation; \(\alpha-t>0,\alpha+2t>0\). Set
\[
G=\frac{6\beta\alpha d^2(5\alpha-8t)}{(\alpha-t)^2(\alpha+2t)^4},\qquad K=\kappa-\beta G.
\]
For K>0, exact implicit differentiation yields
\[
y_\kappa=(1-y)/K>0,\quad
y_d=-12\beta\alpha d/[(\alpha-t)(\alpha+2t)^3K]<0,\quad y_g=\delta G/K.
\]
If additionally \(5\alpha>8t\), \(\operatorname{sgn} y_g=\operatorname{sgn}\delta\), with zero response at delta=0. These assumptions are **sufficient**, not necessary. K=0 is a singular branch point where the displayed derivative formula is unavailable. K>0 is stability of the symmetric pseudo-gradient direction; it does not alone prove full-game Nash uniqueness or dynamic stability of arbitrary adjustment processes. Whole-branch monotonicity follows only if all assumptions hold along that branch. No all-parameter comparative static is proved.

Economic content: more costly differentiation raises residual similarity; a greater demand intercept/net production margin increases the profit scale and supports differentiation. In this model d=a−c is not literally population. At fixed other parameters design depends on κ/d². Positive delta means technical substitution dominates the network-benefit channel in effective Cournot competition, inducing less differentiation under the stated regularity conditions.

**Analytic boundary counterexample to unconditional strict signs.** Take rho=eta=9/10,d=1,kappa=1/10. With rivals' designs zero, \(q_i(x)=d(\alpha-\beta x)/(\alpha^2-\beta^2x^2/2)\). For every x in [0,1],
\[
F_i(x)\leq\kappa-6\beta d^2(\alpha-\beta)^2/\alpha^5<0.
\]
Thus x_i=0 is the strict global best response; (0,0,0) is a boundary Nash. Strict derivative conclusions fail there (the boundary branch is locally constant in κ,d). This does not contradict the interior theorem. The bound and its positivity are recorded as exact rationals by the new code.

## 5. A4 / Proposition B — member and outsider response

At the SW symmetric Nash z define \(s=\beta z,P=\alpha-s,L=\alpha+2s\). The unilateral Jacobian diagonal/off-diagonal and AB-edge forcing are
\[
\ell=-\kappa+6\beta^2d^2(\alpha-2s)(2\alpha+s)/(P^2L^4),
\quad h=3\beta^2d^2(3\alpha-2s)/(PL^4),
\]
\[
p=6\delta\beta d^2(\alpha-2s)(2\alpha+s)/(P^2L^4),
\quad r=6\delta\beta d^2(\alpha^2-2\alpha s+4s^2)/(P^2L^4).
\]
Independent exact cancellation verifies every formula and
\(p-r=6\delta\beta d^2(\alpha-3s)/(P^2L^3)\).
The reduced IFT system is
\[
\begin{pmatrix}\ell+h&h\\2h&\ell\end{pmatrix}(u',v')^T=-(p,r)^T.
\]
It gives
\[
u'=(-\ell p+hr)/[(\ell-h)(\ell+2h)],\quad
v'=[2hp-(\ell+h)r]/[(\ell-h)(\ell+2h)],\quad
u'-v'=(p-r)/(h-\ell).
\]

**Correct theorem statement:** Assume the SW profile is a strict interior Nash, and the local stationary continuation consists of Nash equilibria, for example by the full-cube strict-concavity/Rosen condition in §3. If delta>0, alpha>3beta z, and −ell>2h, then u'(0)>v'(0)>0. Proof: h>0, p>r>0, −J is a nonsingular strictly diagonally dominant M-matrix with positive inverse; the displayed gap is positive. If delta<0 under the same feasibility and equilibrium hypotheses, u'<v'<0. This is a one-sided local g result; it does not prove u'(g)>v'(g) for all g.

The three inequalities alone establish local stationary comparative statics and local SOC, **not** global Nash uniqueness. Hence PR #9's algebra is correct, but its generic equilibrium interpretation requires the explicit Nash-continuation hypothesis. Economically, the edge directly perturbs member firms more; the outsider responds through Cournot competition and design interactions. Alpha>3beta z makes that direct forcing difference positive; diagonal dominance bounds strategic feedback. Neither inequality is a deep institutional restriction or an empirically estimated threshold.

## 6. A5 / corrected Proposition C — incidence and local consent

Under B's hypotheses, with eta>=0, define
\[
D=d^2[\rho/L^2-2\delta(1+2s)/L^3-6\delta\alpha/(PL^3)],
\quad C=\beta d^2(\eta+2s)/L^3,\quad V=3\beta d^2(\alpha-2s)/(PL^3).
\]
At SW, \(CS_{x_j}=-C\) for all j, \(\Pi_{A,x_B}=\Pi_{A,x_C}=-V\), and **\(\Pi_{A,x_A}=0\)** by the firm's Nash FOC. Total differentiation of national welfare therefore gives
\[
m'(0)=D-C(2u'+v')-V(u'+v')=D-\mathcal L.
\]
The corrected loss is the **sum** C(2u'+v')+V(u'+v'). Both components are positive under B. This assembled identity is tested independently; the code also verifies the literal PR #9 expression differs by 2V(u'+v'), preserving a reproducible failure rather than silently changing the source.

If **0<D<mathcal L**, frozen design has positive marginal member participation gain D, but endogenous design has negative gain m'. This condition is necessary and sufficient for this particular strict local sign contrast once the incidence decomposition and positive loss apply; the combined B hypotheses are merely convenient sufficient conditions. By continuity, both signs persist at all sufficiently small positive depths, at each qualifying parameter vector. No common uniform positive depth is certified across the new region.

**Accession identity.** At the symmetric origin a country's welfare derivative has a common incident-edge coefficient a and a nonincident-edge coefficient b, including the Nash design response. A bilateral member sees a=m'; outsider sees b=o'; IS sees 2a+b=i'. Hence (i−o)'=2m'. This is symmetry/linearity, not a new general standards theorem. It implies small-g endogenous accession refusal as well as negative terminal bilateral gain.

In the frozen game \(\widehat o'=D+6\delta d^2/(PL^2)\), so \(\widehat i'=3D+6\delta d^2/(PL^2)\) and \((\widehat i-\widehat m)'=2D+6\delta d^2/(PL^2)>0\) when delta>0,D>0. Thus sufficiently small positive IS offers satisfy C's application, both incumbent approvals, and B's initial acceptance against fragmentation. This is feasibility, not a universal optimizing-depth formula.

## 7. Nonempty parameter region — exact new certificate

Use coordinates (z,eta,rho,d), with
\[
z\in[0.7185,0.7187],\quad\eta\in[0.75795,0.75805],\quad
\rho\in[0.89995,0.90005],\quad d\in[0.999,1.001],
\]
and define \(\kappa=6\beta\alpha d^2/[P L^3(1-z)]\), exactly enforcing the original SW FOC. This does not change primitives; it parameterizes their admissible values by the equilibrium design. Its coordinate derivative is
\[
\kappa_z=\kappa[1/(1-z)+\beta/P-6\beta/L]>0.
\]
The interval certificate gives κ_z>2.7166, so the image of the interior is an open set in the **original four primitive coordinates** by the inverse-function theorem. Its κ enclosure [0.8477298462,0.8533172972] is **not** an independently selectable rectangular κ range.

Conservative summaries (display decimals; exact bounds in JSON):

| Quantity | Certified enclosure |
|---|---|
| delta | [0.1419,0.1421] |
| alpha−3beta z | [1.026232195,1.026607775] |
| −ell−2h | [0.764250605,0.770443495] |
| u'(0) | [0.059894654,0.061736422] |
| v'(0) | [0.031811776,0.032803528] |
| u'−v' | [0.027091126,0.029924645] |
| D | [0.006115097,0.007423209] |
| mathcal L−D | [0.007374196,0.009231004] |
| κ−54beta²d²/(eta²alpha²) | [0.236496889,0.245998854] |

The last row guarantees global asymmetric design uniqueness over the entire policy cube, and the SW root is interior by construction. The IFT then gives an interior Nash continuation for small g, so B/C are genuine equilibrium conclusions on this open primitive region. This is **PROVED — COMPUTER-ASSISTED**, using exact rational intervals. It establishes nonvacuity and positive dimension, **not** that the reversal is economically widespread. The box is a deliberately conservative audit neighborhood, not a new optimized witness or an all-depth parameter-region theorem.

## 8. A6 / Proposition D — complete policy solution at rho=eta

Let rho=eta=r in (0,1). M=I+beta X does not depend on H,g or regime; the privately optimized design game is identical after all government histories. Given its unique interior Nash z, Q=d/(alpha+2beta z)>0 is constant. Each compatible pair adds rho g Q² to each country's identical domestic CS, while profits and design cost stay fixed. Thus exactly
\[
m(g)=o(g)=s+\rho gQ^2,\qquad i(g)=s+3\rho gQ^2.
\]
For every g>0, C strictly prefers i to o, each incumbent strictly prefers i to m, and B strictly prefers the anticipated i to rejecting for s. Government A therefore globally maximizes i over [0,1] at g=1. Under the stated affirmative tie rule, the on-path regime is IS. The positive-depth allocation is unique; redundant off-path strategies/zero-depth labels need not be unique.

**Explicit nonvacuous sufficient conditions**, closing the previously assumed equilibrium foundation:
\[
\kappa>\max\{54\beta^2d^2/(r^2\alpha^2),\ 6\beta d^2/\alpha^3\}.
\]
The first bound proves full asymmetric strict concavity/Rosen uniqueness; the second gives symmetric F(0)>0. F(1)<0, so an interior symmetric stationary root exists and is the unique global Nash by strict own concavity. At r=9/10,d=1,kappa=1 the two bounds are exactly 200/363 and 600/1331, both below one. These conditions suffice for all government histories. B is PSD everywhere and PD at the interior equilibrium, including g=1. This D theorem is **PROVED — ANALYTIC**, under explicit primitive sufficient conditions. It is a cancellation benchmark on a codimension-one surface, not a general regime transition threshold or an open region of maximum-depth optimality.

## 9. Validation, earlier theorem consistency and limits

Executed with pinned Python dependencies: SymPy1.13.3, NumPy2.2.6, SciPy1.15.3, mpmath1.3.0, Python3.12.14.

* New independent checker: **28 exact identities PASS**, including off-symmetry SU quantities/FOCs and an independently differentiated IS accession identity; all new Fraction region inequalities PASS, universal X PSD vertex checks PASS, exact balanced benchmark and boundary examples PASS. Finite differences of actual unilateral profits reproduce the design slopes within the documented tolerance; these numerical checks are not proof.
* Original baseline Krawczyk program rerun: **PASS**, 1,000 rational g cells, zero splits; member derivative upper −0.0079701929973, accession derivative upper −0.0150388833378; frozen C gain lower +0.0002346166231; displayed frozen IS lower 2.4413970373 exceeds all-SU envelope upper 2.4235735642 and SW upper 2.4220784217. These are existing computer-assisted proof results, distinct from the new local-region proof.
* Freeze verifier rerun: **PASS**, all 11 v2-protected blobs unchanged. No old freeze, theorem or historical audit was overwritten.
* New workflow `.github/workflows/v2b-stage13a-independent.yml` runs the independent checker and freeze check. Actual remote run status is recorded separately; merely adding workflow YAML is not a CI PASS.

| Claim | Status | Remaining qualification |
|---|---|---|
| A1 matrix/market identities | PROVED — ANALYTIC | Interior/uniqueness conditions must accompany formula |
| A symmetric derivative formulas | PROVED — ANALYTIC | CONDITIONAL — REGULARITY ASSUMPTIONS; not boundary/global-all-theta |
| B ell,h,p,r and response rank | PROVED — ANALYTIC | Requires Nash continuation beyond local SOC |
| Literal PR #9 C Eq.(9) | FAILED | Preserve; issue separate correction before manuscript integration |
| Corrected C local consent reversal | PROVED — ANALYTIC | Conditional on explicit sufficient assumptions |
| B/C nonempty open primitive region | PROVED — COMPUTER-ASSISTED | Local in g; conservative small region |
| Existing theta0 all-g reversal | PROVED — COMPUTER-ASSISTED | Rerun old canonical certificate; not new multi-parameter certificate |
| D maximum-depth IS | PROVED — ANALYTIC | Explicit sufficient conditions; rho=eta only |
| General policy threshold or general g*(theta) | UNRESOLVED | Not asserted by this audit |
| Numerical derivative agreement | NUMERIC EVIDENCE ONLY | Diagnostic only |

**Disposition:** correct the mathematical display and explicit hypotheses in a separate research revision before integrating PR #9 into a new theorem freeze. Return these two claims to Stage4/4A review, not the already sound older frozen theorem. There is no evidence requiring a new demand function, another firm, or a changed governmental agenda to repair the audited results.
