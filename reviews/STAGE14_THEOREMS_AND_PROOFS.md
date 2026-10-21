# Stage 14 — Theorems, proofs, counterexamples and boundaries

Source fixed: `79b1a2a140754699a5a4c6d27aa469608e508bee` (PR #12); PR #9 is `07b275fd5693d8160234bf2e318e24e2fa4878c2`, PR #10 is `7521ba0169cc0e6ef2f9cdbd61accc9b59f63884`. This audit does not alter the frozen model or manuscripts. Run `python verification/stage14_math_audit.py > verification/stage14_math_audit.log` from repository root. All interval inequalities in its JSON use `fractions.Fraction`; decimal output is display only. No earlier V2b verification program is imported. Code independently derives derivatives using differentiation of linear systems at the symmetric point, rather than copying Cramer's-rule expressions from Stage 13A.


## Final Stage14 integration note

The three economically ranked **candidate packages** are: (1) local redesign–national-incidence–consent reversal, including the explanatory amplification identity and the nonadditive local test; (2) institution-specific all-depth frozen/FULL reversal on a nonexplicit open primitive neighborhood, an ordinary robustness corollary; (3) the direct-grand-offer boundary showing that the participation failure is agenda dependent. These are parts of one candidate contribution, not three separately novel economic mechanisms.

The conditional center premises in section 7 are discharged by the fresh successful executions in `verification/stage14/canonical_global_rerun.log`, `stage13a_rerun.log`, `nonlinear_rosen_rerun.log` and `nonlinear_policy_rerun.log`, plus the exact Pareto gap rerun recorded in `pareto_rerun.log`. They do not give a numerical parameter radius. A separate global nonlinear check at the inherited phi=x² is retained; it is not the new nonadditive test.

## 1. Findings and mathematical scope

The corrected local consent mechanism survives independent derivation. A useful explanation is **amplified net competitive interaction and the national incidence of rivals' redesign**, not re-differentiation in the canonical parameter region. The all-depth baseline result depends on its separate repaired uniform interval certificate. The present new clean-room program proves local statements and two targeted diagnostic results; it does not re-certify the old all-depth program.

There is no newly discovered fatal contradiction in the frozen baseline in the inspected material. This does not imply that publication novelty or importance passes. Most newly displayed deductions below are routine reorganizations/corollaries of existing results and must not be counted as additional independent economic discoveries.

## 2. Corrected sign and independent incidence derivation

Use `a=alpha=2-eta`, `b=beta=1-rho`, `delta=rho-eta`, `t=beta z`, `P=alpha-t`, `L=alpha+2t`. At fragmentation `q=(d/L)1` and

`R=M^{-1}=(I-(t/L)11')/P`.

For firm i, `E_i=M_{x_i}` has beta/2 on the two incident edges and zero otherwise. Hence

`q_[i]=-R E_i q`,

`q_[ij]=R E_j R E_i q+R E_i R E_j q`.

These unilateral derivatives produce the published `ell,h,p,r` coefficients before imposing member symmetry. The code checks the own and cross Jacobian expressions exactly with SymPy. Own-profit stationarity gives only `Pi_{A,x_A}=0`; it does not eliminate consumer effects or rivals' effects on the domestic firm's worldwide income.

Independent demand-matrix differentiation gives

`CS_{x_j}=-C`, `Pi_{A,x_B}=Pi_{A,x_C}=-V`,

where

`C=beta d²(eta+2t)/L³`,

`V=3 beta d²(alpha-2t)/(P L³)`.

Therefore the correct induced loss is

`Lloss=C(2u'+v')+V(u'+v')`.

PR #9's retained historical research display subtracts the second component; the corrected-minus-literal expression is exactly `2V(u'+v')`. The canonical manuscript `02a_analytic_design_results.tex` and `A_analytic_proofs.tex` use the correct plus sign and explicitly identify the historical erratum. Under Proposition B conditions both components are genuine losses. At the true baseline SW root, the new exact interval enclosure gives

- `D in (0.0067294,0.0068066)`;
- `Lloss in (0.0150668,0.0150725)`;
- `m'(0) in (-0.0083431,-0.0082602)`.

These bounds are deliberately wider than the preceding Stage 13A bounds and independently reproduce the strict signs. No bare FOC root is promoted to Nash: the actual fixed-parameter SW root is bracketed by exact FOC signs on `[0.7185,0.7187]`; the full asymmetric Rosen bound is re-evaluated as a strict rational inequality, and global uniqueness plus symmetry identify the genuine interior Nash.

## 3. A clearer structural threshold — explanatory restatement, not a third discovery

Write

`A=d²/L²`,

`B=d²[2(1+2t)/L³+6alpha/(P L³)]`,

`Cstar=Lloss/delta`.

Under Proposition B assumptions, `A,B,Cstar>0`. The frozen direct effect and redesign loss satisfy

`D=rho A-delta B`, `Lloss=delta Cstar`.

Consequently the local strict frozen/endogenous reversal holds if and only if

`A/(B+Cstar) < delta/rho < A/B`.

The left inequality says the net competitive incidence, including rivals' design response, is large enough to overturn the government's initial gain; the right says the initial fixed-design forecast still predicts a gain. The interval is nonempty because `Cstar>0`. For the baseline true root, conservative exact-interval displays are

`lower threshold in (0.1550183,0.1550454)`,

`delta/rho=71/450=0.157777...`,

`upper threshold in (0.1600761,0.1601028)`.

**Crucial qualification:** these thresholds themselves depend on the original primitive vector through beta, alpha, the fragmentation root and its response Jacobian. This is an explicit structural test, not a comparative-static theorem obtained by varying delta/rho while holding the threshold coefficients fixed. In the canonical model `delta=alpha-beta-1`, so alpha, beta and delta are not independent primitives. This is a transparent equivalent form of corrected Proposition C, not independent novelty.

## 4. IS amplification instead of assumed re-differentiation

For the genuine interior symmetric IS branch let `t=delta g+beta y(g)` and `K=kappa-beta G(t)>0`. The established Nash FOC gives `y_g=delta G/K`. Thus

`t_g=delta+beta y_g=delta*kappa/K`.

This identity is independently checked exactly in the new SymPy program. If `G>0`, then `0<K<kappa`. The endogenous response amplifies the magnitude of the net Cournot cross interaction relative to the fixed-design value delta:

- if `delta>0`, `y_g>0`, so firms choose *more* residual similarity, with `t_g>delta>0`;
- if `delta<0`, `y_g<0`, so residual differentiation increases, with `t_g<delta<0` on a valid branch;
- if `delta=0`, private allocation is unchanged along this symmetric IS branch.

It is wrong to describe the canonical witness as firms restoring differentiation to offset technical compatibility. The result concerns the **net** Cournot coefficient after network feedback. The actual substitution coefficient has derivative `B_ij,g=rho+beta y_g`, which is a different object. For delta>0 both net and gross substitution rise; for delta<0 the design response may offset some gross substitution, but neither the full offset nor its welfare sign follows automatically.

The bound `5alpha>8t` is needed for `G>0`. If it fails, or interiority/regularity fails, the amplification sign conclusion is unavailable. No full-demand generalization follows from this scalar identity alone.

## 5. Targeted test 1: a coherent nonadditive compatibility/design coupling

The unnormalized trial `B=B0+epsilon(H Hadamard X)` is **inadmissible over the full original strategy cube for epsilon>0**: at `H=X=11'` its off-diagonals are `1+epsilon` and two eigenvalues are `-epsilon`. That trial is not used as economic robustness evidence.

The accepted diagnostic is instead

`B_epsilon=(rho-epsilon)H+(1-rho)X+epsilon(H Hadamard X)`,

for `epsilon in [0,1/1000]`; preserve diagonal one, the original cost, government order and strategy sets. This is a genuine nonadditive mapping because the marginal technical-substitution effect depends on residual design. It is a separate diagnostic model, not a silent amendment of the freeze.

**Economic coherence on all g and all asymmetric designs.** H and X are PSD. The Schur product theorem makes `H Hadamard X` PSD, and all three coefficients are nonnegative. Thus B_epsilon is PSD throughout the entire strategy/policy cube. The fulfilled-expectations M has nonnegative off-diagonal entries at most `1-eta`, since `epsilon<rho-eta`. The original positive-quantity contraction proof applies. Also `||M_xi||_infinity<=beta+epsilon`, `M_xixj=0`, so the sufficient full-cube Rosen bound becomes

`kappa > 54(beta+epsilon)² d²/(eta² alpha²)`.

The new code checks this uniformly for epsilon in the stated interval with exact rationals. Hence the alternative does not require an ad hoc equilibrium selector. Interiority near g=0 follows from the unchanged interior SW root and the implicit-function theorem.

At fragmentation H has zero off-diagonal entries, so the SW design game and z are exactly unchanged. Define

`delta_e=delta+epsilon(z-1)`, `rho_e=rho+epsilon(z-1)`.

At g=0, the pseudo-gradient Jacobian is unchanged. The member and outsider policy forcing are

`p_e=6delta_e beta d²(alpha-2t)(2alpha+t)/(P²L⁴) - 3epsilon alpha d²/(P L³)`,

`r_e=6delta_e beta d²(alpha²-2alpha t+4t²)/(P²L⁴)`.

The extra negative member term is essential: it is the mixed derivative `M_xi,g` on the AB edge. Simply replacing delta in the additive formulas would miss it. The code independently derives both formulas from `q_xg=R M_g R M_x q+R M_x R M_g q-R M_xg q` and checks exact equality.

Use these forcings in the unchanged 2x2 Nash response system. Replace `(rho,delta)` by `(rho_e,delta_e)` in D; the consumer and rival incidence coefficients C,V at SW remain unchanged. Exact Fraction interval arithmetic over **all epsilon in [0,.001] and the true root bracket** confirms

- frozen direct member slope remains positive;
- actual member slope remains negative;
- each actual grand-union welfare slope remains positive;
- u' and v' remain positive.

The JSON/log provide the exact rational endpoint certificates. This establishes a local-depth consent reversal with a nonzero cross derivative in the demand mapping, plus Pareto-improving direct grand offers for small depths. **It does not certify all-positive-depth failure in the alternative**, nor arbitrary nonlinear kernels. Its contribution is to reject the claim that the *local* reversal mathematically requires exact additive separability.

## 6. Targeted test 2: agenda boundary and the outside-option wedge

For a smooth symmetric continuation, let a country's marginal welfare gain from an incident compatibility edge be `mu`, and from the nonincident edge be `nu`. Then

`m'=mu`, `o'=nu`, `i'=2mu+nu`, `(i-o)'=2mu`.

This follows from linearity of the differential and permutation equivariance. It is not a novel coalition theorem. In the present endogenous game the new interval computation proves

`mu=m'(0)<0`, `nu=o'(0)>0`, `i'(0)>0`.

Conservative canonical values are `mu in (-.0083431,-.0082602)`, `nu in (.3678348,.3678985)`, and `i' in (.3511488,.3513781)`.

Hence for every sufficiently small g>0:

1. The terminal bilateral union loses for its members (`m(g)<s`).
2. The outsider prefers staying outside that bilateral union to joining at inherited g (`i(g)<o(g)`).
3. A direct three-country IS offer with rejection to SW benefits **each** country (`i(g)>s`) and is unanimously accepted.

This is an analytic agenda boundary, independently supported by exact intervals at the true baseline root. It does not merely rely on the earlier pointwise numerical gap at g=.05. More generally the sufficient and necessary local inequalities for this wedge are `mu<0` and `2mu+nu>0`, i.e. `nu>2|mu|`.

The canonical all-depth certificate implies every original SPNE has no substantive agreement, but **that is not coalition-proof or strong stability against unrestricted joint deviations**. If all three governments can make a direct joint IS deviation, i(.05)>s already supplies a Pareto-improving one. The default protocol excludes that move. Therefore claims about a generally stable fragmented international system must be narrowed to bilateral-first inherited-depth SPNE.

With unrestricted budget-balanced transferable utility, any bilateral allocation whose total gain `2mu+nu=i'(0)>0` can locally compensate both members from the outsider's gain; similarly grand allocation gains allow compensation. But this is a **different** contracting structure requiring participation by the third government before an enforceable transfer. It cannot be described as a policy already optimized by the current game, and it is no new transfer-implementation theorem. The analysis identifies the excluded institutional margin rather than proving legal or political feasibility.

## 7. Safe topological full-depth neighborhood corollary

This corollary is valid if the repaired center certificates establish all the uniform premises below; it is not a substitute for verifying those certificates.

**Premises at theta0:** (a) all histories g in [0,1] have positive output and unique interior design Nash, with a uniform strict global Rosen margin and uniformly nonsingular Nash Jacobians; (b) reduced welfare paths are C1 and `m_g<=-a<0`, `(i-o)_g<=-b<0` uniformly on [0,1]; (c) frozen-design IS(.05) has strict consent margins and exceeds `sup_g frozen_m(g)` and SW by a strict amount; (d) actual IS(.05) strictly Pareto dominates SW. The supplied manuscript's center derivative bounds are -0.0079701929973 and -0.0150388833377; their executed repaired interval certificates must be consulted, not inferred from a finite grid.

**Conclusion:** a nonempty open neighborhood U of theta0 in the original symmetric primitive coordinates `(d,eta,rho,kappa)` preserves (i) all-g endogenous nonformation in the specified protocol, (ii) positive-depth frozen-design IS as an optimal governmental outcome, and (iii) Pareto-improving hypothetical actual IS(.05).

**Proof:** Compactness of the regime/policy/design sets and strict center margins preserve positive quantities and full-cube Rosen uniqueness for all theta sufficiently close to theta0. Uniform interiority of the center root follows from its compact continuous image inside the open design cube. Parametric IFT and a finite cover of the policy continuum give a jointly continuous and C1 unique Nash continuation on a common parameter neighborhood; no g-dependent parameter neighborhood is silently interchanged with a common one. Reduced payoff derivatives are uniformly continuous on the resulting compact policy set, so retain upper bounds -a/2 and -b/2 after shrinking U. For every symmetric theta, all regimes coincide at g=0 exactly. Integrating derivatives therefore proves the strict payoff inequalities for every g>0, including depths arbitrarily near zero. Pointwise uniform level perturbation alone would not suffice near zero; the derivative margin is the crucial ingredient.

The frozen SW Nash varies continuously in theta. Frozen regime welfare is therefore jointly continuous in theta,g, and its maximum over the compact SU interval is continuous. The strict vote inequalities at .05 and strict gap to the full SU envelope persist on a common neighborhood. The set of weakly consent-feasible IS offers is closed in compact [0,1]; its proposer maximum exists. The strict candidate .05 beats SW and all SU alternatives, so every optimal economic outcome can be supported by a positive IS offer (ties between feasible IS offers may remain). Finally continuity preserves the actual strict Pareto gap at .05. Intersect the finitely many neighborhoods to obtain U.

**Limits:** no radius, rectangular box or globally monotone primitive comparative static is proved. In particular U is not the explicitly certified Stage13A local-derivative coordinate box. This is an ordinary continuity corollary giving a precise existential scope to the original all-depth mechanism, not a new general industrial-organization mechanism. No arbitrary country asymmetry or variable function space is claimed.

## 8. Semantics of rho and evidence boundaries

Rho weights technical compatibility in the quadratic substitution matrix while beta=1-rho weights residual similarity. It is not a pure units normalization because H and X are independently controlled and H also enters the separate network term eta H. But varying rho changes both the direct policy-to-substitution channel and the marginal private design-to-substitution channel. Calling it simply the strength of network effects would be wrong (that role belongs to eta). The normalization `B_ii=1` fixes the own quadratic coefficient; rho can still be an economically independent primitive relative to eta and kappa.

The local Nash and welfare system can be expressed using alpha,beta,delta, but `delta=alpha-beta-1` restricts them. No comparative static may treat all three as independent while claiming to remain inside canonical V2b. Estimating the separate channels from quantities, prices and firm attributes would require an additional empirical identification argument; algebraic separation of symbols is not evidence of empirical identification.

The demand-system design variable is an index of pairwise residual similarity, not a fully specified physical attribute or spatial location. The quadratic consumer utility validates demand integrability and welfare accounting, but does not by itself justify any particular physical design distance, taste heterogeneity or production technology. Calls for a richer attribute model should therefore be assessed as interpretation/portability concerns, not an automatic mathematical invalidity of the present reduced-form choice.
