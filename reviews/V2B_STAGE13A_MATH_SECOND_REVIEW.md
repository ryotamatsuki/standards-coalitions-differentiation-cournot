# Stage 13A: independent second mathematical review

Date: 2026-10-21 JST. Source inspected: `paper/sections/01_model.tex`, `02_equilibrium.tex`, `A_proofs.tex`, historical v2 repair record, then PR #9's research note. No frozen file or earlier theorem was changed. This review concerns canonical `phi(x)=x` only.

## Verdict and a material erratum

The unilateral differentiation formulas, policy-forcing coefficients, conditional design-response ordering, and balanced-channel policy benchmark survive independent derivation. **PR #9 equation (9), as printed, fails:** the rival-profit loss is subtracted inside the definition of the induced loss. Its sign must be positive. The reported baseline numbers use the intended positive sum, not the printed formula. This is a genuine formula error rather than a counterexample to the intended economic mechanism.

Write `C=beta*d^2*(eta+2s)/L^3` and `R=3*beta*d^2*(alpha-2s)/(P*L^3)`. Under Theorem B assumptions both are positive. The correct statement is

\[
 m'(0)=D-\mathcal L,\qquad
 \mathcal L=C(2u'+v')+R(u'+v').
\]

The printed expression instead gives `L_printed=C(2u'+v')-R(u'+v')`. At the baseline this is approximately `-.00463730487`, whereas the intended loss is `+.01506974413`. Consequently `0<D<L_printed` does not hold at the claimed witness. Classify the printed theorem C as **FAILED**, and the corrected conditional theorem as **PROVED — ANALYTIC**, subject to actual Nash-continuation assumptions below. Retain the old expression as historical evidence rather than silently editing it.

## 1. A genuinely independent quantity derivation

Let the three off-diagonal elements of the symmetric Cournot matrix be `A=m_AB`, `B=m_AC`, `C=m_BC`, and its common diagonal be `alpha`. Cramer's rule gives

\[
 \Delta=\alpha^3-\alpha(A^2+B^2+C^2)+2ABC,
\]
\[
 q_A=d\frac{(\alpha-C)(\alpha+C-A-B)}{\Delta},\quad
 q_B=d\frac{(\alpha-B)(\alpha+B-A-C)}{\Delta},\quad
 q_C=d\frac{(\alpha-A)(\alpha+A-B-C)}{\Delta}.
\]

This follows from the original Cournot FOC holding expected use fixed, then imposing fulfilled expectations: `(I+B_demand-eta H)q=d1`. It is not a derivative of a consumer's fulfilled-expectations objective. It independently yields `q=dM^{-1}1`, the IS scalar quantity, and SU quantities in PR #9.

For arbitrary parameters, invertibility alone is insufficient: one must require positive quantities and uniqueness of the nonnegative quantity equilibrium. A convenient sufficient condition is `M` positive definite and all three Cramer numerators positive (since then `Delta>0`). Symmetric positive definiteness makes the associated linear complementarity problem strictly monotone, hence the nonnegative equilibrium unique. These conditions are sufficient, not necessary for uniqueness at a particular right-hand side.

A simple uniform parameter condition covering the baseline is `rho>=eta>0`, `rho<1`, `eta<1`. Then all off-diagonal entries lie in `[0,1-eta]`, and

\[
 \alpha-2(1-\eta)=\eta>0.
\]

The truncated fixed-point map maps `[0,d/alpha]^3` into itself, has sup-norm contraction factor at most `2(1-eta)/alpha<1`, and its untruncated numerators are uniformly positive. Thus all regimes, depths, and asymmetric designs have a unique interior output continuation.

The original admissible bounds `rho in (0,1), eta in [0,1)` alone do **not** imply this. At `rho=1/100, eta=99/100, IS,g=1,x=(0,0,0),d=1`, the matrix has diagonal `101/100` and off-diagonal `-98/100`. Its symmetric quantity would be `-20/19`. Since all cross effects are negative, every nonnegative fulfilled-expectations equilibrium would have all firms active; the unique linear-system solution is negative, so no nonnegative fulfilled-expectations equilibrium exists. This is a counterexample to an unconditional continuation claim, not to PR #9's conditional claims.

## 2. Unilateral derivatives and independently checked Jacobian

For `s=beta z`, `P=alpha-s`, `L=alpha+2s`, differentiating the Cramer numerator and determinant **before** imposing symmetry gives

\[
 q_{A,x_A}=-\frac{\beta d\alpha}{PL^2},\qquad
 q_{A,x_B}=q_{A,x_C}=-\frac{\beta d(\alpha-2s)}{2PL^2},
\]
\[
 q_{A,g}^{SU}=-\frac{\delta d\alpha}{PL^2},\qquad
 q_{C,g}^{SU}=\frac{2\delta ds}{PL^2}.
\]

The unilateral Nash FOC is `F_i=6q_i q_{i,x_i}+kappa(1-x_i)=0`. At the symmetric origin, full Cramer-rule symbolic differentiation independently confirms all four PR #9 formulas:

\[
 \ell=-\kappa+\frac{6\beta^2d^2(\alpha-2s)(2\alpha+s)}{P^2L^4},\qquad
 h=\frac{3\beta^2d^2(3\alpha-2s)}{PL^4},
\]
\[
 p=\frac{6\delta\beta d^2(\alpha-2s)(2\alpha+s)}{P^2L^4},\qquad
 r=\frac{6\delta\beta d^2(\alpha^2-2\alpha s+4s^2)}{P^2L^4}.
\]

**Actually executed:** a separate ephemeral SymPy program formed the full asymmetric 3-by-3 matrix, replaced columns by `d1`, calculated determinants, differentiated the resulting rational functions in the independent `x_A,x_B,x_C,g`, then imposed symmetry. The four differences from these formulas simplified to exact zero. It did not import the PR #9 verification script. An additional standard-library `Fraction` calculation verified the Cramer first/second own derivatives at the rational off-equilibrium point `alpha=621/500,beta=1/10,z=7/10,delta=71/500,d=1`.

Under `delta>0`, `alpha>3s`, and `-ell>2h`, the Jacobian is negative definite at the origin, `p>r>0`, and

\[
 u'-v'=\frac{p-r}{h-\ell}>0,
\]

while the inverse of `-F_x` is entrywise positive, giving `v'>0`. The ordering is therefore correct. It is a local derivative statement at `g=0`, not a global ordering for every depth.

**Important scope condition:** pointwise diagonal dominance certifies a locally stable stationary branch and local own second-order conditions; it does not certify uniqueness on the full asymmetric design cube. A stationary continuation must not automatically be labelled a Nash continuation. One can supply global own concavity/Rosen strict monotonicity, or strict unique global unilateral best responses at the baseline plus compactness and local second-order conditions. The frozen baseline already has the stronger global certificate. Generic versions of B/C must state the extra hypothesis explicitly.

## 3. IS comparative statics and boundary limitations

Independent unilateral differentiation yields

\[
 F(y,g)=\kappa(1-y)-\frac{6\beta\alpha d^2}{(\alpha-t)(\alpha+2t)^3},\quad
 t=\delta g+\beta y.
\]

Its implicit derivatives in PR #9 are correct when `0<y<1`, `alpha-t>0`, `alpha+2t>0`, and `K*=kappa-beta G>0`. The sign `sgn y_g=sgn delta` additionally requires `5alpha-8t>0`. These are sufficient conditions for the stated signs on the chosen smooth branch. `F_y` moves all symmetric equilibrium coordinates together; it is not the individual own-payoff second derivative. The own second-order condition and genuine Nash status must therefore be established separately.

Strict `y_kappa>0` and `y_d<0` are interior statements. A concrete boundary diagnostic is `rho=eta=9/10,d=1,kappa=1/10`. Against rivals choosing zero, a firm's own quantity after choosing `x` is

\[
 q_i(x,0,0)=\frac{d(\alpha-\beta x)}{\alpha^2-\beta^2x^2/2}.
\]

For `x in [0,1]`,

\[
 q_i\ge d(\alpha-\beta)/\alpha^2,\qquad
 q_i'\le- d\beta(\alpha-\beta)/\alpha^3,
\]

so

\[
 F_i\le\kappa-\frac{6\beta d^2(\alpha-\beta)^2}{\alpha^5}<0.
\]

Thus zero is a strict global best response and `(0,0,0)` is a boundary Nash. This branch remains constant over a nontrivial range of cost/scale parameters; strict comparative-static derivatives fail there. This result does not assert that this example has no other Nash equilibria.

## 4. Welfare bridge and edge symmetry

The Cramer derivatives imply

\[
 CS_{x_j}=-\frac{\beta d^2(\eta+2s)}{L^3},\qquad
 \Pi_{A,x_B}=\Pi_{A,x_C}=-\frac{3\beta d^2(\alpha-2s)}{PL^3}.
\]

The own-profit design derivative vanishes at an interior Nash. This proves the corrected induced-loss formula in the opening erratum. The direct fixed-design effect is

\[
 D=d^2\left[\frac{\rho}{L^2}-\frac{2\delta(1+2s)}{L^3}-\frac{6\delta\alpha}{PL^3}\right].
\]

Therefore `0<D<L_corrected` yields opposite frozen/endogenous member slopes. Differentiability turns the strict slopes into strict signs on some interval `(0,epsilon)`; it says nothing about larger positive depths.

For a smooth permutation-equivariant continuation, let the derivative of country A's payoff for one incident compatibility edge be `mu` and for the nonincident edge be `nu`. Then `m'=mu`, `o'=nu`, `i'=2mu+nu`; hence `(i-o)'=2m'`. This identity is linearity and symmetry, not a new coalition theorem. It applies to both actual and frozen-design paths provided they are smooth at the symmetric origin.

## 5. Demand feasibility is more general than the original witness

For three firms, `X` is positive semidefinite over the whole cube. It is affine in the three design coordinates, and the exact vertex determinants are:

| Number of unit design coordinates | `det X` |
|---|---:|
| 0 | 1 |
| 1 | 1/2 |
| 2 | 0 |
| 3 | 0 |

All one- and two-dimensional principal minors at each vertex are nonnegative. Convexity of the PSD cone proves the assertion for the cube. These principal minors were checked independently with exact standard-library `Fraction` arithmetic. Every regime's `H` is also PSD for `g in [0,1]`: its nontrivial blocks are equicorrelation blocks with off-diagonal `g`. Consequently `B=rho H+(1-rho)X` is PSD for **every** original admissible `rho`, independently of `eta`. The problem with unrestricted high network effects is fulfilled-expectations output feasibility, not consumer conditional concavity.

At a symmetric design `z<1`, `X=(1-z)I+zJ` is positive definite. Since `beta>0`, `B` is then positive definite even at full technical depth. Off-path endpoint semidefiniteness must not be promoted to strict definiteness.

## 6. A nonvacuous global theorem for `rho=eta`

Set `rho=eta=r in (0,1)`, `alpha=2-r`, `beta=1-r`, `d>0`. The following entirely primitive sufficient conditions make PR #9 theorem D unconditional within this stated parameter class:

\[
 \boxed{\quad
 \kappa>\max\left\{
 \frac{54\beta^2d^2}{r^2\alpha^2},
 \frac{6\beta d^2}{\alpha^3}\right\}.
 \quad}
\]

Proof:

1. `M=I+beta X` is independent of policy, with off-diagonal entries in `[0,beta]` and strict row-dominance slack `alpha-2beta=r`. The contraction argument gives positive output and `||q||_infinity<=d/alpha` throughout the asymmetric cube.
2. `||M^{-1}||_infinity<=1/r`, `||M_xi||_infinity<=beta`, and `M_xixj=0`. Therefore every second derivative of each firm's operating profit `3q_k^2` is bounded in absolute value by `18 beta^2 d^2/(r^2 alpha^2)`. The symmetric pseudo-gradient Jacobian has row upper bound at most `-kappa+54 beta^2d^2/(r^2 alpha^2)<0`. Own strict concavity, pure Nash existence, and global Rosen uniqueness follow on the full asymmetric cube.
3. Symmetry then forces a common design. The scalar FOC at zero is `kappa-6 beta d^2/alpha^3>0`; at one it is strictly negative. Continuity gives an interior stationary point, and global own concavity makes it Nash. Global uniqueness excludes all asymmetric alternatives.
4. Policy cannot change this unique private equilibrium or quantities. Every compatible edge raises each country's CS by `r g Q^2`, leaving private profits/costs unchanged. Thus `m=o=s+r g Q^2`, `i=s+3r g Q^2`.
5. For every `g>0`, C strictly prefers accession to outsider status; each incumbent prefers approval; and B prefers the anticipated IS outcome to rejection. The proposer's IS payoff is strictly increasing on the entire compact interval, so the unique positive-depth optimal economic allocation has `g*=1,IS`. Weak-affirmative tie rules handle zero-depth histories. Do not claim uniqueness of irrelevant zero-depth labels or of all off-path strategy representations.

This class is nonempty without numerical search: `r=9/10,d=1,kappa=1` has global Rosen threshold `200/363<1` and interiority threshold `600/1331<1`, checked exactly. It is a three-dimensional primitive family on the knife-edge manifold `rho=eta` inside the four-dimensional primitive space; it is not an open four-dimensional policy-transition theorem.

## 7. Classification

| Claim | Independent mathematical status |
|---|---|
| General Cournot formula | PROVED — ANALYTIC, conditional on positive unique continuation; explicit sufficient domain supplied |
| IS unilateral FOC and conditional comparative statics | PROVED — ANALYTIC; actual Nash and interiority conditions essential |
| Origin coefficients `ell,h,p,r` | PROVED — ANALYTIC; separately exact-symbolic checked |
| Member/outsider response ordering | PROVED — ANALYTIC for regular actual Nash branch; local in depth |
| Printed equation (9) / printed induced-loss condition | FAILED; rival-profit term has wrong sign |
| Corrected induced-loss reversal | PROVED — ANALYTIC under stated conditions; local only |
| `(i-o)'=2m'` | PROVED — ANALYTIC symmetry identity |
| `rho=eta` policy benchmark | PROVED — ANALYTIC on explicit sufficient primitive class above |
| Full asymmetric uniqueness for every admissible parameter | FALSE as an unqualified claim; not asserted by the frozen theorem |
| All-depth nonformation from local inequalities | UNRESOLVED in general; baseline needs its separate existing uniform certificate |

This review did not rerun the old all-depth interval certificate or independently formally verify a proof assistant. The executed exact checks concern Cramer symbolic identities, PSD vertices, rational sufficient-condition witnesses, and the listed analytic arguments. Academic priority and RIO publication importance are separate from this mathematical verdict.
