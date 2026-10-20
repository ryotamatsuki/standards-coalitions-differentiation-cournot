# Standards Coalitions, Endogenous Product Differentiation, and Cournot Competition

**Status: WORKING NOTES — NO THEORY FREEZE / NO SUBMISSION AUTHORIZATION.**  
Last archived: 2026-10-21 (Asia/Tokyo). This repository captures exploratory conversations and independently reproducible algebra checks; it is **not** a completed or refereed proof of a unique subgame-perfect equilibrium.

## Stage 2 literature novelty gate — 2026-10-21

**Canonical Stage 2 verdict: CONDITIONAL GO (not closed).**
- Broad novelty claims **KILLED**: compatibility-versus-competition, endogenous design per se, 3-country standards unions and outsider veto, differentiation's influence on country-standard incentives, and network strength versus substitutability are established earlier.
- Restricted V2b candidate **UNRESOLVED**: ex-ante government g commitment -> ex-post costly firms' design Nash -> positive-depth IS under frozen x but no positive-depth agreement under endogenous x.
- A decisive governmental predecessor is Gandal & Shy (2001), whose original theorem text was not obtained. **One material Stage 2 blocker:** original-source theorem absorption for government standards-union models, led by Gandal–Shy and complemented by Baake–Boom timing comparison. No lack-of-access inference of novelty.
- Full and partial primary/source comparisons (15 items): [closest-paper ledger](literature/V2B_STAGE02_CLOSEST_PAPERS_2026-10-21.md).
- [Canonical gate report and absorption map](reviews/V2B_STAGE02_NOVELTY_KILL_GATE_2026-10-21.md).
- Stage 4A independent mathematical adversarial audit **not yet conducted**. Stage 6 novelty recertification may **not** start before Stage 2 completion and Stage 4/4A GO. No theory freeze.

---

## Current frontier: V2b additive design/compatibility separation (2026-10-21)

**Latest result: a computer-assisted continuous-g coalition reversal certificate at an exact rational parameter witness.**
- [Full proof statement, assumptions and computational scope](docs/V2B_CONTINUOUS_REVERSAL_CERTIFICATE_2026-10-21.md)
- [Reproducible interval proof script](verification/v2b_interval_reversal_certificate.py)
- [Earlier finite-grid witness](docs/V2B_REGIME_REVERSAL_NUMERICAL_WITNESS_2026-10-21.md) retained as historical preliminary evidence.

V2b **differs materially from V1**: governments choose compatibility `g`, firms choose residual homogeneity `x_i`, and cross-firm substitution is `B_ij=rho*H_ij+(1-rho)*(x_i+x_j)/2`. Firms incur symmetric real design cost `kappa*(1-x_i)^2/2`. V1's `z_i >= g` constraints, welfare and cutoffs **do not carry over**.

At `eta=0.758, rho=0.9, kappa=0.8505`, rational-interval checks over the full continuum establish that the **endogenous-firm-choice game selects no positive-depth agreement**, while a **frozen-SW-design counterfactual admits a positive-depth IS that dominates every SU policy**. The inequalities persist in a nonempty but unquantified open neighborhood. This is a **conditional computer-assisted result**, not an independent human-reviewed theorem or a claim of originality. No theory freeze or submission authorization has been granted.

---

## Archived V1 research question (historical specification)

Three initially symmetric countries A, B, C each host one firm; each firm sells in all three countries. Governments negotiate a common *minimum product-homogeneity / harmonization depth* and firms subsequently choose realized homogeneity subject to that floor. Harmonization increases same-standard network usefulness but also makes products closer substitutes in Cournot markets.

**Archived V1 timing (not the latest V2b design game):**

1. A proposes an A–B standards union and common depth `g ∈ [0,1]`; B accepts/rejects. Rejection gives SW.
2. If A–B forms SU, C applies to join or stays outside.
3. A and B approve/reject C's application; upon approval IS forms at **exactly the same depth g fixed at Stage 1** (no renegotiation).
4. Firms simultaneously choose homogeneity `z_i`: SW all `[0,1]`, SU members `[g,1]` / outsider `[0,1]`, IS all `[g,1]`.
5. Cournot competition in each of the three symmetric national markets, with fulfilled expectations for network sizes.

No side payments; acceptance at indifference is a **selection convention** rather than an intrinsic property of the game. Distinguish literal SW/SU/IS institutional labels from economically equivalent zero-depth outcomes.

## Navigation

- [Full primitives and timing](docs/MODEL_SPECIFICATION.md)
- [Equilibrium algebra, regime classifications, caveats](docs/EQUILIBRIUM_LEDGER.md)
- [Chronology and changes of assumptions](docs/RESEARCH_HISTORY.md)
- [Symmetric standards-adoption costs and SU example](docs/COST_EXTENSION.md)
- [Empirical interpretation and limits](docs/APPLICATIONS_AND_SCOPE.md)
- [Prior literature / audit queue](literature/PRIOR_ART_QUEUE.md)
- [Open problems and proof requirements](reviews/OPEN_PROOF_OBLIGATIONS.md)
- [Reproducible SymPy checker](verification/symbolic_audit.py)

Run `python -m pip install sympy scipy` and `python verification/symbolic_audit.py` to check the published working identities and illustrative parameter values.

## Key guardrails

- Do **not** copy theory-freeze labels or submission readiness from older projects.
- Do **not** silently assert all SPNE are classified. Some continuation equilibria, off-path histories, and tie-breaking remain unverified.
- The claimed `4/5`, `6/7`, and `~0.884049` cutoffs belong to the specific quadratic-utility model and the recorded equilibrium-selection conventions.
- An early model **allowed IS renegotiation** of depth; the current model **forbids it**. Results from these variants must never be mixed.
- This project is distinct from [endogenous-interoperability-standards-coalitions](https://github.com/ryotamatsuki/endogenous-interoperability-standards-coalitions) (previously terminated affine-Bertrand / spatial line of research) and [private-compatibility-standards-coalitions](https://github.com/ryotamatsuki/private-compatibility-standards-coalitions).

## Research stance

Preserve zero-cost symmetric baseline even if SU does not survive on the equilibrium path; report the limitation rather than tuning costs to force a desired result. Symmetric adoption-cost extensions are exploratory, not the canonical baseline.
