# Stage20 adversarial SU-optimal-existence audit — rigorous facts vs numerical stress
Date 2026-10-22 JST; supplements Draft PR #20. **Finding: SU-optimal existence NOT PROVED. A broad numerical search found no valid-grid SU winner; rigorous OPEN NEIGHBORHOOD NO-SU theorem proved at eta=rho.**

## 1. Exact game/decision envelopes

At any correctly defined three-firm Nash continuation let s=SW country payoff, m(g)=SU member payoff, o(g)=SU outsider payoff, i(g)=IS common national payoff. The bilateral-first inherited-g stage, anticipating C and incumbents' vote, yields:
- terminal IS if i(g)>=s, i(g)>=o(g), i(g)>=m(g);
- terminal SU if m(g)>=s and (i(g)<o(g) or i(g)<m(g)) (assuming weak acceptance upon ties);
- otherwise SW.
Define V_I=sup{i(g): g∈[0,1], terminal IS feasible} and V_U=sup{m(g):g∈[0,1], terminal SU feasible}, with empty-set sup -infinity. SU-optimal **requires** V_U>max(s,V_I) AND a maximizing offer attained. Merely showing m(g)>s and outsider veto at some g is INSUFFICIENT.

## 2. Theorem — genuine OPEN SET with NO terminal SU optimum

**Theorem (global grand-standard dominance near balanced network effects).**
Fix rho0=eta0∈(0,1), kappa>0, lambda>=0, d>0 and a fixed historically installed reference z whenever lambda>0. Suppose at the center the firm design equilibrium for the entire allowed policy strategy set is unique, symmetric, strictly interior and regular, with strictly positive fulfilled-expectation Cournot quantities; assume these regularity margins are uniform and strict (e.g., the inherited global Rosen bounds). Then there exists epsilon>0 such that, for the original model's same kappa,rho0,d,lambda and eta varying in (eta0-epsilon,eta0+epsilon), the government's unique selected policy DEPTH AND TERMINAL TYPE are

**g*=1 and IS, never SU or SW**, under the inherited weak-tie acceptance and original bilateral-first negotiation protocol.

**Proof.** Exactly at eta=rho, `M=I+B-eta H=I+(rho-eta)H+(1-rho)X` is INDEPENDENT of H at any x. Hence all downstream output/firm design profiles are independent of coalition regime and policy g. By the assumed unique symmetric equilibrium write q_i=q0>0 and x_i=zbar. Each undirected standards edge changes B by rho*g at the two symmetric off-diagonal locations, and CS=q'Bq/2 therefore increases exactly rho*g*q0². Profits and once-paid design costs are identical across regimes. Thus

W_i(SW)=s,
W_i(SU,g)=s+rho*g*q0² (for ALL i, including C),
W_i(IS,g)=s+3*rho*g*q0² (for ALL i).

So IS g=1 strictly satisfies initial B assent, outsider accession and incumbent widening. Its strict margin over EVERY SU proposer payoff for any g∈[0,1] is >=2*rho*q0². Its grand national payoff has uniformly positive derivative 3*rho*q0² for all g. Positivity, full design Nash uniqueness, interiority and the real-analytic policy welfare continuation persist on a common open neighborhood of the center via uniform game regularity plus compactness of g∈[0,1]. Consequently there exists epsilon>0 on which (i) IS g=1 remains strictly unanimously accepted, (ii) IS g=1 strictly exceeds the sup of all possible terminal bilateral payoffs and SW, and (iii) the derivative of the IS proposer payoff remains positive for ALL g∈[0,1]. Hence government g*=1 and IS on that neighborhood. QED.

The theorem proves a nonempty IS-open-regime and SU exclusion near rho=eta; it does NOT prove SU never optimal outside it. The size of epsilon is existential, not interval-certified.

## 3. Broadened numerical search — NUMERICAL ONLY, NOT an impossibility proof

Stand-alone locally executed reproducible `/mnt/data/scan_su_audit.py` and `/mnt/data/regime_search.py`:
- pseudorandom seed 21; N=300,000;
- rho uniform (0.08,0.9999);
- eta uniform (0.03,min(0.995,(2+2rho)/3-0.0005)); the eta cap is a screening restriction to avoid clear negative IS quantity branches at certain full depths;
- kappa loguniform (0.09,100);
- lambda=0 in ~20% cases, else loguniform (1e-6,1000);
- 70 evenly spaced depths g=j/70 PLUS 70 geometrically spaced depths g=10^(-7+7j/70);
- for EVERY regime and depth the actual 2-index SU/1-index IS firm-design Nash FOCs are solved independently by nonlinear root iteration, then country-specific welfare and every veto are evaluated, with design x in (0,1), positive quantities and numerical solver success REQUIRED at each sampled depth.

Result JSON, independently re-run:
  attempted parameter draws = 300000
  fully grid-valid at ALL 140 depths = 190388
  some SU feasible across the full search = 3429
  fully grid-valid SU actually beating both SW and IS = **ZERO**
  best SU-minus-IS margin among fully grid-valid draws = -0.0000775680978

Important qualifiers:
- A numerical solver returning a root at 140 points does NOT rigorously prove a full Nash game, global uniqueness, nor quantities at intermediate unsampled depths.
- The search restricted the eta distribution and has finite samples; the absence of an observed counterexample cannot establish SU global impossibility.
- SU can be locally feasible but lose to an ACCEPTED IS at a different g, as in canonical eta=.758,lambda=5 (Stage18, certified): SU proposer max ~0.00022056 over SW, while IS optimizer yields ~0.02058599 over SW.

## 4. FALSE POSITIVE from inadmissible negative-quantity history

An exploratory point approximately (rho=.12773875, eta=.69824186, kappa=22.56468, lambda=34.13852) reports apparently competitive SU at g≈.7667; but when the SU continuation is pushed toward g=.8 and later, the original all-interior full Cournot/Nash formulas become inapplicable: at g=.7667 the outside firm's quantity is already approximately 0.0076103 and the numeric interior SU Nash solver ceases to yield a valid positive-quantity equilibrium at g=.8. Directly extrapolating q=M^{-1}d1 past the boundary would produce economically invalid NEGATIVE output.

One cannot restrict the government menu post hoc to positive-interior g or declare a no-entry corner without building and proving the CORRECT nonnegative Cournot complementary equilibrium and firms' renewed design choice. Such a different extension has NOT been audited and does not establish SU optimality in the frozen V2b continuum.

## 5. Exact mathematical question STILL OPEN

Does there exist any economically admissible original-V2b primitive vector and a subgame-perfect proposer offer for which final terminal SU strictly beats SW and the optimal attainable terminal IS? Neither a SU witness nor a universal impossibility theorem has been established. The model may have a **missing middle** due to zero treaty-entry costs and a symmetric three-country consumer surplus channel, but this is a HYPOTHESIS, not a result. Proving it would require a symbolic dominance reduction or global interval verification over a justified primitive box, with proper parameter-space coverage, all-depth terminal Nash and tie/attainment analysis.

**Publication gate:** The author REQUESTED A PROOF, and an unconditional yes/no proof is not delivered. Report **OPEN** rather than retroactively relabeling broad samples as a theorem. If an admissible SU region is never rigorously produced, the three-category headline MUST NOT be published as proved; the two-regime SW-versus-IS selection may be an alternate agenda-dependent economic theorem. No extra primitive, manuscript/main/Freeze mutation or journal submission.


## Correction (2026-10-22): strict interior numerical search gate
The FIRST run mistakenly treated a symmetric IS firm-design output y=0 as passing an interior strategy check. A fresh full 300000-draw seeded rerun, changing the admissibility condition from y>=0 to **0<y<1** and requiring 0<u,v<1 on every sampled depth, yields **190388** fully 140-point grid-valid draws, **3429** draws with some SU-feasible offer, and **zero** fully grid-valid SU-optimal winners. Prior counts 208606 and 3696 are superseded. Numerical Newton and FOC checks cannot establish full all-g Nash optimality; the stress search is explicitly NOT proof.
