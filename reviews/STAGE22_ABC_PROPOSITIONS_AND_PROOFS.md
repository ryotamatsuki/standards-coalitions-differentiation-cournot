# Stage22 — Three linked propositions A / B / C, before any manuscript revision

**Scope and verdict:** A and B are proved on a **certified nonempty OPEN neighborhood** of the original V2b canonical primitive vector, contingent only on the already-executed Stage14 uniform Krawczyk/Rosen certificates. B also has a clean general **LOCAL** sufficient-condition proof independent of that vector. C has (i) a **unique LOCAL** design-friction threshold at the canonical vector and a certified full-game IS outcome at lambda=5; (ii) a **global analytic** SW/IS switch at network threshold eta=6/7 on the limiting rho=1 family and a genuine endogenous-design local strip near that boundary (Stage21 proof). NO single unrestricted global primitive-region theorem for arbitrary eta,rho,kappa,d; NO general claim that all lambda>lambda_c select terminal IS; no publication priority claim.

## 0. Original game; distinct firms/governments; labels and admissibility

Three countries A,B,C and one firm per country, each selling into three symmetric markets. Policy link matrix H has H_ii=1, and offdiagonal H_ij=0 under SW, H_AB=H_BA=g under bilateral SU(AB), and all offdiagonal H_ij=g under IS. Residual design x_i∈[0,1], X_ij=(x_i+x_j)/2 for i≠j and X_ii=1. Define
 B=rho H+(1-rho)X, M=I+B-eta H,
 alpha=2-eta, beta=1-rho, delta=rho-eta.
Conditional consumer quadratic utility is integrable, consumers form fixed expectations during Cournot deviation and fulfilled expectations after, so M q=d 1. At positive interior Cournot q, p_i-c=q_i. Country welfare and profit are
 CS=(1/2)q'Bq,
 Pi_i=3q_i²-K_i(x_i), W_i=CS+Pi_i,
 K_i=kappa(1-x_i)²/2 + lambda(x_i-z)²/2.
The ORIGINAL model is lambda=0. With lambda>0, the reference z is the original SW Nash, fixed across policy histories and across changes in lambda.

The national benchmark s=W_A^SW=W_B^SW=W_C^SW; SU payoffs m=W_A^SU=W_B^SU, o=W_C^SU; IS payoff i=W_A^IS=W_B^IS=W_C^IS, each evaluated at its actual 3-firm design Nash and Cournot equilibrium at g. At g=0 all four equal s.

The government negotiation **protocol matters**: A offers bilateral AB at inherited depth g∈[0,1], B votes anticipating C's later accession at the SAME g; C and incumbents can veto accession; all vote yes when indifferent. IS at depth g iff i(g)>=max{s,o(g),m(g)}. Terminal SU iff m(g)>=s and an enlargement vote strictly fails (i(g)<o(g) or i(g)<m(g)). All other cases are SW. A chooses g optimizing actual terminal payoff; a conditional allocation comparison alone is never an SPNE proof.

Maintained mathematical regularity: positive Cournot quantities, unique full 3-firm Nash in x (not just a stationary symmetric root), smooth continuation in all three policy regimes; for global open-neighborhood A additionally **uniform** full-cube Rosen margins and strict global derivative certificates over every g∈[0,1].

## Lemma 1 (permutation-edge incidence; exact and primitive-free)
At g=0, introduce three independently small compatibility edges e_AB,e_AC,e_BC. The country payoffs after firms' equilibrium responses are C¹ in e. Because the three countries are symmetric at zero and firms' Nash is unique, permutation equivariance implies two real numbers mu and nu such that the marginal effect of an incident edge on a country's reduced welfare is mu and the marginal effect of a nonincident edge is nu. Consequently, along the SU_AB one-edge path
 m_g(0)=mu, o_g(0)=nu,
while along the common-IS three-edge path
 i_g(0)=2mu+nu,
 [i(g)-o(g)]_g|0=2mu,
 [i(g)-m(g)]_g|0=mu+nu.
Proof: take derivatives along the sum of independent edge directions and count which two edges touch a given country. The same identities hold for endogenous x and restricted/frozen x and for lambda>=0 whenever the equilibrium is unique/smooth. **This is a symmetry/envelope lemma, not a new discovery or a global vote equivalence.**

## Lemma 2 (the national incidence lost through endogenous residual design)

At original SW take true symmetric root z:
 kappa(1-z)=6 beta alpha d²/[(alpha-t)L³],
 t=beta z, P=alpha-t, L=alpha+2t, q0=d/L.
For fixed design, an AB edge changes the fulfilled Cournot matrix by delta, leading to a national SU member partial welfare slope
 D= rho*d²/L² -delta*d²*(2*(1+2t)/L³+6*alpha/(P*L³)).
The frozen outsider slope is
 nu_F=rho*d²/L²-delta*d²*2*(1+2t)/L³ +12*delta*d²*t/(P*L³).
Derivation: at fixed x, R=M^{-1}=(I-(t/L)11')/P and M_g q0=delta*q0*(1,1,0)'; hence
 q_m,g=-delta*alpha*q0/(P L),
 q_o,g=2delta*t*q0/(P L),
 CS_g=rho*q0² -2delta*(1+2t)*q0²/L;
 member profit slope=6q0 q_m,g; outsider slope=6q0 q_o,g.

For ENDO design define the correctly differentiated **unilateral** pseudo-gradient F_i=∂Pi_i/∂x_i, J=F_x, f=F_g. Then x_g=-J^{-1}f, including rivals' reaction, rather than treating all x as a social planner choice.

At SW, the derivatives of country-A welfare with respect to each design, using its OWN FOC, are
 W_A,x_A=-C, W_A,x_B=W_A,x_C=-(C+V),
 C=beta*d²*(eta+2t)/L³,
 V=3beta*d²*(alpha-2t)/(P L³).
Under SU_AB symmetry x_A'=x_B'=u', x_C'=v'. Therefore

 mu_N=m_g(0)=D - ℒ,
 ℒ=C(2u'+v')+V(u'+v').

This is the correct **PLUS** rival-profit incidence, not the historical PR#9 sign error. When beta>0, rho>eta, firms' pseudo-gradient is regular, and C,V,u',v'>0, ℒ>0. The sufficient *local participation reversal* is
             0<D<ℒ.
Then mu_F=D>0 but mu_N=D-ℒ<0, and by Lemma1 the outsider joining slope also flips from 2D>0 to 2mu_N<0.

At the original canonical theta0=(d,eta,rho,kappa)=(1,379/500,9/10,1701/2000), z≈.718592707322111, exact Fraction-root brackets imply
 D≈.0067679241288,
 ℒ(0)≈.0150697441253,
 mu_N≈-.0083018199964,
 nu_N≈+.367866966,
 (2mu_N+nu_N)≈+.351263326.
The fixed-design outsider edge slope nu_F≈+.385953180. Thus frozen and endogenous grand direct gains are both locally positive despite the bilateral veto flipping.

**Lemma 2 proof detail:** differentiating CS=q'Bq/2 including B_x and q_x, and differentiating the exporting home firm's 3q_A², yields the stated C and V. The own firm's private FOC cancels ONLY its own optimized profit derivative (NOT the consumer term and not rival firms' changes to its worldwide profit). Chain rule supplies ℒ.

## Proposition A (endogenous product design creates otherwise absent fragmentation)

**A-local, general sufficient-condition form.** Suppose the center is interior, regular, beta>0, rho>eta, positive C,V and SU firm responses, and
 0<D<ℒ, nu_N> -2mu_N, nu_F> -D.
Then, for all sufficiently small positive depths:
1. Frozen firms: m_F(g)>s, i_F(g)>o_F(g), i_F(g)>m_F(g), i_F(g)>s; hence the bilateral-first government procedure ACCEPTS a positive IS offer.
2. Endogenous firms: m_N(g)<s and i_N(g)<o_N(g), so the bilateral-first procedure ends SW at such depths, while actual i_N(g)>s (Pareto-improving conditional grand allocation).

**Proof.** Lemma1 yields m_F'=D>0, (i_F-o_F)'=2D>0, (i_F-m_F)'=D+nu_F>0, i_F'=2D+nu_F>0. For ENDOG mu_N<0, (i_N-o_N)'=2mu_N<0 and i_N'=2mu_N+nu_N>0. All level differences vanish at g=0, so continuity and first-order Taylor expansion turn each strict derivative into the corresponding strict level inequality on some (0,epsilon). QED.

**A-global, nonempty OPEN primitive set.** At the canonical theta0, the independently executed Stage14 parameter-interval Krawczyk all-g certificate establishes
  m_N,g(g)<-0.0079701929973,
  [i_N(g)-o_N(g)]_g<-0.0150388833377
for ALL g∈[0,1], as reported by its strict global *upper* derivative enclosures. Since both gaps equal zero at g=0, integration yields m_N(g)<s and i_N(g)<o_N(g) at every g>0. No positive-depth original bilateral-first offer survives: terminal **SW is the SPNE regime**.

In the *same original primitives/agenda/demand/costs* but with x_i fixed to SW level z at all subsequent histories, Stage14's exact all-depth benchmark has at g=1/20:
  outsider accession i_F-o_F>0.000234616623,
  i_F(g)>2.4413970373,
  s<2.4220784218,
  sup_{g∈[0,1]}m_F(g)<2.4235735642.
The fixed-design IS offer is accepted (incumbent comparison strict too) and outperforms **every** terminal SU and SW offer. Weak-acceptance and compactness imply an optimal positive IS governmental proposal. Meanwhile actual i_N(1/20)-s>0.0169346278736 by the exact Pareto certificate: a hypothetical grand pact remains Pareto-improving even when the original path is obstructed.

These exact strict inequalities plus a **uniform** Rosen/positive-output Jacobian margin survive on a common OPEN neighborhood U of theta0 in the FULL original (d,eta,rho,kappa) coordinates. Proof: compactness of g∈[0,1] plus the strict global derivative margins gives uniform negative differences after parameter perturbation, including g→0; a finite-cover IFT and maximum theorem preserve smooth interior Nash, strict frozen acceptance, and the positive frozen-IS-to-global-SU-envelope gap. Consequently the **A-global conclusion holds on nonempty open U**, not just on one isolated numerical calibration. The size of U is existential, not an explicit rectangular primitive box. No claim for all admissible parameter values.

## Proposition B (the institutional outside option, not inefficiency alone, blocks cooperation)

**B-local, general sufficient condition.** If the original fully optimized firm design continuations satisfy
           mu_N<0<2mu_N+nu_N,
then for every sufficiently small g>0:
- original AB-first/inherited-depth procedure yields SW (B refuses eventual SU since m_N(g)<s, and C refuses to enlarge since i_N(g)<o_N(g));
- a **DIRECT grand offer** at the *same g*, with each country comparing i_N(g) to SW s and no intervening SU outside option, is UNANIMOUSLY acceptable and yields the strictly Pareto-improving IS allocation.

**Proof.** The first statement follows from Lemma1 and negative m and outsider margins; the second from i_N,g(0)=2mu_N+nu_N>0 and i_N(0)=s. A direct IS offer's acceptance does NOT require i>=o, since the terminal outside option in this different game is SW. Both bargaining procedures use the SAME actual equilibrium firms and the same B,M,K and policy depth; only the extensive-form available proposal/rejection paths differ. QED.

**B-global at canonical theta0.** A-global rules out all positive bilateral-first offers at any g. Stage14 exact intervals at g=.05 imply i_N(.05)>s by at least .0169346278736. Hence if direct IS offers may instead be made, some strictly accepted grand proposal exists, and it strictly dominates SW and every terminal SU alternative under the original payoffs. Under a compact weak-acceptance menu an optimal direct grand offer is attained and is substantive. **This proves an institutional outcome reversal at the same original primitives**, NOT that direct-grand availability always solves the problem for arbitrary theta.

One *cannot* infer a general result for transfers, renegotiation, different coalition formation protocols, noncooperative deviations by multiple governments, or coalition-proof stability. Those are unmodeled extensions.

## Lemma 3 (private-design adjustment sensitivity)

Fix original theta0; use legacy SW Nash z FIXED for all lambda>=0 in K_i. At SW, pseudo-gradient Jacobian of the original design game has diagonal ell and uniform offdiagonal chi, while AB edge-policy forcing is f=(p,p,r), with (d² factors included)
 ell=-kappa+6 beta² d²(alpha-2t)(2alpha+t)/(P² L⁴),
 chi=3 beta² d²(3alpha-2t)/(P L⁴),
 p=6 delta beta d²(alpha-2t)(2alpha+t)/(P² L⁴),
 r=6 delta beta d²(alpha²-2alpha*t+4t²)/(P² L⁴).
At the theta0 certified root, ell<0, chi,p,r>0, and -ell>2chi. For every lambda>=0, define A_l=lambda-ell and Delta_l=(A_l+chi)(A_l-2chi)>0.
Then, solving -J(lambda) x_g=f gives
 u'_lambda=(A_l*p+chi*r)/Delta_l,
 v'_lambda=(2chi*p+(A_l-chi)*r)/Delta_l.

Proof: reduce the symmetric 3x3 system
 (A_l-chi)u'-chi*v'=p,
 A_l*v'-2chi*u'=r;
apply Cramer's rule and factor the determinant.

The matrix Q_l=-J(0)+lambda I is a strictly diagonally dominant nonsingular M-matrix, Q_l^{-1}>0 componentwise. Consequently
 rvec_l=Q_l^{-1} f>0,
 (drvec_l/dlambda)=-Q_l^{-2}f<0 componentwise.
Since C,V>0 and ℒ(lambda)=C(2u'_lambda+v'_lambda)+V(u'_lambda+v'_lambda), ℒ is continuous STRICTLY DECREASING from ℒ(0)>D>0 to 0 as lambda→infinity.

## Proposition C1 (a UNIQUE local primitive threshold that restores agreement feasibility)

At fixed original theta0, with lambda as the sole added original-architecture adjustment-cost curvature and legacy z held fixed, there exists exactly one lambda_c>0 solving
       ℒ(lambda_c)=D.
Further,
 0<=lambda<lambda_c => mu(lambda)<0, **no positive-depth offer sufficiently near g=0** is accepted under the original inherited-depth government protocol;
 lambda>lambda_c => mu(lambda)>0, and **every sufficiently small positive-depth IS offer** has positive initial B approval, positive outsider accession and positive incumbent widening votes, with i_lambda(g)>s. Therefore the government can attain positive welfare strictly above SW. (It need not choose IS rather than terminal SU at some other g without an additional global envelope comparison.)

**Proof.** Lemma3 plus intermediate value theorem and strict monotonicity gives the unique lambda_c. Lemma1 gives outsider accession derivative 2mu(lambda), so the same threshold reverses both the initial bilateral-member margin and C's joining margin. At theta0 the outsider welfare response nu(lambda) is positive for all lambda≥0: it is the frozen positive direct term minus a positive-weight function of the firm reactions, which are strictly decreasing, and nu(0)>0. Thus for lambda>lambda_c, i'=2mu+nu>0 and i'-m'=mu+nu>0; along with mu>0 and i'-o'=2mu>0 all government votes accept for small g. With lambda<lambda_c the member and outsider margins have negative derivatives, precluding positive small-depth union. At equality first derivatives vanish, so SECOND-order conditions remain necessary; no regime is assigned at exactly lambda_c.

Original exact Fraction interval tests enclose
         0.93538 < lambda_c < 0.93539.
Independent root algebra gives lambda_c≈0.935389039955848.
Additional, separately certified GLOBAL results: for all lambda sufficiently near 0, SW persists at every g by uniform strict Stage14 margins; at lambda=5, Stage17/18 prove unique government-optimal IS at 0.05433320681<g*<0.05433320682, with C weakly indifferent at the terminal offer. **Do not** infer that lambda_c is the global SW/IS regime threshold for every lambda: it is a local-origin vote threshold.

## Proposition C2 (network externality produces an exact global SW/IS cutoff on a controlled family)

On the **rho=1 LIMIT FACE**, beta=1-rho=0 and x_i=1 in every government history; the private design margin is NOT strategic on that face. Keeping original d>0, kappa>0, lambda=0 and eta∈(0,1), set
 theta_N=(1-eta)/(2-eta), D_N=d²/(2-eta)².
Exact Nash national payoffs:
 s=(9/2)D_N;
 m(g)=D_N[(4+g)/(1+theta_N*g)^2+1/2];
 o(g)=D_N[(1+g)/(1+theta_N*g)^2+7/2];
 i(g)=D_N[(9/2+3g)/(1+2theta_N*g)^2].
Thus
 m(g)-s=D_N*g*[1-8theta_N-4theta_N²*g]/(1+theta_N*g)^2.
For eta<=6/7 (theta_N>=1/8), this is negative at every g>0 and i(g)-o(g)<0 at every g>0 by the exact positive-polynomial certificate in Stage21. Hence original government outcome is SW.

For eta>6/7 (0<theta_N<1/8), choose h=min{1,2(1-8theta_N)}>0. Stage21's exact rational polynomial inequalities prove i(h)>s and i(h)>o(h), i(h)>m(h), and i(h)>sup_{all g∈[0,1]}m(g). Therefore an accepted grand proposal beats every SU and SW alternative; IS is the government-optimal terminal regime. This is a complete TRUE global regime classification on the rho=1 limiting family with **no SU** and an exact eta cutoff 6/7.

**Endogenous-design extension (Stage21):** for any compact eta interval strictly inside (0,1) straddling 6/7, and fixed d,kappa>0, there is a rho_bar<1 and a smooth implicit eta_c(rho) with eta_c(1)=6/7 such that for rho_bar<rho<1 (so beta>0 and firms ACTUALLY redesign strategically), the same SW-versus-IS and absent-SU classification survives. The proof uses strong-monotonicity/IFT at beta=0, uniform strict margins away from eta_c and a quadratic Taylor argument near the transition, where m-s and outsider joining payoff are negative of order g² at the critical point and the accepted grand gain is first-order in the positive marginal perturbation. See Stage21 exact proof; eta_c(rho) is NOT generally equal to 6/7 and no explicit formula is yet available. This does **not** cover arbitrary rho or cost ratios.

## Proposition hierarchy and publishability warnings

- A core *causal reversal* and B protocol boundary should be combined in ONE main theorem with Lemma1 and Lemma2. Their general local assumptions use mu,nu and are not an unconditional all-primitive SPNE classification. The separately certified all-depth theta0 + open-neighborhood statement supplies a genuine equilibrium-type result; no explicit neighborhood radius exists.
- C1 is a separate adjustment-cost-extension threshold, NOT a new universally established cost-of-standards economic law. A and B require no extra cost at all; C1 lambda is ONE established extension, not introduced to manufacture A.
- C2 is a useful network-strength global taxonomy and open endogenous-design strip, but on rho=1 itself x_i=1 so no active private design; do not pitch rho=1 as evidence of design-caused SW.
- None of A,B,C is uniquely novel by virtue of using symmetric Cournot / network effects / no-standard SPNE. The integrated national participation sign reversal, actual grand Pareto gain and controlled alternative agenda are the candidate increment relative to Lambertini–Rossini, Barrett–Yang, Cabral–Salant, Klimenko, Costinot, Grossman–McCalman–Staiger, Gandal–Shy, Takarada–Kawabata and Cheng–Huang. Closest full final paper gaps persist.
- A possible strong abstract phrasing: "When technical standards are negotiated bilaterally before potential accession, post-agreement privately optimal residual product repositioning can reverse member and outsider consent incentives, prevent every positive-depth agreement, and sustain fragmented subgame-perfect outcomes even though a direct multilateral agreement strictly Pareto-improves on fragmentation. An adjustment-cost threshold and a network-intensity phase theorem identify when the impediment disappears." State region and agenda limitations immediately.

References within THIS repo: reviews/STAGE14_THEOREMS_AND_PROOFS.md and verification/stage14/canonical_global_rerun.log, verification/stage14/pareto_rerun.log; reviews/STAGE14RS_ONE_EXTENSION_PROPOSITION.md, reviews/STAGE18_OPTIMAL_DEPTH_ANALYTIC_THEOREM.md, reviews/STAGE21_NO_SU_MISSING_MIDDLE_THEOREM.md, and literature/STAGE21_SW_REVERSAL_PRIOR_ART_AUDIT.md.

**No manuscript production files, main branch or Theory Freeze changed.**
