# V2b Stage10 — Reviewer Verifiability Map
**Audit applicability: FULL** for theorem-bearing computer-assisted international-standards game. Correctness of source proofs, reproducibility of their CI and intelligibility of the manuscript chain are distinct obligations.

## Claim → manuscript bridge → proof

| Frozen claim | Manuscript object and bridge equation | Main proof / appendix object | Machine reproducibility | Current limit |
|---|---|---|---|---|
| T1 every S,g,x unique interior Cournot | Consumer FOC holding n^e fixed: p=a1−Bq+ηHn^e; firm q FOC p_i−c=q_i; fulfilled n^e=q → Mq=1, M_ii=1.242, offdiag≤.242 | Section 3 and App A contraction, lower bound on raw best responses over cube [0,1/1.242]^3 | Frozen Stage4A Krawczyk independent math plus reproducible code | Valid at θ0, not all η/ρ |
| T2 global firm Nash, not symmetric root selection | π_i=3q_i²−cost, q_{x_i}=−M⁻¹M_{x_i}q, F_i=6q_iq_{i,x_i}+κ(1−x_i) | Section 3, App A: compact x cube, strict own concavity, symmetric Jacobian diagonal dominance κ>.81 and interior uniform root faces | verification/v2b_stage04a_krawczyk_cleanroom.py | Lean NOT proves all-x Nash |
| T3 all-g country policy vetoes | SU y=(u,u,v), IS x=(y,y,y), M_member(g), O_out(g), I_IS(g), S_SW; \(d M/dg=W_g+\nabla_x W\cdot x_g\) | Section 4 + App A: Krawczyk roots 1000 rational [j/1000,(j+1)/1000], upper derivative signs <−.00797019 and <−.01503888 for member and I−O. Backward induction C then B then A | Stage4A script, fixed CI | IF all-g sign coverage fails, proposition FAILS; no "201 grid proves" |
| T4 frozen x produces positive IS | Define x^SW once from true SW Nash, restrict x across EVERY history; evaluate \(\widehat I(.05)−\widehat O(.05)>0\), \(\widehat I(.05)−\widehat M(.05)>0\) and supremum over all SU depth | Section 4 and App A: interval roots for xSW, all-g SU envelope 500 rational cells | Stage4A script | Counterfactual DIFFERENT firm game; not actual parent game Nash |
| T5 endogenous IS welfare > SW | W_i=½qᵀBq+3q_i²−cost; I(.05)−S>0 exact rational interval | Section 5, generated welfare table and App B | verification/v2b_stage06_pareto_holdout.py and stage07 evaluator | IS off-path hypothetical; not first-best |
| T6 claimed nearby θ | Continuity/strict uniform signs/unique Nash imply unspecified open neighborhood | Section 6 stated as nonquantified implication only | Stage4A strict margins | Cannot claim uniform radius or generic class |
| T7 p=2 diagnostic (one new form) | X_ij=(x_i²+x_j²)/2; x_i design cost still κ(1−x_i)²/2, unilateral own derivative changes; maintain SAME θ and agenda | Section 6 and App C: 3×3 Rosen Gershgorin all-x g, all-g SU and IS root face signs; frozen g=.05 failed; g=.005 succeeded by ≈9.1e−7 | verification/v2b_alt_quadratic_rosen_interval.py + v2b_alt_quadratic_policy_interval.py | Does NOT imply continuous p∈[1,2] proof; original fixed-g failed prereg |

## Independent equation reconstruction (main path)
1. From utility, demand inverse holding expected n fixed and positive quadratic coefficient.
2. From conditional Cournot at fulfilled n=q, calculate M=I+(ρ−η)H+(1−ρ)X, not the consumer Hessian B; check diagonal=2−η.
3. Solve q=M⁻¹1, derive Δ operating profit across 3 markets as 3q_i² and deduct design cost ONCE; CS=½qᵀBq.
4. Compute firm design **unilateral** gradient and root. Do NOT differentiate along symmetric u or y simultaneously as a firm's best-response deviation.
5. In SU reduce after proving global design-game uniqueness to u=v_members, v=outsider. Define m,n,D and q_m,q_o in App A; reduced W member/out. For IS, derive y scalar continuation. Root inclusions global in g by certificates, not root solver alone.
6. Differentiate government welfare along equilibrium designs via IFT, sign entire continuum with rational intervals. Integrate from g=0 common welfare. C then B then A choose incompatible outcome.
7. Freeze each firm's x to own SW Nash (different strategy-feasible set). Recalculate SU and IS, prove policy strict support and all other g SU envelope bound. Do NOT transfer endogenous x'(g) to this counterfactual.
8. Compare unattainable (but feasible conditional) IS(.05) to actual SW with true reoptimization for both: strict Pareto gap, not optimizer.
9. p=2 source separately re-derives all x/g logic; Lean proof only Rat proxy welfare 4 inequalities, NOT Nash root membership or full SPNE.

## Appendix trust and coverage information
Shared SymPy/mpmath symbolic and interval kernels trusted by both Stage4A pipelines, not fully independent formal proof. Exact rational g cells, outward interval signed margins, and source CI logs are accessible. Lean4 v4.24.0 source is a **pointwise rational sign cross-check at proxies**, not the entire economic theorem. User scope approval does not certify a personal independent proof. The main paper must cross-reference appendix labels describing these limits.

## Construction reviewer arrival targets
By Section 2 every strategy/action constraint and benchmark defined; by Section 3 clear FOCs, matrices and uniqueness argument; Section 4 the all-g proposition has its two signed derivative target formulas; Appendix explains roots, bounds, continuity argument and falsification/negative result. No proof may say merely "a solver checked the claim" without stating the exact quantified object and interval domain.
