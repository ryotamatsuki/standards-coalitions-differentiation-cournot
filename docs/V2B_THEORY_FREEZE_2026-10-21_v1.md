# V2B-THEORY-FREEZE-2026-10-21-v1
**Stage:** 8 — Canonical Theory Freeze, research-paper-workflow v2.9. **Date:** 2026-10-21 (JST).
**STATUS: FROZEN, MODEL-SPECIFIC / INSTITUTION-SPECIFIC EXISTENTIAL ECONOMIC THEORY.**
**AUTHOR CONTRIBUTION SCOPE CONFIRMED** in chat (the user replied 「承認する」 to the stated limited claim); personal independent reproduction of every proof is NOT documented.
**PAPER OR JOURNAL ACCEPTANCE NOT CERTIFIED.** This is the single source of truth for V2b after theory freeze; historical docs/MODEL_SPECIFICATION.md and docs/EQUILIBRIUM_LEDGER.md contain **V1**, are archival, and MUST NOT be quoted as V2b model specifications.

## 0. Freeze identity, scope and change control

Frozen baseline only: V2b **additive-separable residual design** φ(x)=x, X_ij=(x_i+x_j)/2, with technical compatibility and residual product homogeneity independent. One separately preregistered **DIAGNOSTIC robustness alternative** φ(x)=x² has complete separate math certificates but is not part of the canonical baseline. No parameter tuning, extra asymmetric country type, standard-adoption fixed cost, trade taxes, transfers, installed-base law, endogenous country count, unilateral standards choice or renegotiation is admitted by this freeze.

Research question: Can costly post-government product differentiation endogenously make a standards alliance that looks consent-feasible with frozen firm designs fail, **even when grand multilateral interoperability is Pareto superior to fragmentation after true firm reoptimization**, under a specified bilateral-first, third-country opt-in standards architecture?

Contribution statement: A strictly defined EXISTENCE COUNTEREXAMPLE for a staged three-government/three-firm sequential game. Both φ=x and separately certified φ=x² share the same exact rational parameter witness and produce existential frozen-IS versus endogenous-no-agreement, with positive hypothetical multilateral national welfare gains. The government bargaining protocol is essential; no general standardization-fragmentation or innovation-disincentive theorem is claimed. The qualitative result is established for an unquantified open parameter neighborhood of the exact witness **in each separately defined model**, NOT across an arbitrary function class.

## 1. Players, economy, actions and information

- Sovereign principals A, B, C; firms 1,2,3 respectively headquartered in these countries. Three symmetric independent national product markets, each with the same three differentiated products, quantities and costs. Firms sell in EVERY country and earn profits from all THREE markets, while each government counts the CS of its own market and its home firm's *worldwide* income.
- Complete publicly observed histories and choices; no exogenous uncertainty or asymmetric types. Each stage is common knowledge. Firms simultaneously choose designs, then firms simultaneously choose quantities in each country.
- Stage 1: A proposes an AB standards/technical-compatibility union SU at a real depth g∈[0,1]; B accepts or rejects. Rejection => standards fragmentation SW.
- Stage 2: after an accepted SU, C decides whether to apply for accession. Nonapplication => SU(AB) remains.
- Stage 3: if C applies, both A and B decide to approve/reject; unanimous approval => IS(ABC) while keeping EXACTLY the original g. Any veto => SU(AB). No renegotiation after C's application.
- Stage 4: in any reached S∈{SW,SU,IS}, each firm simultaneously chooses x_i∈[0,1], with x_i=0 maximum differentiation, x_i=1 maximum residual product homogeneity; **no lower bound x_i≥g**, no regulatory constraint forcing whole-product equality. Firms pay one-time real global product-design cost κ(1−x_i)²/2.
- Stage 5: each firm chooses output q_i^t≥0 in EACH t∈{A,B,C} separated Cournot market. In the symmetric fulfilled-expectations continuation q_i^A=q_i^B=q_i^C=q_i; consumers' network expectations n^e match realized per-market q on the equilibrium path and are **held fixed when taking own Cournot quantity deviations**.
- Tie rule for government's acceptance: B accepts SU when indifferent; C applies when indifferent; A/B approve C when indifferent. Note g=0 makes physical compatibility and all continuation allocations identical across *membership labels*; zero-depth labels may depend on indifference refinements, thus government **institutional SPNE profiles are NOT claimed unique**. The result is about substantive g>0 agreements only.
- Government welfare is not a budgeted fiscal objective. There are NO transfers/side payments/commitment deposits/subsidies/adoption fees, market-entry bans or trade restrictions. Standard compatibility and variety-design costs are distinct.

## 2. Frozen primitive utility, demand, price and design matrix

Let a−c=d=1, η=379/500=.758, ρ=9/10=.9, κ=1701/2000=.8505. (All witness values are exact rationals; claims about nearby values require separate stated bounds.) Per-market utility at expected network n^e:
\[
U(q\mid n^e)=a{\bf1}^{\top}q-\frac12q^\top Bq+\eta q^\top H n^e,\quad
B=\rho H+(1-\rho)X.
\]
H_ii=X_ii=1.
- SW: H_ij=0 for i≠j;
- SU(AB): H_12=H_21=g, others off-diagonal 0;
- IS(ABC): H_ij=g for all i≠j.
Canonical V2b X_ij=(x_i+x_j)/2 for i≠j, and X_ii=1. (Separately tested φ(x)=x² variant X_ij=(x_i²+x_j²)/2 with SAME cost κ(1−x_i)²/2.)

Consumer inverse demand from the utility taking n^e as fixed:
\[
p=a{\bf1}-Bq+\eta H n^e.
\]
At fulfilled network expectations n^e=q, firms' interior Cournot KKT equalities are:
\[
Mq=d{\bf1},\quad
M=I+B-\eta H=I+(\rho-\eta)H+(1-\rho)X.
\]
Here M_ii=2−η=1.242 and M_ij∈[0,.242], M≽I, q_i>0 for every history's S,g,x and the exact witness. The supremum Cournot best-response contraction coefficient is bounded by 2*.242/1.242<1, ensuring unique strictly positive Stage 5 continuation for all strategy profiles, not a numerical root selection. Relevant demand B is PSD; strict preference concavity at extreme boundary designs is NOT claimed.

Firm i's equilibrium world operating income is 3q_i² since p_i−c=q_i in each symmetric market at equilibrium. Firm payoff:
\[
\Pi_i=3q_i^2-\tfrac{\kappa}{2}(1-x_i)^2.
\]
Once-paid cost (NOT three times). Within each national market fulfilled-expectations CS is:
\[
CS=\tfrac12 q^\top Bq.
\]
Country i welfare:
\[
W_i=CS+3q_i^2-\frac{\kappa}{2}(1-x_i)^2.
\]
World welfare is \(\sum_i W_i=3CS+3\sum_i q_i^2-\frac{\kappa}{2}\sum_i(1-x_i)^2\). Do NOT double-count network benefit in CS or global costs.

## 3. Stage-4 continuation and certificates

Given S,g, define q(x;S,g)=M(x;S,g)^{-1}d1. Each firm's unilaterally deviating design derivative is:
\[
F_i(x;S,g)=\partial_{x_i}\Pi_i
=6q_i\,\partial_{x_i}q_i+\kappa(1-x_i),\quad
\partial_{x_i}q=-M^{-1}(\partial_{x_i}M)q,
\]
holding all OTHER firms' designs fixed; not a derivative along joint symmetry path. All firms have compact x∈[0,1]. Strict own concavity and diagonal-strict concavity/Rosen bound certify a single pure Nash (including asymmetric and boundary strategies) after all histories for the witness. For canonical V2b the sufficient analytic bound κ>81(1−ρ)²d² holds: .8505>.81. Independent Stage4A Krawczyk interval enclosures and full deviation checks establish the government-continuation roots. For p=2 alternative, full 3×3 pseudo-gradient Gershgorin negative definiteness over all asymmetric x/g is interval-certified separately, and root face signs plus all-g welfare derivatives are checked anew. The p=1 Hessian bound MUST NOT be substituted for the changed nonlinear derivative in p=2.

There is no firm Nash multiplicity requiring arbitrary symmetric equilibrium selection at this exact witness. Global uniqueness of the institutional-label government SPNE is NOT stated; government continuum outcomes are addressed in Section 4.

## 4. Precise theorem and counterfactual quantifiers

Define Mφ(g) = A/B SU-member national welfare at the UNIQUE Stage4 design Nash followed by Stage5, Oφ(g)=C's SU outsider national welfare, Iφ(g)=each country's symmetric IS national welfare, and Sφ=SW national welfare (each conditional on appropriate unique follower Nash).

### T1 — Market continuation (PROVED — analytic, at exact witness)
For every regime S and every g∈[0,1] and x∈[0,1]^3, q>0 and the fulfilled-network Cournot continuation is unique. Canonical p=1, separately p=2.

### T2 — Firm design Nash (PROVED — model-specific computer-assisted/analytic, at witness)
For every regime S and every g∈[0,1], there exists one and only one x*(S,g) in the firm's full x-cube, which is interior in both tested φ systems. Canonical p=1 analytic Rosen curvature and root inclusion; p=2 entirely separate interval Rosen/Gershgorin plus signed root boxes. Formal Lean model-level proof NOT available.

### T3 — Endogenous no positive-depth technical standard (PROVED — computer-assisted at witness, given specified institution)
For EACH φ∈{x,x²}, for EVERY REAL g∈(0,1]:
\[
M_\phi(g)<S_\phi,\qquad I_\phi(g)<O_\phi(g).
\]
All real g in (0,1] are covered by mathematical rational interval sign certificates, not merely dense finite numerical grids. Both inequalities are zero at g=0. Therefore C optimally declines any substantive IS accession and A/B will not join an SU whose continuation is worse than SW. Every SPNE has no substantive positive-depth coalition along path, though formal zero-depth labels may vary by tie.

This is **INSTITUTION-SPECIFIC**, not a generic claim for simultaneous A/B/C negotiation, other voting agendas, or compulsory worldwide standards.

### T4 — Frozen-design regime reversal (PROVED — restricted counterfactual game)
Construct a different game with all government actions and welfare cost accounting held fixed, but restrict **each firm to x_i=x_SW* from the true SW firm Nash after EVERY government history**; it is NOT an endogenous Nash of the original unconstrained firm game.
For EACH φ∈{x,x²}, there EXISTS some ghatφ∈(0,1] such that C applies, A/B approve, B accepts and proposer A strictly prefers that IS to SW or every terminal SU policy (SU compared over the ENTIRE g interval). Witnesses:
- canonical p=1 ghat=1/20=.05;
- separate nonlinear p=2 ghat=1/200=.005, with frozen C participation strict but VERY SMALL ≈9.10e-7.

With accept/apply/approve at indifference the feasible government policy set is compact and at least one proposer-optimal positive-depth IS offer exists in this frozen restricted-strategy game. Its optimizing depth is NOT given in closed form.

### T5 — Endogenous positive *hypothetical* multilateral welfare (PROVED — pointwise rational interval)
For EACH φ∈{x,x²}, if an IS at EXACT g=1/20=.05 were imposed/exogenously attained and firms REOPTIMIZED design under IS:
\[
I_\phi(.05)>S_\phi.
\]
Each of the three ex ante symmetric countries strictly gains compared with SW, despite the absence of substantive positive-depth agreement in original Stage1–3 SPNE. For p=1 national gap ≈0.016934628 and world gap ≈0.050803884; for p=2 national gap ≈0.016601147. Neither welfare optimum g nor unrestricted social planner first best is solved. In the original protocol the allocation is NOT an on-equilibrium-path political outcome.

### T6 — Qualitative open parameter neighborhoods (CONDITIONAL, unquantified)
The strict inequalities, uniform interval bounds and stable Stage4 Nash imply a nonempty open local parameter neighborhood around the exact witness **for each separately specified φ model**. No radius was computed. Do NOT describe results as generic over parameters, broadly robust, all Cournot markets or arbitrary φ.

### T7 — Broad claims NOT proved / rejected
- Original pre-registered SAME g=.05 frozen C accession under p=2: **REJECTED / STRICTLY NEGATIVE** ≈−0.000440395. A distinct small positive depth g=.005 satisfies T4; this does NOT retroactively pass the original same-g hypothesis.
- All real exponents p between 1 and 2, all differentiable φ, all Cournot marginal costs and all government agendas: NOT PROVED; universal rhetoric rejected. Boundary φ≡0 eliminates design-to-substitution effect and collapses frozen vs endogenous, so an unrestricted-function claim would be false.
- Marginal derivative equality [I−O]'(0)=2M'(0) is symmetry/graph edge-additivity, not a second novel theorem.
- A hypothetical direct 3-country unanimity offer at g=.05 with rejection to SW is accepted by all under the derived payoffs; demonstrates that no-agreement is specific to AB-first consent. Legal feasibility, contracts and alternate global optimal equilibrium are not proved.
- A specific historical ChaoJi/GSM state veto from private differentiation is NOT documented, and ISO committee voting is not this 2+1 government game.

## 5. Equilibrium/SPNE history-completeness and corner ledger

S∈{SW,SU,IS}, each g∈[0,1], each x_i∈[0,1], each q_i^t≥0; expect n^e=q in rational equilibrium. For B refusing Stage1 => SW; C not applying => SU; C applying then A/B veto => SU; C applying and unanimous approval => IS with inherited g; subsequent firm design and Cournot unique regardless of off-path prior approval decisions. Under exact witness, Stage5 q_i always strictly positive even when an arbitrary upstream off-equilibrium firm chooses x boundary; no output active set missing. Stage4 unique interior Nash for every regime/g eliminates equilibrium asymmetric/corner designs. Government ties at g=0 can lead different nominal coalition labels; outcome equivalence must be used, not claim unique SPNE. Individual government rejection histories and offer-continuum boundary g=1 handled. A numerical solver failure is NEVER evidence an action is unattractive; code distinguishes successful interval certificate from candidate failure or unresolved cells.

Participation comparison conventions: C chooses between outsider SU and accepted IS at the SAME g; B rejects to SW; A can choose ANY g and cannot force C's joining. A/B unanimous vote can only approve/reject, not revise g. Frozen counterfactual government menus are identical.

## 6. Benchmarks, policy meaning and economic interpretation

Benchmark definition B0 SW = no offdiagonal technical standard compatibility, even though products remain substitutes by X; B1 SU = AB standard link only; B2 IS = all cross-compatibility edges g; B3 frozen-design policy evaluation = the counterfactual restricted-strategy game, not a physically forced actual equilibrium; B4 exogenously constituted IS(.05) = only a constrained welfare comparison; B5 direct 3-country unanimity = separate hypothetical agenda, NOT canonical SPNE.

Economic mechanism: promised compatibility changes positive network benefit and product substitutability, firm residual design shifts resulting own and rival rent, government values domestic consumer surplus plus home firm's global profits, and sequential member formation and outsider's SU advantage jointly block a final Pareto-improving international agreement. This is *one* design-and-consent mechanism, not two independent margin-reversal theorems.

Policy inference limited to **diagnosis**: frozen-design forecasts can give a mistaken prediction of the achievable coalition regime. No subsidies, implementation fees, legal authority, WTO compatibility, transfers or external enforcement are optimized; no actual public authority is advised to impose a certain standard. This is not a regulatory cost-benefit estimate for a real standard.

## 7. Empirical/institutional reference boundary

France/Germany GSM development cooperation (1984; 13-country mobile operator MoU in 1987) and Japan–China CHAdeMO/CEC ChaoJi (2018 bilateral standards actor technical cooperation, later broader standards effort) show *plausible* bilateral-to-multilateral technological standard activity prior to later bodies' global standardization. They do not literally instantiate this A/B government consent and C applicant veto protocol. Formal regulatory ISO/IEC votes, mandatory USB-C market law and two-sided installed-base charging networks are not represented faithfully. Treat as introduction motivation only, never as theorem verification.

## 8. Closest original literature / priority limitations

- Gandal & Shy (2001 JIE): published FULL source provided by author, original Props 1–5 audited. Three sovereigns, mutual recognition and exclusive SU/outsider effects and domestic CS+home exports are well-known. Their full foreign-recognition/no formal SU can still produce compatible standards; this is NOT our incompatible SW. Their firms have exogenous Salop locations and play Bertrand prices, with no post-government firm design investment.
- Cabral & Salant (2014 IJIO / 2009 accessible preprint): standardization can discourage future R&D and alter nonstandardization incentives; broad private investment deterrence is prior art.
- Buchholz & Hattori (2024 / 2021 WP): coalition and technology interactions causing coordination paradox are prior art.
- Takarada–Kawabata (2025): exogenous differentiation affects regional mutual-recognition; C nonmember membership restrictions are not new.
- Economides and coauthors: network-vs-rivalry standards trade-off and firm-led standards coalitions well-established.
- Rosen (1965), Poincaré–Miranda, Krawczyk, IFT and rational-interval bounds are methodological tools, NOT new theory results.

Original full proofs of Baake–Boom and some journal-vs-WP versions remain uninspected, at user direction; inaccessibility is not evidence of novelty. No priority certification against every possible general coalition/follower-investment theorem. Maximum economic claim: the *specified combined government-consent/private-postdesign channel*, tested in two product kernels, makes a Pareto-welfare-positive international standard inaccessible under one bargaining protocol.

## 9. Proof/execution/reproducibility source-of-truth manifest

**Analytic and mathematical claims**:
- Canonical Stage4 proof: reviews/V2B_STAGE04_MINIMAL_MODEL_GATE_2026-10-21.md, verification/v2b_stage04_primitive_reconstruction.py.
- Canonical independent Stage4A: reviews/V2B_STAGE04A_ADVERSARIAL_CERTIFICATION_2026-10-21.md, verification/v2b_stage04a_krawczyk_cleanroom.py, GitHub CI run https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39480815816.
- Canonical original universal interval signs: verification/v2b_interval_reversal_certificate.py.
- p=2 alternative: reviews/V2B_ALT_QUADRATIC_STAGE04_04A_CERTIFICATION_2026-10-21.md, verification/v2b_alt_quadratic_rosen_interval.py, verification/v2b_alt_quadratic_policy_interval.py, CI https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39516205888 (both jobs PASS after fixing early typo; early failing CI retained).
- Stage6/7 national and world welfare: verification/v2b_stage06_pareto_holdout.py and verification/v2b_stage07_welfare_institutions.py and reports reviews/V2B_STAGE06_CONTRIBUTION_CLOSURE_2026-10-21.md and reviews/V2B_STAGE07_WELFARE_GENERALITY_INSTITUTIONAL_GATE_2026-10-21.md.

**Generality / contribution**:
- reviews/V2B_STAGE075A_CONTRIBUTION_ROBUSTNESS_CERTIFICATE_2026-10-21.md. Classification: INSTITUTION-SPECIFIC for main government-coalition results, CONDITIONALLY PORTABLE for well-defined follower Nash and hypothetical Pareto at the two φ kernels.
- reviews/V2B_STAGE075A_FINAL_GO_AFTER_AUTHOR_CONFIRMATION_2026-10-21.md, Stage7.5A GO.
- reviews/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD_V2B_2026-10-21.md, user expressly accepted narrow research scope, not independent proof reproduction.

**Embedded formal verification**:
- formal/V2bWelfareCore.lean, Lean 4 v4.24.0 pinned by root lean-toolchain; no mathlib. Four pointwise rational welfare-sign comparisons at x_SWproxy and x_ISproxy in p=2 model have kernel-checked proofs 'decide +kernel', no 'sorry', 'admit', local 'axiom' or 'sorryAx'; standard Lean axioms only. CI https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39517673634 PASS; historical initial failed syntax tactic run 39517506979 retained.
- reviews/V2B_STAGE075A_FORMAL_VERIFICATION_GATE_2026-10-21.md; EXACT FORMAL COVERAGE = **PROOF-CRITICAL CORE ONLY**, never FULL CLAIM. No Lean proof of true Nash-root membership, all-g government derivative, Cournot demand or SPNE; these components remain in trusted SymPy/mpmath/Python Stage4A rational-interval files. Formal code alone does not validate nonencoded economic primitives.

**Software and unresolved statuses**:
- Frozen source CI runs prove software executed, not publication novelty or author independent verification. mpmath, SymPy and NumPy/SciPy trust boundaries must be explained in a computer-assisted-proof appendix.
- All q/x/g endpoint, near-zero C advantage (~9.1e−7), and the original negative p=2 same-depth case are mandatory regression checks.
- Stage9 should organize an eventual production LaTeX repository or subfolder WITHOUT rewriting this freeze document.

## 10. Freeze controls and allowable next work

**No changes without explicit new project decision, earliest affected stage rollback and repeat of Stage4A, Stage7.5A, the formal gate and Stage8 freeze** whenever a payoff, game tree, equilibrium, theorem quantifier, design mapping, standard meaning or cost accounting changes.

Allowed *without* theory modification: reorganizing repository; drafting LaTeX to match this exact specification; gathering accessible citations; improving proof exposition and independent reproducibility; correcting typos with no content change, with provenance; finding a target journal later in workflow. If the manuscript discovers a false economic claim, reopen analytic stage instead of silently changing theorem or swapping φ functions.

Do NOT replace V2b baseline with V1 old z≥g model, do NOT add p=2 as a coequal new government architecture, do NOT label institutional no-agreement generic, do NOT claim same-depth frozen p=2 acceptance at g=.05, and do NOT assert complete Lean economic theorem or human mathematical reproof.

**Stage 8 freeze verdict:** restricted V2b canonical theoretical object FROZEN as identifier V2B-THEORY-FREEZE-2026-10-21-v1, with a separately certified p=2 diagnostic and explicitly limited legal/empirical/academic scope.
