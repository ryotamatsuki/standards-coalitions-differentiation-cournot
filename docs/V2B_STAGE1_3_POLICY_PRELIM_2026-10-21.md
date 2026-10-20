# V2b provisional government continuation (2026-10-21)

**WORKING RESEARCH / NOT THEORY FROZEN.** This is a new, separate additive-homogeneity variant. Do not overwrite V1 or treat an old theory freeze as authoritative.

## Primitives
- Three symmetric governments, three domestic firms each serving all three equal national markets.
- Fixed coalition harmonization g: A proposes g to B; C applies for entry; A and B approve unanimously. IS inherits exactly the SU value of g.
- Stage 4: each firm chooses x_i in [0,1], with real resource design cost kappa*(1-x_i)^2/2.
- Stage 5: Cournot equilibrium of M q = 1 (normalization a-c=1).
- H_ii=X_ii=1, H_ij=g iff same standard (otherwise zero); X_ij=(x_i+x_j)/2; B=rho H+(1-rho)X; M=I+B-eta H.
- Government welfare W_i= (q'Bq)/2 + 3*q_i^2 - kappa*(1-x_i)^2/2.
- No standard adoption costs, transfers, market-size asymmetry or home-bias.
- Numerical examples use **high-kappa / interior Stage-4 equilibrium** regime and are NOT exhaustive formal proofs.

## Exact benchmark: eta=rho
When eta=rho, M=I+(1-rho)X, and all firms' demand-and-differentiation best-response correspondences are independent of coalition and g. When the Stage-4 continuation is unique and symmetric, all quantities, firm profits and design costs coincide across SW/SU/IS. For symmetric per-market quantity Q>0:
- W_SU_member(g)=W_SU_outsider(g)=W_SW+rho*g*Q^2
- W_IS(g)=W_SW+3*rho*g*Q^2
For any g>0, C strictly wants accession, A and B approve, and A chooses g=1. Thus a **full IS at g=1** is the backward-induction outcome under the specified bargaining and tie conventions (and unique symmetric continuation).

This proof establishes a knife-edge slice of the policy game, not a global theorem for arbitrary eta and rho.

## C entry and the government optimization
Write the Stage-4 equilibrium-generated welfare as M(g)=W_A^SU=W_B^SU, O(g)=W_C^SU, and I(g)=W_i^IS (same across countries). Accessions are approved only if I(g)>=M(g) and C accepts only if I(g)>=O(g). For g where both hold, the Stage-1 offer returns I(g), otherwise M(g); B can reject in favor of W_SW. At equality, choose application/approval, but pure-strategy existence needs a separate discontinuity/off-path audit.

## Numerical example: endogenous vs frozen differentiation
Parameters: eta=0.64, rho=0.77, kappa=5, a-c=1. The previous Stage-4 sufficient high-kappa criterion is satisfied: kappa > 81*(1-rho)^2 = 4.2849, since eta<rho.

SW: x_SW≈0.943111440, W_SW≈1.592598494.

**Endogenous x**:
- C's admissible positive-depth IS interval is approximately 0<g<=g_C≈0.382765417; the binding point satisfies I(g_C)=O(g_C).
- At g_C: I≈1.673094922, M≈1.595537881; A/B approve.
- Best numerical SU member welfare beyond C's cap ≈1.595877078, at g≈0.573547456. This is far below I(g_C).
- Hence **IS, g≈0.382765417** is the computed Stage-1 policy candidate.

**Frozen x** at each firm's SW choice x=0.943111440:
- C's cap g_C≈0.451137260.
- At g_C: I≈1.687469250.
- Best numerical SU member welfare beyond C's cap ≈1.596975426, below the admitted IS payoff.
- Hence **IS, g≈0.451137260** is the computed frozen-differentiation benchmark.

Holding firms' differentiation fixed therefore overstates the largest C-acceptable integration depth in this illustration by ≈0.068372; the endogenous choice reduces the government's compatible integration depth ≈15.16% relative to the frozen result. This is a **policy depth effect, not a SW/SU/IS coalition-label reversal**. The mechanism is that g affects residual product homogeneity, thus C's SU option and IS entry gain.

Use `python verification/v2b_policy_numeric.py` (NumPy and SciPy required) to reproduce the C entry thresholds, continuation payoffs and benchmark.

## Broader computational diagnostic, NOT a theorem
In a coarse 12x12 (eta,rho) parameter-grid study, filtering to positive-demand/high-kappa Stage-4 sufficient-uniqueness regime and numerically evaluating 26 g-values per cell, the candidates observed were zero-depth SW-equivalent and positive-depth IS. No positive-depth terminal SU was found. One cell had an interior IS g different between endogenous and frozen x. Neither this finite search nor the illustrative calculations establish absence of SU or exhaustively classify all SPNE.

## Open / mandatory audits
1. Independently verify the earlier sufficient Rosen-type condition for Stage-4 uniqueness and every displayed differential bound; do not treat passing numerics as mathematical proof.
2. Establish global government payoff maximization on the entire g interval and whether knife-edge participation indifference is implementable by the specified extensive-form strategies.
3. Identify whether any robust parameters yield terminal positive-depth SU or a change of final coalition regime when design is endogenous (rather than only a depth shift).
4. Perform theorem-level prior-art matching before claiming novelty.
5. Study inclusion of symmetric real adoption costs only after documenting the zero-cost baseline.
