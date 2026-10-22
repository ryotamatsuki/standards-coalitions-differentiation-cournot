# Stage 13R: Economic proof exposition audit

Reviewed manuscript SHA: `c7b52ac10a701c682479e8f57c1343ceed1df719`. Date: 23 October 2026 JST. Locations refer to the canonical 20-page PDF and frozen TeX. This is a simulated editorial audit, not the journal’s decision.

## Judgment and proof dependency

Correctness and exposition receive different assessments: mathematical consistency PASS in the audited scope; proof conventions/readability CONDITIONAL. Short economic proofs are already possible in this model. The main all-depth theorem needs a more legible hierarchy, not deletion of its global-domain and implementation steps.

The necessary dependency is: conditional consumer preferences → fulfilled Cournot quantities → unilateral private-design FOCs on the full cube → unique Nash and symmetry reduction → national welfare gradient → local edge incidence and consent → interval inclusions and derivative bounds at every depth → integration into level constraints → government-optimal outcome → uniform perturbation argument. A reduced stationary solution alone would not establish the middle of this chain.

## All six numbered results

| Result | Correctness/conditions | Economic proof practice | Adopted treatment |
|---|---|---|---|
| Lemma 1, edge incidence (p.6) | Permutation symmetry and differentiable unique continuation yield two edge coefficients. Directions give (i-o)′=2m′. Right derivatives at g=0 suffice. | Short proof is conventional and intelligible; post-proof novelty disclaimer is unnecessary. | KEEP proof; state the outsider comparison’s economic role. |
| Lemma 2, national incidence (p.7) | Chain rule gives D-L with positive V contribution. Positivity assumptions are sufficient, not necessary. | Proof is clear conditional on the national gradient; its short derivation should appear in Appendix A. | Add 13R-06 identities; retain consumer and rival-profit incidence. |
| Theorem 3, local reversal (p.8) | All gaps begin at zero; strict derivative signs imply local level signs. The additional nu conditions supply incumbent and grand comparisons. | Conditions are readable but partly reduced-form; Appendix B makes their primitive evaluation possible. Stand-alone member margin must be distinguished from B’s initial vote. | KEEP conditions and short proof; repair terminology and add 13R-03. |
| Theorem 4, all-depth open region (pp.8–9) | Separate endogenous all-depth failure, frozen feasible IS dominance, and direct IS gain. Uniform strict regularity supports a qualitative neighborhood. | Current proof reads partly as a computational verification report. Its three logical steps and economic conclusion should lead. | 13R-05, certificate table, retained Appendix D/E details. |
| Proposition 5, direct agenda (p.11) | Different rejection history changes consent. Closed direct-feasible depth set supports an optimal direct offer. | Straightforward corollary, useful for scope; no need to re-advertise it as “not independently novel.” | KEEP proof and same-continuation interpretation; compress self-rating. |
| Proposition 6, lambda threshold (pp.12–13) | Positive inverse of strict M-matrix; derivative -Q^-2 f<0. Positive weights imply monotone loss and unique crossing. | This is an elegant conventional proof: matrix property → response monotonicity → economic cutoff. Do not replace it with a numeric root. | KEEP. Add a plain statement that frictions attenuate the private response, with no global regime inference. |

## Appendix-by-appendix audit

**A, pp.14:** The inverse, fixed-design q_g and CS_g reproduce D and nu_F. The national gradient is the important compressed step. The adopted additional derivation below is a proof of an existing identity, not a new claim.

At the symmetric no-agreement Nash, a unilateral increase in x_j changes outputs according to
\[
(q_{x_j})_j=-\frac{\beta\alpha q_0}{PL},\qquad
(q_{x_j})_k=-\frac{\beta(\alpha-2t)q_0}{2PL}\quad(k\ne j).
\]
Consequently \(\partial_{x_j}CS=-C\) for every j. For the resident firm, its own design derivative is zero by its Nash first-order condition, whereas
\[
\partial_{x_k}\Pi_j=6q_0(q_{x_k})_j=-V\quad(k\ne j).
\]
Adding consumer surplus to resident profit yields Equation (16), and the chain rule then gives Equation (18).

**B, p.15:** The diagonal and cross-Jacobian and forcing coefficients determine the unilateral Nash response. These formulas also make Theorem 3’s reduced-form conditions evaluable from primitives. With lambda, replace J by J-lambda I. The response system and determinant factors agree with the main text. No Nash/planner substitution was found.

**C, p.15:** Exact rho=1 welfare formulas are consistent with the network-face replay. The coefficient 211/196 is correct but should not be a bare assertion. With t=(1-rho)z, z=1 on the face, and induced loss of order (1-rho)^2, direct symbolic differentiation gives mu_eta=2401d²/512 and -mu_rho/mu_eta=211/196. This independently confirms the displayed coefficient for the stated near-face extension.

**D, pp.15–16:** X is affine over the cube; its four vertex types have nonnegative principal minors. The policy H spectra are nonnegative. B is therefore PSD. For 0<eta<rho<1, N’s row sum is at most 2(1-eta) and the contraction maps the positive quantity cube to itself. The Jacobian perturbation bound makes the symmetric part uniformly negative definite under the displayed sufficient inequality. This establishes existence on compact individual strategy sets and uniqueness of the full game, including boundary strategies. An interior included root is consequently a genuine global Nash. Keep the exact strict Rosen margin. Reference Rosen for the standard theorem rather than implying an internal audit report supplies the existence theorem.

**E, pp.16–18:** The full-game uniqueness is established before imposing policy symmetry. For SU, uniqueness implies x_A=x_B, and F_B=F_A recovers all three unilateral FOCs. For IS, equality of all three designs reduces computation to a scalar unilateral FOC. Global own concavity/uniqueness excludes off-symmetry unilateral deviations. The two numerical methods are correctly distinguished despite the historical routine name krawczyk_IS. The computation encloses every real depth in 1,000 adjacent intervals; it does not certify only 1,000 points. Nonsingularity plus inclusion gives smooth continuations. Welfare derivatives are lifted into the national functions, integrated from common g=0, and used in actual government votes.

The fixed-design IS-feasible set is closed. A candidate strictly above fragmentation and the entire bilateral envelope means its maximizer over that closed set dominates every other terminal regime. This avoids a false appeal to continuity of the discontinuous overall terminal-payoff map. For primitive persistence it suffices to keep the fixed g=1/20 candidate strictly feasible and above the continuous supremum of the full bilateral payoff function on a fixed compact depth interval; no continuity of a changing voting-feasible correspondence is needed. Retain uniform negative derivative margins to control all arbitrarily small positive g.

**F, pp.18–20:** The face proof explicitly exhibits accepted IS dominating the whole SU envelope, rather than merely showing IS is feasible. Its rational inequalities and threshold classification replay. The active-design strip relies on a local quadratic sign argument plus strictly negative away-from-zero margins. Positive mu permits h of order mu, producing first-order grand gain versus a second-order bilateral envelope; nonpositive mu excludes every depth. Clarify inherited notation and the inward continuation from x=1: for beta>0 the leading own-design FOC gives 1-x_i of positive order beta near the critical face, whereas the base face solution lies on the boundary. Do not infer smooth interior equilibrium at beta=0 itself.

## Proposed certificate table for Appendix E

| Mathematical object | Method/domain | Conservative certified statement | Economic use |
|---|---|---|---|
| Full-game equilibrium | Analytic full-cube concavity/monotonicity | Unique Nash; included roots are interior | Root identity and unilateral deviations |
| SU continuation | 2D Krawczyk, 1,000 intervals covering [0,1] | Root in each interior design box; nonsingular reduced Jacobian | m_N and o_N and their derivatives |
| IS continuation | Scalar interval Newton, same cover | Root in each interior interval; negative scalar derivative | i_N and derivative |
| Endogenous member slope | Outward interval arithmetic | m_N′<-0.00797 | m_N(g)<s for every g>0 |
| Endogenous accession slope | Same | (i_N-o_N)′<-0.01503 | Outsider rejects inherited enlargement |
| Frozen integrated candidate | g=1/20 | i_F>2.4413970373; i_F-o_F>0.0002346166 | Strict acceptance |
| Frozen alternatives | Full [0,1] interval cover | s<2.4220784218; sup m_F<2.4235735642 | Candidate beats every terminal SU and SW |
| Endogenous direct alternative | Root bracket g=1/20 | i_N-s>0.0169346278 | Direct grand proposal improves all countries |

These displayed bounds deliberately round in the conservative direction. Keep the high-precision underlying interval outputs in the replication supplement. The qualitative open neighborhood follows analysis, not an executed four-dimensional primitive box.

## Fresh execution evidence

Executed from the pinned checkout, after dependency installation. Primary runtime: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0, mpmath 1.3.0. The interval source sets iv.dps=35; the separate Pareto source sets iv.dps=40. Initial runs failed for missing mpmath; installation resolved that environment error. A failed first invocation is not reported as a successful proof.

The main two sources have identical bytes at the manuscript SHA and the historical certificate commit `54ac8389f2c45d56b2e587a62c62f226cc121f95`:

- `verification/v2b_stage04a_krawczyk_cleanroom.py`: SHA256 `25c92e800a255ddfd0712f3a9095f83a2a69c70addcf0d16f75fc7b65289fd74`.
- `verification/v2b_stage06_pareto_holdout.py`: SHA256 `7134e55cd6dcb3e3f0f6cc8af27c698240364c4f0670ef37c0324231b4757a28`.

Exact commands for an environment with the recorded packages installed:

```bash
python verification/v2b_stage04a_krawczyk_cleanroom.py
python verification/v2b_stage06_pareto_holdout.py
python verification/stage14rs_adjustment_cost.py
python verification/stage21_no_su_phase_theorem.py
```

Observed output (verbatim local replay; timings are incidental):

### global_replay.log

```text
INDEPENDENT PROFIT DEVIATION PASS: max FOC error 6.316291933927687e-10
KRAWCZYK SIGN CERT SUCCESS accepted= 1000 splits= 0 max upper derivatives= -0.007970192997334808 -0.015038883337750794 seconds= 6.711511911999992
FROZEN CERT SUCCESS C lower gain= 0.0002346166230648035 IS lower= 2.441397037346308 SW upper= 2.4220784217382687 SU upper= 2.423573564131729
PASS: adversarial stage 4A independent method, all g∈[0,1]
```

### pareto_replay.log

```text
SW welfare interval [2.42207842170099674065445696512306149094921077, 2.42207842173413007870226725168272109909056935]
IS(g=1/20) welfare interval [2.43901304960775892906795958464672485044440495, 2.43901304964048755531493755099436589936360644]
strict per-country Pareto gain interval [0.0169346278736288503656923329640037513538356017, 0.0169346279394908146604805858713044084143956692]
PASS: Pareto-improving IS possible even with endogenous firm design
Global game unreachability requires separately passed Stage-4A all-g proofs.
```

### adjustment_replay.log

```text
lambda0 {'member': (-0.008301819998396649, -0.00830181999425662), 'outsider': (0.36786696575374817, 0.36786696575693073), 'grand': (0.35126332575695485, 0.3512633257684175), 'up': (0.06081023173475353, 0.06081023173546352), 'vp': (0.0323048168860621, 0.032304816886467566)}
lambda_lower {'member': (-3.6040359777890524e-08, -3.6036383826202255e-08), 'outsider': (0.3777561815641332, 0.3777561815671229), 'grand': (0.37775610948341365, 0.3777561094943552), 'up': (0.027623584424572696, 0.027623584424865805), 'vp': (0.014119278485059766, 0.014119278485215728)}
lambda_upper {'member': (3.8253352313846565e-09, 3.829311182331523e-09), 'outsider': (0.3777562294697064, 0.37775622947269605), 'grand': (0.37775623712037687, 0.37775623713131845), 'up': (0.027623423303282203, 0.02762342330357531), 'vp': (0.014119193339999926, 0.014119193340155886)}
lambda1 {'member': (0.00024813258725923964, 0.00024813259123058497), 'outsider': (0.3780544816044969, 0.37805448160748106), 'grand': (0.37855074677901535, 0.3785507467899422), 'up': (0.02662023899222523, 0.026620238992506817), 'vp': (0.013589671047349226, 0.013589671047498692)}
PASS: exact rational sign certificates at true SW Nash root
SCOPE: unique local crossing by M-matrix monotonicity; global policy-depth threshold unproved
```

### network_replay.log

```text
PASS: global rho=1 selection eta<=6/7 -> SW, eta>6/7 -> IS; SU never optimal
PASS: explicit accepted grand depth min(1,2*(1-8theta)) defeats every SU offer
PASS: strict quadratic gap at threshold and nonzero network-strength transversality
SCOPE: original rho<1 endogenous-design no-SU region follows by smooth/compact proof in reviews; not a universal theorem
```

## Separate full-matrix reconstruction

A fresh scratch calculation constructed all three unilateral FOCs directly from M and q, without importing earlier V2b modules. It solved the full 3-variable design system and evaluated consumer surplus plus resident worldwide profit. This is an independent floating-point consistency check, not a new interval proof. Frozen-design FOC residuals need not vanish after the policy changes, because that treatment constrains designs.

```json
{
  "z": [
    0.7185927073221111,
    0.7185927073221111,
    0.7185927073221111
  ],
  "s": 2.4220784217184685,
  "table": {
    "frozen": {
      "m-s": 0.0002723816370884258,
      "i-o": 0.00023461666824431404,
      "i-s": 0.019318615645242954
    },
    "Nash": {
      "m-s": -0.00047347417138166037,
      "i-o": -0.0012465472341340877,
      "i-s": 0.016934627905352606
    }
  },
  "incidence": {
    "W_gradient": [
      -0.03388799825199129,
      -0.13970896530768329,
      -0.13970896530768329
    ],
    "x_response": [
      0.06081023173343247,
      0.06081023173898358,
      0.032304816888206744
    ],
    "D": 0.006767924154438275,
    "loss": 0.01506974412496512,
    "mu_N": -0.008301819970526845
  },
  "figure3": {
    "shape": [
      41,
      41
    ],
    "cell_mismatches": 0,
    "errors_first": []
  }
}
```

The independent endogenous FOC norms at g=.05 are below 3e-17. Every published Table 2 entry agrees after rounding to nine decimals. The all-cell Figure 3 check compares display rectangles with the archived numeric array; it does not rerun or certify every classification. The scientific verification scripts have not been edited.

## Proof revision stopping rule

No new theorem is demanded. Close 13R-03/05/06/08/09/17, preserving all displayed conditions. Re-run scientific checks only once after actual revisions if formulas, code pointers or result scope change; editorial-only changes require source/formula diff, LaTeX/reference checks and visual inspection. If the main certificate fails after any scientific change, return to the affected mathematical stage rather than rewriting the prose around it.

## Interior-box check and reproducible independent audit

A separate check evaluated the same 1,000 midpoint candidate centers used by the successful zero-split certificate. Including the 0.0002 box half-width and an extra 1e-12 rounding allowance gives the following conservative approximate extrema (order: SU member, SU outsider, IS design): lower [0.71842310855792, 0.7184088585935297, 0.7184696515590566], upper [0.7665537407629089, 0.747188858285737, 0.8219305905147843]. Thus none of the certified boxes is near the design-cube boundary. The interval inclusion, not this midpoint check alone, establishes the root for every depth.

The following scratch audit source is included as text so that its independent matrix/table/display checks are reviewable without changing the research code. It requires the recorded NumPy/SciPy environment and execution from the repository root.

```python
import numpy as np, json, platform, hashlib, pathlib, re
from scipy.optimize import root,brentq
D=1.;eta=.758;rho=.9;kappa=.8505
E=[]
for j in range(3):
 e=np.zeros((3,3));e[j,:]=(1-rho)/2;e[:,j]=(1-rho)/2;e[j,j]=0;E.append(e)
def values(x,g,reg):
 H=np.eye(3)
 if reg=='SU':H[0,1]=H[1,0]=g
 if reg=='IS':H=H+g*(np.ones((3,3))-np.eye(3))
 X=(np.asarray(x)[:,None]+np.asarray(x)[None,:])/2;np.fill_diagonal(X,1)
 B=rho*H+(1-rho)*X;M=np.eye(3)+B-eta*H;q=np.linalg.solve(M,np.ones(3))
 f=np.array([6*q[j]*(-np.linalg.solve(M,E[j]@q))[j]+kappa*(1-x[j]) for j in range(3)])
 W=.5*q@B@q+3*q*q-kappa/2*(1-np.asarray(x))**2
 return f,W,q
z=root(lambda x:values(x,0,'SW')[0],np.ones(3)*.72).x
s=values(z,0,'SW')[1][0]
r={'z':z.tolist(),'s':s,'table':{}}
for treatment in ['frozen','Nash']:
 wa={}
 for regime in ['SU','IS']:
  x=z if treatment=='frozen' else root(lambda x:values(x,.05,regime)[0],z,tol=1e-11).x
  f,w,q=values(x,.05,regime);wa[regime]=w
  r.setdefault('continuations',{})[treatment+'_'+regime]={'x':x.tolist(),'q':q.tolist(),'W':w.tolist(),'FOC_norm':float(np.max(np.abs(f)))}
 r['table'][treatment]={'m-s':wa['SU'][0]-s,'i-o':wa['IS'][0]-wa['SU'][2],'i-s':wa['IS'][0]-s}
h=1e-5
WG=np.array([(values(z+np.eye(3)[j]*h,0,'SW')[1][0]-values(z-np.eye(3)[j]*h,0,'SW')[1][0])/(2*h) for j in range(3)])
xg=(root(lambda x:values(x,h,'SU')[0],z,tol=1e-11).x-root(lambda x:values(x,-h,'SU')[0],z,tol=1e-11).x)/(2*h)
Df=(values(z,h,'SU')[1][0]-values(z,-h,'SU')[1][0])/(2*h)
r['incidence']={'W_gradient':WG.tolist(),'x_response':xg.tolist(),'D':Df,'loss':float(-WG@xg),'mu_N':float(Df+WG@xg)}
# Reconcile ALL plotted cells with the archived boundary-aware map, without claiming rerun classification.
data=np.load('stage11_v05_package/verification/figure3_boundary_aware_map.npz')
source=pathlib.Path('manuscript/stage13_figure3_tikz.tex').read_text()
panels=source.split('\\begin{scope}')[1:];errors=[]
for panel,key in zip(panels,['F','N']):
 arr=data[key];nr,nc=arr.shape
 rects=re.findall(r'\\fill\[(mapSW|mapIS)\] \(([\d.]+),([\d.]+)\) rectangle \(([\d.]+),([\d.]+)\)',panel)
 for i in range(nr):
  for j in range(nc):
   px=(j+.5)/nc;py=(i+.5)/nr
   match=[0 if c=='mapSW' else 2 for c,a,b,cc,dd in rects if float(a)<px<float(cc) and float(b)<py<float(dd)]
   if len(match)!=1 or match[0]!=int(arr[i,j]):errors.append([key,i,j,match,int(arr[i,j])])
r['figure3']={'shape':data['F'].shape,'cell_mismatches':len(errors),'errors_first':errors[:4]}
for treatment,expected in [('frozen',[.000272382,.000234617,.019318616]),('Nash',[-.000473474,-.001246547,.016934628])]:
 assert np.allclose(list(r['table'][treatment].values()),expected,atol=5.1e-10,rtol=0)
assert not errors
print(json.dumps(r,indent=2))

```
