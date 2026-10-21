# Stage 14 — Model semantics and economic consistency

Date: 2026-10-22 JST. Source: PR12 head `79b1a2a140754699a5a4c6d27aa469608e508bee`, *International Standards Coalitions and Endogenous Product Design*. Canonical map only unless explicitly stated. Earlier V1, Private Compatibility, and public-private bargaining projects are excluded.

## Objects that must not be conflated

| Object | Decision maker / meaning | Economic limitation |
|---|---|---|
| `g in [0,1]` | A proposes technical interface compatibility depth; accepted union members share it | C cannot renegotiate this depth at accession |
| `H_ij` | Off diagonal: g for members of the same union, zero otherwise; diagonal one | SW has no off-diagonal link, SU only AB, IS all three links |
| `x_i in [0,1]` | Firm i chooses costly residual similarity after government decisions | This is a reduced-form substitutability shifter, not a derived physical product-location metric |
| `1-x_i` | The reverse index of that SAME residual attribute | No second independent strategy; a higher value means more differentiation |
| `X_ij=(x_i+x_j)/2` | Pairwise residual similarity, diagonal one | Even identical residual indices do not imply identical full products |
| `rho` | Weight of technical interface similarity in conditional substitution B | Not a government's policy variable and not network intensity eta |
| `B=rho H+(1-rho)X` | Consumer quadratic substitution matrix | Distinct from the fulfilled-expectations Cournot matrix M |
| `eta` | Network willingness-to-pay strength at fixed expected local use | Expectations are held fixed during unilateral quantity deviations |

The source uses “homogeneity” and “similarity” interchangeably; prefer **residual similarity index** throughout. Product differentiation is a defensible *reduced-form* interpretation of `1-x_i`; a Lancaster attribute-space foundation, an empirically measured distance, or independent quality choice has not been established. Adding a second design variable would not cure this by itself.

## Demand, quantities and welfare, independently reconstructed

With fixed expected use n, `U=a 1'q - q'Bq/2 + eta q'Hn`. Therefore `p=a1-Bq+eta Hn`. B is symmetric, so integrability holds and the conditional Hessian is -B. H is PSD in the three listed regimes. X is affine on the design cube; all its principal minors at the eight vertices are nonnegative (Stage13A exact checks rerun). Convexity of the PSD cone then gives X PSD on the cube and hence B PSD for every allowed rho. At boundary points strict definiteness need not hold. Demand is conditional on n: differentiating utility after substituting n=q would yield a different demand system and is not permitted here.

Firm quantity FOC at fixed n: `p_i-c-q_i=0`, because B_ii=1. Fulfilled expectations n=q give

`M q=d1`, with `M=I+B-eta H`, `alpha=M_ii=2-eta`, `beta=1-rho`, `delta=rho-eta`.

For any primitive a, where the interior continuation is regular,

`q_a=-M^{-1} M_a q` (plus `M^{-1}1` if a=d), and along that fulfilled equilibrium `p_a=q_a` for a other than c. An interface edge changes M with weight delta, whereas a residual edge changes it with weight beta. The direct substitution and network channels can offset, even though they are separate in utility. A more competitive conditional demand coefficient B alone does not determine the equilibrium quantity response.

Consumer surplus is `U-p'q=q'Bq/2`. Its derivative is `CS_a=q'B q_a + q'B_a q/2`; the explicit matrix term and the induced quantity term both matter. Adding `eta q'Hq` again double counts utility. Worldwide firm income is `Pi_i=3q_i^2-kappa(1-x_i)^2/2`; design expenditure is paid once. National welfare is `W_i=CS+Pi_i`. World welfare is `sum_i W_i=3CS+3sum_i q_i^2-sum_i K_i`. Counting each firm's worldwide profits once, across home countries, is consistent.

At the witness, M's off diagonals are in [0,.242], its diagonal is 1.242, and the nonnegative quantity fixed point is an interior contraction on its invariant cube. The fresh canonical certificate checks asymmetric firm deviations, globally unique interior design Nash, and every g. These are substantive restrictions. For arbitrary eta>rho, the parameter domain alone does NOT guarantee a nonnegative fulfilled-expectations equilibrium: the inherited exact counterexample eta=.99, rho=.01, IS g=1, x=0 gives the inadmissible linear solution q_i=-20/19 and no nonnegative fixed point. General results require explicit equilibrium assumptions.

## Is rho an independent economic parameter?

It is independent of eta and of g in the primitives, but its comparative statics simultaneously change beta and delta. They cannot be varied as three unrelated primitives: `delta=alpha-beta-1`. Holding eta fixed, a rho increase changes both the interface channel and the residual design channel. Rewriting `r_i=beta x_i` does not eliminate rho: the strategy domain becomes [0,beta] and costs become `kappa(beta-r_i)^2/(2 beta^2)`. Thus rho is not merely a harmless units normalization; nor has an empirically identified rho been supplied.

## Minimality and revisions proposed, not applied to the manuscript

Keep the single x_i. Replace any “two independently chosen differentiation and homogeneity levels” by “one residual similarity index and its reverse differentiation index.” Replace an unconditional “standardization induces re-differentiation” by the sign-conditioned Nash comparative static; in the certified main region firms choose MORE similarity. Replace “stable international regime” by “substantive subgame-perfect outcome of the stated bilateral-first accession game.” Arbitrary coalition deviations, renegotiation, transfers, and direct grand offers are not in that equilibrium concept.

These wording changes are review proposals. Frozen primitives, prior proof scripts, main, and the existing manuscript sources are unchanged by Stage14.
