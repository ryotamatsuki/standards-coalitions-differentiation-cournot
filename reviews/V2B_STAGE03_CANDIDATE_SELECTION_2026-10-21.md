# Stage 3 — Selected candidate mechanism and contribution memo
**Date 2026-10-21; workflow: research-paper-workflow v2.9, Stage 3.**

## Canonical Stage-3 verdict
**GO — SELECT V2b AS THE ONLY STAGE-4 MODEL CANDIDATE.** This is a research-mechanism selection, not a Stage-4 mathematics GO, Stage-4A adversarial PASS, or Stage-6 theorem-priority certificate.

**Upstream caveat:** Stage 2 retained a CONDITIONAL GO with a source-access/theorem absorption blocker for a decisive predecessor (Gandal–Shy 2001, plus Baake–Boom 2001 theorem-level checks). The author explicitly directs progression without waiting for presently unavailable full texts. This waives neither the uncertainty nor the requirement to disclose it at Stage 6: novelty remains **UNRESOLVED**. This Stage-3 GO is **candidate-selection only**; it is not an ordinary all-prior-gates-green research release.

## 1. The selected question (RQ-01)

When governments commit to a compatibility agreement before private firms make costly independent product-design decisions, **can reoptimizing design reverse the governments' incentive to form and admit members to an international standard coalition, relative to an otherwise identical frozen-design policy game?**

This question remains focused on **a new comparative result in a five-stage strategic game**, not on an alleged novel utility component.

## 2. Bounded structurally distinct candidates

| ID | Structure | Economic issue / tests | Disposition |
|---|---|---|---|
| **C1 V1** | Government compatibility g **also** imposes firm-product homogeneity floor z>=g | Clean closed-form bargaining but cannot adequately separate interface compatibility from whole-product similarity. | **DEFER / ARCHIVE**, retain prior results; cannot substitute for RQ-01. |
| **C2 V2a** | Firm products choose x_i with cross-similarity x_i*x_j after government g | Adds genuine post-policy design. But if rival x_j=0, firm's own design has no impact on pairwise substitution; discovered multiple asymmetric firm Nash equilibria complicate well-defined government continuation. | **REJECT FOR CURRENT PAPER**, preserve counterexamples. |
| **C3 V2b** | Additive cross-similarity X_ij=(x_i+x_j)/2, simultaneous costly x_i after sovereign g, then Cournot | Firm controls product residual similarity without imposing g as design floor. A symmetric concave-game sufficient bound makes every firm's Stage-4 continuation unique. Rigorous interval-code witness suggests reversal of government coalition outcome. | **SELECT**, sole Stage 4 candidate. |
| **C4 adoption fee / interface aftermarket / compulsory market-access law** | Introduces new agents/costs or regulation after Stage 4 | Each may be worth future research, but not necessary to produce current candidate reversal; risks hand-fitting of regional agreement. | **NOT AUTHORIZED**, defer to Stage 7.5A portability decision if theory survives. |

No feature accumulation; no extra firms, market asymmetry, market access law, or government transfers at this stage.

## 3. Application-neutral mechanism fingerprint

**Actors:** three symmetric sovereign principals with individual national welfare, three home firms optimizing globally across three identical national Cournot markets.

**Decisions/timing:** (1) A proposes bilateral compatibility depth g to B, B accepts; (2) C seeks admission; (3) A/B approve unanimously with same g; (4) firms simultaneously choose costly design similarity x_i in [0,1]; (5) each of three identical national markets clears in Cournot under fulfilled network expectations.

**Interaction:** a government-chosen weighted edge matrix H increases both consumer product substitution rho H and fulfilled network benefit eta H; firm choices shift substitution by (1-rho)X where X_ij=(x_i+x_j)/2. Thus design incentives depend on government coalition graph. National W_i includes identical domestic CS, home firm's three-market profits, once-paid design cost.

**Canonical reduced form:** three-agent continuous-strategy Nash continuation q(x,g,S)=[I+(rho-eta)H+(1-rho)X]^{-1}(a-c)1 on proven inner domain. Government sequential bargaining applies to the induced welfare W_i(g,S;x^*(g,S)). Compare to EXACT SAME upstream policy game but exogenously hold x_i=x_SW^* after every history.

**Important benchmark control:** frozen x is a separate restricted-strategy counterfactual. It is NOT a predecessor's theorem being contradicted, nor obtained by naively taking kappa -> infinity (that takes x towards one instead). Keep design costs' level unchanged between comparisons; policies and welfare functions otherwise identical.

## 4. Mechanism exactly decomposed, with independent differentiation

Denote symmetric SU members' chosen similarity u(g), outsider's v(g). At g=0, SW/SU/IS markets coincide. The SU member welfare derivative is:
\[
M'(0)=W_{M,g} + W_{M,u}u'(0)+W_{M,v}v'(0).
\]
At exact rational witness eta=379/500, rho=9/10, kappa=1701/2000, a-c=1:
- unique symmetric SW x = 0.7185927073221104.
- u'(0)=+0.0608102317352140; v'(0)=+0.0323048168863242.
- W_{M,u}(0)≈−0.17359696; W_{M,v}(0)≈−0.13970897.
- **Fixed-design/direct** W_{M,g}(0)≈+0.00676792412884.
- **Private-design feedback** W_{M,u}u'+W_{M,v}v'≈−0.01506974412526.
- **Endogenous total** M'(0)≈−0.00830181999641.

Therefore **the strategic feedback reverses the sign** of the government's marginal incentive to form an SU. By permutation symmetry, C's marginal accession gain [I(g)-O(g)]' at g=0 equals 2 M'(0), so its sign also reverses. This is a *local decomposition*, not an unconditional global theorem.

Reproduction: verification/v2b_stage03_mechanism.py independently reconstructs the primitive Cournot matrix, firm unilateral design derivatives, implicit u',v', and direct fixed-policy derivative. Existing separate continuous-g certificate: verification/v2b_interval_reversal_certificate.py (CI previously PASS), proving global welfare and accession inequalities at the witness under its interval-implementation assumptions.

## 5. Closest prior and provisional absorption map

- Economides–Flyer (1998): compatibility raises network value but reduces differentiation and intensifies competition. **Known component**, not originality.
- Baake–Boom (2001): quality choice before private compatibility agreement, then pricing. **Known component**, its timing not equivalent to government-before-design without further derivation; original full propositions inaccessible.
- Gandal–Shy (2001): governments' standards coalition under network effect and switching costs. **Most serious government-level parent threat**; accessible abstract does not allow definitive theorem comparison.
- Takarada et al (2020); Takarada–Kawabata (2025): regional/multilateral standards and C-country welfare participation; 2025 §5.4 includes effects of **exogenous differentiation**. **Kills broad differentiation-affects-standards claim.**
- Generic concave-game and backward-induction results imply well-defined stage continuations; may absorb mathematics of existence/uniqueness, but no inspected general result has yet been shown to directly imply *this particular sign and coalition-regime reversal*. **Unresolved full-game priority**.

See literature/V2B_STAGE02_CLOSEST_PAPERS_2026-10-21.md for source titles, access grade and exact comparisons. The current stage does not claim novelty.

## 6. Nested controls, falsifiers, and stop rules

- **Frozen-design control:** x_i=x_SW^* at every policy history, same eta,rho,kappa and same costs; required positive-depth IS must satisfy C application, A/B approval, A willingness vs SW and all SU.
- **Zero-compatibility control:** g=0 makes SW/SU/IS behavior and payoff equivalent independent of labels. Do not call g=0 a substantive coalition.
- **Balance control:** eta=rho removes all g from equilibrium q and firm Stage 4 choice, while CS can increase with g. Requires careful distinction between output and welfare.
- **Negative/no-reversal case:** for other eta,rho,kappa regimes the private-design term may reinforce, be irrelevant, or be insufficient to switch policy sign; *a generic reversal is not assumed*.
- **Fatal mathematics test:** any feasible off-path government deviation or firm boundary/corner that makes a claimed SW-vs-IS global SPNE comparison invalid.
- **Fatal novelty test:** a known theorem that directly implies the post-policy design-vs-fixed coalition-regime sign change under a valid object/variable mapping.
- **Economic portability kill:** any honest model-independent claim is falsified by economically credible alternative function forms or expectations mapping at Stage 7.5A. If so narrow to V2b-only rather than alter model ad hoc.

**Stop rule:** Freeze V2b primitives for Stage 4/4A. Do not generate V2c or re-tune adoption fees merely to force SU. Stage 4 audits the present candidate; on a mathematical failure return to earliest affected stage and record it. Existing conditional Stage 2 source limitation stays open, cannot be reclassified as literature novelty evidence.

## 7. Research maturity and Stage 4 contract

MATHEMATICS: restricted headline witness has computer-assisted certified **construction evidence**, but no logically independent Stage 4A PASS; all-parameter SPNE classification not proven.
NOVELTY: UNRESOLVED, prior-art source ceiling explicitly documented.

**Stage 4 required deliverables** (no blanket GO inferred from earlier CI):
1. Write a full self-contained model statement and equilibrium claims with strategy/history domains, tie rules and demand expectation convention.
2. Independently rederive consumer demand, Cournot market continuation, all firm Stage-4 unilateral gradients, strict concavity/sufficient uniqueness bound.
3. Check global SU/IS membership and off-path participation at all g (including g=0/1), using an evaluator separate from the reported certificate.
4. Check the continuous-g sign certificates' algebra, interval covering and implicit-function linking; distinguish one witness/open neighborhood from a global theorem.
5. Provide claim-level theorem certificate and **a single GO/CONDITIONAL GO/NO-GO** verdict with unresolved histories explicitly counted.
6. If Stage 4 GO is justified, **Stage 4A (clean-room independent adversarial certification)** comes next; do not skip directly to Stage 6 novelty re-kill.

**Stage 3 verdict: GO (mechanism selection, with upstream literature caveat).**
