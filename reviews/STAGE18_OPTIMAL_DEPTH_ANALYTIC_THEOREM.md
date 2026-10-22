# Stage18 — Analytical characterization and unique government-optimal standards depth

Research date: 2026-10-22 JST. Branch stacked directly over PR #17. **Mathematical gate PASS for the specified canonical theta0, lambda=5, under acceptance when indifferent; economic priority remains UNRESOLVED.** No general closed form in elementary radicals is claimed.

## 1. Scope and equilibrium convention

Retain the canonical V2b three-country bilateral-first, inherited-depth game, with *one* additional resource-cost curvature:
K_i = kappa(1-x_i)^2/2 + lambda(x_i-z)^2/2.
Let (d,eta,rho,kappa)=(1,379/500,9/10,1701/2000), lambda=5; alpha=2-eta, beta=1-rho, delta=rho-eta. Here z is the original symmetric fragmentation Nash, the unique relevant root of

kappa(1-z)(alpha-beta z)(alpha+2 beta z)^3 - 6 beta alpha = 0,

enclosed by a 150-step Fraction-bisection sign certificate near z=0.7185927073221112.

Crucial tie rule: A government accepts an accession offer whenever its payoff is weakly no worse than rejection. Under strict rejection on exact indifference, the accepted depth set is open at its upper boundary and a pure optimal proposal may FAIL TO EXIST even though its supremum and unique limiting depth are well-defined. This is not an innocuous numerical convention.

## 2. CLOSED RATIONAL PARAMETRIZATION of the grand-agreement design continuation

In IS put y=x_A=x_B=x_C, t=delta*g+beta*y. Private design Nash FOC:

(kappa+lambda)y -kappa-lambda z + 6 beta alpha /[(alpha-t)(alpha+2t)^3] = 0.

Therefore

y(t)=(kappa+lambda z -6 beta alpha /[(alpha-t)(alpha+2t)^3])/(kappa+lambda),
g(t)=(t-beta*y(t))/delta,
q(t)=1/(alpha+2t).

The EXACT national grand-agreement welfare as a rational function of t (coefficients algebraic in z) is

V(t)={9/2+3[rho*g(t)+beta*y(t)]}/(alpha+2t)^2
      -kappa(1-y(t))^2/2-lambda(y(t)-z)^2/2.

Also
y_t=6 beta alpha (5alpha-8t)/{(kappa+lambda)(alpha-t)^2(alpha+2t)^4},
g_t=(1-beta*y_t)/delta>0 on the certified branch.

Writing B(t)=rho*g(t)+beta*y(t), the exact unconstrained analytic derivative is
V_t = 3 B_t/(alpha+2t)^2
      -(18+12 B)/(alpha+2t)^3
      +[kappa(1-y)-lambda(y-z)]y_t,
B_t=rho/delta-(beta*eta/delta)y_t.

A stationary interior proposer policy would satisfy V_t=0. IT DOES NOT in the feasible IS portion for lambda=5.

## 3. Exact bilateral continuation and outsider feasibility equation

In SU=AB with outsider C, let u=x_A=x_B, v=x_C,
t_B=delta*g+beta*u, h=beta(u+v)/2, T=alpha(alpha+t_B)-2h^2,
q_m=(alpha-h)/T, q_o=(alpha+t_B-2h)/T,
R_AA=(alpha^2-h^2)/[(alpha-t_B)T].

The COMPLETE full-three-firm Nash conditions (not a planner's symmetric joint derivative) are

0 = -3 beta q_m [R_AA*q_o+q_m^2] +kappa(1-u)-lambda(u-z),
0 = -6 beta q_o [(alpha+t_B)q_m-h*q_o]/T +kappa(1-v)-lambda(v-z).

The exact outsider's national welfare is
W_C^SU(g)= (1+rho*g+beta*u)q_m^2 + (7/2)q_o^2 +2h q_m q_o
          -kappa(1-v)^2/2-lambda(v-z)^2/2.

Define the analytic accession constraint
Phi(g)=V(t(g))-W_C^SU(g).

All quantities are rational in the variables (g,z,y,u,v), whose private Nash equations are polynomial after clearing strictly positive denominators. The optimizer is therefore a REAL ALGEBRAIC NUMBER: exactly the UNIQUE root of this explicitly defined algebraic system subject to

0.05433320681 < g* < 0.05433320682.

This is an **exact algebraic implicit/root-form characterization, NOT an elementary explicit formula in radicals**. No assertion that the particular high-degree algebraic root is impossible to express by radicals is made. The parameter t rationally parametrizes the IS branch, but SU continuation still requires an algebraic Nash root.

## 4. Global existence/uniqueness and binding-vote proof, exact rational interval certificates

Independent standard-library Fraction interval arithmetic with forward-mode automatic differentiation, parametric Krawczyk fixed-point inclusion for both symmetric SU and IS firm Nash continuations, and the inherited full asymmetric Rosen uniqueness criterion certify:

- Phi'(g)>0 on [0,0.02] (seven final subintervals).
- -0.01 < Phi'(g) < 0.01 on [0.02,0.04] (five final subintervals); exact Phi(0.03)>0.00012657, so throughout [0.02,0.04], Phi(g)>0.00002657.
- Phi'(g)<0 on [0.04,1] (26 final subintervals).
- V'(g)>0 on [0,0.06] (one parametric certificate).

Phi(0)=0 and strict increase for g>0 near 0. Exact Nash Krawczyk point boxes with rational legacy root at the two rational endpoints certify Phi(0.05433320681)>3.9812e-14 and Phi(0.05433320682)<-5.3379e-14. Hence the sole POSITIVE consent zero lies strictly between them, and C accepts exactly 0<=g<=g* under weak acceptance (strictly prefers for 0<g<g*).

At the enclosed root, certified strict B bilateral consent vs SW, strict incumbent widening IS vs SU, and strict IS welfare vs SW hold; C is indifferent and accepts by the specified tie rule. With V'(g)>0 until g*, this IS continuation is the unique welfare-maximizing feasible grand standard.

Inherited Stage17 independently proves sup_{g in [0,1]} W_A(SU,g)<2.4405, while the accepted IS at g=.05 has W_A>2.4410780. SW has ~2.4220784. Thus neither any terminal SU nor SW offers can defeat the optimal accepted IS. **This completes the government's global best-response depth AND regime choice** at the canonical lambda=5 point conditional on the weak-vote tie convention, and establishes a pure-strategy SPNE under the game's inherited rational off-path continuation and tie convention.

## 5. Certified and approximate welfare

g* in (0.05433320681,0.05433320682).
W_i(IS,g*) in (2.4426644148904,2.4426644148941).
W_i(IS,g*)-W_i(SW) in (0.0205859931719,0.0205859931756).
National welfare gain relative to SW: about 0.84993091%. The magnitudes are UNCALIBRATED model numbers, not empirically estimated benefits.

## 6. Editorial limitations
- The physical interpretation of residual design index x and policy depth g remains reduced form.
- All global optimization conclusions above are for original theta0 and lambda=5 ONLY, not arbitrary lambda/theta or arbitrary institutions.
- This is not a simple radical closed-form value: rational parametrization plus an uniquely isolated algebraic constraint root is the appropriate exact formulation.
- Government tie acceptance is essential; under strict rejection at indifference the pure optimum is not attained.
- Closest prior-theorem priority (particularly Klimenko 2009 and Grossman–McCalman–Staiger 2021) is NOT cleared. Do not convert mathematical PASS to journal novelty PASS.
- No new primitive, no changes to main/Theory Freeze/old manuscript, no submission.

Reproducibility: stage18 exact Fraction/Krawczyk code and published interval outputs should be retained with this review; the full self-contained auditor is also provided to the author as a downloadable Python artifact in the present ChatGPT conversation.
