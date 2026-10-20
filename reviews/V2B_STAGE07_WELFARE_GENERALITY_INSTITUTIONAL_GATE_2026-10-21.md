# Stage 7 — Welfare, generality and institutional validation; theory-paper conventions
**Date:** 2026-10-21 JST. **Workflow:** research-paper-workflow v2.9 Stage 7. **Canonical verdict: GO FOR RESTRICTED, INSTITUTION-SPECIFIC DIAGNOSTIC RESULT, NOT A GENERAL STANDARDS THEOREM.** Stage 7.5 full-theory investment decision NEXT; no theory freeze, proof-assistant PASS, manuscript drafting authorization, journal acceptance implication, empirical confirmation or cross-model portability.

## 1. How much real-world institutional matching does a theory paper need?

A pure-theory paper generally does **not** require a specific historical event that exactly instantiates its entire extensive game. What it *does* require is a credible abstraction that isolates economically meaningful strategic forces, consistent agent objective/timing, rigorous equilibrium results, a clear falsifiable/conditioned lesson, and bounded claims about the empirical scope. This is a source-grounded synthesis, **not a publisher rule that any plausible analogy automatically passes peer review**.

Verified methodological and editorial sources:
- Simon Board and Moritz Meyer-ter-Vehn, **Writing Economic Theory Papers** (UCLA faculty teaching note, 2014/2018 versions): theory papers must answer “Why should I care?”, distinguish a truly new question/model/result from mere notation, and explain an economically important result. Faculty PDF https://www.econ.ucla.edu/sboard/teaching/writingeconomictheory.pdf ; accessible copy https://citeseerx.ist.psu.edu/document?doi=ba9f380e9872cf0595abac97c9eeb60af0aeeb34&repid=rep1&type=pdf .
- William Thomson (1999), **The Young Person's Guide to Writing Economic Theory**, *Journal of Economic Literature* 37:157–183, DOI https://doi.org/10.1257/jel.37.1.157 ; Duke archival PDF https://econ.duke.edu/sites/econ.duke.edu/files/documents/Thomson,%20William%20-%20Guide%20to%20Writing%20Economic%20Theory_0.pdf . Requires transparent explicit definitions/assumptions, clear quantifiers/lemmas and illustrations not confused with proof; a special numerical example cannot stand in for a general claim.
- Robert Sugden (2000), **Credible worlds: The status of theoretical models in economics**, *Journal of Economic Methodology* 7:1–31, DOI https://doi.org/10.1080/135017800362220 ; record https://ideas.repec.org/a/taf/jecmet/v7y2001i1p1-31.html : models can be credible counterfactual “worlds”, not literal faithful replicas of institutional reality. Interpreting credibility does not justify every invented rule.
- **Harvard Economics, Writing Economics**, pp. 6–7, https://www.economics.harvard.edu/sites/g/files/omnuum5991/files/econ/files/writingec_f2014_0_1.pdf : theoretical models intentionally simplify complex real phenomena; success means conceptual/economic predictions, not empirical fit from the mere presence of an analogy.
- Elsevier **Journal of Economic Theory** publisher scope https://shop.elsevier.com/journals/subjects/social-sciences-and-humanities/economics-and-finance/general-economics-and-teaching/general-economics : original innovative theory, with relevant rigor. **International Journal of Industrial Organization** official guide https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/publish/guide-for-authors : theoretical and empirical industrial organization including technical change/regulation. These are journal scope descriptions, not a guarantee that V2b qualifies for editorial review.

**Verdict for the user's question:** **YES, INSTITUTIONAL MOTIVATION SUFFICIENT AT THE STYLIZED THEORETICAL-MODEL LEVEL**, provided the paper is expressly about pre-globalization bilateral/limited-party *technical interoperability agreements*, not a literal reconstruction of ISO/IEC committee voting, nor an asserted explanation of why a specific historical C refused. Exact A/B-first proposal, no depth renegotiation on C admission, and unanimous member approval are **pivotal institutional assumptions** and must be called assumptions in the theory rather than facts about GSM/ChaoJi.

## 2. Primary-source institutional cases: fit vs abstraction

Original institution case ledger: [V2B_STAGE07_PRE_INTERNATIONAL_TECHNICAL_ALLIANCES_2026-10-21.md](../literature/V2B_STAGE07_PRE_INTERNATIONAL_TECHNICAL_ALLIANCES_2026-10-21.md).
- **GSM:** GSMA original timeline https://www.gsma.com/about-us/who-we-are/our-history/ : CEPT created pan-European GSM initiative 1982; **France and Germany** jointly agreed GSM development **1984**; 15 operators/13 countries signed deployment MoU **1987**; ETSI standardization 1989. Bilateral-to-multilateral sequence exists, but A/B did not start everything and there is no verified C veto caused by design.
- **ChaoJi:** original CHAdeMO/China Electricity Council technical collaboration 2018 and later wider IEC/GB/T standard work https://www.chademo.com/ja/chademo3-0 and https://www.chademo.com/ja/chaoji_gbt . Technical g and differentiated residual product/protocol choices are plausible; actors were standards/industry bodies (not precisely identical sovereign governments maximizing domestic CS plus home multinational profit), no proven C sovereign accession or unanimity; electrical charging is two-sided/installed-base network rather than contemporaneous demand n=q.
- **US-EU TTC:** represents standards-position coordination, not necessarily *deployed positive* interoperability g; therefore weaker technological mapping.
- **ISO itself** employs technical committees and national standards body voting, NOT A/B propose to C and require 2-person unanimous admission. ISO official stages https://www.iso.org/stages-and-resources-for-standards-development.html . International standards body decision procedure should not be claimed as V2b.
- **Interpretation:** These cases are motivating *existence proofs of a strategic environment*, not an empirical test of the theorem. The government vs national technical standards alliance representation remains an acknowledged simplification.

## 3. Complete model/accounting

Three identical countries with identical national demand and three distinct home firms producing in *all three* separate national markets. At Stage 1 government A proposes AB technical compatibility g∈[0,1] for B consent; C may apply; A/B approve unanimously without renegotiating g; firms choose residual product similarity x_i∈[0,1] with once-only real κ(1−x_i)²/2; firm Cournot quantities then chosen, network expectations fulfilled. Distinct g vs x_i.

U(q|n^e)=a1'q−(1/2)q'Bq+η q'H n^e, B=ρH+(1−ρ)X, X_ij=(x_i+x_j)/2 for i≠j, H_ij=g if sharing same technical standard and 0 otherwise, and diagonals 1. For consumers' optimal demand, n^e held fixed; at fulfilled n^e=q, CS=(1/2)q'Bq. This is NOT gross welfare U alone and **network externality is not to be double counted**. Firm global operating income=3q_i², and resource investment cost κ(1−x_i)²/2 is deducted ONCE. W_i=CS+3q_i²−κ(1−x_i)²/2; world welfare=sum_i W_i=3CS+sum_i(3q_i²)−sum_i cost_i. a−c=1.

**Exact witness** (η,ρ,κ)=(0.758,0.900,0.8505), rational form (379/500,9/10,1701/2000). For g=1/20=.05, independent-from-production evaluator verification/v2b_stage07_welfare_institutions.py and CI check https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39512057217 passed.

| Regime | x vector approx | q vector approx | Domestic CS per country | World home-firm operating profit of A | Once-paid cost of A | W_A | W_C | World welfare |
|---|---|---|---:|---:|---:|---:|---:|---:|
| SW | (.718593,.718593,.718593) | (.721647,.721647,.721647) | .893429657 | 1.56232434 | .03367557 | 2.422078422 | 2.422078422 | 7.266235265 |
| SU (AB) | (.721595,.721595,.720197) | (.717468,.717468,.721865) | .910285907 | 1.54427994 | .03296090 | 2.421604948 | 2.440259597 | 7.283469492 |
| IS | (.726109,.726109,.726109) | (.713561,.713561,.713561) | .943405641 | 1.52750808 | .03190067 | 2.439013050 | 2.439013050 | 7.317039149 |

All welfare positive and costs counted correctly. At g=.05:
- A/B SU vs SW = **−0.000473474** (a *small but strict* negative at rational witness).
- C SU outsider premium vs its IS payoff = **+0.001246547** (C rejects admission at this g).
- IS vs SW **+0.016934628 per country**, world total **+0.050803884**; strict interval result from Stage 6 reproduction.
- SU world vs SW **+0.017234227**, despite A/B each losing nationally.
- IS world vs SU **+0.033569657**.
These are equilibrium payoffs of the associated regime continuations; IS is hypothetical if no government agreement under the canonical AB-first consent game.

**Stage 4A global continuation:** the separate Krawczyk interval certificate proved for every g∈(0,1] at this witness W_A^SU(g)<W_SW and W_C^SU(g)>W_i^IS(g). Hence no positive-depth agreement on path in the specified sequential game. These are restricted computer-assisted proofs, NOT a theorem for every η,ρ,κ.

## 4. Economic welfare/organizational wedge and policy claims

1. **National versus world welfare:** government A/B sees its domestic CS improvement partially wiped out by lost global home-firm rent (home firm's 3-market profits). SU can increase total world welfare despite negative member national payoff. This is a real conflict between country objectives, not a pure bilateral money transfer by definition.
2. **Outsider strategic opportunity:** C as SU outsider benefits from domestic CS and home-firm market position more than from joining IS at g=.05. This makes enlarged agreement undesirable for C even though IS is better for all than SW.
3. **Post-standard design feedback:** the firm changes nonstandardized product design, shifting substitution and country gains from the standards agreement. This makes the incentive distortion stronger. Fixed-SW-design alternative instead leads to positive IS.
4. **Agenda sensitivity:** a *different*, hypothetical single-stage **unanimous all-three agreement at g=.05 versus rejection to SW** would be accepted by all three since IS dominates SW after endogenous design. This is *not* a feasible move of the canonical A/B-first game and no SPNE/remedy of an implemented policy is claimed. It shows the diagnosis is institution/protocol-specific.
5. **Normative benchmark, not planner first best:** IS(g=.05) is a Pareto-improving **feasible-regime outcome if exogenously imposed** and is not proven to solve any social planner maximization problem. Side payments, global mandates, multilateral simultaneous contracting, commitment/enforcement and renegotiation have not been modeled and must not be called implementable instruments under V2b's formal game.
6. **Potential quantitative fragility:** loss to an SU member at g=.05 is only ~0.000473 and C's outside advantage ~0.001247 in normalized welfare; test parameter robustness honestly. 27-point sample varying η,ρ,κ ±0.001 at fixed g=.05 preserved both strict disadvantages and Pareto benefits, but this is NOT a continuous-g SPNE proof for perturbed parameters; Stage4A strict slack gives qualitative unquantified open-neighborhood continuation.

**Correct diagnosis label:** *welfare-positive multilateral technical interoperability can be sequentially blocked by endogenous downstream residual-design response plus nationally asymmetric intermediate coalition incentives*, in the very specific AB-first game. **Do NOT claim** compulsory full standardization is universally efficient; it is not the unrestricted first-best and need not survive alternative bargaining.

## 5. Portability/generality honesty

- Proven analytically for all policy g only at exact rational witness and inferred unspecified nonempty open neighborhood with the same primitives (local robustness, not quantified interval).
- Small design-parameter numerical perturbation: 27 parameter triples, fixed g=.05, preserved signs; not alternate function-form tests.
- **Not tested:** nonadditive characteristic substitution X, nonlinear/saturating network externality n, installed-base adoption, cost heterogeneity, endogenous firm entry, bilateral bargaining where C can join without unanimous A/B vote, flexible harmonization renegotiation g, simultaneous multilateral formation.
- The most driving assumptions are **(i) AB-first participation agenda and fixed g, (ii) companies' costly x after agreement, (iii) country objective CS+world home-firm profits, (iv) network/substitution cross terms**. The LQ utility, additive pairwise similarity, quadratic cost and perfect symmetry might be convenience but **the result's survival away from them has NOT been shown**.
- The prior V2a multiplicity and V1 product-floor baseline do not constitute an alternative-formulation robustness result for V2b's exact coalition reversal.
- This supports a narrow **INSTITUTION-SPECIFIC / MODEL-SPECIFIC** result, not a generic theory of ISO policy.

## 6. Testable/empirically recognizable conditional predictions (NOT observations)
- Under bilateral pre-standard coordination that actually commits member product-interoperability, subsequent observable product residual specifications can adjust even though interface compatibility is fixed; static frozen-design projections of accession may be wrong.
- Countries initially benefiting as standards outsiders may oppose later harmonization even if a grand agreement exceeds full incompatibility for every country.
- With a binding technical standard and national objectives including exported profits, shared consumer benefits need not make all governments favor intermediate member-only harmonization.
- The validity domain includes nontransferable/generic consent rules; predictions are **conditional**, not empirical findings about Japan/China/GSM or regulatory ISO/IEC voting.

## 7. Result-to-exposition triage (for a possible future Stage 10; NOT manuscript initiation)
| ID | Result | Best editorial form | Proof / evidence | Safe wording | Not allowed |
|---|---|---|---|---|---|
| T1 | Stage-5 quantities positive unique at witness; Stage-4 global firm Nash unique under Rosen curvature bound | Lemma + concise proof / technical appendix | Stage4A matrix bounds and independent gradient checks | A sufficient-condition lemma at restricted parameter class | Universal Nash uniqueness |
| T2 | g>0 SU bad for A/B and accession bad for C across continuum | **Main Proposition** with explicit witness, interval-certificate appendix | Stage4A Krawczyk 1000 intervals, CI PASS | Exists an open neighborhood within this model with positive-depth non-agreement | Generic fragmentation |
| T3 | Yet IS(.05) strictly Pareto superior to SW for all three after endogenous design | **Corollary / pair with T2**, welfare table | Stage6 rational interval proof, Stage7 welfare evaluator | A Pareto-superior compatibility is blocked by this agenda | First-best social planner claim |
| T4 | Frozen-SW-design restriction admits positive-depth IS preferred to every SU / SW | **Counterfactual Proposition** or part of main T2 | Stage4A rational-interval full SU envelope | Endogenous design changes coalition outcome relative to frozen benchmark | Causal identification from observed data |
| M1 | dW_SU/dg = direct + design feedback, and g=0 outsider local 2× identity | **Mechanism explanation + figure** | Stage3 symbolic differentiation | One local causal channel and simple symmetry identity | Two independently novel theorem results |
| E1 | ChaoJi and GSM original institutional history | **Introduction 1 paragraph with caveat**, not central theorem | official CHAdeMO/GSMA primary records | Examples of bilateral pre-standard coordination followed by broadening | Exact historical test of third-veto mechanism |
| R1 | Robustness to additive-X param cube | **Appendix table or one-line limitation** | 27 numeric points + Stage4A continuity | Some local parameter robustness | General functional-form robustness |
| P1 | Simultaneous three-party direct treaty at g=.05 would be acceptable | **Discussion diagnostic**, maybe institutional graphic | strict W_IS>W_SW at exact witness | Bargaining agenda matters in a hypothetical outside game | Already demonstrated implementable treaty or formally solved extended SPNE |

Visual suggestions if any future manuscript: one clear 3-node coalition/agenda tree; a single welfare table (SW/SU/IS); if plotted, a welfare-versus-g curve with all thresholds explicitly certified and legend declaring parameter witness. No unverified grand regime map.

## 8. Bounded family/extension register and hard stop
| Variant | Parent | Added assumptions | New possible learning | Evidence maturity | Disposition |
|---|---|---|---|---|---|
| V2b current | Stage4A/6 | NONE | Design-sensitive sequential blockage | Strict restricted theorem + independent welfare | **CORE; retain** |
| frozen x benchmark | V2b | Restrict x_i to SW Nash constant across all histories | Bias in coalition feasibility from ignoring reoptimization | Stage4A proof | **CORE COUNTERFACTUAL** |
| direct 3-party unanimous agenda | V2b | New offer/consent protocol in a separate hypothetical counterfactual | Shows protocol—not net benefits alone—drives failure | Strict payoff comparison only; full alternate SPNE not solved | **DIAGNOSTIC, NOT NEW THEOREM** |
| x_ij=x_i*x_j (old V2a) | V2b | Different characteristic mapping with known multiplicity | Possible failure of continuation uniqueness | Prior exploratory counterexamples, no V2b regime reversal replication | **ARCHIVED; NOT robustness PASS** |
| nonlinear network, actual market-access mandate, transfers, renogotiation | V2b | Multiple new primitives | May change application/implementation | Not tested | **DEFER; DO NOT TUNE** |

**Stage-7 outcome:** **GO FOR WELFARE AND INSTITUTIONAL VALIDATION AT A DIAGNOSIS-ONLY, MODEL/AGENDA-SPECIFIC SCOPE.** Importantly **does not certify generality across alternative model formulations**, nor authorizes full-theory freeze or journal manuscript. Forward to **Stage 7.5 full-theory investment decision**, which applies a stricter portability criterion and may require CONDITIONAL GO before Stage7.5A.

**Remaining strongest substantive barrier:** Does the design-sensitive Pareto-blockage retain substantial economic content under one **credible non-cosmetic alternative to additive residual similarity / contemporaneous linear network demand**, while preserving the original bilateral-first agenda? This is the right question for Stage7.5; current stage may not silently replace the canonical model.
