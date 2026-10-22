# Stage21 — Exact Missing-Middle Theorem (restricted primitive family; endogenous-firm-design extension)

**Decision (2026-10-22): CONDITIONAL RESEARCH GO.** We have PROVED global absence of an optimal terminal SU on the entire rho=1 face with 0<eta<1. Moreover, via uniform strict Nash regularity, analytic perturbation, and a quadratic transition argument, we have a NONEMPTY region with rho<1, so original endogenous firm designs remain strategic, where the optimal terminal government outcome switches **SW directly to IS without SU**. This does NOT certify universal absence of SU for arbitrary original primitives or corner-output extensions. No added primitive; original V2b lambda=0 suffices.

## Model and protocol (not optional)

Three symmetric economies/firms. Governments choose one depth g∈[0,1], first AB bilateral then C accession at the **same inherited depth**, conditional on C's own and incumbent consents. Original fulfilled-expectations Cournot equation

M q=d 1, M=I+B-eta H=I+(rho-eta)H+(1-rho)X,

B=rho H+(1-rho)X, X_ij=(x_i+x_j)/2, x_i∈[0,1]. Network willingness-to-pay eta differs from technical substitutability rho. Firm once-paid design cost kappa(1-x_i)^2/2. Here lambda=0, no optional adjustment extension. Country payoff W_i=CS+3q_i²-kappa(1-x_i)^2/2, CS=q'Bq/2. Exact government terminal gates, weak votes at indifference:

IS at g: i(g)>=max{s,o(g),m(g)}.
SU at g: m(g)>=s and [i(g)<o(g) or i(g)<m(g)].
Otherwise SW.

Let g>0 for substantive agreement; g=0 is equivalent to SW.

## Theorem 1 (EXACT complete SW/IS classification, NO optimal SU on rho=1 face)

Let rho=1, eta∈(0,1), kappa>0 and d>0. Then residual design is x_i=1 in every history, unique (private cost minimization). Define a=2-eta, theta=(1-eta)/(2-eta)∈(0,1/2), D=d²/a²>0. Exact Cournot/welfare formulas:

s=D*9/2;
m(g)=D[(4+g)/(1+theta*g)^2+1/2];
o(g)=D[(1+g)/(1+theta*g)^2+7/2];
i(g)=D[(9/2+3g)/(1+2theta*g)^2].

### Weak networks: 0<eta<=6/7 iff theta>=1/8

m(g)-s = D*g*(1-8theta-4theta²*g)/(1+theta*g)² <0 for every g>0.

Also

i(g)-o(g)
= -D*g*P(theta,g)/[(1+theta*g)^2(1+2theta*g)^2],

P=14theta^4*g³+(42theta³+theta²)*g²+theta*(45theta-2)*g+(16theta-2).

For theta>=1/8 and g>0, P>0 (including equality theta=1/8 because its linear term is then strictly positive). Thus C strictly vetoes grand accession at EVERY positive depth and AB is also rejected against SW. Government selects SW.

### Strong networks: 6/7<eta<1 iff 0<theta<1/8

Set v=1-8theta>0. For ANY bilateral depth g∈[0,1],

m(g)-s=D*g*(v-4theta²*g)/(1+theta*g)² <= D*v.

We construct an EXPLICIT grand offer, not an optimizing grid,

**h(theta)=min{1, 2(1-8theta)}=min{1,2v}**.

We prove three inequalities simultaneously:
(i) i(h)>s+D*v >= sup_g m(g);
(ii) i(h)>o(h);
(iii) i(h)>m(h).

Hence the original bilateral-first tree accepts grand IS(h), and the proposer strictly prefers it to ALL terminal SU outcomes at ANY depth, and to SW.

If theta<=1/16, h=1. Both member and outsider SU payoff at h=1 are at most D*11/2. Meanwhile
i(1)>=D*(15/2)/(9/8)^2=D*160/27>D*11/2,
and i(1)-s>=D*77/54>D>=D*v.
All required inequalities follow.

If 1/16<theta<1/8, set 0<v<1/2, theta=(1-v)/8, h=2v.
Elementary rational algebra, with
Q(v)=2(v-2)^2(v+1)^2>0 and
R(v)=Q(v)(v²-v-4)^2>0,
gives:

[i(h)-s-D*v]/D
=v [4+19v+24v²-5v³-2v⁴]/Q(v)>0;

[i(h)-o(h)]/D
=v² [280+492v-83v²-240v³+42v⁴+28v⁵-7v⁶]/R(v)>0;

[i(h)-m(h)]/D
=v [192+304v+132v²-77v³-48v⁴+6v⁵+4v⁶-v⁷]/R(v)>0.

For 0<v<1/2, negative high-order monomial magnitudes are bounded:
5v³+2v⁴<3/4<4;
83v²+240v³+7v⁶<51<280;
77v³+48v⁴+v⁷<13<192.
Hence all three brackets are strictly positive. This completes the analytic accepted-dominant-grand-offer construction without needing the maximizing g.

The IS weak-acceptance depth set is closed in compact [0,1], nonempty and has strictly positive accepted witness; proposer payoff i(g) is continuous. Hence an IS maximum is attained, and its terminal outcome is globally proposer-optimal since all SU payoffs lie strictly below i(h) and s<i(h). Final regime IS.

**Complete face classification:**
0<eta<=6/7 : SW;
6/7<eta<1 : IS;
SU never proposer-optimal for any eta on rho=1.

The theorem includes a genuine explicit *primitive cutoff* eta_c=6/7, not a constructed second SU threshold. The optimal IS depth need not equal h(theta), which is a sufficient winning witness rather than argmax.

## Theorem 2 (genuine endogenous design: NO SU across a nontrivial rho<1 parameter strip)

**Statement.** Fix d>0, kappa>0, lambda=0 and any closed network interval K=[eta_minus,eta_plus] contained strictly inside (0,1), with eta_minus<6/7<eta_plus. There exists rho_bar∈(eta_plus,1) and a C^1 function eta_c(rho) with eta_c(1)=6/7, defined for rho_bar<rho<=1, such that the ORIGINAL V2b game with rho∈(rho_bar,1), eta∈K has a unique globally regular, positive-quantity and INTERIOR three-firm residual design Nash in each admissible history; government terminal outcomes satisfy

eta<=eta_c(rho)  => SW at every positive-depth offer;
eta> eta_c(rho)  => an accepted positive-depth IS offer strictly beats SW AND EVERY possible SU proposer payoff, and an optimal IS proposal is attained;
no SU government-optimal region exists ANYWHERE in this restricted parameter strip.

**Sketch made rigorous by standard uniform IFT/compactness bounds**:

(1) At beta=1-rho=0, all firms optimally choose x=1 and F_i= -kappa(x_i-1). Its pseudo-gradient Jacobian is exactly -kappa I. For eta in K and all g∈[0,1] across SW/SU/IS, the fulfilled Cournot quantities are uniformly positive and the quantity matrices uniformly nonsingular. By compactness, for beta sufficiently small positive, the full firm's pseudo-gradient is uniformly strongly monotone in x on the strategy cube (Jacobian symmetric part <=-kappa I/2) and quantities remain positive. In particular, each regime/history has a unique Nash; for beta>0 small the own differentiation marginal incentive pushes the FOC strictly inward from x_i=1, and at x_i=0 the positive kappa term dominates. The unique Nash is interior and analytic in (eta,rho,g) by a uniformly nonsingular IFT.

(2) Away from eta0=6/7, Theorem1 has strict decisive margins throughout each compact subinterval: for eta<eta0, SU member gain and C joining margin are strictly negative for all g>0, including a strictly negative g-derivative at zero. For eta>eta0, the explicit continuous h(theta) witness beats SW and the *global envelope* of all SU member payoffs, with all votes strictly accepted. These margins persist, uniformly across any closed subinterval away from eta0, under sufficiently small beta>0.

(3) Near the transition eta0, use the smooth full-model functions
M(g,p)=m(g,p)-s(p), V(g,p)=i(g,p)-o(g,p), J(g,p)=i(g,p)-s(p), H(g,p)=i(g,p)-m(g,p),
where p=(eta,rho), and define mu(p)=M_g(0,p). All four vanish at g=0. By **permutation symmetry of the undirected three-edge standards game**, the exact local identity V_g(0,p)=2 mu(p) holds for EVERY p (this is not an empirical assumption).
At the critical face point p0=(eta0,1), theta=1/8 and D=d²/(2-eta0)²,
M(g,p0)=-D*g²/[16(1+g/8)²],
V(g,p0)=-D*g²*[29/64+25g/256+7g²/2048] /
                  [(1+g/8)²(1+g/4)²],
J_g(0,p0)=H_g(0,p0)=3D/4>0.
Moreover mu(p0)=0 and
**partial_eta mu(p0)=8*d²/(2-eta0)^4=2401*d²/512>0.**
By IFT there is a unique C^1 cutoff eta_c(rho) near rho=1 with mu(eta_c(rho),rho)=0, and sign mu=sign(eta-eta_c(rho)).

(4) By strict quadratic negativity at p0, continuity of second derivatives, and uniform negative margins away from g=0, there exist a,b,c,B,epsilon>0 and a neighborhood of p0 such that for all 0<=g<=epsilon,

M(g,p)<=mu(p)*g-a*g²,
V(g,p)<=2mu(p)*g-b*g²,
V(g,p)>=2mu(p)*g-B*g²,
J(g,p)>=c*g, H(g,p)>=c*g,

and M(g,p)<0,V(g,p)<0 for epsilon<=g<=1.
If mu<=0, all SU member gains and C joining margins are strictly negative for every g>0, hence SW.
If mu>0, pick grand offer h=mu/B (shrink neighborhood to make h<=epsilon). Then V(h)>=mu²/B>0, J(h)>0,H(h)>0. For every depth, sup_g M(g,p)<=mu²/(4a); yet J(h)>=c*mu/B>mu²/(4a) for sufficiently small mu. Hence accepted IS(h) strictly dominates ALL bilateral proposer payoffs, even without requiring their actual acceptance. A pure optimal accepted IS is attained by compactness and weak voting. This proves direct SW->IS switch with no SU near p0.

(5) A finite open cover joins neighborhoods from step2 to the critical block step4 over arbitrary eta compact interval K. Choosing rho_bar<1 sufficiently close to1 yields the statement uniformly across K.

This is a **real endogenous-product-design theorem**, not merely rho=1 where the private design is inactive. It is not a universal SU exclusion for all eta,rho,kappa: rho is restricted sufficiently near1, eta to compact K, d,kappa fixed, and all equilibria are the original interior regime.

## Referee-readable economic mechanism

The reason there is no stable final bilateral middle on this model slice is not that a bilateral network agreement never helps. When the member gain first becomes positive, its payoff advantage over SW is **second order** in the distance from the crossing, whereas the grand coalition's accepted positive-depth offer provides a **first-order** proposer gain; the third-country joining margin tracks twice the bilateral member's initial derivative by three-country permutation symmetry. Government depth can adjust so that outsider votes are satisfied before the bilateral offer can beat the optimized grand alternative. The explicit h(theta) construction shows this is true globally on rho=1; the quadratic perturbation extends it to genuinely endogenous firm design near rho=1.

## Scope/priority
- Strong progress, **not** the universal theorem "SU never optimal in the entire original parameter space." No proof for arbitrary rho far from1 or invalid/corner Cournot histories.
- Prior art: generic absent-middle coalition thresholds are not automatically novel; compare carefully with Gandal & Shy (2001) and Klimenko (2009). This is a model-specific mechanism and a real economic primitive cutoff.
- Only Draft research notes and a review-only LaTeX theorem; no original manuscript, frozen parameters or main modified.
- Exact algebraic proof regression code: verification/stage21_no_su_phase_theorem.py.