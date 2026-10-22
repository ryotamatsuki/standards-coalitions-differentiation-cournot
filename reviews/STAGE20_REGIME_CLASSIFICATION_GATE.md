# Stage20 — Can a primitive threshold classify SW / SU / IS?
2026-10-22 JST. Original three-country bilateral-first, inherited-depth V2b. Stacked above Stage19. **Research verdict: strong candidate headline ONLY IF the SU region is proved nonempty.** No such proof currently exists. The requested three-regime phase portrait is NOT established.

## 1. Precise backward-induction government decision sets (one offer depth g)
Let s denote SW national welfare; m(g,p), o(g,p), i(g,p) respectively the bilateral member, bilateral outsider, and country-in-grand-national welfare following all firms' TRUE design Nash. p denotes a primitive path, preferentially eta with rho,kappa,d fixed and lambda=0 original model (avoid centering interpretation of a moving legacy z). The existing bilat-first protocol presents AB at g, then inherited-g accession by C subject to home and incumbent votes. Direct multilateral offers are not in the menu.

The offer yields terminal IS (under weak acceptance upon indifference) if:
  i(g,p) >= s   (initial country B expects successful accession and accepts),
  i(g,p) >= o(g,p)   (C consents),
  i(g,p) >= m(g,p)   (existing coalition consents to expansion).
An initial AB agreement need NOT satisfy m>=s if later grand accession is anticipated; demanding this incorrectly deletes admissible IS histories.

The same depth yields terminal SU if:
  m(g,p)>=s (B accepts the eventual SU outcome)
  AND (i(g,p)<o(g,p) OR i(g,p)<m(g,p)) (C or the incumbents strictly reject enlargement).
At equality one must follow the specified weak-acceptance/tie convention and not silently count two incompatible terminal continuations. If all votes fail the eventual terminal payoff to the proposer is s (SW).

Let E_I(p), E_U(p) denote those depth sets for g in (0,1]. Define offer payoff envelopes
  P_I(p)=sup_{g in E_I(p)} i(g,p), P_U(p)=sup_{g in E_U(p)} m(g,p),
with sup empty set = -infinity. The government's overall welfare value has supremum V(p)=max{s,P_I(p),P_U(p)}. This is a **correct decision reduction**, NOT an economic threshold theorem by itself. Actual pure-government-SPNE existence and selected depth need attainment and weak-vote tie checks; SU terminal feasible set can be open.

Under strict, attained comparisons: SW if s>max(P_U,P_I), SU if P_U>max(s,P_I), IS if P_I>max(s,P_U). Ties or nonattainment require a separate theorem. This is a tautological screening lemma; it should be in an appendix rather than advertised as a novel result.

A genuine primitive THREE-region theorem would require explicit eta1<eta2 with e.g. strict SW for eta<eta1, strict SU for eta1<eta<eta2 and strict IS for eta>eta2. Nonempty SU regime is a MATHEMATICAL GATE, not a desired conclusion.

## 2. A new exact structural benchmark theorem: eta=rho>0 => grand IS, g*=1
For all positive d, 0<eta=rho<1, beta=1-rho, sufficiently regular/unique interior private Nash, and the unchanged once-paid symmetric residual-design cost specification (including lambda=0), the technical-link coefficient in the fulfilled-expectations Cournot matrix vanishes: delta=rho-eta=0. Thus any H_ij off-diagonal g changes B substitution AND network utility equally but leaves M=I+B-eta H, the private design Nash and Cournot equilibrium quantities **IDENTICAL across SW, SU and IS at every g**.

By Nash uniqueness/symmetry, all three firms' original private residual index equals z and output q0=d/(2-eta+2beta*z)>0 at every history. Since CS=q'Bq/2, and each new undirected link increases CS by rho*g*q0^2, while firms' worldwide profit/resource cost is policy-independent:
  s = W_i(SW),
  W_i(SU,g) = s+rho*g*q0^2    (one AB edge),
  W_i(IS,g) = s+3rho*g*q0^2  (AB, AC, BC edges).
These are exact for EVERY g, and for EVERY country i (same global CS + symmetric home profit).

Thus all required votes are strictly positive for any g>0, the proposer strictly wants g=1, and **unique substantive government-terminal regime is IS at g*=1** under the actual bilateral-first agenda. This statement makes NO phase-classification claim for eta on either side of rho. A bare delta=0 is a STRUCTURAL DESIGN RESPONSE boundary, not an SW/SU/IS triple cutoff. The strict gains are analytically derived without interval numerical arguments or new primitives.

## 3. Fixed-parameter rigorous anchors from the inherited stack
- Original lambda=0 theta0=(eta=.758,rho=.9,kappa=.8505,d=1): inherited Stage14 exact all-g proof gives terminal SW under original protocol. No positive-depth accepted bilateral or subsequent grand offer, but hypothetical direct grand is Pareto beneficial.
- lambda=5 same eta=.758: inherited Stage18 exact proof gives terminal IS optimal depth 0.05433320681<g*<0.05433320682, assuming weak acceptance at indifference. Stage17 excluded terminal SU/SW via complete bilateral payoff envelope.
- Original lambda=0, eta=rho=.9: new structural theorem gives terminal IS g*=1. Explicit sample z≈0.58695017 and q0≈0.82142943, but the theorem is general.

Thus SW and IS are genuine outcomes at varied original network-effect eta and/or optional lambda. **There is currently NO proven example of a government-optimal terminal SU in this exact V2b variant.** It is incorrect to present a three-phase diagram as established.

## 4. Conservative numerical exploration — NOT a rigorous phase certificate
Independent full-3-firm design Nash diagnostic with exact derived unilateral first-order conditions, numerical root and continuous-g sampling (script maintained separately as a diagnostic artifact): for rho=.9, kappa=.8505, d=1, eta in {.740,.750,.758,.765,.770,.780,.800,.900}, lambda in {0,1,5}, computed terminal proposer choices are SW at eta<=.75, IS at eta>=.765, and the eta=.758 status follows earlier exact anchors (SW at lambda0, IS for lambda1/5). No SU winner appears in these 24 cases. Some terminal SU offers ARE feasible (for eta=.765 or lambda5 eta=.758), but their optimized payoff is lower than accepted IS alternatives. The grid is NOT an all-depth supremum or all-eta interval proof. Near boundaries, root and grid artifacts could obscure tiny payoff regions.

A broader exploratory random-grid search across eta,rho,kappa,lambda with locally valid firm roots likewise found no clear SU-best case; this search is not exhaustive and cannot establish SU impossibility in the model.

## 5. Required theorem tests before calling this a full-paper headline
1. Correct original sequential veto/anticipatory B decision sets; do not use SU member consent as a prerequisite for IS.
2. Choose p=eta as the FIRST single-primitive family with rho=.9, kappa=.8505, lambda=0; network effects must be economically central. Compute SU and IS full Nash continuations with justified existence and valid quantities.
3. Prove or disprove that E_U can be proposer-optimal anywhere on an eta interval. If SU is EMPTY as an optimal outcome, **publish a two-regime impossibility/selection result if novel** rather than inventing p1,p2.
4. If SU exists, locate two ordered thresholds with strict signed crossings and no disconnected price/policy islands, using symbolic sufficient conditions plus rigorous interval exclusions. Distinguish existence vs uniqueness and tie conventions.
5. Check the same classification against Gandal & Shy (2001 JIE), whose published abstract already shows a three-country SU under conversion costs; and Klimenko (2009 JIE), which reports compatibility choices depending on network intensity. Do not claim novelty of 3 outcomes itself.
6. Only upon regime theorem + priority clearance elevate to the **MAIN Proposition** of the revised normal-length paper. Until then this is exploratory Stage20: CONDITIONAL GO, NOT full-paper submission GO.

No main/Theory Freeze edits, no journal submission or added primitives.
