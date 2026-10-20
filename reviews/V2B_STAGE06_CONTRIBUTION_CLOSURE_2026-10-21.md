# V2b Stage 6 targeted closure: Pareto-improving standards blocked by endogenous-design-sensitive consent

**Audited:** 2026-10-21 JST. **Workflow:** research-paper-workflow v2.9 Stage 6. **Canonical updated verdict: GO — RESTRICTED TO STAGE-7 WELFARE/INSTITUTIONAL VALIDATION; NOT AN ACADEMIC PRIORITY CERTIFICATE.** Former Stage 6 CONDITIONAL GO is superseded for project routing; original document preserved as historical report. Stage 4A exact-witness mathematical result remains unchanged. Source-limited competing models (especially full Baake–Boom 2001, journal-versus-WP differences) remain disclosed; the user specifically instructed not to halt due to unavailable full texts.

## A. What has changed in the claimed economic contribution

**Old and invalid as standalone originality:** "firms adjust design, so standardization deters investment and causes no agreement"; "SU-members and outsider entry incentives simultaneously change sign" (at g=0 the latter is TWO TIMES the former by symmetric edge-additivity — a single mechanism, not two discoveries); network-versus-competition, nonmember veto, mixed interoperability and quality, or Rosen uniqueness. Cabral–Salant, Buchholz–Hattori, Gandal–Shy, Takarada and standard game theory absorb those broad components.

**Exact narrowed nontrivial economic proposition:** in the V2b five-stage sequential three-sovereign standards consent game, an **international interoperability agreement that is strictly Pareto-improving over full incompatibility CAN EXIST at a positive technical compatibility depth, after the firms have re-optimized all their costly residual product designs, but IS is inaccessible as a subgame-perfect result**. Why? The country C has an outside option of keeping its technology separate while A/B form SU; C can make *even more* national surplus as a nonmember than by joining IS. Additionally, A/B will not initiate SU when firms have reoptimized because it is nationally worse than SW. Yet if products were artificially frozen at the no-standard designs with all government institutions and design cost levels unchanged, positive-depth IS is sequentially feasible and strictly more profitable than any SW/SU. This is a sharper message than "less R&D if a common standard is imposed": the interoperability **benefit remains positive even under actual private strategic adjustment**, but **agreement sequencing and outsider option prevent Pareto gains**. The firm-design feedback changes this institutional feasibility, not simply the market value of standards.

### Exact model and witness
As recorded in Stage-4A:
- Government A proposes AB standard compatibility g∈[0,1] to B; if B accepts, C may ask to enter; A/B unanimously approve; IS depth = original AB g, no renegotiation.
- Firms 1,2,3 independently choose costly residual homogeneity x_i∈[0,1] after compatibility is set, before Cournot sales in three identical national markets, with once-paid κ(1-x_i)^2/2.
- B=rho H+(1-rho) X; H_ij=g on common-standard pairs, X_ij=(x_i+x_j)/2; fulfilled-network inverse-demand Cournot M=I+B-eta H; W_i=.5q'Bq+3q_i²−κ(1−x_i)²/2.
- (a-c, eta, rho, kappa)=(1, 379/500, 9/10, 1701/2000).

### Certified qualitative conditions and a NEW strict welfare bound
**All real g∈(0,1], endogenous x:** prior independent Stage-4A Krawczyk interval proof establishes
M_SU(g)<W_SW and I_IS(g)<O_SU(g). Therefore no **substantive positive-depth** SU/IS can be reached in the stipulated government's extensive-form game. Literal labels at g=0 are indifferent/tie-dependent; no unique institutional SPNE claimed.

**Nevertheless at EXACT g=1/20 with endogenous x**, new independent exact-rational mpmath.iv bounds and globally unique Stage-4 Nash:
- x_SW∈[0.71859270731, 0.71859270734],
  W_SW ∈ [2.4220784217009967, 2.4220784217341301].
- x_IS(g=.05)∈[0.72610900359, 0.72610900362],
  W_IS(.05)∈[2.439013049607759, 2.439013049640488].
- **STRICT per-country Pareto gain W_IS(.05)−W_SW ∈ [0.01693462787362885, 0.016934627939490815] > 0.**
These are interval enclosures (rounded here for exposition). For all three symmetric countries, the same welfare improvement applies. **It is a hypothetical allocation under exogenous achievement of IS, not a feasible subgame-perfect agreement in the current sequential consent rules.** No planner optimum or implementable remedial mechanism is implied.

Numerical SU at g=.05 (not used for strict global inequalities): A/B W_SU≈2.421604947547 (<W_SW), outsider C W_SU≈2.440259596858 (>IS W≈2.439013049624). Thus even though IS is strictly Pareto superior to SW, both the member formation incentive and the outsider’s accession incentive are strategically obstructed at this depth.

**Frozen-SW-design control (verified earlier Stage 4A):** x kept at x_SW for each government history, with unchanged cost level. At .05, C would apply, A/B approve, and I_frozen(.05)≈2.441397037364 beats all possible terminal SU member payoffs, so A chooses a positive-depth IS. This is a COUNTERFACTUAL game, not a second equilibrium of the endogenous original.

New rational-interval witness script: verification/v2b_stage06_pareto_holdout.py. Scope: proves positive Pareto gap at g=1/20 and isolates SW and IS roots by opposite signed unilateral FOCs, leveraging existing global Rosen uniqueness. The global no-integration proof remains Stage-4A's separately verified all-g certificate. Dedicated CI: .github/workflows/v2b-stage06-pareto-holdout.yml.

## B. Causal decomposition (local at SW, NOT a generic comparative statics theorem)

Write M_SU(g)=W_A^SU, and in the unique SU member/outsider Nash set x_A=x_B=u(g), x_C=v(g). By ordinary chain rule, including the strategic design:
dM_SU/dg = W_g + W_u u' + W_v v'.

Independently re-derived from the primitive H,X, 3×3 Cournot inverse and firm unilateral FOCs (see verification/v2b_stage03_mechanism.py and the new local stand-alone calculation in the stage audit):
- At g=0, x_SW≈0.718592707322, u'(0)≈+0.060810231735, v'(0)≈+0.032304816886, so firms **raise residual product homogeneity / REDUCE costly differentiation after compatibility**.
- **Direct effect on A country's CS: +0.346626325569**, plus **direct effect on own-firm global profit net design expenses: −0.339858401440**, sum **+0.006767924129**.
- **Indirect firm design feedback on CS: −0.005216219629**, plus **indirect feedback on home-firm profit net design: −0.009853524497**, sum **−0.015069744125**.
- Overall marginal government welfare under SU: **−0.008301819996**.
- This is an account-level **national consumer gain versus export-firm loss and endogenous rivals' cross-substitution externality**; not Cabral–Salant’s future R&D technology imitation/free-riding incentive.
- Caveat: large positive consumer-surplus direct effect and negative home firm profit direct effect nearly cancel at this calibrated witness; **do not claim quantitatively robust broad welfare effects**.
- At g=0, graph-edge/symmetry identity [I_IS−O_SU]'=2M_SU' is STANDARD and not a standalone theorem. Frozen: +0.013535848; endogenous: −0.016603640. The direct+indirect mechanism is ONE sign switch, with derived C entry implication, not two discoveries.
- National firm best responses obey envelope for firm-owned product characteristic, but national welfare includes CS and OTHER firms' design effects; national government's derivative is **not** the private firm's design gradient.

## C. Theorem-level absorption, including version integrity

### Gandal–Shy 2001 (provided full publisher PDF)
Original 21p read across Props 1–5: countries recognize foreign standards; Salop fixed product locations/degree of difference, Bertrand price, firm no post-policy design; conversion-cost and network-only polar cases. A country outside any formal SU can nevertheless **fully recognize all foreign standards**, so their "no SU" is NOT V2b's incompatible SW. Government SU and outsider logic fully prior art; narrow endogenous-design and Pareto-superior-but-blocked consequence not direct corollary. See literature/GANDAL_SHY_2001_FULLTEXT_V2B_ABSORPTION_2026-10-21.md. Full unpublished user PDF NOT copied to GitHub.

### Cabral–Salant: carefully distinguish versions and exact claims
- **Published IJIO (2014) metadata/abstract**: https://doi.org/10.1016/j.ijindorg.2013.07.006. Positive statement: a common standard reduces R&D through free riding; maintaining different standards may improve innovation and consumer welfare. Publisher article's full proof remains unavailable.
- **Most recent accessible author preprint READ for this audit: March 2009, 21p**: https://pages.stern.nyu.edu/~lcabral/workingpapers/CabralSalantMar09.pdf. Here **Proposition 1 (printed p8)** concerns when firms avoid a common standard at state D(0,0), despite short-run profit advantages from standardization; **Proposition 2 (printed p12)** gives conditions under which no standardization is socially preferred. **The earlier 2008 WP's Proposition 2/3 numbering must NOT be mechanically transferred to the March 2009 revision or 2014 journal.** Earlier Stage 6 log's proposition numbers reflected 2008 version; the scope is version-specific and must be revised in paper bibliography before submission.
- **DIRECT absorption of BROAD innovation-cooperation discouragement, but NOT direct absorption of V2b's strict Pareto-improving grand compatibility (even AFTER firms reoptimize) blocked by 3-governments’ two-step participation and SU outsider opportunity.** Their dynamic firms voluntarily agree technologies and future R&D quality; V2b concerns governments' national welfare, competition substitutability and accession with unchanged g, with no dynamic innovation and no agreement costs.

### Buchholz–Hattori 2024 (Economic Modelling; 2021 CESifo WP)
2024 journal abstract: https://doi.org/10.1016/j.econmod.2024.106722; author WP: https://www.ifo.de/DocDL/cesifo1_wp9354.pdf. Country outsider chooses technology BEFORE coalition formation, which can alter public-good provision and world welfare. General cooperation-technology paradox and endogenous coalition are prior art. But the role/order of firms versus government, equilibrium welfare components and V2b’s sequential offer and accession conditions differ; their propositions do not by themselves entail the V2b controlled fixed-x/optimized-x standards outcome. Do not call paradox idea new.

### Takarada–Kawabata (2025 DP701)
Original 36p: https://oikono.econ.nagoya-cu.ac.jp/wp-content/uploads/sites/2/2025/02/DP701_Kawabata_February2025.pdf. §5.4 printed p22–23: exogenous differentiation can change regional MR feasibility; earlier propositions deal with countries’ MR and outsider opposition. Government standards outsider veto not new. V2b uses technical interoperability with positive network term, not their safety-rule mutual recognition with negative consumption externality; post-policy private product design not modeled. Yet their regional-to-multilateral consent insights remain a serious **component** predecessor.

### General coalition and follower-effort classes
Three-coalition externality games (Ray–Vohra, Bloch, standard game theory), Rosen design Nash, ordinary IFT/envelope and edge-additivity identities are all existing techniques. They can generate generic Pareto-blocked examples once the payoff table is supplied; they do NOT by themselves fix V2b demand/substitutability, post-policy reaction, or the cross-government inequality signs. **The generic nature of accession holdout lowers conceptual novelty, but an exactly identified endogenous-design source of this holdout is a legitimate tightly scoped mechanism candidate.**

**Source-scoped judgment:** NO DIRECT ABSORPTION FOUND in the checked original propositions of these four specific papers and general tools for the entire restricted **controlled counterfactual + Pareto-superior but strategically blocked** proposition. This is NOT a universe-wide completeness statement, nor "EVIDENCE-SCOPED NOVELTY CERTIFIED" while closely relevant original works/version text remain inaccessible. Journal originality and editorial value remain review risks.

## D. Editorial value and closure of the prior Stage-6 material blocker

**Provisional answer to "What would an economist learn that Cabral–Salant did not show?"**
A policy prediction can be wrong by **regime, not just by predicted investment, welfare level or timing**: a frozen-design evaluation may predict that a positively compatible international standard is consent-feasible; after firms choose their other product characteristics, the same standard can be **strictly Pareto superior** to fragmentation yet **inaccessible** due to the sequential formation of a regional coalition and third-country outside option. The distortion is induced by market competition and national rent shifting **without** multi-period R&D, standard adoption costs, external market access/fees, asymmetric countries, or transfer bans specially introduced after finding the example. This provides a precise diagnostic benchmark for international standards coordination models.

**Strongest surviving reviewer attack:** The local entry factor-of-two is a symmetry tautology; the result relies on a special additive X and a small unquantified open neighborhood; coalition holdout with profitable grand coalition is broadly familiar; Cabral–Salant already shows investment effects reversing standardization incentives. Merely stacking these known ideas might not clear IJIO/JIE thresholds. Explicitly state original limited contribution is **not** general nonstandardization paradox, but *welfare-positive international standard blocked by endogenous-design-sensitive accession path*. Stage 7 must test welfare and institutional portability before claiming broad importance. No separate "second sign flip theorem" allowed.

The specific former Stage-6 blocker (**what is the substantive policy/economic lesson beyond Cabral?**) now has a defensible **narrow** answer with a newly verified strict payoff inequality. Therefore Stage 6 authorizes a bounded downstream evaluation, not a theory freeze or journal submission.

### Canonical verdict
**GO — narrowly scoped to entering Stage 7 Welfare/Generality/Institutional Validation with V2b primitives UNCHANGED.**

This **does not** mean:
1. Academic theorem priority has been certified across inaccessible literature.
2. V2b delivers an analytically characterized large parameter set rather than an open neighborhood of one witness.
3. An alternative international simultaneous treaty, side payment, binding multilateral mandate, planner allocation or renegotiation has been proved feasible/optimal.
4. The 3-country coordination failure is a generic sign for all rho/eta/kappa or product design mappings.
5. Formal verification in Lean or author-independent economic referee review is complete.
6. User has authorized Stage-8 theory freeze or manuscript drafting.

**Stage 7 compulsory tests before any publication decision:** distinguish (a) positive national CS / negative home-firm profit, (b) world welfare and actual Pareto ranking at standardized counterfactual, (c) national-welfare objectives and potential transfers without assuming transfer technologies, (d) sequential coalition formation protocol plausibility, (e) differences among technical interoperability, national regulatory mutual recognition and compulsory market-access standards, and (f) alternative product-design microfoundation generality test without yet changing canonical V2b. If the causal novelty becomes merely a payoff-table restatement under plausible alternative models, issue NO-GO or restrict to short research note; no ad hoc model extensions as rescue.

## E. Independent unverified future-question memo (NOT Stage-3 authorization)

1. **CROSS-PAPER (unverified):** Under what institutional bargaining/agenda rules can a strictly Pareto-improving grand standard be implemented when intermediate SU is payoff-unfavorable? Learning = welfare/implementation gap from sequencing (not “standardize more”); strongest kill is classic coalition formation with nonconvex externalities; minimum falsifier: compare exactly the same reduced government welfare under simultaneously offered all-three agreement versus AB-first without introducing new costs, then verify SPNE under both. If generic holdout theorem fully absorbs, **STOP**.
2. **AUDITOR-INFERRED (unverified):** When do more realistic separable component product characteristics make interoperability Pareto improving but block intermediate coalitions? Learning = robustness of the *specific private design externality*, not mere claim of product-design flexibility. Strongest kill is known attribute-space endogenous differentiation and Cabral’s technology/innovation result. Minimum falsifier: construct one defensible alternate X preserving demand PSD and reprove a restricted witness with Stage 4A review; if no robust region, narrow scope rather than continually tune parameters.

These alternatives are distinct from the current claim and are NOT implemented in this Stage 6 report. No new model authorized.

## F. Provenance / artifact pointers

- Existing published Gandal–Shy full-text mapping: literature/GANDAL_SHY_2001_FULLTEXT_V2B_ABSORPTION_2026-10-21.md
- Prior Stage-6 historical CONDITIONAL GO document: reviews/V2B_STAGE06_NOVELTY_REKILL_2026-10-21.md
- Exact Stage-4A Krawczyk and frozen policy validation: verification/v2b_stage04a_krawczyk_cleanroom.py
- New rational interval Pareto comparison: verification/v2b_stage06_pareto_holdout.py
- CI: .github/workflows/v2b-stage06-pareto-holdout.yml
- Prior local decomposition: verification/v2b_stage03_mechanism.py (reconfirmed by an independent primitive-first symbolic direct/indirect CS and profit calculation). New source decomposition values above can be independently recomputed with these primitives.
- Research state files to mark conditional Stage 6 verdict as historically superseded by this limited GO.

**Re-review trigger:** new exact prior theorem demonstrating all these inequalities (not just the general idea) as a direct corollary, failure of explicit world welfare test, fatal institutional misinterpretation, or loss of the strict inequality with a minimally credible product attribute/demand alternative requires downgrade at Stage 7 / Stage 7.5A.
