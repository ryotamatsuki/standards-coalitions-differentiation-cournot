# V2b Stage 23 — Theorem-level closest-prior comparison: Buccella–Fanti–Gori and Cheng–Huang
Date: 2026-10-22 JST. Supplement to Stage23 Draft PR #24. Source research scope as-of 2026-10-22.
**Verdict: NO DIRECT FORMAL ABSORPTION by the exact inspected main BFG(2023) Proposition 1 and publicly visible Cheng–Huang(2025) Proposition 5 appendix; MATERIAL MECHANISM OVERLAP remains, and FULL PRIORITY IS UNVERIFIED. NO journal-submission GO.**

## Exact sources and access depth
- Buccella, Fanti & Gori (2023), *Strategic product compatibility in network industries*, *Journal of Economics* 140:141–168, DOI 10.1007/s00712-023-00834-x. Full public version-of-record HTML https://link.springer.com/article/10.1007/s00712-023-00834-x ; full author preprint (31 pages) https://www.ec.unipi.it/documents/Ricerca/papers/2023-290.pdf . Inspected main paper sections 2–4, equations (1)–(7), (24), (31)–(36), (39)–(49), Proposition 1, Lemmas 1–4 and Result 1. Author preprint Proposition 1 appears on PDF page index 15 (zero based), and DOI version is authoritative.
- BFG(2023) supplementary Online Appendix: publisher identifies **Supplementary file1 DOCX 603 KB**. Springer main article explicitly says it develops a horizontal-differentiation version of the compatibility decision game, with network effect and substitutability changing equilibria. Raw DOCX not retrieved in this session; **UNVERIFIED — HORIZONTAL-DIFFERENTIATION SUPPLEMENT ABSORPTION NOT RESOLVED**. Do not infer from the appendix description that degree of differentiation is firm-optimized; the published main text treats firms' choice of K/NK and k, not continuous independent residual x.
- Cheng & Huang (2025), *Quality competition and product compatibility in network industries*, *Journal of Economics* 145:31–57, DOI 10.1007/s00712-024-00896-5. Publisher public preview https://link.springer.com/article/10.1007/s00712-024-00896-5 gives full Appendix 1 model expressions and Appendix 2 **Proof of proposition 5** (especially two veto scenarios). Published main text Propositions 1–4 and full Proposition 5 statement not public in inspected material. ResearchGate shows publisher preview only. Contemporary author conference abstract https://www.econ.sinica.edu.tw/59/archives/35017f8537f57acf confirms three stages: compatibility decision, quality, then pricing. **Not a complete fulltext proof audit.**
- Additional, distinct BFG(2024): *Product Quality and Product Compatibility in Network Industries*, *B.E. Journal of Theoretical Economics* 24:299–339, DOI 10.1515/bejte-2023-0014; earlier working paper https://www.ec.unipi.it/documents/Ricerca/papers/2023-291.pdf (public indexed abstract; PDF request timed out). **2026 corrigendum** DOI 10.1515/bejte-2025-2001 exists, published 26(1):225–226. Its corrective scope was NOT fetched. Do NOT silently mix this with the **different** BFG(2023) *Strategic product compatibility* paper.

## BFG 2023: literal strategy, welfare and the closest theorem
Demand equation (1):
`p_i = 1 - q_i - q_j + n (y_i + k y_j)`, with fulfilled expectations `y_i=q_i`; two firms are quantity-setting Cournot rivals. First, each **firm** selects a discrete compatibility status K/NK. Second, if endogenous, it selects degree k in [0,1] to maximize **firm profit**. Third it produces quantity. Its profit `Pi_i=(p_i-w)q_i-Z 1{K}` deducts a quasi-fixed **compatibility-entry cost** Z; no government offers, no third government, and no endogenous residual-design variable x with cost kappa*(1-x)^2/2.
At positive network effect n>0, the symmetric K/K second-stage private profit `1/(3-n(1+k))^2-Z` satisfies
`dPi/dk = 2n/(3-n(1+k))^3 > 0`, so endogenous k*=1, a CORNER. This is not V2b's interior residual x Nash.
**Proposition 1** (published §3.4): define binary-profit differentials `Delta_A = Pi^(K,NK) - Pi^(NK,NK)`, `Delta_B = Pi^(NK,K)-Pi^(K,K)`, and `Delta_C = Pi^(NK,NK)-Pi^(K,K)`. For increasing Z and positive n, equilibrium classifications are: (1) K/K unique Pareto efficient for firms (Z<Z_C); (2) K/K unique firm-Pareto inefficient (Z_C<Z<Z_A); (3) both K/K and NK/NK symmetric SPNE but NK/NK firm-payoff dominates (Z_A<Z<Z_B); (4) NK/NK unique firm-Pareto efficient (Z_B<Z<Z_TH). Signs are tested by profit comparisons at a discrete firms' choice node, not by national welfare consent derivatives. Pareto firm profitability here is NOT identical to all three V2b national welfare levels.
**Result 1 (§4)** under exogenous k permits asymmetric anti-coordination K/NK equilibria. It is NOT the V2b counterfactual fixing residual designs at original fragmentation Nash while governments still optimally choose g.

### Exact overlapping demand-family projection (important anti-false-novelty check)
At rational expectations, the BFG demand/Cournot FOC reduces to:
`(2-n)q_i+(1-nk)q_j=1`. A frozen TWO-firm V2b quantity matrix has diagonal `2-eta` and cross `(rho-eta)g+(1-rho)x` at equal fixed residual x. Taking formal boundary values `eta=n, rho=0, g=k, x=1, d=1` reproduces the **BFG quantity matrix exactly**. This was independently checked by SymPy. Therefore BFG and V2b are NOT wholly unrelated demand families: their restricted Cournot market equation overlaps. But this mapping has `x=1` FIXED, uses the rho=0 boundary, reduces 3 firms and international markets to 2, and **does not map endogenous x, private cost kappa, government national W, the 3-country game tree, or the participation-sign reversal**. Do not claim a full structural nesting or full disjointness.

### BFG direct-absorption test against V2b A/B/C
A: BFG Prop1 has neither `m_g(0)=D-L` nor member+third-government accession `(i-o)_g=2m_g`, nor the controlled frozen-vs-firm-design comparison with the SAME government strategy set. Thus **direct theorem absorption by Proposition 1: REFUTED (conditional on inspected original statement)**. Its familiar message 'endogenous compatibility can change SPNE' is already PRIOR ART and must be explicitly conceded.
B: BFG first-stage firm's compatibility decision and unilateral deviations produce coordination/prisoners' dilemmas; no direct grand government proposal or rejection-payoff contrast. Hence no direct proof of V2b institutional B, but generic agreement-game effects already anticipated.
C1: BFG quasi-fixed Z paid upon choosing compatible status is categorically different from V2b lambda*(x-z)^2/2 charged on residual redesign relative to past x. BFG Z thresholds cannot be numerically or economically equated with V2b lambda_c~0.935389. Abstract similarities in adaptation-cost comparative statics are not novelty.
C2: BFG n affects equilibrium types but neither V2b rho=1 threshold eta=6/7 nor globally optimal government coalition is derived by its Proposition 1. BFG's Online Appendix horizontal differentiation could exert stronger conceptual coverage; UNVERIFIED.

## Cheng–Huang: specifically verified Proposition 5 appendix
Published abstract and author conference record: TWO firms determine compatibility under possible veto; conditional on compatibility, firms choose intrinsic VERTICAL quality (their `q_i`, not V2b output q_i); firms then compete in prices, with endogenous market shares. Network parameter `alpha` and asymmetrically valued quality enter market segment endpoints. Producer profits determine compatibility-stage deviations; NO country government or national profit-and-domestic-CS participation vector.
Publisher **Appendix 2: Proof of proposition 5**:
- Under *both-firm veto*, a mutual incompatible profile remains SPNE because one firm cannot alone alter incompatibility; unilateral desire to select compatible status can leave its payoff unchanged (publisher lines ~227–243). The appendix also finds compatible outcome as an SPNE in the analyzed case (~268–274), so NEVER assert incompatibility is uniquely selected for all alpha based solely on the appendix.
- Under *no-firm veto*, a mutual incompatible profile is destabilized by a profitable unilateral switch to compatible outcome and does not satisfy the two-stage decision equilibrium (publisher lines ~291–309). Here the set of deviations is changed by the veto institution.
These arguments are a **strong conceptual predecessor for veto-perpetuated inefficient incompatibility and institutional decision-rights**, but do NOT derive V2b's inherited-depth outside-option wedge `mu_N<0<2mu_N+nu_N`: V2b government rejections respond to differences in country welfare after firm's Nash design, rather than unilateral technological impossibility under a firm's veto. V2b direct-grand vs inherited depth comparison retains unanimous government participation; Cheng–Huang 'no veto' allows unilateral compatibility. Treat the institutional B as related but not synonymous.
A: no controlled `same government game + fixed x vs reoptimizing residual x` comparison in verified Appendix2. Published main Propositions 1–4 inaccessible: **UNVERIFIED FOR COMPLETE-PAPER ABSORPTION**.
B: generic veto/no-veto switch is anticipated (conceptual overlap B); specific inherited-depth C accession vs SW direct-grand not in inspected appendix (candidate D institutional remainder).
C: quality-network comparative statics are PRIOR ART; no basis to equate alpha cutoff with eta=6/7, nor quality investment cost with lambda_c.

## Cross-model theorem absorption matrix
| Required mapping for direct absorption | BFG 2023 Prop1 | CH 2025 public Prop5 appendix |
|---|---|---|
| 3 countries, 3 national welfare maximizers | ABSENT (2 firms) | ABSENT (2 firms) |
| Country welfare = own domestic CS + worldwide home-firm net profits | ABSENT (2 firm profit game, aggregate welfare ex-post) | ABSENT (firm profit game, welfare ex-post) |
| Original g policy independent of residual design x | ABSENT (k itself firm's compatibility extent) | ABSENT (binary compatibility, vertical quality) |
| Firm Nash x chosen AFTER government g decision | ABSENT | ABSENT |
| The frozen-vs-endogenous design comparisons hold original government strategy set fixed | ABSENT | ABSENT |
| Initial country member vote and later outsider vote under inherited depth | ABSENT | ABSENT |
| Local m'=D-L, (i-o)'=2m', i'=2m'+o' | NO comparable government payoff differential | NO comparable government payoff differential |
| Same firm continuation yet changed direct-grand outside option | ABSENT | ABSENT |
| Theorem 0<D<L forces country participation reversal + Pareto grand >SW | NOT IMPLIED by observed Prop1 | NOT IMPLIED by public Appendix2 |
No full-strategy-set/utility-preserving parameter mapping exists within **the inspected results**. But missing CH numbered propositions and BFG horizontal appendix preclude an exhaustive negative whole-paper absorption claim.

## Independent economic-value critique
1. The conditional insight left for V2b is **private Nash redesign's consumer/export-profit national-income incidence changing TWO government consent constraints while direct grand welfare remains positive, under an identical governmental agenda**. Neither merely having product endogeneity nor veto is new.
2. It is still possible a generalized investment/coalition theorem formally or economically covers this mechanism. This audit does NOT clear all outside literature (Grossman–McCalman–Staiger 2021, Lambertini–Rossini 1998, Klimenko 2009, etc.).
3. B is most vulnerable to the accusation that changing only feasible coalitions/outside options makes the outcome obvious. Pitch B as the boundary that isolates scope of A, not a second independent major discovery.
4. C1/C2 are diagnostic boundaries with model-specific parameter restrictions, not evidence that prior studies lack their generic qualitative mechanisms.
5. While stage22 exact-A main result and opening proof are substantial, narrow inherited-depth architecture may be a strong editorial concern; direct-grand makes the fragmentation non-coalition-proof. Reject an unconditional generalization.

## Updated Stage23 research gate
**REOPEN remains appropriate**, but the direct-formal-absorption risk from the INSPECTED BFG Prop1 and CH public Appendix2 is reduced: neither directly states or proves A. Preserve distinction between 'direct absorption not demonstrated', 'mechanism novelty actually secured', and 'standard journal quality achieved'. No GO; no STOP based on merely similar labels.

### Residual minimal evidence to close
1. Retrieve BFG 2023 Springer 603KB supplementary DOCX and check if horizontal differentiation parameter is merely exogenous versus Nash-optimized after compatibility decision.
2. Obtain CH 2025 *full published main* Prop1–5 theorem statements, bounds/figures and verify whether fixed-vs-endogenous quality comparisons plus compatible/incompatible country welfare are explicitly made.
3. Inspect BFG 2024 *Product Quality...* publication and its 2026 corrigendum before relying on their exact welfare or side-transfer propositions.
4. Referee kill-test: formalize whether `D-L` + national outsider incidence contains a nontrivial predicted disagreement not explainable by a generic commitment/veto theorem. If necessary use only a minimal alternative institutional comparison, not unbounded extensions.
