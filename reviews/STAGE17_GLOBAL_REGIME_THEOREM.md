# Formal theorem: all-depth exclusion of terminal bilateral agreements

**Theorem (conditional government-equilibrium regime selection at theta0, lambda=5).** In V2b with (d,eta,rho,kappa)=(1,379/500,9/10,1701/2000), preinstalled design z equal to original fragmentation Nash and the additional one-time residual cost 5(x_i-z)^2/2, there exists a strictly accepted positive-depth AB -> ABC offer at g=1/20 such that A's welfare exceeds its payoff from ANY terminal AB bilateral agreement at ANY g in [0,1], and exceeds SW. Under the original government's menu, any attained proposer-optimal SPNE outcome (if a pure SPNE satisfying the tie conventions exists) must therefore end in IS rather than SU or SW.

**Proof part 1 (global x enclosure).** For any policy regime/history and all x in [0,1]^3, M=I+B-eta H has diagonal alpha=2-eta=621/500 and nonnegative off diagonal at most beta+delta=1-eta=121/500. Hence each row is strictly diagonally dominant with slack eta=379/500, q=M^{-1}1 is strictly positive by the standard positive-invariant Cournot fixed-point contraction and q_i<=1/alpha. The induced one-firm quantity derivative q_{x_i}=-M^{-1}M_{x_i}q has |q_{i,x_i}|<=beta/(alpha eta), as ||M^{-1}||infty<=1/eta and ||M_{x_i}q||infty<=beta/alpha. Hence |6q_i q_{i,x_i}|<=P:=6 beta/(alpha^2 eta)≈0.5131435248. Under strict interior global Rosen uniqueness, all three firm unilateral first-order conditions at lambda=5 give (kappa+5)x_i=kappa+5z+6q_i q_{i,x_i}. The signs at the boundary guarantee all optimal x_i interior: at x_i=0, kappa+5z-P>0; at x_i=1, -5(1-z)+P<0. With the exact inherited z root bracket, this yields

x_i ∈ [(kappa+5 z_lower-P)/(kappa+5), (kappa+5 z_upper+P)/(kappa+5)] ⊂ (0.67,0.85).

**Proof part 2 (analytic elimination of Cournot).** In terminal SU at depth g, by full unique Nash and AB permutation symmetry put x_A=x_B=u, x_C=v. Define
 t=delta*g+beta*u, h=beta*(u+v)/2, T=alpha*(alpha+t)-2h².
 Quantities solve q_A=q_B=(alpha-h)/T and q_C=(alpha+t-2h)/T.
 The exact country-A welfare is

 W_A(SU,g,u,v)=(4+rho*g+beta*u)q_A² + (1/2)q_C² + 2h q_A q_C -kappa(1-u)²/2 -5(u-z)²/2.

For g∈[0,1], u,v∈[0.67,0.85] the denominator T has strictly positive rational interval lower endpoints. A proof-oriented exhaustive adaptively bisected Fraction arithmetic computation gives

sup_{g,u,v} W_A(SU,g,u,v) < 2.4405.

The computation starts from one closed box, splits only if the mathematically outward interval upper bound is ≥2.4405, and terminates after EXACTLY 10510 child boxes with no uncleared boxes. This is a certificate for the whole continuum, NOT a grid evaluation at sample points. No dependence on the FOC or numeric Nash continuation within this second step.

**Proof part 3 (strict accepted grand benchmark).** Imported unchanged Stage16 independent Krawczyk and Rosen checks certify that the AB agreement with inherited g=1/20 receives B's strict acceptance and C's strict accession as well as incumbents' strict enlargement acceptance, at lambda=5. Its national welfare interval satisfies W_A(IS,1/20)>2.4410780. Original fragmentation is SW≈2.42207842. Therefore the accepted IS offer strictly beats the terminal bilateral global upper bound and no-agreement payoff. By backward induction, any proposer-optimal attained final regime cannot be SW or SU. QED.

**Scope:** not claiming g*=0.054333..., a unique policy-depth SPNE, a global lambda threshold, all-cost generality, transfer or renegotiation stability, empirical magnitudes, or originality in the full prior literature. Tie-breaking and existence of a government best response on an open acceptance set remain explicit. The theorem is a strict revealed-preference elimination of two regimes, not the full solution of a continuous extensive-form game.

**Reproduction:** `python verification/stage17_global_su_envelope.py` from repository root, Python standard library only; it invokes previously tested Stage16 source once. Any failure of the branch cover, z enclosure or accepted-grand welfare bound raises AssertionError, so a misleading 'PASS' cannot be printed.
