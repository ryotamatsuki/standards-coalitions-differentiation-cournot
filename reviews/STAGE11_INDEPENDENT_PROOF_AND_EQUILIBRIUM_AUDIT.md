# Stage 11 — Independent proof and equilibrium audit (Referee 3)

Date: 2026-10-22. Repository input: `1146745c548734370de190899ac43370649a3c29`. Manuscript: the full LaTeX in Library ZIP `stage25_jpet_v04_with_refined_phase.zip`, version 2; extracted `stage25_jpet_v04/stage25_jpet_v04.tex`. This review does not adopt previous verdicts. Stable workflow v2.9 applies. No manuscript, Theory Freeze, or main-branch edits were made.

## Verdict and scope

**Mathematical correctness: PASS for the specified center/local theorems after fresh reconstruction and interval replay. Equilibrium validity: PASS conditional on the manuscript's mandatory weak-acceptance convention applying at every voting history. Proof verifiability: CONDITIONAL.** No fatal mathematical counterexample to the center controlled reversal was found. The article does not yet expose enough of the full-cube Nash proof, interval algorithm, and network-strip proof for a referee to verify its strongest assertions from the paper and appendix alone. This is MAJOR BUT FIXABLE, chiefly APPENDIX DETAIL NEEDED. A numerical Figure 3 failure must not be used to invalidate the separately replayed center theorem, or vice versa.

These PASS findings do not certify every phase-diagram parameter, a general demand system, arbitrary network intensity, an explicit open-neighborhood radius, or alternative negotiation protocols. This is an audit of a mathematical model, not an actual journal decision.

## 1. Materials, execution and evidence boundaries

Read: manuscript's model, every displayed theorem/lemma/proposition and appendix; `reviews/STAGE14_THEOREMS_AND_PROOFS.md`, `reviews/STAGE21_NO_SU_MISSING_MIDDLE_THEOREM.md`, `reviews/STAGE22_ABC_PROPOSITIONS_AND_PROOFS.md`; `verification/stage23_independent_reconstruction.py`; the full historical cleanroom Krawczyk and Pareto programs. Workflow Stage 11 and equilibrium-multiplicity refinement were checked.

The historical `verification/stage14/canonical_global_rerun.log` and `pareto_rerun.log` are **not present** in this checkout, although SHA256 digests are retained in `verification/stage14/source_manifest.json`. No claim to have read these absent logs is made. Re-running the underlying source supplies fresh, separately named evidence:

| Evidence | Status and precise scope |
|---|---|
| `verification/stage11/independent_matrix_audit.py` and `.json`/`.log` | Fresh implementation; no production imports. Full 3-firm unilateral matrix derivatives, numerical local Nash response, national gradient, edge identities, C1 numeric cutoff; exact-rational consumer-PSD vertex checks and global Rosen margin. Floating-point portions are diagnostics. |
| `verification/stage11/canonical_global_replay.log` | Successful replay of historical `v2b_stage04a_krawczyk_cleanroom.py`; 1000 exact-endpoint policy intervals covering every real g in [0,1], no adaptive splits needed. Mpmath outward-rounded interval arithmetic, not a formal proof assistant. |
| `verification/stage11/pareto_replay.log` | Successful replay of `v2b_stage06_pareto_holdout.py`; interval enclosure of actual endogenous IS(.05) minus SW. |
| `verification/stage11/adjustment_cost_replay.log` | Successful replay of exact Fraction root-bracket and threshold endpoint signs; local in g only. |
| `verification/stage11/network_face_replay.log` | Successful replay of exact Fraction rho=1 polynomial verification. The rho<1 extension is a mathematical compactness/Taylor argument, not numerically certified by this script. |

The first attempted interval execution failed because mpmath was unavailable. Installing mpmath and SymPy enabled the recorded successful run; the successful log supersedes that failed execution, rather than calling the failure PASS.

## 2. Primitives to Cournot and consumer welfare

Holding expectations fixed, differentiation of the stated quadratic consumer payoff gives p=(c+d)1-Bq+eta H qbar. Bii=1, so the own-quantity derivative of firm i's market profit is p_i-c-q_i. At its interior Cournot optimum p_i-c=q_i. Fulfilled expectations then give (I+B-eta H)q=d1. Three identical segmented destination markets imply worldwide operating profit 3q_i^2; the design cost is incurred once. This justifies Pi_i=3q_i^2-K_i, not a cooperative firm objective.

At fixed expectations, consumer surplus is U(q;qbar)-p'q = q'Bq/2. Network terms cancel between utility and expenditure. Imposing qbar=q after that calculation preserves the expression. National welfare uses one destination market's consumer surplus plus the resident firm's profits across all three destinations. Multiplying CS by three would change the country payoff and is incorrect.

### Consumer-domain attack, including asymmetric unilateral deviations

Symmetry of B alone does not prove concavity. A stronger proof is available here. X is affine in x in the three-dimensional cube. At each of the eight binary vertices, all seven nonempty principal minors are nonnegative, checked exactly by the fresh script. Thus all eight X matrices are PSD, and convexity of the PSD cone implies X(x) is PSD for every x in [0,1]^3. H is PSD under SW, SU (eigenvalues 1+g,1-g,1), and IS (1+2g,1-g,1-g). Therefore B=rho H+(1-rho)X is PSD for rho in [0,1], on the full government-policy and private-design cubes. Strict definiteness is not universal at g=1 and boundary designs; the concave consumer problem is sufficient for the inverse-demand construction. Add this argument to the appendix rather than relying on an undefined 'regular range'.

At the canonical center and a sufficiently small primitive neighborhood, rho>eta>0. Write M=alpha I+N with nonnegative off-diagonal N, zero diagonal, and row sums at most 2(1-eta). Set u=d/alpha and l=u[1-2(1-eta)/alpha]>0. The quantity fixed-point map q -> u1-Nq/alpha maps [l,u]^3 into itself and is a strict contraction because 2(1-eta)/alpha<1. Hence all full-cube continuation quantities are positive and unique. Also ||M^{-1}||_infinity <= 1/eta and ||q||_infinity<=d/alpha. These are stronger statements than positivity at a selected root.

## 3. Actual unilateral design Nash and global deviations

For E_j=M_{x_j}, E_j has beta/2 on the two incident symmetric off-diagonal pairs, zero elsewhere. The independent matrix derivation gives

q_{x_j}=-M^{-1}E_j q,

q_{x_j x_k}=M^{-1}E_j M^{-1}E_k q+M^{-1}E_k M^{-1}E_j q,

F_i=6q_i(q_{x_i})_i+kappa(1-x_i),

J_ij=6[(q_{x_i})_i(q_{x_j})_i+q_i(q_{x_i x_j})_i]-kappa 1{i=j}.

This differentiates each firm's own profit with rivals' designs fixed, before solving the joint system. A symmetric joint derivative of 3q(y)^2 would be wrong. Policy forcing uses q_g=-M^{-1}M_gq and q_{x_i g}=M^{-1}M_gM^{-1}E_iq+M^{-1}E_iM^{-1}M_gq. Solving Jx_g+F_g=0 yields the Nash strategic response.

### Full-cube Rosen proof, independently justified

Since ||E_i||_infinity<=beta, the quantity bounds above imply

||q_{x_i}||_infinity<=beta d/(eta alpha),

||q_{x_i x_j}||_infinity<=2 beta^2 d/(eta^2 alpha).

Every entry of J+kappa I consequently has absolute value <=18 beta^2 d^2/(eta^2 alpha^2). The symmetric part is negative definite if

kappa > 54 beta^2 d^2/(eta^2 alpha^2).

At the canonical exact primitives the strict margin is

989813109503 / 4103248806000 = approximately 0.24122668556087554.

This proves own-profit strict concavity and strict diagonal concavity/strong monotonicity on the **entire asymmetric design cube**, hence at most one full Nash and validity of finite unilateral deviations. Existence follows from compact convex strategy sets and continuous own-concave profits. A certified interior FOC root is therefore the unique full Nash, not merely a stationary root. The bound is for the canonical region; it must not be asserted across the entire Figure 3 lattice without checking it or supplying another proof.

At SW the fresh full-system numerical root is z=0.7185927073221112, all quantities approximately 0.7216472682419359, FOC residual below 6e-17. At g=.05 and all g enclosed by the interval replay, the SU member/outsider reduced roots and IS symmetric root are interior. The uniform full-cube uniqueness proof identifies their embedding as the full three-firm Nash. It is legitimate to reduce to (u,v) after establishing exchangeability plus full-game uniqueness; it is not legitimate to use the two-dimensional stationary solution alone.

## 4. Complete independent reconstruction of the local headline theorem

This proof uses the manuscript-facing primitives and Appendix A; it does not require a historical verdict.

At SW put t=beta z, P=alpha-t, L=alpha+2t. M=PI+t11', so R=M^{-1}=(I-t11'/L)/P and q0=d/L. For an AB edge, M_g has delta at AB and BA. Thus q_A,g=q_B,g=-delta alpha q0/(PL), q_C,g=2delta t q0/(PL). Differentiating CS gives

CS_g=rho d^2/L^2-2delta(1+2t)d^2/L^3.

Adding 6q0 q_A,g yields exactly the displayed D. Adding 6q0 q_C,g yields the displayed nu_F. These calculations independently establish the direct fixed-design slopes.

Differentiating CS with respect to each x_j, including both B_x and q_x, gives CS_{x_j}=-C, where C=beta d^2(eta+2t)/L^3. Differentiating A's worldwide profit with respect to B's or C's design gives -V, V=3beta d^2(alpha-2t)/(PL^3). Its derivative with respect to A's own design vanishes by the unilateral FOC, including its own cost derivative. Hence

W_A,x=(-C,-C-V,-C-V).

AB exchangeability gives x_g=(u',u',v')=-J^{-1}F_g. Taking its dot product with W_A,x yields

m_N'(0)=D-C(2u'+v')-V(u'+v')=D-Lloss.

The rival-profit component has the **plus** sign inside Lloss. The fresh independent computation gives D=.006767924128844749, Lloss=.015069744125257701, mu_N=-.008301819996412952; u'=.060810231735214, v'=.0323048168863242. These floats cross-check the formulas; the interval/theorem evidence does not rest on decimal agreement.

For a fixed country, write the three independent edge derivatives as (mu,mu,nu), because two edges are incident and one is not. AB activates one incident edge for a member and the nonincident edge for C; IS activates all three. Therefore m'=mu, o'=nu, i'=2mu+nu, (i-o)'=2mu, (i-m)'=mu+nu. This counts edge effects; it does not appeal to an unexplained 'symmetry'. Fresh centered differences at h=1e-4,1e-5,1e-6 cross-check the edge-count identities to about 1e-9.

Under the theorem's explicit conditions 0<D<Lloss, nu_N>-2mu_N, and nu_F>-D, all compared gaps vanish at zero and their relevant first derivatives are strictly signed. Differentiability implies a common epsilon>0 for which all signs hold for every 0<g<epsilon: frozen i>s,m,o; endogenous m<s and i<o but i>s. The baseline voting tree then accepts frozen integration and blocks endogenous integration, while direct endogenous IS strictly improves all countries against SW. This fully reconstructs the **local** headline theorem. No all-depth conclusion follows from this proof alone.

## 5. All-depth center and open-neighborhood theorem

The successful Krawczyk replay uses exact rational constants and interval endpoints with outward-rounded mpmath arithmetic; floating root approximations choose boxes/preconditioners only. For each of 1000 intervals covering [0,1], strict inclusion supplies an SU/IS stationary root enclosure. Together with the full-cube Rosen argument above, those roots identify unique global Nash continuations. The replay certifies:

m_N,g < -0.007970192997334808,

(i_N-o_N)_g < -0.015038883337750794.

The displayed manuscript decimal upper bounds are slightly weaker and therefore safe. Integrating from common zero gaps at g=0 proves both rejection inequalities for every positive depth, including depths between grid points. No omitted off-path proposal can repair this within [0,1].

The same replay verifies frozen IS(.05) is strictly accepted and records

IS lower 2.441397037346308,
SW upper 2.4220784217382687,
SU all-depth upper 2.423573564131729,
outsider consent lower gain .0002346166230648035.

Thus a feasible IS candidate beats every SW/SU payoff, including any feasible SU proposal. The separate Pareto replay verifies the endogenous direct-grand gain by interval-enclosed FOC roots. This is an actual all-depth center certificate, not a numerical depth grid.

### Optimal proposal existence: a previously suspected objection is resolved

Compactness of the entire policy menu alone would not suffice if the terminal-payoff map is discontinuous. Here a stronger argument works: S_IS={g:i(g)>=s,m(g),o(g)} is closed in compact [0,1]. The continuous payoff i attains its maximum on S_IS. The strictly accepted .05 candidate exceeds the entire SU envelope and s, so that maximizing feasible IS proposal is globally optimal in the actual government game. The argument needs to be stated explicitly; it is not a failure of the theorem. For direct-grand the analogous closed set is {g:i(g)>=s}.

### Open-set inference

The exact strict full-cube Rosen and quantity margins survive small primitive perturbations. Compactness in g and strict interiority of the center's continuous Nash paths imply uniform interior/regularity margins. A finite-cover implicit-function argument supplies a jointly smooth Nash continuation on one common primitive neighborhood. Uniform continuity then preserves strict negative derivative upper bounds (for example half their center margins). Integrating those derivative inequalities remains decisive even as g approaches zero; preserving only strict level gaps at selected positive g would be insufficient. Frozen acceptance at .05, the strict gap over the full SU envelope, and direct-grand welfare gain persist by continuity and maximization on a compact set. Intersecting these neighborhoods proves a nonempty open set in the stated four symmetric primitives. There is no explicit radius and no general-function or country-asymmetry theorem.

## 6. Extensive-form reconstruction and multiplicity attack

After A announces g, B anticipates the enlargement continuation. If B accepts, each incumbent's accession outside option is m and C's is o. Under mandatory affirmative votes at indifference, enlargement occurs iff i>=m and i>=o. If it occurs, B's initial acceptance requires i>=s. If it does not, initial acceptance requires m>=s and leads to SU. Otherwise SW. This derives i>=max{s,m,o}; these are not unrestricted-core inequalities.

A simultaneous unanimity vote without a tie rule would permit a coordinated rejection equilibrium: with two or more vetoes, each voter is nonpivotal and indifferent. The manuscript **does specify acceptance when indifferent**. Read as a mandatory strategy convention at every on- and off-path history, it eliminates those rejection equilibria: any nonpivotal rejecting voter must instead approve. A lone veto is justified only by strict preference for the outside option. Consequently no fatal voting-multiplicity flaw is established. To avoid a referee guessing the meaning, formally state whether votes are sequential/perfectly observed or simultaneous, and state that the mandated tie rule applies to nonpivotal as well as pivotal votes. This is BRIDGE NEEDED, not grounds to impose a different unmodeled bargaining refinement.

The baseline makes g binding through accession. Allowing direct IS offers changes the rejection option to SW; hence i>s can suffice even though i<o in the inherited bilateral accession game. With a different g' after enlargement, static consent i(g')>=max{m(g),o(g)} can be feasible near g=0, but this does not solve an unspecified renegotiation game. The manuscript correctly avoids a bargaining-invariant/coalition-proof claim.

## 7. C1 and C2

### C1 local adjustment-cost threshold

At SW the extra cost has zero marginal effect at legacy z. The Nash Jacobian becomes J-lambda I and forcing is unchanged. At the center J has diagonal ell≈-.817140038944638 and common cross term chi≈.0249082233652459, with -ell>2chi. Thus Q_lambda=-J+lambda I is a strictly diagonally dominant nonsingular M-matrix; Q_lambda^{-1}>0. For positive f, r_lambda=Q_lambda^{-1}f>0 and dr_lambda/dlambda=-Q_lambda^{-2}f<0. The induced loss, a strictly positive linear combination of these responses, falls continuously from a value greater than D to zero. Exactly one local threshold follows. The fresh numeric root .935389039955866 lies in the stated bracket; this calculation is **not** a new rigorous root-bracket certificate. A fresh replay of `stage14rs_adjustment_cost.py` additionally re-establishes exact Fraction root-bracket and endpoint signs in `verification/stage11/adjustment_cost_replay.log`; together with the independent monotonicity proof, this rigorously confirms the stated strict cutoff interval. No global SW/IS transition at this lambda follows. The manuscript properly limits its claim to member/outsider slopes.

### C2 network boundary

At rho=1 residual design disappears and cost minimization gives x=1; active private redesign is absent. Direct substitution derives the three displayed payoffs. The fresh script verifies the two decisive rational identities symbolically, including the outsider polynomial P(T,g). For T>=1/8 all coefficients of P are nonnegative and the g-linear coefficient is strictly positive, while m-s<0 for every g>0; hence SW for eta<=6/7. For T<1/8 the Stage21 explicit accepted grand witness h=min{1,2(1-8T)} beats s and the entire SU envelope; its cleared-polynomial positivity argument is valid. The exact replay passes.

The rho<1 strip is not established by that executable. The Stage21 Taylor/compactness proof uses full Nash regularity near beta=0, the identity (i-o)'=2mu, strictly negative second derivatives of m-s and i-o at the critical origin, and positive grand/member-widening slopes. These suffice: when mu>0 a feasible depth of order mu delivers a grand gain of order mu and beats the bilateral envelope of order mu^2; when mu<=0 the second-order and away-from-origin margins block every depth. This is a defensible restricted strip, not an arbitrary-rho theorem. The manuscript's Appendix C merely refers readers to the Stage21 file and does not expose this essential proof. Include it in a supplementary mathematical appendix or move the restricted-strip claim out of the main claimed results until that appendix exists. The rho=1 formulas themselves do not prove the extension.

## 8. Classification, regression and minimal proof repairs

| Finding | Classification | Repair without new model |
|---|---|---|
| Undefined maintained consumer range and omitted full-cube domain proof | APPENDIX DETAIL NEEDED; MAJOR BUT FIXABLE | State rho>eta>0 center neighborhood; supply PSD vertex/convexity, positive-quantity contraction and exact Rosen bound. |
| All-depth theorem points to missing named historical logs and no executable map in ZIP | APPENDIX DETAIL NEEDED; MAJOR BUT FIXABLE | Attach immutable source, current replay logs, versions/hashes, certificate targets, root-identification proof and one-command instructions. |
| Voting history and nonpivotal indifference interpretation compressed | BRIDGE NEEDED; MINOR to MAJOR depending final wording | Formalize extensive form and universal mandated acceptance at indifference; derive gates by backward induction. |
| Optimal IS existence compressed to compactness | BRIDGE NEEDED; MINOR | State closed IS-feasible-set maximization and domination of the entire SU envelope. |
| Active-design network-strip proof outside article | APPENDIX DETAIL NEEDED; MAJOR BUT FIXABLE | Add the critical quadratic argument with uniform neighborhoods, or restrict article to the proved face result. |
| New general/global bargaining inference | No such claim supported | Preserve inherited-depth, no-renegotiation limits; no model extension required. |

**Certification regression:** no mathematical regression of center A/B/C was demonstrated. The failure to provide a self-contained manuscript-facing proof package is a Stage 10/13 exposition/verification packaging deficiency; it does not warrant inventing a Stage 4A mathematical failure. The independently identified Figure 3 classification failure is a numerical implementation/certification regression at **Stage 9 (numerical illustration)**; it does not invalidate the separately replayed center A/B theorem. Reopen that stage, correct the algorithm/classification, and recertify numerical claims before passing the present gate. If the mandatory indifference convention is removed, or the theorem is changed to unrestricted bargaining/all equilibria without that convention, equilibrium certification must return to Stage 4A/7.5A rather than being patched by prose.

## 9. Referee 3 report

**Summary.** A valid local incidence mechanism links unilateral firm design to national agreement consent. Fresh matrix reconstruction and a successful all-depth interval replay support the center/global controlled-regime contrast on a qualitative open primitive neighborhood. The main theorem is stronger than its local chain-rule formula, but highly institution-specific.

**Major concerns.** The article outsources indispensable proof objects to historical files not packaged with the supplied ZIP. Full-cube Nash and consumer-domain proofs, exact certificate algorithms/targets, and the active-design network-strip proof need a proper mathematical supplement. Do not certify the Figure 3 plane from the successful center certificate.

**Minor concerns.** Formalize vote order and nonpivotal ties; replace bare compactness by closed-feasible-set existence; give the Rosen sufficient inequality explicitly and identify its parameter scope. Distinguish the rigorous fresh Fraction C1 bracket replay from the independent floating-point confirmation.

**Potentially fatal objections.** None established for the center/local theorems after attempted domain, finite-deviation, optimal-offer, and voting-multiplicity attacks. Simultaneous-vote multiplicity becomes material if mandatory acceptance at indifference is not part of the maintained game. A negative all-depth replay or an invalid full-cube Nash certificate would invalidate the strongest theorem; the actual replay succeeded.

**Recommended decision.** MAJOR REVISION / CONDITIONAL GO on proof grounds, with no new economic model required. Center mathematical correctness is supported; proof verifiability must improve before Stage 12 progression is used to imply a submission-ready theorem package.

## 10. Reproduction commands and environment

Run from repository root (all output files under `verification/stage11/`):

```bash
python verification/stage11/independent_matrix_audit.py > verification/stage11/independent_matrix_audit.log 2>&1
python verification/v2b_stage04a_krawczyk_cleanroom.py > verification/stage11/canonical_global_replay.log 2>&1
python verification/v2b_stage06_pareto_holdout.py > verification/stage11/pareto_replay.log 2>&1
python verification/stage14rs_adjustment_cost.py > verification/stage11/adjustment_cost_replay.log 2>&1
python verification/stage21_no_su_phase_theorem.py > verification/stage11/network_face_replay.log 2>&1
```

`verification/stage11/math_execution_environment.json` records Python and dependency versions, source SHA, and SHA256 digests of every audited executable. The root agent's separately written `independent_incidence_symbolic.py` adds 20 exact symbolic identities and a separate log; it was not imported into the fresh matrix audit. No shared earlier-module import is being called an independent derivation.

The mathematical PASS is scoped to the local theorems and replayed center certificate plus stated continuity inference; C2's restricted strip is supported by the inspected written proof, while **its presentation in the article remains incomplete**. Therefore proof verifiability is CONDITIONAL, rather than treating external-proof dependence as a counterexample to an otherwise defensible mathematical argument.
