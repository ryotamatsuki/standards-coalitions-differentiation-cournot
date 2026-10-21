# Model specification (CURRENT: depth fixed through IS accession)

> **HISTORICAL V1 ONLY — NOT THE CURRENT V2b SPECIFICATION.** For all V2b research/manuscript work use the [Stage 8 canonical V2b freeze](V2B_THEORY_FREEZE_2026-10-21_v1.md). The V1 minimum-product-homogeneity constraint z≥g and demand matrix here are superseded and MUST NOT be mixed into the V2b independent technical-compatibility g and residual-design x model.


## Players and timing
A, B, C are ex ante symmetric sovereigns. Firms 1, 2, 3 are respectively headquartered in A, B, C. Each sells in every national market. Representative consumers and demand are symmetric across markets.

1. Stage 1: A proposes SU between A and B and depth `g∈[0,1]`. B accepts (SU proceeds) or rejects (SW final). This specific proposer/veto protocol is **an additional formalization** of the original general "A–B negotiation"; do not conflate it with Nash bargaining.
2. Stage 2: On an accepted SU, C chooses whether to apply to join.
3. Stage 3: If C applies, A and B decide whether to accept (all approval needed); accepted => IS, rejected => SU. **No depth renegotiation: the SU's g remains the IS's g.**
4. Stage 4: Firms simultaneously choose realized homogeneity `z_i`, where `0=maximum differentiation`, `1=full homogeneity`.
   - SW: all `z_i∈[0,1]`.
   - SU(AB): `z_1,z_2∈[g,1]`, `z_3∈[0,1]`.
   - IS(ABC): all `z_i∈[g,1]`.
5. Stage 5: Simultaneous Cournot quantities in each of the 3 national markets.

Production marginal cost `c` constant, `a-c=1>0` as normalization, `eta ∈ [0,1)`. No differentiation investment cost in the canonical baseline; no entry barriers; no migration costs; no transfers. Common national adoption cost `K(g)` is an **extension**, not a baseline primitive.

## Preferences and consumer prices
Within one national market, `q=(q1,q2,q3)'`, and `n^e` is expected per-country equivalent global network participation (world output divided by three under symmetric country demand). Consumer utility conditional on expectations:
```
U(q | n^e) = a * 1' q - (1/2) q' B(z) q + eta * q' H(z,S) n^e.
```
- `B_ii=1`, `B_ij=z_i*z_j` for i≠j.
- `H_ii=1`; `H_ij=z_i*z_j` if i and j belong to the **same** standard; zero otherwise.
- Fulfilled network expectations: `n^e=q` only **at equilibrium**, holding expectations fixed when a firm changes contemporaneous quantity.
- Inverse demand from marginal utility: `p=a*1-B q+eta H n^e`.
- At fulfilled expectations each Cournot firm i's FOC, provided q_i>0:
```
(2-eta) q_i + Σ(j≠i) [1-eta*same_standard(i,j)] z_i*z_j*q_j = a-c (=1).
```
Let `A=2-eta` and `k=1-eta`. The full interior quantity profile solves `M(z,S) q=1`, with `M_ii=A`, `M_ij=(1-eta*same_standard(i,j))*z_i*z_j`.
An algebraic inverse is not automatically a valid equilibrium when any component is negative. Verify nonnegative constraints, best responses, expectation consistency, and possible singularities for **every** upstream history.

## Profits and national welfare
At an interior Cournot equilibrium, `p_i-c=q_i`, so one-country operating profit of firm i is `pi_i=q_i^2`. Each firm's total world profit is `3*q_i^2` for symmetric national markets.

Consumer surplus for given fulfilled expectations evaluated as `U(q|q)-p'q=(1/2)*q' B q`. National objective:
```
W_A = CS_A + 3*pi_1; W_B = CS_B + 3*pi_2; W_C = CS_C + 3*pi_3.
```
No customs revenues, fiscal transfers, bias toward domestic goods, or cross-border profit redistribution. For the cost extension, subtract **each participating government's identical real adoption resource cost**, not a C-specific penalty.

## Caveats needing formal resolution
- `g` describes **minimum homogeneity**, not compatibility independent of product design. That link is strong and suits only design-constraining standards.
- Network utility `eta*q'Hn^e` includes expected own-product network and is linear in current consumption; there is a potential adoption/stock-vs-flow issue.
- Standards groups with `g=0` are institutionally distinct but observationally/strategically equivalent on the selected market continuation.
- Government proposal, voting, and indifference conventions must be stated when claiming an SPNE. When a strict cutoff optimum is not attained under rejection-at-indifference, a pure-strategy solution may require additional qualification.
