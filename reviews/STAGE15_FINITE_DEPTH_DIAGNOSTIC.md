# Stage 15 — Independently recomputed finite-depth voting boundaries

Model: three-country symmetrical V2b, d=1, eta=379/500, rho=9/10, kappa=1701/2000, adjustment cost lambda*(x_i-z)^2/2 once. Fragmentation design z=0.7185927073221112, fragmentation national welfare s=2.422078421718469. For policy depths g in (0,1] solve each firm's unilateral FOC and the fulfilled expectations linear system Mq=1 with diagonal 2-eta and off-diagonals beta(x_i+x_j)/2+delta*H_ij. Compute B=rho H+beta X off diagonal, B_ii=1, CS=q'Bq/2; Pi_i=3q_i²-kappa(1-x_i)²/2-lambda(x_i-z)²/2. Countries receive W_i=CS+Pi_i. This is a fresh floating point numerical diagnostic independent of the earlier exact Stage14/14RS implementation.

| lambda | Approx. outsider accession ceiling g_C | Strict feasible depth 0.95*g_C | Gain per country (IS vs SW) at depth 0.95*g_C |
|---:|---:|---:|---:|
| 0.94 | 0.00020641 | 0.00019609 | 0.00007408 |
| 1.0 | 0.00279541 | 0.00265564 | 0.00100344 |
| 1.5 | 0.01908557 | 0.01813129 | 0.00686088 |
| 2.0 | 0.02953296 | 0.02805631 | 0.01062637 |
| 5.0 | 0.05433321 | 0.05161655 | 0.01959265 |
| 10.0 | 0.06503201 | 0.06178041 | 0.02347260 |

The first root of i(g)-o(g)=0 numerically bounds *the small-depth interval* of positive outsider voting. A finer global scan and interval certification would be needed to rule out disconnected feasible intervals. At the reported depths, the bilateral and incumbent votes are also strictly positive; the numerical g_C need not be the globally largest accepted depth without separate proof. At lambda=1 and g=.01, i-o is about -0.0000127297, and at lambda=2 and g=.05, about -0.0001766735, despite a positive local derivative at zero in both cases. These finite-g rejections contradict any broad reading of the local threshold.

At lambda=0 original all-g proof is inherited from Stage14. At lambda>0 do not infer existence or uniqueness of a GLOBAL phase threshold solely from local M-matrix monotonicity. Near lambda_c the surviving depths and welfare gains collapse to zero. Do not claim empirically meaningful magnitudes without calibrating design indices and costs. Proposer welfare optimization and vote tie-breaking at g_C are not rigorously certified here; strict interior feasible offers suffice for nontrivial agreements locally.

Testing: `verification/stage15_global_depth_diagnostic.py` recomputes model primitives and uses a separate numerical nonlinear design solver. Its float accuracy checks and equilibrium FOCs are diagnostics, not exact interval certificates.
