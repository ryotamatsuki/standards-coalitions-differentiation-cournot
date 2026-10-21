# Standards Coalitions, Endogenous Product Differentiation, and Cournot Competition

## LATEST WORKFLOW STATUS — STAGE 9 GO (2026-10-21)

- **Stage9 reproducible production scaffold COMPLETE** without altering any Stage8 economic primitives, proof source, Lean kernel file or the exact-v2b parameter witness. [Stage9 gate report](reviews/V2B_STAGE09_REPRODUCIBILITY_GATE_2026-10-21.md).
- **[CI — ALL FIVE JOBS PASS](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39524698485)**: frozen 9-blob source-integrity guard, canonical Stage4A+Pareto/national welfare, nonlinear p=2 Rosen+all-g government inequalities, limited Lean4 arithmetic proof and LaTeX/BibTeX scaffold build. An initial first-run LaTeX formatting error was corrected; [failed run](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39524532077) retained.
- [Production instructions and Makefile commands](production/README.md); [LaTeX scaffold](paper/main.tex) with model/equilibrium/results/welfare/robustness/literature/discussion/proofs sections; [original-paper bibliography](paper/references.bib), [deterministic welfare-table generator](production/scripts/generate_welfare_table.py), [fixed Python3.12 dependencies](production/requirements-stage9.txt), [frozen 9-blob manifest](production/freeze_manifest.json).
- [Theorem/evidence correspondence T1–T7](production/THEOREM_CERTIFICATE_MAP.md) and [benchmark, negative-experiment and proof-failure register](production/BENCHMARK_AND_FAILURE_REGISTER.md). **Lean proves only 4 pointwise rational PROXY inequalities** and baseline all-g math remains Stage4A computer-assisted. p=2 pre-registered frozen C at g=.05 remains a failure.
- GitHub Actions includes a **downloadable 7-day PDF BUILD ARTIFACT (Stage9 shell, NOT manuscript)**. **NEXT: Stage10 section-by-section paper construction.** Theory freeze ID V2B-THEORY-FREEZE-2026-10-21-v1 remains authoritative.

---


## CURRENT CANONICAL STATUS — STAGE 8 THEORY FREEZE COMPLETE (2026-10-21)

- **Freeze identifier:** `V2B-THEORY-FREEZE-2026-10-21-v1`. **[AUTHORITATIVE frozen V2b model and theorem/proof register](docs/V2B_THEORY_FREEZE_2026-10-21_v1.md)**, original frozen Git blob SHA `ca16f0d4699364c7466d463c40e01cb5eaa2d8e5`. **[Stage 8 checklist and freeze certificate](reviews/V2B_STAGE08_THEORY_FREEZE_CERTIFICATE_2026-10-21.md)**.
- **Author's user-message approval:** 「承認する」 to the previously specified institution-specific existence proposition; documented in [Author Intellectual Contribution Record](reviews/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD_V2B_2026-10-21.md). Approval DOES NOT claim personal independent reproduction of AI/math proofs.
- **Stage 7.5A NOW GO, not conditional:** [Final scope/portability/formal GO](reviews/V2B_STAGE075A_FINAL_GO_AFTER_AUTHOR_CONFIRMATION_2026-10-21.md). Earlier CONDITIONAL GO and Stage 7.5 original diagnostic failure remain historical records.
- **Formal Verification Gate:** **PASS — selected pointwise exact-rational arithmetic proof-critical CORE only**. [Lean 4 source](formal/V2bWelfareCore.lean), [CI PASS](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39517673634). NOT a complete formalized Nash/SPNE or all-g model theorem, which relies separately on Stage4A interval proofs.
- Canonical V2b φ(x)=x; separately certified p=2 φ(x)=x² diagnostic robustness, with **g=.05 frozen C approval FAILURE** still on record, but existential positive-depth frozen IS at g=.005 independently interval proven. Positive-depth endogenous governments do not agree for any g at exact witness; hypothetical IS(.05) is Pareto better than SW in both tested φ models. **Institution-specific, not generic.**
- **NEXT STAGE = Stage 9 — production/reproducibility setup**, NOT journal manuscript submission. Stage8 frozen economic rules cannot be modified without change control/affected audit replay. Old docs/MODEL_SPECIFICATION.md, docs/EQUILIBRIUM_LEDGER.md are HISTORICAL V1, explicitly marked not current V2b.

---


## CURRENT CANONICAL GATE — Stage 7.5A CONDITIONAL GO (2026-10-21)

- **Generality/quantifier/portability audit completed.** The headline is an **INSTITUTION-SPECIFIC existential counterexample** under the specified A/B-first unchanged-g/C opt-in consent game, with both φ(x)=x and φ(x)=x² proving the exact-witness frozen-positive-IS versus endogenous-no-positive-coalition reversal. No generic result for all design/network functions or alternative institutional agendas.
- [Stage 7.5A claim-scoped Contribution Robustness Certificate](reviews/V2B_STAGE075A_CONTRIBUTION_ROBUSTNESS_CERTIFICATE_2026-10-21.md). The φ=x² original fixed-depth g=.05 frozen C application **FAILED**, while certified g=.005 frozen C application is positive by only ≈9.1×10⁻⁷. Preserve both facts and avoid same-depth claims. A direct unanimous ABC offer at g=.05 would be accepted relative to SW in the separate hypothetical protocol, highlighting agenda-specific blockage.
- **Lean 4 v4.24.0 exact-rational proof-critical welfare core: PASS, LIMITED SCOPE.** [Lean source](formal/V2bWelfareCore.lean); [CI PASS](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39517673634); [source/theorem fidelity, standard axiom and exclusion ledger](reviews/V2B_STAGE075A_FORMAL_VERIFICATION_GATE_2026-10-21.md). Formally verifies FOUR inequalities at explicit RATIONAL design proxies only. Actual Nash root enclosure, full g continuum and full economic SPNE remain in separate Stage4A interval certificates; no full-model Lean proof.
- [Canonical Stage 7.5A CONDITIONAL GO red-team report](reviews/V2B_STAGE075A_GENERALITY_FORMAL_RED_TEAM_GATE_2026-10-21.md). **ONE REMAINING BLOCKER:** [AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD draft](reviews/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD_V2B_2026-10-21.md) needs author's substantive judgment/confirmation of mechanism, model assumptions, scope and proof limits; do not misrepresent author independent verification.
- **Stage 8 THEORY FREEZE / manuscript NOT AUTHORIZED until Stage 7.5A closes after author review.** Earlier Stage7.5 and Stage6/7/4A results stand within their historical scopes. Do not retune coefficients, change canonical model or hide negative robustness results.

---


## CURRENT RESEARCH GATE — Stage 7.5 GO → Stage 7.5A (2026-10-21)

- **Stage 7.5 CONDITIONAL GO blocker CLOSED for the NARROW EXISTENTIAL claim**, NOT for original fixed-depth g=.05 robustness. The exact SAME parameters and 2+1 government institution were held fixed under a pre-registered non-cosmetic residual-design variant `X_ij=(x_i²+x_j²)/2`. The complete **endogenous SW-equivalent** versus **frozen-design positive-depth IS** reversal was proven again, now at frozen `g=1/200=.005`, with independently certified firm Nash/global welfare signs for all g.
- **DO NOT ERASE THE NEGATIVE RESULT:** under the nonlinear alternative at originally pre-registered `g=.05`, frozen C still **rejects** IS (gain ≈ −0.000440395). The positive g=.005 participation gain is extremely small (≈9.10×10⁻⁷); the existential claim survives, the uniform/same-g claim does not.
- New reproducible global certifications: [entire 3-firm asymmetric strategy Rosen uniqueness](verification/v2b_alt_quadratic_rosen_interval.py); [all-g nonlinear agreement and positive frozen g=.005 IS](verification/v2b_alt_quadratic_policy_interval.py); [dedicated 2-job CI, both PASS](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39516205888). Earlier first CI run FAILED due a variable-name typo; fixed and re-run PASS, with original failure log retained.
- [Stage 4/4A diagnostic math proof ledger](reviews/V2B_ALT_QUADRATIC_STAGE04_04A_CERTIFICATION_2026-10-21.md). [Stage 6/7 limited regression (no new priority claim)](reviews/V2B_ALT_QUADRATIC_STAGE06_07_REGRESSION_2026-10-21.md). [Current canonical Stage 7.5 full-theory investment decision — GO](reviews/V2B_STAGE075_REPAIR_CLOSURE_AND_FULL_THEORY_GO_2026-10-21.md).
- **NEXT MANDATORY STAGE: Stage 7.5A quantifier/portability red team AND formal-verification gate**. Stage 8 freeze/manuscript NOT YET authorized; no claim of all-formulation generality or publication-level academic novelty.
- CANONICAL V2b `X_ij=(x_i+x_j)/2` remains **unchanged**. The quadratic design map is a *diagnostic robustness experiment* only. Real-world bilateral technology coordination (GSM, ChaoJi) supports **motivation**, not exact 2+1 sovereign accession rules or empirical C refusal.

---


## Current route: Stage 7 GO / Stage 7.5 CONDITIONAL GO (2026-10-21)

- **Theory-paper convention:** A faithful reconstruction of ISO voting or a demonstrated historical three-country accession veto is **not a prerequisite** for a stylized economic theory paper. The abstraction must instead explain the causal question, defend pivotal institutional assumptions and restrict external claims. Original examples: **France–Germany GSM** and **Japan–China ChaoJi** pre-international/bilateral technical cooperation. A/B consent + C application + fixed inherited g is **a model assumption**, not a claimed ISO/GSM/ChaoJi procedure.
- [Stage 7 welfare, generality and institutional audit — restricted GO](reviews/V2B_STAGE07_WELFARE_GENERALITY_INSTITUTIONAL_GATE_2026-10-21.md): endogenous IS at g=.05 has strictly positive country welfare advantage over SW of ~0.016934628, world gain ~0.050803884, yet is strategically blocked by canonical AB-first agenda. This is diagnosis, not an implemented remedy or unrestricted first best. [Independent welfare evaluator CI PASS](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39512057217).
- [Stage 7.5 full-theory investment decision — CONDITIONAL GO](reviews/V2B_STAGE075_FULL_THEORY_INVESTMENT_DECISION_2026-10-21.md). One material blocker: fully quantify portability of original full-game coalition-regime inversion to a credible non-cosmetic product-similarity function.
- [PRE-REGISTERED nonlinear design alternative](reviews/V2B_STAGE07_DESIGN_PORTABILITY_PREREG_2026-10-21.md): `X_ij=(x_i²+x_j²)/2` (diagnostic only, unchanged eta/rho/kappa and institutional game). [Recomputed Nash and 201-depth grid](verification/v2b_stage075_nonlinear_design_diagnostic.py), [CI PASS for **honest diagnostic execution**](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39514462211). Endogenous SU negative + C refuses + IS Pareto gain survive at g=.05; but fixed-design **C accession fails at the pre-specified g=.05** (gain ~−0.000440395), so the pre-registered fixed-g robustness criterion **FAILS**. Tiny positive fixed-design C gain at g=.005 is exploratory and does NOT retroactively pass pre-registered test or certify global SPNE.
- **No Stage 7.5A GO, no Theory Freeze, no manuscript, no broad novelty, no formal Lean PASS.** Next a single bounded original-parameters nonlinear-X full-continuum firm/government verification, then rerun relevant gates. No ad hoc model adjustment or coefficient tuning. Stage-6 restriction and historical unavailable-paper source caveats remain.

---


> **Stage 7 institutional evidence update (2026-10-21):** [Four primary-source cases of bilateral/multi-party pre-international technical alignment](literature/V2B_STAGE07_PRE_INTERNATIONAL_TECHNICAL_ALLIANCES_2026-10-21.md): strongest engineering analogue = **Japan–China ChaoJi (CHAdeMO/CEC 2018, international experts join 2019, IEC track later)**; strongest government/bilateral→multilateral trajectory = **France–Germany GSM (1984, 13 countries' telecom operator MoU 1987)**. US–EU TTC = governmental standards-position coordination, NOT deployed positive-g compatibility; Australia–NZ joint standards = cooperation often *after* international-first adoption. **No case establishes the exact C sovereign application/AB unanimous veto or observed design-induced rejection.** These analogues strengthen motivation but do not validate the full V2b institution or prove generality. No model or gate change.


> **STAGE 6 ROUTING UPDATE — 2026-10-21:** The former CONDITIONAL GO is superseded by **GO strictly for Stage 7 welfare/generality/institutional validation** after an added exact-rational inequality: at g=1/20, **endogenous** firm-design IS is strictly Pareto superior to SW (W_IS−W_SW∈[0.0169346278736,0.0169346279395]), although Stage-4A proves that all g>0 SU member payoffs fall below SW and outsider C vetoes IS. Thus grand interoperability is socially attractive but unattainable under the prescribed sequential A/B-first consent; the fixed-SW-design policy game instead selects positive-depth IS. This is a **narrow model-specific economic contribution**, not the general investment/standardization paradox already in Cabral–Salant or a claim that two independent sign flips were found (the C entry derivative is twice AB's by symmetry). Evidence: [Stage 6 closure](reviews/V2B_STAGE06_CONTRIBUTION_CLOSURE_2026-10-21.md), [rational interval reproduction](verification/v2b_stage06_pareto_holdout.py), [CI PASS](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39509567087). Academic-priority and alternative-model portability remain UNRESOLVED; no theory freeze.


> **Published original-source update (2026-10-21):** The author supplied the complete Gandal–Shy (2001) *Journal of International Economics* paper (21 pages). All five propositions and the model, union and network sections were reviewed. The historical "full text missing" designation below is superseded. **The paper DOES NOT directly absorb the restricted V2b ex-post firm-design coalition reversal**, although government standards unions, mutual-recognition dominance, outsider welfare and network effects are established prior art. Crucially, Gandal–Shy's **no formal union can still yield fully mutual recognition**, which differs from V2b's incompatible SW. **Stage 6 remains CONDITIONAL GO** due to wider prior-art/editorial questions. Full proposition mapping: [Gandal–Shy original-paper audit](literature/GANDAL_SHY_2001_FULLTEXT_V2B_ABSORPTION_2026-10-21.md).


## Stage 6 — Novelty Re-Kill: CONDITIONAL GO (2026-10-21)

- **CURRENT-PAPER CANONICAL VERDICT: CONDITIONAL GO**, not novelty certification. Stage 4A restricted mathematical PASS persists, but originality is **UNRESOLVED / PARTIALLY ABSORBED** and Stage 7 is **not yet unconditionally authorized**.
- **New serious predecessors:** Cabral–Salant (2014 IJIO; fully inspectable 2008 WP, Props 1–3) already proves investment-driven failure of otherwise appealing standardization; Buchholz–Hattori (2024 Economic Modelling; inspectable 2021 WP Props 1–3) already proves coalition–endogenous technology paradoxes. 2025 Takarada–Kawabata §5.4 discusses exogenous differentiation changing regional standards incentives. Retract any broad claims that these general mechanisms are novel.
- **One material blocker:** explain/prove substantive independent economic knowledge in the *narrow* V2b result — **governments commit fixed-depth compatibility, firms select costly residual substitutability afterward, and both AB union incentive and C accession incentive change sign** — that is not already an immediate known investment-and-coalition corollary. Without this, downgrade to NO-GO or research note instead of ad hoc model expansion.
- **User instruction honored:** Gandal–Shy (2001) NOW fully reviewed; unavailable Baake–Boom (2001) and revised journal proof texts remain expressly UNRESOLVED source limitations, **not** evidence of novel theory; work not stopped for unavailable full text.
- [Full Stage 6 canonical verdict, proposition ledger, editor-value audit, independent future questions](reviews/V2B_STAGE06_NOVELTY_REKILL_2026-10-21.md).
- [Updated actual-theorem / generic-parent absorption matrix](literature/V2B_STAGE06_PARENT_THEOREM_ABSORPTION_2026-10-21.md).
- **Next:** one bounded Stage 6 contribution/parent-theorem absorption closure, followed by Stage 6 GO → Stage 7 if successful; otherwise NO-GO/narrow research-note disposition. No theory freeze.

---


**Status: WORKING NOTES — NO THEORY FREEZE / NO SUBMISSION AUTHORIZATION.**  
Last archived: 2026-10-21 (Asia/Tokyo). This repository captures exploratory conversations and independently reproducible algebra checks; it is **not** a completed or refereed proof of a unique subgame-perfect equilibrium.

## Stage 4A — independent adversarial mathematics: restricted GO (2026-10-21)

- **Canonical verdict: GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS, narrowly for the V2b exact-rational witness/open-neighborhood sign reversal.** No universal all-parameter government SPNE theorem, mathematical portability or claim of academic priority.
- [Stage 4A theorem-scope and red-team audit](reviews/V2B_STAGE04A_ADVERSARIAL_CERTIFICATION_2026-10-21.md).
- [Independently rederived SU and IS policy-root Krawczyk verifier](verification/v2b_stage04a_krawczyk_cleanroom.py). [GitHub Actions PASS](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39480815816). **1,000 rational g intervals; 0 unresolved sign or enclosure cells.** Checks frozen benchmark at g=.05 versus all SU policies, plus unilateral firm profit perturbations.
- Reviewer had access to public Stage-4 claims: not a fully blinded clean-room review. New script does **not** call previous solvers and uses Krawczyk/interval Newton instead of original Poincare–Miranda face-sign approach; both methods still share SymPy/mpmath interval arithmetic and require later proof-assistant/audited implementation as appropriate.
- Preliminary Formal Verification Gate = **FORMALIZATION APPLICABLE**; no Lean/mathlib or other formal verification PASS. Highest-priority target is quantified all-g derivative signs and root enclosures. Reassess and close at Stage 7.5A, not Stage 4A.
- **Next: Stage 6 Novelty Re-Kill** with theorem-by-theorem prior art. User requested skipping inaccessible full texts for now; Stage 2 remains literature-conditional, and inaccessible predecessor results remain an explicit unresolved novelty threat, not evidence of originality.
- Formal government membership at g=0 is indifference-selection dependent; theorem concerns **substantive positive-depth agreements** only.

---

## Stage 4 minimal-model gate — restricted GO (2026-10-21)

- **Canonical verdict: GO for the exact-rational V2b witness and continuity-open neighborhood only.** Government substantive IS under frozen SW designs versus no positive-depth union under endogenous costly designs.
- Complete input and proof-scope ledger: [Stage 4 audit](reviews/V2B_STAGE04_MINIMAL_MODEL_GATE_2026-10-21.md).
- Independent-from-production Stage-4 primitive reconstruction: [script](verification/v2b_stage04_primitive_reconstruction.py), [CI](.github/workflows/v2b-stage04-primitive.yml); **PASS**. This is a second implementation and numerical diagnostic, **not** the logically independent Stage-4A red-team gate.
- Full continuum sign certificate: [rational-interval source](verification/v2b_interval_reversal_certificate.py); [CI run](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39472853173) previously **PASS**.
- **Next: Stage 4A independent mathematical adversarial certification**, including a preliminary formalization-applicability decision. Stage 2 inaccessible old-paper theorem priority still UNRESOLVED by author instruction.
- NOT certified: broad full-parameter SPNE mapping, independent proof audit, general functional-form portability, theorem-level novelty, theory freeze or manuscript readiness.

---

## Stage 3 candidate selection — GO (2026-10-21)

- **Selected model: V2b only** for the upcoming Stage 4 mathematical gate. V1 is an archived baseline; V2a multiplicity is a preserved negative; additional adoption costs / interface aftermarket / market-access law are deferred.
- [Formal Stage 3 GO and contribution memo](reviews/V2B_STAGE03_CANDIDATE_SELECTION_2026-10-21.md).
- [Independent primitive-first Stage 3 policy-feedback diagnostic](verification/v2b_stage03_mechanism.py) and [CI workflow](.github/workflows/v2b-stage03-feedback.yml) (PASS).
- At witness (eta,rho,kappa)=(0.758,0.9,0.8505), SU member direct marginal welfare = +0.006767924; endogenous firm-design feedback = -0.015069744; **total = -0.008301820**. This is an exactly specified model-specific local numerical decomposition, not a universal theorem.
- **Stage 2 remains CONDITIONAL GO** because original government-standards predecessor theorem access is incomplete; the user authorizes proceeding provisionally, not treating missing sources as novelty evidence.
- Stage 4 construction/mathematics gate **next**; Stage 4A clean-room adversarial audit then Stage 6 novelty re-kill, conditional on legitimate routing.
- No theory freeze, no academic priority claim, no full-game mathematical adversarial certification.

---

## Stage 2 literature novelty gate — 2026-10-21

**Canonical Stage 2 verdict: CONDITIONAL GO (not closed).**
- Broad novelty claims **KILLED**: compatibility-versus-competition, endogenous design per se, 3-country standards unions and outsider veto, differentiation's influence on country-standard incentives, and network strength versus substitutability are established earlier.
- Restricted V2b candidate **UNRESOLVED**: ex-ante government g commitment -> ex-post costly firms' design Nash -> positive-depth IS under frozen x but no positive-depth agreement under endogenous x.
- The decisive governmental predecessor Gandal & Shy (2001) has NOW been verified in the full published original; its five propositions do not directly absorb V2b's narrow post-policy design reversal. **One material Stage 2 blocker:** original-source theorem absorption for government standards-union models, led by Gandal–Shy and complemented by Baake–Boom timing comparison. No lack-of-access inference of novelty.
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
