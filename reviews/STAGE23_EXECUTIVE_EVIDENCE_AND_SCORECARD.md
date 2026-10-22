# V2b Stage 23 — Executive verdict, provenance, independent checks
As of 2026-10-22 JST. **Research verdict: REOPEN (evidence-sensitive), NOT STOP. Submission readiness: NO.** No journal is recommended for submission at this gate. This is an internal simulated adversarial review, NOT external peer review.

## Model, provenance, and correct scope
- Stage22 Draft PR #22: head `d8e76f9f865f3e5a0573ae4df342367a9ddfbe39`; primary theorem text `reviews/STAGE22_ABC_PROPOSITIONS_AND_PROOFS.md` (blob `0fe83ebb5ec4a8d0202328b39a8f4a0dfd9a141a`).
- Stage21 PR #21 (head `ace62cdc8d5f8020534012d42d2a88a7f593dfda`), `reviews/STAGE21_NO_SU_MISSING_MIDDLE_THEOREM.md` (blob `de4069ab74ca007c109ac72b341466e3ef157970`).
- Historical Stage14 original exact interval results: `verification/stage14/canonical_global_rerun.log` (blob `0ea8acff4887367497dd12c4fea0b7749be43e2c`) and `verification/stage14/pareto_rerun.log` (blob `acda89acf84ab943f4f40195aaf77556a626dc20`). Stage14 main review `reviews/STAGE14_THEOREMS_AND_PROOFS.md` (blob `eb57875822f480ca3a9d151862d60f379f8bc537`).
- The restored research input is `M=I+B-eta H`, `B=rho H+(1-rho)X`, `CS=q'Bq/2`, `Pi_i=3q_i^2-K_i(x_i)`, `W_i=CS+Pi_i`; originally `K_i=kappa(1-x_i)^2/2` (lambda=0). The optional `lambda(x_i-z)^2/2` is strictly an EXTENSION.
- Original three-country government agenda: A proposes AB at depth g, B votes anticipating later C accession at **identical inherited g**, and C plus incumbents may veto. Weak votes accept. SW=no substantive links; SU=one bilateral link; IS=three country links. Government maximizes actual terminal payoff, not merely local vote surplus.
- Past PR9 sign issue **corrected**: induced welfare loss is `C(2u'+v')+V(u'+v')`, plus rival-export-profit incidence. Do not use the historical minus sign.

## Independent reconstruction completed in Stage23
A NEW local clean-room Cournot/design-Nash numerical reconstruction, without importing repository scripts, was run in Python 3.13.5, NumPy 2.3.5, SciPy and SymPy 1.14.0. The authoritative fresh code and output are attached in this Stage23 ChatGPT conversation (`independent_reconstruction.py`, `reconstruction_log.json`); source should be mirrored to this branch before claiming repo-local reproducibility.
At canonical (d,eta,rho,kappa)=(1,0.758,0.9,0.8505), z=0.7185927073221112:
- g=.05 FROZEN: m-s=+0.0002723816371; i-o=+0.0002346166682; i-s=+0.0193186156452.
- g=.05 ENDOGENOUS: m-s=-0.0004734741714; i-o=-0.0012465472341; i-s=+0.0169346279054.
- Independently reconstructed origin D=+0.0067679241288, L=+0.0150697441253, mu=D-L=-0.0083018199964; u'=+0.0608102317352, v'=+0.0323048168863.
- SymPy EXACT identities rechecked: rho=1 face m-s factorization, i-o polynomial expression and eta=6/7 strict quadratic signs; d(mu)/d(eta)=2401*d^2/512 and d(mu)/d(beta)=10339*d^2/2048 at the critical face; cutoff beta slope = -211/196. These are VERIFIED mathematical identities (assuming model expressions), not all-depth Nash certification.

Historical independent Stage14 interval log reports `KRAWCZYK SIGN CERT SUCCESS accepted=1000 splits=0` and uniform upper bounds `m_g < -0.0079701929973`, `(i-o)_g < -0.0150388833377`. Frozen all-depth comparator reports accepted positive IS and upper SU-envelope. This code was inspected via connector, and GitHub Stage22-associated historical Actions report success. **Stage23 **DID re-execute the original Stage4A full-depth Krawczyk/Rosen source through GitHub Actions on the Stage23 head**; the current CI evidence is linked below. The local container did not clone or re-run this code independently, and no new independently authored global interval algorithm was implemented. Distinguish successful CI reproduction of the existing code from a complete line-by-line independent proof audit. Do NOT equate finite-depth reconstruction with full certification. Stage18 global lambda=5 theorem is inherited, not independently rerun.

## Four-axis research assessment
- STRUCTURE: CONDITIONAL — known ingredients (network/Cournot, endogenous private design, standard coalitions), with a materially specified government-before-design and three-country inherited-depth accession combination.
- MECHANISM: CONDITIONAL — country incidence of firms' Nash responses reversing TWO distinct consent constraints; plausible nontrivial residual, not yet cleared of general theoretical absorption.
- PROPOSITIONS: CONDITIONAL — local identity and pointwise signs independently reconstructed; inherited all-g center and Stage21 region require full proof replay; C1 uniquely LOCAL, C2 rho=1 special case and rho<1 restricted strip.
- ECONOMIC SIGNIFICANCE: CONDITIONAL — implementation of Pareto-improving standards contingent on private repositioning and legal agenda; baseline numerical payoff difference is small and uncalibrated, but categorical equilibrium reversal is not dismissed merely due to magnitude.

## Research quality scorecard
| Axis | Gate | Evidence and limitation |
|---|---|---|
| Mathematical Correctness | CONDITIONAL | Fresh local reconstruction, plus successful GitHub full-depth Krawczyk replay on Stage23 SHA; line-by-line interval-proof audit remains |
| Structural Novelty | CONDITIONAL | Coherent distinct staging; antecedent design/standards already present |
| Mechanism Novelty | CONDITIONAL | Controlled fixed-x versus endogenous-x country consent reversal |
| Proposition Novelty | UNVERIFIED | Cheng-Huang final numbered text and additional general theories incomplete |
| Economic Significance | CONDITIONAL | Participation wedge; institution-specific and quantitatively uncalibrated |
| Robustness and Scope | CONDITIONAL | Open neighborhood asserted under uniform certificate; rho=1 exact, rho<1 narrow |
| Institutional Plausibility | CONDITIONAL | Inherited bilateral-depth gate plausible in some lock-in arrangements, not generic ISO |
| Independent Paper Contribution | UNVERIFIED | Unresolved strongest direct or mechanism-equivalence literature gate |
| Standard Journal Threshold | UNVERIFIED | Cannot endorse submission before the novelty gate |
| Submission Readiness | FAIL | No Stage23 final full manuscript nor Stage23 all-depth rerun, and literature gate open |

## Explicit decision
**REOPEN, not STOP:** no independent mathematical contradiction or demonstrated full predecessor absorption was identified. This does not justify a preemptive GO. Necessary minimal actions: (1) complete published Cheng-Huang numbered results and Buccella online horizontal-differentiation supplement absorption map; (2) archive the NEW Stage23 GitHub Actions full-depth replay log and formally inspect all proof assumptions, boundaries, and source SHA256; (3) provide institutional foundation or a tiny alternate veto/depth-renegotiation sensitivity, without changing main model; (4) after the above, editor-level significance gate. No unconditional generalization is demanded.

**Question:** Does this research offer a sufficiently novel and economically meaningful theoretical contribution, considering its complete model structure, strategic mechanisms, propositions, and implications, to justify submission to a credible peer-reviewed economics journal? **NOT YET VERIFIED** (corresponding to **REOPEN**).

## Stage23 current-head exact all-depth CI rerun — NEW EVIDENCE (2026-10-22)

This section supersedes the earlier 'fresh replay UNVERIFIED' label **for CI execution only**. On GitHub Actions Stage23 head `47c438e991122dcaad597ad46d09327e0e5e45e8`, the original Stage4A independent Krawczyk workflow **completed successfully**: [run 39738980678](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39738980678), job 119691340931. Decoded Actions job log gives:

```
INDEPENDENT PROFIT DEVIATION PASS: max FOC error 6.802372276570878e-10
KRAWCZYK SIGN CERT SUCCESS accepted= 1000 splits= 0 max upper derivatives= -0.007970192997334808 -0.015038883337750794 seconds= 10.939080222000001
FROZEN CERT SUCCESS C lower gain= 0.0002346166230648035 IS lower= 2.441397037346308 SW upper= 2.4220784217382687 SU upper= 2.423573564131729
PASS: adversarial stage 4A independent method, all g∈[0,1]
```

Also [Stage23 local reconstruction run 39738980649](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39738980649) succeeded, with frozen vs endogenous signs and exact rho=1 face identities. [Stage14 mechanism run 39738980808](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39738980808) and [continuous-depth certificate run 39738980852](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39738980852) succeeded. **This is a VERIFIED rerun of the existing certificate on the Stage23 GitHub source, not a wholly new independent proof.** Fresh validation of assumptions and source-to-inequality coverage is still CONDITIONAL. The 2026-10-22 nonlinear alternative check separately reported an original frozen-design C-vote FAIL at g=.05 before proving an existential coalition reversal at g=.005; it is not a main-model counterexample.
