# Stage 16 — Adversarial final focused audit (2026-10-22 JST)

**Decision: CONDITIONAL GO for retaining the ONE residual-design adjustment-cost extension as research; journal-submission and main-manuscript incorporation NOT authorized. Full-paper-headline originality remains REOPEN.**

## Original request and four gates
1. **Closest literature:** Grossman–McCalman–Staiger (2021 Econometrica) FULL published Props 1–5 and adaptation-cost discussion at p.238 have been checked. This proves endogenous design costs affecting government standards policy is **already known**. Klimenko (2009 JIE) publisher abstract/academic record checked, full final numbered propositions UNAVAILABLE. Barrett–Yang, Lambertini–Rossini, Cabral–Salant, Cheng–Huang have inherited gaps. No universal priority clearance; see `../literature/STAGE16_PRIOR_ART_KILL.md`.
2. **Economic foundation of z:** must be defined as an ex ante installed *legacy residual design* (identical across symmetric firms) at stage 0, not renegotiated/optimized after standards are proposed. For the controlled theta0 counterfactual choose its legacy value to equal the lambda=0 SW design Nash z(theta0)≈0.718592707322. This is a substantive predetermined-reference convention, not a measured physical product distance. At SW the penalty and its first derivative vanish and Nash z persists at all lambda. It may be criticized as a calibration restriction, not an extra independent policy/choice variable.
3. **Rigorous nontrivial finite depth:** NEW EXACT RESULT for g=1/20 (0.05). Fraction root bracket and Krawczyk/Brouwer interval inclusion plus original globally strict Rosen curvature/unique Nash bounds establish positive welfare margins for every lambda in the explicit interval [499/100,501/100]=[4.99,5.01], not only isolated lambda=5. At lambda=4 outsider strictly rejects, at lambda=2 bilateral member strictly approves but outsider rejects. The theorem is proved for *a fixed positive g and a small explicit adjustment-cost band*, not a complete global institutional threshold.
4. **Optimized government depth:** an independent floating-point scan finds at lambda=5 the FIRST outsider accession zero at g≈0.0543332068142; unconstrained bilateral member welfare maximum ≈0.00022056 above SW at g≈0.09335; IS welfare ≈0.02058599 above SW at the putative outsider ceiling. Numerical evidence points to a boundary-constrained IS choice, but **neither global feasibility enumeration nor unique policy optimum nor all vote/tie handling is rigorously certified**. Exact proof only ensures a strict feasible offer at g=.05 and global proposer welfare *at least* its payoff if a maximizing accepted path exists. No claim g*.05433 is rigorously found.

## Exact welfare and agreement witness at lambda=5, g=.05
- SU incumbent member minus SW: [0.00017335225, 0.00017368070] >0.
- IS outsider minus SU outsider (accession): [0.0000368992, 0.0000375668] >0.
- IS incumbent minus SU incumbent: [0.0188259434, 0.0188266095] >0.
- IS each country minus SW: [0.0189996241, 0.0189999617] >0; 0.7844% of baseline SW country welfare.
- Uniform lambda in [4.99,5.01]: outsider margin [0.0000038509, 0.0000706149] >0; all other strict votes and grand gains >0.

The once-paid `lambda*(x_i-z)^2/2` term appears only once in home firm's WORLD profit and thus once in national W. At g=0 the direct derivative w.r.t policy of that adjustment term is zero because x_i=z. Finite g adjusts BOTH behavior and resource expenditures, without a claim that all incidence is behavioral at finite g.

## Publication significance
What is newly rigorously shown WITHIN V2b: (i) local unique lambda consent crossing; (ii) a positive finite-depth g=.05 agreement with all subgame acceptance votes strictly positive on an explicit lambda band; (iii) a distinct outsider gate where members approve but outsider rejects at lambda=2 and 4. However the result is still coupled to the bilateral-first / inherited-depth protocol and expensive flexibility λ≈5.88 times kappa. Grossman et al. broadly preempt the 'cost of adaptation changes government standards' thesis. The bounded residual institutional proposition may not be substantively novel enough for a full paper; priority and relevance remain conditional.

**Final choice:** Route A remains CONDITIONAL (one more tightly scoped full-text priority/optimized-depth certification only if importance is defensible). Route B stays available: original Stage14 Level2 paper, adjust short/regular full length to journal, no new variables. A successful mathematical certification does not force adoption.

Draft PR stacked on PR15, main/Theory Freeze/original manuscript unchanged. Exact reproduction code `verification/stage16_fixed_depth_certificate.py` and CI separate from all earlier V2b math.
