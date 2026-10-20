# V2b Stage 4 / Stage 4A bounded repair — nonlinear residual product design
**Date:** 2026-10-21 JST. **Model role:** pre-registered diagnostic alternative; **NOT a change to canonical V2b**. **Economic result:** existential coalition reversal survives a non-cosmetic change of functional form at exactly the SAME eta, rho, kappa and government agenda. The original pre-registered fixed-g=.05 prediction **REMAINS FALSE**, explicitly preserved.

## One changed assumption, specified BEFORE results
Canonical V2b cross-firm substitution: X_ij=(x_i+x_j)/2, i≠j, X_ii=1.
Alternative pre-registered in reviews/V2B_STAGE07_DESIGN_PORTABILITY_PREREG_2026-10-21.md:
\[
X_{ij}=(x_i^2+x_j^2)/2,\quad i\ne j,\qquad X_{ii}=1.
\]
All else strictly identical:
\[
a-c=1,\quad \eta=379/500,\quad \rho=9/10,\quad \kappa=1701/2000;
\quad B=\rho H+(1-\rho)X,\quad n^e=q,
\]
3 symmetric governments/countries/firms; A proposes AB g; B consent; C applies; A/B unanimously accept, IS retains same g; firms then choose costly x_i∈[0,1], pay cost κ(1−x_i)²/2 ONCE, and Cournot compete in 3 identical national markets. W_i=.5q'Bq +3q_i²−κ(1−x_i)²/2.

Quadratic design similarity is a genuine strategic alternative, not x relabeling: private cost remains quadratic in original x and a firm's marginal effect on substitution now depends on x. Technical-interface g remains independent of residual design x. X is PSD by defining z_i=x_i²∈[0,1] and convex-combining the 8 PSD Boolean additive-kernel matrices. At this witness M=I+(ρ−η)H+(1−ρ)X≽I, M_ii=1.242 and M_ij∈[0,.242], so q>0 and Cournot unique globally by sup-norm BR contraction.

## Claim ALT-4-01 — Stage 4 design continuation globally unique (PASS at exact witness)
The **separately implemented full 3-player pseudo-gradient**, without SU/IS symmetry assumptions and without imports from canonical V2b modules, is
\[
F_i(x)=6q_i(x)\frac{\partial q_i(x)}{\partial x_i}+\kappa(1-x_i),
\quad \frac{\partial q}{\partial x_i}=-M^{-1}M_{x_i}q.
\]
The symmetric part of its 3×3 Jacobian J(x,g,S) is tested for strict negative definite via outward-rounded rational-interval Gershgorin row dominance over the **entire four-dimensional cube** (x_A,x_B,x_C,g)∈[0,1]^4, separately for SW/SU/IS.
- SW: one full interval box passes.
- SU: one full interval box passes.
- IS: five accepted adaptive rational boxes after four subdivisions pass.
- Largest Gershgorin row upper bound is STRICTLY NEGATIVE in every accepted box; no missing corners or asymmetric choices.
Each firm payoff is strictly concave in own x, Nash exists on compact convex strategy sets, and Rosen diagonal strict concavity ensures a unique pure Nash at every S,g. Unlike the earlier linear-X curvature bound κ>81(1−ρ)², this is a **direct nonlinear pseudo-gradient curvature proof**; the linear-X bound is NOT reused after x² substitution.

Reproduction: verification/v2b_alt_quadratic_rosen_interval.py, independent GitHub Actions job full-space-unique-firm-nash.

## Claim ALT-4A-02 — Unique interior continuation and endogenous government no-agreement (PASS by continuous rational intervals)

Under SU symmetry, denote x_A=x_B=u, outsider x_C=v. Set
\[
A=2-\eta,\quad \beta=1-\rho,\quad
m=(\rho-\eta)g+\beta u^2,\quad n=\frac{\beta(u^2+v^2)}2,\quad
D=A(A+m)-2n^2.
\]
Then q_m=(A−n)/D and q_o=(A+m−2n)/D. **Unilateral Nash derivatives** multiply the original additive-X marginal firm substitution by 2u (member) and 2v (outsider); firms do not jointly deviate along the symmetric branch. The IS symmetric condition likewise multiplies the derivative by 2y:
\[
F_{IS}(y,g)=\kappa(1-y)-
\frac{12\beta y A}{
[A-((\rho-\eta)g+\beta y^2)]
[A+2((\rho-\eta)g+\beta y^2)]^3}.
\]

Exact-rational closed intervals certify uniform inward Nash gradient signs for all g∈[0,1], with
\[
(u,v)\in(0.60,0.67)\times(0.60,0.65),\qquad y\in(0.60,0.73).
\]
Poincaré–Miranda plus global Rosen uniqueness gives one and only one continuation at each g.

The proof next covers EVERY REAL g∈[0,1] with 100 exact rational closed cells G_j=[j/100,(j+1)/100]. Each:
1. uses a numerical SU/IS root ONLY to center a rational interval rectangle (half-width .0025);
2. certifies both SU Nash FOCs and the IS Nash FOC change sign on opposing boundaries uniformly for every g∈G_j;
3. certifies SU FOC Jacobian invertibility and IS scalar FOC nonzero derivative;
4. computes the total welfare derivative including equilibrium design responses (u',v',y') by the implicit-function theorem and proves both strict negatives throughout G_j.

Observed maximum signed outward upper bounds across the whole continuum:
\[
\sup_{g\in[0,1]}\Bigl[W_A^{SU}\,'(g)\Bigr]
< -0.0142787366,\qquad
\sup_{g\in[0,1]}\Bigl[\bigl(W_i^{IS}-W_C^{SU}\bigr)'(g)\Bigr]
< -0.0165754742.
\]
These are **conservative interval upper bounds**, not claimed exact derivatives, and the inequalities apply at endpoints as one-sided derivatives. At g=0 all S allocations/welfares coincide. Integrating proves W_A^SU(g)<W^SW and W_i^IS(g)<W_C^SU(g) for ALL g>0 in the alternative game. Hence NO positive-depth government coalition is sequentially realized under the canonical AB-first/C-application protocol, notwithstanding uniquely determined firm continuations.

Reproduction: verification/v2b_alt_quadratic_policy_interval.py. Independently rederives quadratic-X SU/IS FOCs and welfare, interval-faces and continuous government derivative signs. This reuses mpmath/SymPy as a trusted arithmetic kernel and is **NOT a proof-assistant formal theorem** or a fully blinded human audit.

## Claim ALT-4A-03 — frozen-design positive-depth IS EXISTS (PASS; NOT at original g=.05)

The original preregistered test **FROZEN C acceptance at g=.05** is strictly **FAILED**:
\[
I_{\rm frozen}(.05)-O_{\rm frozen}(.05)\approx-0.0004403948<0.
\]
Do not re-label the original test as PASS or claim the preferred international standard has the same feasible compatibility depth as under additive X.

The prior pre-registered ALL-g exploratory screen also found positive C acceptance near g=.005. A new proof checks EXACT g=1/200 (not changing any *primitive* coefficient):
- SW unique design x_SW≈0.610737479601, bracketed by rational bounds with opposite firm FOC signs;
- Holding every x_i fixed at this SAME SW Nash design across government histories, at g=.005,
\[
I_{\rm frozen}-O_{\rm frozen}>9.09880904\times10^{-7}>0,
\]
\[
I_{\rm frozen}-W^{SW}>0.0020414954>0,\qquad
I_{\rm frozen}-M_{\rm frozen}>0.0020392100>0.
\]
- 4,000 exact rational g intervals G=[j/4000,(j+1)/4000] give
\[
\sup_{g\in[0,1]}W_{A,\rm frozen}^{SU}(g)
<2.59626921
<2.59815981
<I_{\rm frozen}(g=.005).
\]
Every possible SW/SU government deviation is inferior to this feasible IS; C applies and A/B approve at the same g. Weak acceptance at indifference ensures existence of a globally optimal feasible positive IS Stage-1 agreement.

**Interpretation:** the preregistered *fixed-depth margin* is fragile, but the substantively promised EXISTENTIAL regime reversal is independently certified for another valid positive depth that was identified before this confirmatory audit. No function/parameter tuning followed the failed test. Because the C acceptance gain is ~10^-6, the quantitative open parameter neighborhood may be VERY SMALL; its size is not estimated.

## Claim ALT-4A-04 — welfare-positive but inaccessible IS survives (PASS)

With firms freely reoptimizing in IS at exactly g=1/20=.05, opposite-sign FOC intervals bracket the unique IS design; the national welfare difference is strictly
\[
W_i^{IS}(.05)-W^{SW}\approx+0.016601147>0,\quad\forall i\in\{A,B,C\}.
\]
The globally certified coalition conditions in ALT-4A-02 nevertheless make this grand compatibility outcome unattainable as an SPNE agreement in the AB-first extensive game. This is a **hypothetical Pareto improvement**, not a policy instrument, first-best or actually observed historical outcome.

Illustrative solver calculations (not needed for mathematical proof):
- SW x≈.610737479601, W≈2.596118318275;
- SU(.05) x_members≈.61349696, x_out≈.61222337, W_members≈2.595101864508, W_out≈2.615125624285;
- IS(.05) x≈.617707153937, W_i≈2.612719465379;
- frozen IS(.005) W≈2.598159813702; frozen C-as-SU-outsider W≈2.598158903819.

## Novelty and claim-scope boundaries
- **Proven model-family comparison:** p=1 (canonical additive X) and p=2 (one pre-registered nonlinear X), same government game and SAME parameter witness, exhibit **EXISTENTIAL** frozen-IS versus endogenous-no-coalition reverse result and positive hypothetical IS welfare.
- **NOT PROVEN:** every continuous p∈[1,2]; general forms phi; all (eta,rho,kappa), general bargaining agendas, endogenous installed-base network utility, joint regulatory/adoption decisions, a real ChaoJi/GSM country refusing accession because of post-standard design.
- Earlier full-g canonical Stage4A certification is a **separate experiment**, not mechanically transferred by substituting x² into old welfare.
- Academic-theorem priority remains source-bounded to the previously checked Cabral–Salant, Buchholz–Hattori, Gandal–Shy, Takarada etc. The generic innovation/cooperation paradox and symmetric marginal C=2×member identity are **known ingredients**.
- Original g=.05 robustness failure is preserved as first-class negative evidence and does not contradict the narrower existential proposition.

## Stage-gate route
**Stage 4 alternative-model math: GO (restricted witness, full strategy domain).**
**Stage 4A alternative-model continuous proof: GO (computer-assisted, two separated scripts, with trusted-arithmetic-kernel limitation).**
These are bounded diagnostic extensions and do not replace frozen V2b primitives. Recheck Stage 6 prior-art scope, Stage 7 welfare, and Stage 7.5 contribution completeness. Stage 7.5A can be authorized only if Stage 7.5 independently issues GO after evaluating the narrower *existential* claim and numerical fragility. Any eventual theory freeze requires the separate Stage-7.5A formal verification applicability/pass and portability attack, not just this result.

**Proof files:** verification/v2b_alt_quadratic_rosen_interval.py and verification/v2b_alt_quadratic_policy_interval.py.
**CI:** .github/workflows/v2b-alt-quadratic-certificate.yml, run https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39516205888 .
