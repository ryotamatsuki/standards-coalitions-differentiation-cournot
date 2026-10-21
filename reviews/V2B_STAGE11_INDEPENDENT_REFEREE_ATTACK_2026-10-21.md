# Stage 11 — Independent Robustness / Hostile Referee Gate (V2b)

**Date:** 2026-10-21 JST  
**Workflow:** research-paper-workflow v2.9, after Stage 10.  
**Manuscript:** *International Standards Coalitions and Endogenous Product Design* (14-page first draft).  
**Source baseline:** `main` at `dcc7287b8cb0ad2a88bf88d8bff1941d6bcb39f3`.  
**Freeze:** `V2B-THEORY-FREEZE-2026-10-21-v1`.  
**Stage 10 CI:** [run 39537935322](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39537935322), SUCCESS (structural and TeX/PDF build, *not* academic proof).  
**Verdict:** **CONDITIONAL GO to Stage 12 (journal/positioning); NOT submission-ready.** No mathematical counterexample was established to the frozen exact-witness claim, but novelty and external proof verifiability remain **substantial editorial risks**. **Do not promote this to journal-level originality certification.**

## 1. Referee position and quantifier discipline

The strongest licensed statement is an **existence counterexample at one exact rational vector** `(d,eta,rho,kappa)=(1,379/500,9/10,1701/2000)` in a *specific* three-country A/B-first, inherited-g, C opt-in, A/B unanimity game. For each of two separately tested substitution maps `phi(x)=x` and `phi(x)=x^2`:

* With firms reoptimizing after policy, **for all real g in (0,1]**, the terminal SU member loses relative to SW and C loses by joining IS relative to remaining outsider in SU; hence no substantive positive-depth agreement is implemented in this procedure.
* A different **restricted-design** game with firms frozen at their SW Nash designs **admits some positive-depth IS**: canonical g=1/20; nonlinear g=1/200. These are *different depth witnesses*.
* The conditional endogenous IS continuation at g=1/20 strictly Pareto-improves on SW, but cannot be implemented through the modeled intermediate SU history.

This is **not** a theorem for arbitrary design functions, all national bargaining structures, all Cournot systems, all parameters, or actual ISO/IEC institutional voting. There is no claim of a quantified open parameter neighborhood, although strictness and regularity suggest unspecified local continuity.

### Direct numerical reconstruction, independent of project programs

Using only the stated U, B, M, cost, country welfare, full three-player unilateral FOCs and SciPy root solving (NOT importing any of the repository's economic modules), we obtained:

| Map | g | SW W | SU member minus SW | IS minus SU outsider | conditional IS minus SW | Frozen C IS-minus-SU |
|---|---:|---:|---:|---:|---:|---:|
| phi=x | .005 | 2.422078422 | -0.000042099 | -0.000087280 | +0.001749915 | +0.000063171 |
| phi=x | .05 | 2.422078422 | -0.000473474 | -0.001246547 | +0.016934628 | +0.000234617 |
| phi=x | 1 | 2.422078422 | -0.027102173 | -0.125082032 | +0.170560618 | -0.108043725 |
| phi=x^2 | .005 | 2.596118318 | -0.000095598 | -0.000195042 | +0.001727503 | +0.000000910 |
| phi=x^2 | .05 | 2.596118318 | -0.001016454 | -0.002406159 | +0.016601147 | **-0.000440395** |
| phi=x^2 | 1 | 2.596118318 | -0.040165078 | -0.163933510 | +0.139234276 | -0.133476802 |

The table is **sample-point corroboration only**. The quantified all-g signs rest on the archived outward-rounded interval code and previously passing CI; this Stage 11 run did **not** constitute a new independent full-interval reimplementation or formalization. The nonlinear same-depth g=.05 counterfactual **FAIL remains FAIL**; positive g=.005 is a separately qualified existential outcome, with a very small consent margin.

### A useful *non-equilibrium* explanatory ablation (not a new theorem)

At each policy, interpolate both SU and IS design vectors between their SW Nash vectors (`lambda=0`) and their respective actual design Nash vectors (`lambda=1`). Intermediate lambdas are artificial **off-equilibrium design configurations** and must not be called equilibria. Numerically, for phi=x, g=.05, the outsider's accession margin changes sign at approximately `lambda=0.15999` and the SU member's gain relative to SW at `lambda=0.36616`. For phi=x^2, g=.005, those thresholds are approximately `0.00465` and `0.02336`, respectively. The latter illustrates *fragility*, not broad economic generality. Do not add these illustrative thresholds to frozen theorems absent separate verification and new scope approval.

## 2. Mathematical referee (R1)

**R1.1 Quantity-stage feasibility — PASS on the stated witness.** The expectation-fixed firm FOC yields `M=I+(rho-eta)H+(1-rho)X`, not the consumer utility matrix `B`. Diagonal entries are `alpha=1.242`, off-diagonal entries lie in `[0,.242]`; the best-response map has contraction factor at most `2(.242)/1.242<1` on `[0,1/alpha]^3`; the untruncated numerators remain positive. The proof properly handles quantity corners. The three identical markets multiply operating profits by three and design cost is charged once.

**R1.2 A tighter independent analytic check on canonical Rosen — SUPPORTS PASS, not a full proof-assistant certificate.** Set `beta=1-rho=.1`, `alpha=1.242`, `D=alpha-2(.242)=.758`. For all full asymmetric `x∈[0,1]^3` and policy g in [0,1], strict row diagonal dominance gives `||M^-1||_infty≤1/D` (Varah bound); positive quantity continuation gives `||q||_infty≤1/alpha`. Since `||M_{x_i}||_infty≤beta` and `M_{x_i x_j}=0` for phi=x, we obtain
`||q_{x_i}||_infty≤beta/(D alpha)=0.106220710`, and
`||q_{x_i x_j}||_infty≤2 beta^2/(D^2 alpha)=0.0280265725`.
Therefore every `|∂^2 (3 q_i^2)/∂x_i∂x_j|` is bounded by `6(0.106220710^2+0.805152980*0.028026573)<0.203092`, tighter than the manuscript's asserted 0.27. Thus `kappa-3(0.203092)>0.24122>0`, sufficient for strict negative row dominance of the symmetric pseudo-gradient; own concavity follows. At x_i=0, F_i>kappa-6*(1/alpha)*0.106221>0.33735, and at x_i=1, F_i<0 (strictly, as output falls when own residual homogeneity increases). Together these also show interior best responses at the canonical witness, regardless of rival designs. **Action:** include this self-contained norm-bound derivation or equivalent detailed proof in the appendix, rather than an unproved "standard bound".

**R1.3 SU / IS firm FOCs — PASS at the level reviewed.** The manuscript correctly differentiates a *unilateral* firm action. In particular `∂q/∂x_i=-M^{-1}M_{x_i}q`; a common symmetric design derivative is not a private FOC. The specialized IS scalar FOC `F_I=kappa(1-y)-6 beta alpha/((alpha-t)(alpha+2t)^3)` was checked from the 3-by-3 inverse, not inferred from a symmetric-profit path.

**R1.4 All-g negative derivative certificate — EVIDENCE EXISTS; INDEPENDENT RE-CERTIFICATION OUTSTANDING.** The archived Stage4A code uses 1,000 initial exact rational g cells, adaptive refinement, interval Krawczyk inclusions, nonsingular design Jacobians, implicit derivatives, and negative outward upper bounds for both country margins. The full proof is dependent on trusted SymPy/mpmath implementations, numerical preconditioners *inside interval enclosure*, and the integrity of code/CI; Lean does not prove all-g signs or Nash uniqueness. **Action:** archive actual machine-readable certificate output, environment versions, all accepted cell counts, worst-case outward interval bounds and SHA; produce a referee-run command; ideally reproduce once with an independent interval library. Do not treat 14-page PDF build as a scientific validation.

**R1.5 Government backward induction — PASS conditional on the two all-g inequalities.** C refuses accession (`i<o`), B refuses any positive-depth SU (`m<s`), so A cannot induce a positive-depth union. g=0 is payoff-equivalent to SW and institutional labels can vary. The frozen-design claim remains a different strategy-restricted game, not a comparative-static equilibrium of the original design game. The all-g frozen SU envelope addresses A's best alternative; manuscript must be precise about weakly affirmative voting/ties and how an optimum is attained.

**R1.6 Model foundation — WATCH.** `CS=.5 q'Bq` follows from *conditional* quasilinear utility when network expectations are held fixed for demand and are fulfilled only in equilibrium. This is mathematically internally coherent, but consumers/firms optimizing while treating `n^e` as fixed is a selected rational-expectations timing assumption, not a theorem of network adoption. Product attribute cost `kappa(1-x)^2/2` makes **differentiation costly**, and rising g induces *more* nonstandardized similarity. Explain clearly why the economic interpretation is not "innovation always falls": it is strategic costly horizontal positioning.

## 3. Generality referee (R2)

**FAIL on broad portability; PASS on properly limited 2-function existence.** The canonical and phi=x^2 results share the same parameters/institution and differ in functional design substitution. They do not identify a robust theorem over an open function class or bargaining formats. Under phi=x^2 the frozen C margin at the originally preregistered g=.05 is negative; selecting .005 passes a logically distinct existential test with a `~9.1e-7` payoff gap. The model contains a concrete **institutional falsification:** bypass bilateral-first and offer unanimous IS(.05) directly against SW; every country accepts because the actual equilibrium IS payoff exceeds SW. This must remain in the abstract/limitations as appropriate, not hidden behind "coalitions fail" language. No new model or tuned parameters were introduced here; theory freeze remains intact.

## 4. Prior-art hostile referee (R3)

Source-specific theorem absorption, not a guarantee of global priority:

| Source and verified accessible scope | Preexisting mechanisms | Unabsorbed residue here | Risk |
|---|---|---|---|
| Gandal & Shy (2001), published primary text previously audited at proposition level | Three countries, government recognition/regional standards unions, outsider incentives, network benefits, national CS + global home-firm profits | Post-government *costly* private residual-design Nash and endogenous-vs-frozen agreement reversal are absent. G&S no-SU may still mean mutual recognition, unlike our SW. | HIGH but not direct theorem identity |
| Takarada & Kawabata (2025), *Multilateral Versus Regional Mutual Recognition*, publicly accessible 36-page Feb. discussion paper, incl. sections 5.3–5.4 | Three-country Cournot, endogenous continuous standards, failed regional MR under independent national-welfare objectives, third-country enlargement veto, differentiated goods comparative reasoning, and product-standard adjustment **fixed costs** | Their product differentiation is exogenous in §5.4; their regulatory standard cost/environmental externality differs; no same model holding policy constant while solving *post-policy Nash residual design* and reversing every positive-depth government proposal. | **VERY HIGH editorial overlap.** Explicitly juxtapose results, not merely cite in background. |
| Cabral & Salant (2014), journal abstract & published bibliographic record confirmed; full published proof not newly checked in this gate | Single technical standard can reduce firm R&D and private innovation effort; separated standards can sustain innovation | Not the specific country A/B-first, C-accession payoff comparison, residual design game, and Pareto-granular blocked full integration | HIGH on economic mechanism; do not claim "standards reduce innovation" as novelty |
| Buchholz & Hattori (2024), verified published abstract | Endogenous technology choices interact with coalition formation to yield paradoxical cooperation and welfare comparative statics | Their timing and global-public-good provision game differ; firm attributes chosen *after* government compatibility, not technology before coalition formation | HIGH conceptual analogy |
| Baake & Boom (2001), IJIO published abstract confirmed | Quality choice, network externalities and compatibility over a four-stage game; direct precedent against "endogenous product design plus standards" as a novel combination | Product quality chosen before subsequent mutual adapter agreement, not post-government residual x and tripartite inherited-depth consent | MEDIUM–HIGH; full propositions still unverified |
| Economides & Skrzypacz (2003 working paper) | Firm-side standards coalitions with network effects and choice over degree of technical compatibility | No verified exact A/B-government vote + downstream residual design + C exit alternative mapping | HIGH background overlap |

Independent public primary/reference entry points:
- https://doi.org/10.1016/S0022-1996(00)00067-2 (Gandal & Shy)
- https://oikono.econ.nagoya-cu.ac.jp/wp-content/uploads/sites/2/2025/02/DP701_Kawabata_February2025.pdf (Takarada & Kawabata, especially introduction and §§5.3–5.4)
- https://doi.org/10.1016/j.ijindorg.2013.07.006 (Cabral & Salant)
- https://doi.org/10.1016/j.econmod.2024.106722 (Buchholz & Hattori)
- https://doi.org/10.1016/S0167-7187(99)00029-6 (Baake & Boom)
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=378340 (Economides & Skrzypacz)

**R3 determination: DISTINCT BUT NARROW; not directly absorbed by the specific inspected predecessor results, but editorial importance is unresolved.** The strongest objection is **not** that any one ancestor has the exact theorem. It is that (a) the standards/innovation tradeoff, (b) third-country coalition blockage, and (c) downstream best responses are well-known components, and a restrictive inherited-g agenda plus a single fine-tuned exact vector may not be important enough for a stand-alone IO contribution. The manuscript must show what *prediction* changes and why a fixed-design benchmark is a realistic decision error, not just that the sign can flip.

## 5. Economic significance / referee (R4)

**MAJOR REVISION risk (editorial, not a mathematical refutation).** The actual result is a combination of three exact-witness inequalities, plus one explicit frozen counterfactual; the proposed "international standards always fail" reading would be wrong. The improvement `IS(.05)-SW=~.016934628` per country is economically more substantial than the SU member loss `~.000473474` and outsider accession loss `~.001246547`; however the normalized units provide no empirical scale or institutional calibration. The economic novelty should be an **endogenous-response participation forecast error**, not a general theory of stalled technical standards. Strengthen:
1. In the introduction/table, display the same-g baseline frozen-vs-endogenous A/B and C participation margins side by side (canonical .05) and the positive conditional IS-vs-SW national welfare gap. This is a particularly concrete counterfactual with no theorem modification.
2. Explain three options distinctly: substantive SW status quo; an SU outsider's attractive continuation; a hypothetical direct three-way offer avoiding this outside option. Distinguish "Pareto improvement from SW" from "Pareto improvement over every intermediate SU allocation" (the latter **does not hold**).
3. State the model's *falsification*: alternative direct unanimous ABC agenda implements the IS(.05) gain. If that makes the conclusion seem institution-dependent, it is a correct feature, not an inconvenience.
4. State strongest rival result Takarada–Kawabata 2025 in the introduction, including fixed costs/differentiation sections and their preexisting examples of failed regional formation and blocked enlargement.
5. Make explicit why conditional network-demand use and costly differentiation are economically plausible. No false identification with ChaoJi/GSM participation votes.

## 6. Referee-visible evidence and Stage 11 exit checklist

| Gate | Verdict | Reason and next action |
|---|---|---|
| Exact model logic / Cournot / global canonical firm Nash | **PASS with exposition repair** | Independent FOC/sample reproduction and tighter analytic curvature bound; manuscript should print enough of proof |
| Certified **all-g** political inequalities | **EVIDENCE-SUPPORTED / NOT independently re-run here** | Existing Stage4A interval certificate and CI; independently archive machine-readable proof logs and a second interval implementation if practical |
| Frozen versus endogenous regime inversion | **PASS at specified witness**, not generic | Both sample-point implementations agree; canonical frozen global SU upper envelope originates in CI archive |
| Functional robustness | **LIMITED PASS** | Two maps only, nonlinear same-depth g=.05 failure prominently retained, g=.005 fragile |
| Institutional robustness | **FAIL AS UNIVERSAL CLAIM** | One-shot direct unanimous ABC produces positive agreement at g=.05 |
| Distinctness from inspected prior art | **CONDITIONAL PASS** | No exact theorem absorption found within examined sources; Takarada–Kawabata and Cabral–Salant particularly dangerous |
| Generalizable economic insight / journal importance | **HOLD FOR EDITORIAL REFRAMING** | Single parameter witness; specific protocol and already known separate ingredients |
| Journal submission now | **NO** | Not a submission certification; Stage 12 journal-positioning and Stage 13 research-article/exposition polishing needed |

**Overall Stage 11 disposition: CONDITIONAL GO to Stage 12 only.** Keep Stage8 frozen 9 blobs untouched. Stage12 should choose an honest journal target based on the proved scope (economic theory/IO/regulatory-standardization vs narrow existence example), not use breadth claims to pursue a stronger outlet. Editing the text, introducing a payoff comparison exhibit, improving a rigorous appendix bound, and independent reproducibility are authorized as *non-theory refinements*. Any material new theorem, parameter tuning, or institutional change requires explicit theory re-freeze and regression certification.

### Provenance limitation

This report combines code/manual mathematical auditing, an independent floating-point numerical reconstruction, the Stage10 certified CI state, and publicly accessible literature. **It is not an independent complete computer-assisted proof of all-g intervals, and not a journal referee's peer review.** It makes no claim about unpublished literature not obtained or publisher versions not read in full.