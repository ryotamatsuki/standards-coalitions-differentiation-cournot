# V2b: continuous-depth coalition-regime reversal — computer-assisted certificate

**Date:** 2026-10-21. **Status:** Strict rational-interval enclosures for the full continuum \(g\in[0,1]\) at one parameter witness; **NOT peer-reviewed, NOT a theory freeze, NOT a novelty claim**. A separately runnable source and CI are provided; independent reproduction and examination of the interval implementation are necessary before using this as a formal manuscript proof.

## Main result (conditional on the documented model and computational certificate)

For
\[
(a-c,\eta,\rho,\kappa)=\left(1,\frac{379}{500},\frac9{10},\frac{1701}{2000}\right)
=(1,0.758,0.900,0.8505),
\]
with fixed SU depth inherited by IS, zero standards-adoption costs, identical countries, three Cournot firms, and *additive* residual homogeneity \(X_{ij}=(x_i+x_j)/2\):

**Endogenous design.** Every strictly positive proposed integration depth \(g>0\) leads C to prefer remaining outside SU. Conditional on SU, both A and B prefer SW to any strictly positive SU depth. Hence there is **no positive-depth agreement in a subgame-perfect outcome**. At \(g=0\), formal SU/IS membership is payoff-equivalent to SW and depends on tie conventions.

**Counterfactual frozen design.** Holding all \(x_i\) fixed at the SW Nash design, \(g=1/20\) gives strictly mutually acceptable positive-depth IS. Its proposer benefit exceeds SW and **every possible SU member payoff** across the entire policy domain \(g\in[0,1]\). Under accession/approval at indifference, the frozen-design government's optimal agreement must therefore involve **positive-depth IS**, even though this note does not analytically identify its maximizing \(g\).

This establishes an actual *coalition-outcome reversal* between an endogenous-design game and its frozen-design counterfactual, subject to validity of the reproducible interval certificate. It does **not** establish SU existence, global comparative statics, or a novel theorem relative to prior literature.

## Formal stage structure and objective

- Stage 1: A proposes SU(AB) and depth \(g\in[0,1]\); B accepts or rejects (SW).
- Stage 2: C decides whether to apply.
- Stage 3: A/B accept C unanimously, with no g renegotiation.
- Stage 4: firms simultaneously choose \(x_i\in[0,1]\); design cost \(\kappa(1-x_i)^2/2\) is paid once per firm, **not once per sales market**.
- Stage 5: in each of three identical country markets, firms play Cournot. At fulfilled network expectations, \(M q=\mathbf1\), where \(M=I+(\rho-\eta)H+(1-\rho)X\).
- National welfare \(W_i=\frac12 q^\top Bq+3q_i^2-\frac{\kappa}{2}(1-x_i)^2\); \(B=\rho H+(1-\rho)X\).

## Why Stage 5 is globally well-posed at the witness

- \(H\) and \(X\) are PSD for every admissible coalition and design vector (including additive \(X_{ij}=(x_i+x_j)/2\)).
- As \(\rho>\eta\), \(M=I+(\rho-\eta)H+(1-\rho)X\succeq I\).
- All M offdiagonal entries lie in \([0,0.242]\), while its diagonal is \(\alpha=2-\eta=1.242\).
- All Cournot best responses satisfy \(0\le q_i\le1/\alpha\). On the cube \([0,1/\alpha]^3\), the network-consistent simultaneous BR map
  \[
  T_i(q)=\frac{\max\{0,1-\sum_{j\ne i}M_{ij}q_j\}}{\alpha}
  \]
  is a contraction in sup norm, with Lipschitz constant \(\le 2(0.242)/1.242<1\). Moreover, the untruncated expression is strictly positive on the entire cube. Therefore a **unique strictly interior quantity equilibrium** exists for every firm-design and policy history.

## Why Stage 4 has a unique pure Nash equilibrium

For all designs, \(\|M^{-1}\|_2\le1\), \(q\) has norm at most \(\sqrt3\), and \(\|\partial M/\partial x_i\|_2=(1-\rho)/\sqrt2\). Differentiating \(q=M^{-1}\mathbf1\) twice gives a uniform bound
\[
\left|\frac{\partial^2(3q_i^2)}{\partial x_i\partial x_j}\right|
\le 27(1-\rho)^2=0.27
\quad \text{for any }i,j.
\]
Hence the symmetric part of the Stage-4 profit-gradient Jacobian is strictly negative definite by row-diagonal dominance if
\[
\kappa>81(1-\rho)^2=0.81.
\]
Here \(\kappa=0.8505>0.81\). Own payoffs are strictly concave; compact convex action sets imply Nash existence (standard concave-game theorem), and diagonal strict concavity implies uniqueness (Rosen criterion). In SW/IS the unique equilibrium is symmetric across all firms; in SU firms 1,2 are symmetric and outsider 3 may differ.

## SU continuation: reduce to a two-variable Nash system

Set \(\alpha=2-\eta\), \(\beta=1-\rho\) and
\[
m=(\rho-\eta)g+\beta u,\quad n=\beta(u+v)/2,\quad
D=\alpha(\alpha+m)-2n^2.
\]
Then \(q_1=q_2=Q_M=(\alpha-n)/D\) and \(q_3=Q_O=(\alpha+m-2n)/D\).
Define each firm's partial design gradient (with its own unilateral design variation, not a joint variation of u) as \(F_M(u,v,g)\) and \(F_O(u,v,g)\). The interval program constructs them from inverse Cournot demand, sets \(F_M=F_O=0\), and uses the implicit function theorem:
\[
\binom{u'}{v'}=-\begin{pmatrix}F_{M,u}&F_{M,v}\\F_{O,u}&F_{O,v}\end{pmatrix}^{-1}
\binom{F_{M,g}}{F_{O,g}}.
\]
All government welfare derivatives **include** endogenous \(u'(g),v'(g)\).

### Machine-checked SU uniform statements

The rational interval program checks the inward-pointing Poincaré–Miranda signs on the four faces of
\[
(u,v)\in[0.7,0.8]^2,\qquad g\in[0,1]
\]
for all g, using 40×80 exact rational cells for each relevant face. Uniform signed face ranges (conservative interval union) are:
\[
F_M(0.7,v,g)\in[0.01078,0.05818],\
F_M(0.8,v,g)\in[-0.06849,-0.02281];
\]
\[
F_O(u,0.7,g)\in[0.00791,0.04508],\
F_O(u,0.8,g)\in[-0.07378,-0.03717].
\]
The Poincaré–Miranda theorem and Stage-4 uniqueness give a unique differentiable SU equilibrium inside the rectangle at every g.

Next, adaptively subdividing \([0.7,0.8]^2\times[0,1]\) into exact rational boxes and applying *outward-rounded interval arithmetic* to the **total derivative** of SU member welfare gives
\[
\boxed{\frac{dW_A^{SU}(g)}{dg}<0\quad \forall g\in[0,1].}
\]
One archived run accepted 6,016 certified boxes after 6,015 subdivisions; the largest outward interval upper bound was \(-1.5733\times10^{-7}\). These counts are implementation-dependent; use the committed source/CI output as verification authority. Since \(W_A^{SU}(0)=W^{SW}\), \(\boxed{W_A^{SU}(g)<W^{SW}}\) for every strictly positive g.

## International accession: globally negative C marginal joining gain

Let \(I(g)=W_i^{IS}(g)\), \(O(g)=W_C^{SU}(g)\). IS design equilibrium satisfies its scalar unilateral Nash FOC:
\[
F_I(y,g)=\kappa(1-y)-
\frac{6(1-\rho)(2-\eta)}{
[(2-\eta)-((\rho-\eta)g+(1-\rho)y)]
[(2-\eta)+2((\rho-\eta)g+(1-\rho)y)]^3}=0.
\]

For 100 initial rational intervals partitioning \([0,1]\), and adaptively refined subsets, the certificate chooses numerical root approximations **only to center enclosure boxes**. At every g interval, exact interval evaluations verify:
- the inward Nash-gradient signs on each face for \((u,v)\) and IS design \(y\);
- nonsingularity of SU's 2×2 Jacobian and IS's scalar FOC derivative;
- the strict inequality
  \[
  \boxed{\frac{d}{dg}[I(g)-O(g)]<0\quad\forall g\in[0,1].}
  \]
The largest outward upper bound in one run was about \(-0.016144\), over 1,823 passing intervals after 1,723 subdivisions. Since \(I(0)-O(0)=0\), \(\boxed{I(g)<O(g)}\) for all \(g>0\). Hence C declines to join at every positive depth.

The interval containment tests and global Stage-4 uniqueness are what turn the check into a **continuous-g certificate**; the numeric root finder is *not* trusted as a proof.

## Frozen design: strict positive-depth IS alternative

The SW design satisfies \(y^*\in[0.71859270731,0.71859270734]\), certified by opposite signs of the exact SW FOC at rational endpoints and Stage-4 uniqueness.

Holding \(x_i=y^*\) fixed, interval evaluation at \(g=1/20\) gives strict margins:
\[
I(0.05)-O(0.05)>0.0002346166,\quad
I(0.05)-M(0.05)>0.01904623,\quad
I(0.05)-W^{SW}>0.01931861.
\]
50 rational subintervals covering \(g\in[0,1]\) give
\[
\sup_{g\in[0,1]}M_{\rm frozen}(g)
<2.433100
<2.441397
<I_{\rm frozen}(0.05).
\]
Thus positive-depth IS is individually rational for C, acceptable to A/B, and dominates the payoff from any SU policy (as well as SW). With the stipulated admission-at-indifference tie convention, the Stage-1 optimal regime in the **frozen counterfactual** must be IS at some positive g; a fine-grained numeric optimizer puts its C cap near \(g=0.077435193\), but that exact value is not needed for the existence/reversal proof.

## An open parameter region, not just an isolated numerical curiosity

Stage-4 uniqueness (\(\kappa>81(1-\rho)^2\)), SU root-face signs, the strict uniform derivatives, and the fixed-design participation/payoff margins all have strictly positive slack at the exact rational witness. By continuity of reduced-form payoffs and their derivatives over the compact policy domain, these strict inequalities persist in a sufficiently small open neighborhood in \((\eta,\rho,\kappa)\). This establishes a **nonempty open parameter region** of the same substantive regime reversal.

Its quantitative size has **not** been certified. Do not assert economically broad robustness or genericity.

## Reproduce and limitations

\`\`\`bash
python -m pip install -r verification/requirements_v2b_interval.txt
python verification/v2b_interval_reversal_certificate.py
\`\`\`

See \`verification/v2b_interval_reversal_certificate.py\` and its dedicated GitHub Actions check.

**Methodological limits:** This is a computer-assisted inequality proof relying on correctness of (i) the displayed economic algebra, (ii) SymPy-generated expressions, (iii) mpmath's outward-rounded arbitrary-precision interval arithmetic, and (iv) the stated game-continuation theorems. No independent proof-assistant formalization, journal referee review, theory freeze, or theorem-by-theorem originality audit has been completed. Do not generalize the particular witness to all parameters.

Related earlier exploratory record: \`docs/V2B_REGIME_REVERSAL_NUMERICAL_WITNESS_2026-10-21.md\`, which was **only a finite-grid conjecture**. This continuous certificate supersedes its previous unresolved proof status, but preserves that log for research provenance.
