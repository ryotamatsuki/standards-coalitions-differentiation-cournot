# Standards Coalitions, Endogenous Product Differentiation, and Cournot Competition

**Status: WORKING NOTES — NO THEORY FREEZE / NO SUBMISSION AUTHORIZATION.**  
Last archived: 2026-10-21 (Asia/Tokyo). This repository captures exploratory conversations and independently reproducible algebra checks; it is **not** a completed or refereed proof of a unique subgame-perfect equilibrium.

## Research question

Three initially symmetric countries A, B, C each host one firm; each firm sells in all three countries. Governments negotiate a common *minimum product-homogeneity / harmonization depth* and firms subsequently choose realized homogeneity subject to that floor. Harmonization increases same-standard network usefulness but also makes products closer substitutes in Cournot markets.

**Timing (current version):**

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
