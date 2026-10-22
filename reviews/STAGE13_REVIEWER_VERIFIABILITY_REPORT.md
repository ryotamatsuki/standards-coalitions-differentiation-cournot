# V2b Stage13 — reviewer-verifiability reconstruction
**Applicability: FULL** (theory-first, dense Cournot/Nash/government theorem and computer-assisted all-depth certificate). Independent editorial review of mathematical **traceability**, not a newly proved mathematical theorem. Stage11 PR27 interval replay remains the numerical/exact source of truth.

## Headline claim → manuscript object → proof → immutable evidence
| Claim | Source chain | Referee-facing proof location | Machine / quantitative support | Review status |
|---|---|---|---|---|
| Consumer and Cournot continuation | quadratic U(q;qbar), B PSD, fixed expectations then fulfilled, Mq=d1, q_i>0 | §2, §3, Appendix full-cube positivity/contraction | independent matrix audit and all-g script in `verification/stage11/` | PASS |
| Private equilibrium x vs cooperative symmetric derivative | `F_i=6q_i(q_xi)_i+kappa(1-x_i)`, J and `x_g=-J^{-1}F_g` | §3, Appendix full cubic domain and unilateral second-order | full-cube Rosen inequality, confirmed global Nash unique in certified region | PASS |
| Local national incidence | CS_x and private FOC → W_A,x=(-C,-C-V,-C-V); edge-count `(i-o)'(0)=2m'(0)` | §4 Lemmas 1–2, Appendix bridge A | `verification/stage11/independent_matrix_audit.py` source | PASS (V sign positive in loss) |
| Local A | frozen D>0 vs Nash D-L<0 and outsider/total slopes | §5 theorem 3 proof, eqs; corresponding Lemmas | exact reference witness, not global from local derivative alone | PASS |
| All-depth global A, original `theta0` + nonempty open neighborhood | 1000 depth interval boxes, certified `dmN/dg<-.007970192997...`, `d(iN-oN)/dg<-.01503888333...` | §5 theorem 4 + latest exact `stage13_proof_supplement.tex`; integrates from common g=0 | `verification/v2b_stage04a_krawczyk_cleanroom.py` and `verification/stage11/canonical_global_replay.log` pinned at Stage11 PR27 commit 54ac838... | PASS on certified center/open neighborhood, not Figure3 rectangle |
| Symmetry reduced SU and IS rigorously lifted | unique full three-firm Nash ⇒ in SU x=(u,u,v), IS x=(y,y,y), reduced stationary FOCs are private unilateral, full strict uniqueness covers off-sym deviations | latest `stage13_proof_supplement.tex` Appendix section 'All-depth computer-assisted bounds'; 2D Krawczyk for SU, scalar interval Newton for IS | source routines `krawczyk_SU`, `krawczyk_IS`, separate full-cube Rosen inequality | PASS |
| Frozen design truly optimal IS | accepted IS at g=1/20, s and entire possible bilateral m(g) dominated; closed feasible IS-depth set has maximizer | theorem4, supplement eqs `eq:frozensup`, `eq:closedfeasible` | exact frozen interval bounds, not a sample grid | PASS |
| Direct grand B | continuation same Nash but outside option is SW instead of preexisting SU | §6 Proposition5, proof | strict i_N(1/20)>s in Stage11 exact replay | PASS conditional on separate procedural agenda |
| Lambda C1 | M-matrix Q_lambda inverse and positive loss decreasing; local bracket | §7 Proposition6 and Appendix lambda | `verification/stage11/adjustment_cost_replay.log` | PASS local only |
| Network-face and narrow active strip C2 | exact welfare face polynomial and near-transition Taylor/compactness inequalities | compact §7, Appendix network face/strip | `verification/stage11/network_face_replay.log`, Stage21 proof record | PASS face + restricted strip only |
| Figure3 | numerical classification for 41x41 two treatments and bounded proposal search | §5 illustration and caption | Stage11 r1 reproducibility: 3362/3362, 11 regression errors repaired, and IS/SW stress checks | PASS as exploratory candidate illustration; **NOT exact all-parameter proof** |

## Proof-critical bridges preserved after compression
1. Individuals maximize *their own* three-market operating profit net once-paid differentiating cost; holding rival designs fixed, not maximizing joint profit along symmetric paths.
2. Network expectations fixed during unilateral Cournot variation, then fulfilled at equilibrium.
3. National welfare counts own country consumer surplus plus worldwide profit of its *resident* firm, not global sum.
4. `W_{A,x}=(-C,-C-V,-C-V)` with **plus V within loss**, own FOC removes only private profit derivative.
5. Every incidence/symmetry local derivative is separated from `g∈[0,1]` interval certificate and uniformly strict primitive-open continuation.
6. Government makes an *optimal proposer choice* not a welfare-maximizing international social planner's decision; feasible depth set closed under weak votes.
7. Full Nash uniqueness justifies SU/IS symmetry reduction and lift, including off-symmetric unilateral deviations; scalar interval Newton is not incorrectly described as full 3D Krawczyk.
8. Figure3 gray cells remain search nonfindings, not nonexistence certificates.
9. No material step delegates an unnamed logic object to program output; exact targets, intervals, inequalities, and limitations stated in supplement.

## Material missing-bridge audit
- **SUBSTANTIVE DEFECT:** none newly detected in this *exposition-only* Stage13 review; this is not a second hostile Stage11 math proof.
- **BRIDGE NEEDED:** none introduced by streamlining. Appendix continues to identify exact algorithm and full-root restoration.
- **APPENDIX DETAIL NEEDED:** none newly introduced; exact historical logs and code remain linked by immutable commit.
- **ROUTINE:** familiar repeated algebra omitted deliberately, with correct definitions and equations retained.

**Decision: PASS — REVIEWER VERIFIABILITY** for integrated sources **subject to successful two-pass PDF build and no missing included files**. If PDF/LaTeX auto-build fails, Stage13 cannot close. Do not treat replay success as new exact generality.
