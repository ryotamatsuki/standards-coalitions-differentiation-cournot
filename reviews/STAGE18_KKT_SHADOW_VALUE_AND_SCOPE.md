# Stage18 KKT complement — binding outsider-vote shadow value

At canonical lambda=5 under the weak-acceptance rule, let Phi(g)=W_C^IS(g)-W_C^SU(g), so feasibility is Phi(g)>=0. The globally optimal depth is the unique positive Phi(g*)=0, enclosed between 0.05433320681 and 0.05433320682. For feasible IS, the government's smooth objective is V(g)=W_A^IS(g); all firms' post-policy design is reoptimized.

At g* the active-constraint KKT condition (maximization with Phi>=0) is

V_g(g*)+mu Phi_g(g*)=0,
mu=-V_g(g*)/Phi_g(g*)>0.

Parametric exact-rational Jacobian/Krawczyk continuation calculations enclose
V_g(g*) in (0.36496517,0.36496786),
Phi_g(g*) in (-0.00932094,-0.00931740),
mu in (39.1554,39.1706).

Since V_g>0 but Phi_g<0, the unregulated grand-coalition policy objective still favors deeper harmonization at g*. The decisive restraint is **C's endogenous outside option**; hence the shadow price is positive. These values are reduced-form model units, NOT money/real-world welfare multipliers.

The constructive closed-form characterization uses rational functions y(t),g(t),V(t) for IS (STAGE18_OPTIMAL_DEPTH_ANALYTIC_THEOREM.md), and algebraic SU firm Nash equations. The unique real root with the rational isolating interval is exact as an algebraic RootOf object, but no finite expression in elementary radicals has been established. We do not assert it is algebraically unsolvable by radicals without a Galois proof.

Proof code verification: `verification/stage18_optimal_depth_interval_certificate.py` completed SUCCESS under GitHub Actions 'Stage18 unique analytic government-optimal depth' run 39699387342, job 119564627435; log says 7 positive-derivative cells, 5 intermediate bounded cells, 26 globally negative-derivative cells, 1 IS-welfare positive-derivative certificate, unique strict root bracket and required votes.

Scope: fixed original theta0, lambda=5, weak acceptance at equality; the general function lambda->g*(lambda) is NOT solved. Independent field-level novelty remains conditional. No submission/merge/freeze changes.
