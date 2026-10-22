# Stage 23 — Independent Economic Significance and Publication Gate

**Date:** 2026-10-22. **Source:** Draft PR #22, head d8e76f9f865f3e5a0573ae4df342367a9ddfbe39. **Status:** REOPEN — Fundamental research / priority and institution mapping required. No journal submission.

## Executive conclusions

1. A (design-endogenization reverses consent) has a replicable local differential mechanism. The canonical result is independently recreated numerically, while all-g Krawczyk/Rosen certificates are **inherited from Stage 14, not newly executed**. Global SPNE is conditionally grounded on those certificates.
2. B (direct grand offer accepted despite bilateral-first veto) is a correct local corollary of the same payoff incidence plus changed outside options. It does not establish a new general bargaining theory and its separate novelty is **Level 1**.
3. C1 is an optional lambda>0 local participation threshold, not a global SW–IS threshold. C2 is an exact network threshold on the rho=1 limit face and a near-face extension where firms respond; its leading coefficient arises from frozen mechanisms and endogenous response only at higher order. They should be subsidiary; C2 may be independent research notes, not a third headline mechanism.
4. The paper-level candidate is **Level 2 (distinct narrow mechanism, not yet Level 3)**. Recent close published predecessors (Buccella–Fanti–Gori 2023; Cheng–Huang 2025; Grossman–McCalman–Staiger 2021), and the restrictive inherited-depth accession protocol, prevent definitive priority/economic-significance clearance.
5. **REOPEN**, not GO/CONDITIONAL GO, because remaining proof/priority/institutional relevance work is substantively research-facing, not just editing. **Not STOP**: a narrow nontrivial national-incidence sign reversal is demonstrably present and could support a specialist submission if distinctness and institutional bite are established.

## Correct source-accounting statement

M=I+B-eta H, B=rho H+(1-rho)X, X_ij=(x_i+x_j)/2, x_i∈[0,1], K_i=kappa(1-x_i)^2/2 for the original lambda=0 game. Positive Cournot solves Mq=d 1, p-c=q; CS=q'Bq/2; worldwide firm profit 3q_i²-K_i; national W_i=CS+profit. Non-negativity, uniqueness of Nash, and all-history regularity are prerequisites, not automatic.

With alpha=2-eta, beta=1-rho, delta=rho-eta, t=beta z, P=alpha-t and L=alpha+2t, the fragmentation FOC is kappa(1-z)=6 beta alpha d²/[P L³]. The frozen incident-edge welfare derivative is

D=rho*d²/L² -delta*d²*[2(1+2t)/L³+6alpha/(P L³)].

The actual local bilateral-member slope is mu_N=D-loss, where

loss=C(2u'+v')+V(u'+v'), C=beta*d²*(eta+2t)/L³, V=3 beta*d²*(alpha-2t)/(P L³).

The V term has a PLUS sign. Using an own-firm envelope to remove home consumer surplus or the effects of rivals' designs on world profit is invalid. Conditional on 0<D<loss, frozen firms have mu_F>0 but endogenous firms have mu_N<0.

Permutation incidence gives m'(0)=mu, o'(0)=nu, i'(0)=2mu+nu, (i-o)'(0)=2mu. Thus mu_N<0<2mu_N+nu_N means bilateral-first inherited-depth rejection coexists with a direct Pareto-improving grand offer at small positive g.

## Independent numeric rerun (SciPy least-squares Nash FOCs; unilateral scalar profit maximization)

At theta=(1,0.758,0.9,0.8505): z=0.7185927073221111. SW welfare=2.4220784217, CS=0.8934296573, profit=1.5286487644.

At g=0.05:

| Regime | Member W | Outside W | Common CS | Member profit |
|---|---:|---:|---:|---:|
| SU, frozen at z | 2.42235080 | 2.44116242 | 0.91055734 | 1.51179347 |
| SU, actual design | 2.42160495 | 2.44025960 | 0.91028591 | 1.51131904 |
| IS, frozen at z | 2.44139704 | n/a | 0.94428224 | 1.49711480 |
| IS, actual design | 2.43901305 | n/a | 0.94340564 | 1.49560741 |

IS actual gain from SW=0.01693463 (+0.699%), driven by CS +0.049976 (+5.594%) and profit -0.033041 (-2.162%). A quantitatively modest uncalibrated welfare gain; qualitative voting reversal substantial.

At lambda=5, independently evaluated IS at g=0.054333206815 yields W=2.442664414892, third-country veto approximately binding against actual SU outsider W=2.442664414892. This numerical check does not certify global optimum/uniqueness or exact root isolation. Stage 18 provides the inherited exact interval claim.

## Symbolic rerun (SymPy independently derived)

On rho=1, theta=(1-eta)/(2-eta), A=d²/(2-eta)²:

s=9A/2; m=A[(4+g)/(1+theta*g)^2+1/2]; o=A[(1+g)/(1+theta*g)^2+7/2]; i=A[(9/2+3g)/(1+2theta*g)^2].

m-s=A*g*(1-8theta-4theta²*g)/(1+theta*g)^2. Therefore eta_c=6/7 for the member local slope. The symbolic factorization of i-o matches Stage 21's polynomial. The first-order fixed-design derivative at (eta,beta)=(6/7,0) is mu_eta=2401*d²/512; mu_beta=10339*d²/2048 and -mu_beta/mu_eta=-211/196. This verifies eta_c(rho)=6/7+(211/196)(rho-1)+O((1-rho)²) **only locally**, assuming the stated smooth continuation.

## Proof completeness and external bounds

The full asymmetric Rosen and Krawczyk all-depth canonical certificates are stored in `verification/stage14/canonical_global_rerun.log`, with reported maxima -0.00797019299733 and -0.01503888333775. The prior log also reports frozen IS acceptance and a positive Pareto gap. Stage 23 has *inspected* those logs but **did not execute** their underlying all-depth programs. Stage 21 near-face IFT/compactness proof is source-reviewed, with restricted rho/eta range; its full rigorous numerical and boundary checks are NOT independently repeated. All-unrestricted-primitive and corner-output regimes remain open. No claim that lambda_c is a global regime boundary.

## Economic novelty objections — ordered

1. Existing 2023 and 2025 network-compatibility models already show that endogenous versus exogenous attributes/compatibility, veto structure and network strength transform SPNE. Exact theory-to-theory mapping to the national vote reversal remains incomplete. This is **publication critical**.
2. Bilateral-first depth inheritance and unilateral third-country veto are designed to make the outsider's intermediate payoff an outside option. The different direct-grand equilibrium is then logically unsurprising. Unless a relevant accession commitment institution is shown, B has weak standalone contribution. **Publication critical**.
3. Frozen x is a controlled counterfactual, not a separate realistic equilibrium institution; the meaningful prediction requires comparing anticipated continuation rules credibly. **Major**.
4. Design x is residual *similarity*, so positive x_g means increasing similarity, not re-differentiating against common standards. Conflating eta and rho or incorrectly calling 1-x an independent strategy invalidates interpretation. **Major exposition**.
5. Some interesting C thresholds lie on a nonstrategic-design face or hinge on lambda>0 not in the main model. Numerical proliferation is no substitute for a clear economic theorem. **Major architecture**.
6. The g=0.05 Pareto improvement is ~0.7% national welfare in normalized units; cannot be represented as a measured policy effect. **Moderate**.

## Journal exploration, not submission recommendation

| Journal | Working tier | Field fit | Research quality threshold currently met? | Comparator |
|---|---|---|---|---|
| International Journal of Industrial Organization | A | Strong IO/network | Not established | Cabral-Salant 2014 theme, requires clearer priority/general contribution |
| Journal of Economics & Management Strategy | A | Moderate | Not established | Broad mechanism and management-relevance threshold |
| Review of Industrial Organization | B | Strong IO theory | Not established | Wang-Zhao 2026 linear Cournot merger; Mukherjee-Sinha 2024 FDI/Cournot; Cohen-Heifetz 2024 location/quality |
| Journal of Economics | B | Strong mathematical-network theory | Not established | Buccella-Fanti-Gori 2023; Cheng-Huang 2025; theory predecessors pose exceptional priority risk |
| Journal of Industry, Competition and Trade | B/C | Strong trade/industrial-policy | Not established | Häckner-Herzing 2026; Ehrhart et al. 2024; policy-facing scope demands concrete policy implications |
| Review of International Economics | B | Moderate/weak due weak explicit trade mechanisms | Not established | No reliable pair of directly comparable recent papers inspected |
| Economics of Governance | C | Protocol/governance marginal | Not established | No reliable set of directly comparable recent standards theory papers inspected |

This table intentionally separates field fit from **quality**. The existence of legitimate venues is NOT an argument for current publishability. No ranking of recommended journals is authorized under the present REOPEN.

## Four independently framed referee recommendations

- Mathematical economics: **CONDITIONAL** on new executions of full-depth certificates, all-history asymmetric Nash/corners and weak-vote attainment. Local math independently replicated; no contradiction found.
- Industrial organization: **CONDITIONAL/FAIL for novelty clearance** because parent economic mechanisms are well established; prioritize exact 2023/2025 theorem-absorption mapping and controlled national vote channel.
- International cooperation: **CONDITIONAL** as a conditional extensive-form result; full third-country veto/inherited-depth institution not source-matched, no transfer/renegotiation theorem.
- Skeptical editor: **Do not submit**. Compact one-theorem design-veto paper could eventually clear, but only after a demonstrated difference from published parent mechanisms and a credible institutional interpretation.

## Finite REOPEN exit tests

1. Obtain and compare full relevant propositions of Cheng-Huang (2025), Buccella-Fanti-Gori (2023), Lambertini-Rossini (1998), Gandal-Shy (2001), Klimenko (2009), Grossman-McCalman-Staiger (2021); record variable mapping and explicit logical non-implication or absorption. If absorbed, **STOP**, do not lower journal standard.
2. Rerun and save exact all-g Stage 14 interval and Stage 21 near-face verification programs from the Stage 22 head, including code commit hashes and statuses. Report unresolved corner histories honestly.
3. Give one economically identifiable protocol class with fixed inherited accession depth and outsider veto; alternatively establish a protocol-comparison theorem for a clearly defined bargaining family without retrofitting model primitives. If no economically plausible interpretation survives, **STOP or change research question**.
4. Condense A+B into main proposition and mechanism + one institutional corollary. Place C2 in Appendix or a separate note and C1 in a short extension unless they directly amplify the core causal test.
5. Compare the contribution standard and theorem depth against genuine contemporaneous articles, not only scope pages. Then re-vote GO / CONDITIONAL GO / REOPEN / STOP.

## Online sources verified on 2026-10-22

- Gandal-Shy 2001: https://doi.org/10.1016/S0022-1996(00)00067-2
- Barrett-Yang 2001: https://doi.org/10.1016/S0022-1996(00)00082-9
- Klimenko 2009: https://doi.org/10.1016/j.jinteco.2008.08.005
- Cabral-Salant 2014: https://doi.org/10.1016/j.ijindorg.2013.07.006
- Grossman-McCalman-Staiger 2021: https://doi.org/10.3982/ECTA17536
- Buccella-Fanti-Gori 2023: https://doi.org/10.1007/s00712-023-00834-x
- Cheng-Huang 2025: https://doi.org/10.1007/s00712-024-00896-5
- JICT official scope: https://link.springer.com/journal/10842/aims-and-scope
- Journal of Economics official scope: https://link.springer.com/journal/712/aims-and-scope
- RIO official scope: https://link.springer.com/journal/11151/aims-and-scope

This Stage 23 is a new conditional independent audit, not an accepted referee report; journal editors have not evaluated this project.