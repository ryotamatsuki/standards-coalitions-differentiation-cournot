# V2b — Analytic Comparative Statics of Endogenous Design and Standards Selection

**Research note / proposed propositions; 2026-10-21 JST.**
**Source:** V2b repaired manuscript PR #5, inherited on PR #8. **NO change** to historical v1 / repaired-v2 freeze, baseline theorem quantifiers or original proof programs.
**Nature of evidence:** algebraic identities independently checked in SymPy, high-precision witness match to existing Stage4A/Stage13; conditional sign propositions derived on paper below. These are not yet externally refereed or independently interval-certified on any **new multi-parameter domain**.
**Scope:** canonical φ(x)=x only. Independent nonlinear φ(x)=x² has not been covered by this analytic comparative-static derivation. Cheng–Huang 2025 source-complete overlap intentionally deferred as instructed.

## 0. Main result for the research direction

The current model **already has analytic closed-form Cournot quantities, explicit unilateral design first-order conditions, and a sequential government optimization game**. It does not generally have elementary closed-form private design roots or a closed-form policy depth, and the original no-agreement proposition is a **specific parameter witness with rigorous all-depth interval proof**. Nevertheless the *same original model* yields meaningful parameter-dependent analytic propositions, particularly:

1. At a regular interior Nash, optimal similarity rises with unit design expense κ and falls with market-size parameter d, conditional on all else constant.
2. In an internationally compatible regime, \(\operatorname{sign} y_g=\operatorname{sign}(\rho-\eta)\), provided the explicit regularity and \(5\alpha>8t\) conditions hold. No unqualified all-parameter sign is asserted.
3. At the symmetric fragmented benchmark, a bilateral-compatibility perturbation causes **members to reduce differentiation more than the outsider** if \(\rho>\eta\), \(\alpha>3\beta z\), and the explicit design Jacobian diagonally dominates. This is a *new conditional analytic member/outsider design response theorem*, not just a numerical one-vector observation.
4. An explicit algebraic test compares the positive *direct* member gain of compatibility against the induced domestic-CS and cross-firm world-profit losses. A local reversal of governmental willingness is characterized by **two explicit inequalities**. The sign of the marginal outsider accession margin is exactly twice the member's marginal SU gain at the symmetric origin.
5. A solvable **regulatory-policy benchmark** exists at \(\rho=\eta\): private design and Cournot quantities are invariant to g and union membership, each compatible link adds \(\rho g Q^2\) to national CS, and the rational governments select a **complete international union with g*=1**. This shows endogeneity of the policy choice with a closed-form outcome under an interpretable balance condition.
6. Only at the frozen witness θ0 do independent global [0,1] interval certificates show every g>0 blocked; the new **local analytic inequalities alone NEVER certify a global no-union outcome**.

## 1. Primitives and analytic market equilibrium

Let \(d=a-c>0,\;\alpha=2-\eta,\;\beta=1-\rho>0,\;\delta=\rho-\eta\). Assume the model's 3-country identical-market primitives and admissible stable interior regions. The fulfilled-expectations Cournot matrix is
\[
 M=I+\delta H+\beta X,\quad M_{ii}=\alpha,\quad
 M_{ij}=\delta H_{ij}+\frac{\beta}{2}(x_i+x_j)\;(i\ne j).
\]
The conditional output solution in each national market is \(q=dM^{-1}{\bf 1}\). Firm i maximizes
\(\Pi_i=3q_i^2-\kappa(1-x_i)^2/2\). For a unilateral design deviation, never a jointly symmetric deviation:
\[
 F_i=6q_i\,q_{i,x_i}+\kappa(1-x_i)=0,\quad
 q_{x_i}=-M^{-1}M_{x_i}q.
\]
For IS define \(t=\delta g+\beta y\). Symmetric output is
\[
Q_I(g)=d/(\alpha+2t)
\]
and the scalar symmetric **firm-Nash** FOC is
\[
F(y,g;\theta)
=\kappa(1-y)
-\frac{6\beta\alpha d^2}{(\alpha-t)(\alpha+2t)^3}=0. \tag{1}
\]
The fragmented equilibrium is the same equation with \(g=0\), \(z=y|_{g=0}\). This is an explicit implicit characterization and not a closed-form expression \(y^*(\eta,\rho,\kappa,d,g)\). Its polynomial equation need not have a simple radical solution.

For SU let \(u=x_A=x_B,v=x_C\) at an equilibrium, \(h_S=\delta g+\beta u,\;n=\beta(u+v)/2,\;D_S=\alpha(\alpha+h_S)-2n^2\). The symmetric-member / outsider market quantities are **closed form**:
\[
 Q_M=\frac{d(\alpha-n)}{D_S},\qquad
 Q_O=\frac{d(\alpha+h_S-2n)}{D_S}.
\]
The two **unilateral** Nash equations can be written explicitly:
\[
\begin{split}
0=F_M(u,v,g)&=\kappa(1-u)-3\beta Q_M
 \left[\left(\frac{\alpha}{2D_S}+\frac{1}{2(\alpha-h_S)}\right)Q_O
              +\frac{\alpha-n}{D_S}Q_M\right],\\
0=F_O(u,v,g)&=\kappa(1-v)-\frac{6\beta Q_O}{D_S}
\left[(\alpha+h_S)Q_M-nQ_O\right]. \tag{2}
\end{split}
\]
Verified by differentiating the **full asymmetric 3×3 matrix** before imposing \(x_A=x_B=u\). Note not derivative \(dQ_M/du\) along a jointly symmetric change! These equations characterize the *extent of differentiation* conditional on government policy; do not falsely claim elementary closed-form \(u(g),v(g)\).

## 2. Theorem A: Analytic IS design comparative statics

At a smooth interior regular equilibrium of (1), define
\[
 G(t)=\frac{6\beta\alpha d^2(5\alpha-8t)}
 {(\alpha-t)^2(\alpha+2t)^4},\quad
 K_*=\kappa-\beta G(t).
\]
Exact derivatives: \(F_y=-K_*,\;F_g=\delta G,\;F_\kappa=1-y,\;
F_d=-12\beta\alpha d/[(\alpha-t)(\alpha+2t)^3]\).

**Conditional theorem:** If \(K_*>0\), \(\alpha-t>0\), \(\alpha+2t>0\), \(0<y<1\), then
\[
\boxed{y_g=\frac{\delta G}{K_*},\qquad
y_\kappa=\frac{1-y}{K_*}>0,\qquad
y_d=-\frac{12\beta\alpha d}{(\alpha-t)(\alpha+2t)^3 K_*}<0.}
\]
If also \(5\alpha>8t\), then \(\operatorname{sign}y_g=\operatorname{sign}(\rho-\eta)\). \(\rho>\eta\) means more technical compatibility induces **less residual differentiation** (higher y); \(\rho<\eta\) means more differentiation (lower y) under the stated stability region; \(\rho=\eta\) implies zero design response for any smooth branch. This is not a statement that every admissible parameter configuration has a unique globally stable design Nash.

**Scaling:** Divide (1) by d² to show design is governed by \(\kappa/d^2\) at fixed \(\eta,\rho,g\). Identical sign conclusions apply to SW root z at g=0.

Witness θ0: \(\alpha=1.242,\beta=.1,\delta=.142,\kappa=.8505,d=1\); certified interior IS y(g) is smoothly positive slope throughout g∈[0,1] under the established baseline uniqueness/regularity:
| g | y(g) | y_g at same depth |
|---|---:|---:|
| 0 | 0.718592707322111 | 0.153925280356752 |
| 0.05 | 0.726109003605945 | 0.146806607751270 |
| 1 | 0.821764639683783 | 0.068086183321997 |
Figures are high precision numerical evaluations of exact analytic expressions, not separate interval certificates or claimed optima.

## 3. Theorem B: Member vs outsider marginal differentiation response

At \(g=0\), let \(z\in(0,1)\) be the symmetric SW-design Nash and set \(s=\beta z,\;P=\alpha-s,\;L=\alpha+2s\). Its scalar equation is
\[
\kappa(1-z)=\frac{6\beta\alpha d^2}{P L^3}. \tag{3}
\]
Assume \(\alpha>3s\) and that the design Nash is locally regular with **strict negative diagonal dominance** below. At the symmetric SW baseline define the firm pseudo-gradient design Jacobian with diagonal \(\ell\) and off-diagonal \(h\):
\[
\ell=-\kappa+\frac{6\beta^2d^2(\alpha-2s)(2\alpha+s)}{P^2L^4},\quad
h=\frac{3\beta^2d^2(3\alpha-2s)}{P L^4}>0. \tag{4}
\]
For the bilateral AB technology edge, the **direct policy derivatives of the unilateral firm FOCs** are (A/B member p, C outsider r)
\[
p=\frac{6\delta\beta d^2(\alpha-2s)(2\alpha+s)}{P^2L^4},\quad
r=\frac{6\delta\beta d^2(\alpha^2-2\alpha s+4s^2)}{P^2L^4}, \tag{5}
\]
and most importantly
\[
p-r=\frac{6\delta\beta d^2(\alpha-3s)}{P^2L^3}. \tag{6}
\]
Since at symmetric origin the pseudo-gradient Jacobian is \(\ell I+h({\bf 1}{\bf 1}^{\top}-I)\), the derivative system is
\[
\begin{pmatrix}\ell+h&h\\2h&\ell\end{pmatrix}
\begin{pmatrix}u'\\v'\end{pmatrix}=-\begin{pmatrix}p\\r\end{pmatrix}.
\]
Solving analytically,
\[
\boxed{
u'=\frac{-\ell p+hr}{(\ell-h)(\ell+2h)},\quad
v'=\frac{2hp-(\ell+h)r}{(\ell-h)(\ell+2h)},\quad
u'-v'=\frac{p-r}{h-\ell}. }\tag{7}
\]
**Comparative-static theorem:** If \(\delta>0,\;\alpha>3s,\;-\ell>2h\), then
\[
\boxed{u'(0)>v'(0)>0.}
\]
Proof: \(-F_x\) is a nonsingular strictly diagonally dominant M-matrix (positive inverse) and \(p>r>0\); (7) yields the ordering. The **extent of private differentiation** \(d_M=1-u,\,d_O=1-v\) consequently falls for both, but more strongly for the two members. If \(\delta<0\) under the same regularity, \(u'(0)<v'(0)<0\). If \(\delta=0\), both marginal design responses vanish. These local results do **not** describe the sign of u−v or the derivative for every g or theta.

At θ0 the exact derivative expressions yield:
\[
\ell=-0.817140038944638,\quad h=0.024908223365246,\quad
p=0.0473711446986142,\quad r=0.0233682096586842;
\]
\[
 u'(0)=0.060810231735214,\quad
 v'(0)=0.032304816886324.
\]
**This proves a parameter-conditional institutional asymmetry of product-design reaction** using the simple original game, without adding any firms, instruments, or functional forms. Claimed standalone novelty remains pending proposition-level prior-work audit.

## 4. Theorem C: Analytic policy-assessment reversal and a direct/induced incidence cutoff

National welfare is \(W_i=\mathrm{CS}+3q_i^2-\kappa(1-x_i)^2/2\). At the fragmented symmetric baseline, with all designs held fixed and only the AB standard link changed:
\[
D:=\left.\partial_g W_A^{SU}\right|_{g=0,x=z{\bf 1}}
=d^2\left[\frac{\rho}{L^2}
-\frac{2\delta(1+2s)}{L^3}
-\frac{6\delta\alpha}{P L^3}\right]. \tag{8}
\]
For \(\delta>0\), its sign is equivalently \(D>0\iff
\delta<\rho L/[2(1+2s)+6\alpha/P]\). **The right side also depends on parameters through the endogenous z**, so this is an *implicit economic cutoff*, not an exogenous universal numerical threshold.

The consumer welfare derivative with respect to **any one** firm's residual homogeneity at that origin is
\[
\mathrm{CS}_{x_j}=-\frac{\beta d^2(\eta+2s)}{L^3},
\]
and the home firm's world-profit cross-derivative with respect to a competing firm's design is
\[
\Pi_{A,x_B}=\Pi_{A,x_C}
=-\frac{3\beta d^2(\alpha-2s)}{P L^3}.
\]
The home firm satisfies \(\Pi_{A,x_A}=0\) at its own design Nash. Therefore
\[
\boxed{
m'(0)=D-\underbrace{
 \frac{\beta d^2(\eta+2s)}{L^3}(2u'+v')
 -\frac{3\beta d^2(\alpha-2s)}{P L^3}(u'+v')
}_{\mathcal L(\theta)>0\text{ under Theorem B assumptions}}. }\tag{9}
\]
This is a compact complete **economic incidence** formula. \(\mathcal L\) is the induced loss from domestic consumer responses and the design of rival exporters, *not the own firm's knowingly marginally unprofitable design move*. All terms are explicit rational functions of \(\eta,\rho,\kappa,d,z\) via (3)–(7).

A **sufficient and economically interpretable local assessment-reversal condition** is
\[
\boxed{ 0<D(\theta)<\mathcal L(\theta),\qquad
\delta>0,\;\alpha>3\beta z,\;-\ell>2h. }\tag{10}
\]
Then the restricted-fixed-design government's terminal bilateral evaluation has **positive** slope \(\widehat m'(0)=D>0\), but the true endogenous design government's slope is **negative** \(m'(0)=D-\mathcal L<0\).

**Graph symmetry identity, independently derivable:** for either the endogenous and the frozen game at SW symmetric origin,
\[
(i-o)'(0)=2m'(0),\qquad
(\widehat i-\widehat o)'(0)=2\widehat m'(0)=2D. \tag{11}
\]
There are two incident edges and one nonincident edge under IS; when one forms SU, the member sees one incident edge and C sees one nonincident edge. Equation (11) is *not a second independent economic mechanism*, it follows from permutations of the three standard edges.

For positive δ and D>0, the **frozen-design restricted government game has feasible international accession at sufficiently small positive g**, not just a positive member margin. Indeed the outsider's local application slope is 2D>0, and the incumbent's approval margin obeys
\[
 (\widehat i-\widehat m)'(0)
 =2D+\frac{6\delta d^2}{P L^2}>0,
\]
while \(\widehat i'(0)=3D+6\delta d^2/(P L^2)>0\) ensures the applicant and incumbent obtain positive payoff vs SW. By contrast, condition (10) makes both true \(m(g)-s\) and \(i(g)-o(g)\) negative for **all sufficiently small g>0**. This establishes a **local** government-consent regime reversal using analytic parameter inequalities. *Proposer-global-optimal IS versus every possible SU depth remains unproved by (10) alone.*

Witness θ0:
\[
z=0.71859270732211115,\quad D=+0.00676792412884482,
\]
\[
\text{induced CS}=-0.00521621962865225,\quad
\text{induced rival exporter profit}=-0.00985352449660545,
\]
\[
\mathcal L=0.01506974412525770>D,\quad
m'(0)=-0.00830181999641288.
\]
At this witness the *additional pre-existing global interval theorem* proves \(m(g)<s,\;i(g)<o(g)\) for **every** g∈(0,1]; the new local theorem explains **why** its signs differ from the frozen assessment. The frozen government full-policy-envelope result (positive IS proposer-optimal) is likewise from the existing separately certified global computation.

## 5. Theorem D: An analytically solved, optimal international standard at rho = eta

Set \(\rho=\eta\in(0,1)\), i.e. \(\delta=0\). Then \(M=I+\beta X\) is **independent of the government regime and technical depth g**. Assume, as in the original game at a regular region, the resulting privately chosen design Nash is unique and interior at x_i=z, with \(q_i=Q=d/(\alpha+2\beta z)>0\). It is the same z in SW, SU, IS, and at every g. This is endogeneity with a stable optimal private choice, **not exogenously fixing firm design**.

At these equilibrium quantities, standardizing exactly one pair raises national CS by \(\rho g Q^2\) and leaves every firm's world profit and design expenditure unchanged. Hence
\[
\boxed{
m(g)=o(g)=s+\rho g Q^2,\qquad
i(g)=s+3\rho g Q^2. }\tag{12}
\]
For every g>0, \(i>m=o>s\). C strictly applies, A/B strictly approve accession, B accepts the initiating AB agreement, and the proposer A maximizes i(g) at **g*=1**.

**Conclusion (conditional analytic global equilibrium theorem):** Under the unique-interior-Nash feasibility assumptions and \(\rho=\eta\in(0,1)\), the sequential government game chooses **maximum-depth IS** (on path) even though private residual design remains optimized. **No frozen/endogenous difference exists** because the Nash itself is policy invariant. This demonstrates a parameter-dependent *endogenous standard choice* analytically without a computational search and provides a meaningful comparator to the certified θ0 in which \(\delta=.142>0\) yields no substantive union at any positive g.

This is a **balanced-channel knife-edge benchmark**. Do not claim it describes an open region or a general sharp threshold; proving transition bands and global g choices outside δ=0 is future work.

## 6. General policy-selection characterization (not pretending to solve every parameter)

For any regular theta and unique design continuation, define conditional country payoffs \(s,m(g),o(g),i(g)\) as in the paper. Under the exact bilateral-first/unanimity/inherited-depth rules, a candidate positive-depth **international standard** requires
\[
 i(g)\ge o(g) \;\text{(C applies)},\qquad
 i(g)\ge m(g) \;\text{(members approve)},\qquad
 i(g)\ge s \;\text{(B accepts initially)}. \tag{13}
\]
A terminal positive-depth SU can be sustained only if \(m(g)\ge s\), and accession does not occur (one of the strict/weak inequalities for accession above fails, with specified tie rules). A chooses g and its feasible continuation to maximize own payoff, comparing all possible depths and SW. For a differentiable interior candidate for IS policy maximization, \(i'(g)=0\) and feasible-node conditions must hold; for SU, \(m'(g)=0\). These FOCs alone do **not** guarantee global optimality in nonconcave policy payoffs or across regime switches. The policy problem is therefore **analytically specified**, but a universal closed-form \(g^*(\theta)\) has not been proved and should not be claimed.

Two rigorously contrasted parameter cases:
- \(\rho=\eta\in(0,1)\): theorem (12) gives **g*=1, grand international union** under regular uniqueness assumptions.
- Frozen witness \(\theta_0=(1,0.758,0.9,0.8505)\): **effective substantive g*=0, no positive-depth agreement** under original game, from existing global rational-interval proof; restricted-frozen design has proposer-optimal **some positive g**, but its exact optimizing depth is not identified. Reporting g=.05 as \(\hat g^*\) would be wrong.

## 7. Replication and stop rules

This report's algebra for SU policy design p,r, Jacobian ℓ,h and local W derivatives was reconstructed by differentiating the full asymmetric Cournot matrix, and its compact formulas were checked via exact SymPy cancellation, with 65-digit mpmath witness calculations. Corresponding verification code was generated as \`v2b_analytic_comparative_statics_verification.py\` in the working environment, whose identity and witness checks passed. These tests do NOT:
- independently recertify a multi-dimensional continuum of model parameters,
- establish global Nash uniqueness outside the frozen witness,
- prove all-depth government failure from a local derivative sign,
- substitute for the needed Stage3 / Stage4A / Stage6 audit if these claims are integrated into an expanded frozen theory,
- show the new conditional results are proposition-level original vs all relevant predecessors.

**Strategic paper architecture:** Keep the simple original demand/cost functions. Put analytic market solution and design FOCs in the model/equilibrium section; make Theorems A/B (design comparative statics) and C (government consent mechanism) visible main results; present theorem D as an interpretive policy benchmark; retain the rigorous all-g witness as an especially sharp equilibrium counterexample rather than a mystery computer-generated finding. Move large matrix algebra/interval certificates to appendix. Referee-complete originality and author signoff are separate gates.

## 8. Bottom line

**The same intentionally simple V2b model can support genuine algebraic comparative statics and an analytically solved full standard-selection benchmark; it is not limited to existence-only simulation.** The next research question is whether the conditional theorem assumptions define economically substantial, nontrivial regions beyond the witness and whether similar mechanism results are already implied by predecessor theories—not to introduce arbitrary firms, subsidies or demand flexibility merely to make the model more general.
