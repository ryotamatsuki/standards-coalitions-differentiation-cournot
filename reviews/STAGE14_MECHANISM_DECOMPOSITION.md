# Stage 14 — Mechanism, identification and counterfactuals

Source fixed at PR12 `79b1a2a140754699a5a4c6d27aa469608e508bee`; 2026-10-22 JST. Mathematical details: `STAGE14_THEOREMS_AND_PROOFS.md` and `../verification/stage14_math_audit.py`.

## What actually happens

In the certified region delta>0: an interface edge raises substitution more strongly than network willingness to pay in the Cournot fixed-point matrix. Firms then economize on costly residual differentiation: the member response u'(0) exceeds the outsider response v'(0), both positive. A government's consumer and rival-design incidence can outweigh its small positive fixed-design interface gain. Its own firm's optimized design profit has zero own-design derivative, but neither domestic consumers nor rival firms are included in that private envelope condition.

At the witness the member's direct welfare slope is approximately +.0067679241; the induced consumer and rival-exporter terms are -.005216220 and -.009853524, producing -.0083018200. This is a **national incidence amplification**, not the finding that firms choose a first-order loss on their own optimized expenditure. The large consumer benefit and exporter-profit loss already nearly cancel in the direct effect. Numerical smallness of the residual must not be hidden by calling the response “large.”

## Five distinct layers

Let F be the full three-firm unilateral design pseudo-gradient, J=F_x, b=F_g, and w=grad_x W_i. On a regular interior Nash branch, `x_g=-J^{-1}b`, hence

`W_i'=W_i,g - w' J^{-1}b`.

1. **Direct policy incidence:** W_i,g fixes every firm's design but lets quantity competition and fulfilled expectations resolve. It already contains both the direct B_g term and quantity responses. It is not a partial derivative with quantities frozen.
2. **Private direct design adjustment:** define J0=diag(J), `r0=-J0^{-1}b`. This is a local own-best-response derivative with rivals' designs fixed.
3. **Strategic feedback:** `r-r0`, where r=-J^{-1}b. The exact decomposition is `W_i'=W_i,g+w'r0+w'(r-r0)`. It counts every induced effect once. It is a named local convention, not a second equilibrium benchmark. Near fragmentation positive cross-design derivatives and a nonsingular M-matrix amplify the direct adjustment. The economic incidence remains in w.
4. **Government depth reoptimization:** choose the proposer-optimal feasible g in EACH government game. Fixed-g comparisons do not themselves locate that maximum. With binding votes, changing feasible sets and sometimes discrete regime changes, an unconstrained envelope derivative is insufficient. The frozen `.05` offer is a strictly feasible witness that dominates every terminal-SU policy, not the identified optimal depth.
5. **Full institutional reorganization:** at each SU/IS history recompute all design and quantity equilibria, then C compares i(g) with o(g), incumbents compare i(g) with m(g), and B compares its anticipated eventual payoff with s. An IS-vs-SW Pareto gain does not imply any one accession vote is positive.

For finite benchmark changes, this order is explicit: first fix a government offer, then change the design strategy set and resolve downstream markets, then resolve government feasibility and optimization. A different sequential decomposition may allocate cross terms differently. Only the final total and the stated local derivative identities are order invariant. No Shapley attribution or unique causal decomposition is claimed.

## Controlled benchmark matrix

No canonical B-EXO/B-T/B-X naming scheme was found in the active V2b model/evaluator. The following are Stage14 definitions, not silently inherited labels.

| Benchmark | Government policy | Firm design | What it identifies |
|---|---|---|---|
| E0: conditional fixed-design allocation | Fix S,g | x fixed at actual SW Nash z after all histories | Direct technical/network market incidence |
| E1: conditional endogenous allocation | Same S,g | Resolve actual private design Nash | Design response at exactly the same offer |
| G0: restricted-design government game | Resolve original complete agenda and optimal g | Fixed z at every history, same once-paid cost | Frozen-design policy forecast, an alternative restricted-strategy game |
| G1: FULL | Resolve same complete agenda and optimal g | Resolve actual design Nash at every history | Actual substantive SPNE outcome |

E0 to E1 changes only firms' strategy freedom. E0 to G0 or E1 to G1 adds government optimization and consent, not a new demand environment. G0 to G1 identifies the difference in predicted institutional outcomes attributable to allowing redesign **under this agenda**. Merely contrasting two unconstrained maxima of national welfare would not do so.

At g=.05 (rounded illustration; interval proofs provide signs):

| Margin | Frozen designs | Actual endogenous designs |
|---|---:|---:|
| Terminal bilateral member m-s | +.000272382 | -.000473474 |
| Outsider accession i-o | +.000234617 | -.001246547 |
| Conditional international i-s | +.019318616 | +.016934628 |

The first row is B's initial comparison only if accession will NOT occur. Under successful anticipated accession, B instead compares i-s. For the actual game C rejects every g>0; B then faces terminal SU and rejects every positive g. In the frozen game some positive international offer is optimal, by the strict feasible-IS versus entire-SU-envelope comparison.

## Ablation and necessity tests

- Freeze design responses: the certified government outcome changes from no substantive union to positive IS. Redesign is necessary for **this controlled contrast**, not for all conceivable failures of standards cooperation.
- Balance channels rho=eta: design and quantities become independent of g; pure consumer network gains lead to IS at g=1 under the supplied curvature/interiority conditions. Government optimization alone does not explain the main witness.
- Remove network benefit eta=0 while retaining delta=rho>0: at fragmentation the fixed-design member slope has `D PL^3/d^2 = -2 rho P s0 - 6 rho alpha <0` (alpha=2). Thus the positive-direct/negative-total reversal condition cannot hold. This is a local necessary condition for the audited mechanism, not a proof that all no-network government games have the same outcome.
- Remove the bilateral-first constraint by permitting a direct grand offer: the witness's endogenous IS(.05) is strictly accepted against SW. Redesign alone is therefore insufficient to block all institutions.
- Remove redesign through delta=0, or set induced incidence to zero: the local reversal D>0>D-L disappears. These are structural boundaries; the general chain rule itself is not novel.

## Observable implications and failed literal examples

An admissible empirical test would compare technically connected interfaces with separately measured residual product features, then estimate post-policy design responses and government outside-option payoffs under an identifiable accession commitment. In the certified local region predict more residual similarity among members, a smaller positive outsider response, and an accession wedge even when a grand allocation beats fragmentation. Mere growth in compatibility or a failed negotiation cannot identify the mechanism.

Official CHAdeMO documentation describes ChaoJi as joint development by CHAdeMO and China's CEC with international partners: <https://www.chademo.com/technology/high-power>. It establishes cross-border interface cooperation, not three sovereign welfare maximizers or fixed-depth inherited admission. EU USB-C rules are mandatory regulation, not voluntary bilateral-first accession: <https://commission.europa.eu/news-and-media/news/eu-common-charger-rules-power-all-your-devices-single-charger-2024-12-28_en>. Both can illustrate the distinction between technical interfaces and other product attributes; neither is validated evidence for the institutional theorem. No exact real-world implementation of the required agenda was established in this audit.
