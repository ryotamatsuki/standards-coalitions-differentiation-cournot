# V2b Stage25 — Locked specification for Figure 3: two-dimensional government-equilibrium phase diagrams
**Date:** 2026-10-22 JST. **Status:** figure SPECIFICATION LOCK; pilot computations exploratory, not the final computed/certified figure, and no plot is claimed to have been produced.

## 0. Scope and paper claim
Target: JPET-oriented Stage25 English working draft v0.2. Figure 3 is a controlled 2-panel numerical *terminal-government-equilibrium* phase map under the EXACT Stage22 inherited-depth, bilateral-first sequential voting game. It does not map equilibrium feasibility at an arbitrarily fixed g, nor does it depict Nash-design FOC roots untested for globality. The only intended exogenous contrast between panels is private residual-design policy: **F: frozen x_i at each cell's SW Nash z(theta)** vs **N: private Nash x_i reoptimized after each policy regime**. Government strategy sets, backward induction, utility, network effects, Cournot competition, welfare and absence of transfers identical.

## 1. Plot domain and conditioning
* Horizontal: kappa (residual design cost curvature), 0.70 <= kappa <= 1.05.
* Vertical: eta (network term in M=I+B-eta H), **focused zoom** 0.742 <= eta <= 0.772.
* Both panels: d=1, rho=0.9, lambda=0 (ORIGINAL model), g chosen endogenously by government A in [0,1]. Other characteristics, country/market counts and bilateral-first inherited-depth protocol exactly Stage22. Conventional x∈[0,1].
* Canonical witness marker (kappa,eta)=(0.8505,0.758), **F: government-optimal positive IS; N: all-g SW**, previously proven at that primitive center and on a nonexplicit open neighborhood.
* The displayed vertical zoom is selected *because a sparse, non-certified pilot found the SW→IS and F-IS/N-SW region inside it*; do not suggest it is full primitive space. An optional appendix map eta∈[.70,.86] with the same kappa range shows full-slice context, only if actual numerical classifications support it.
* Regularity pilot: original-model full-cube sufficient Rosen bound kappa>54(1-rho)^2 d^2/[eta^2(2-eta)^2]; on the specified rectangle RHS≤0.61977, so kappa≥.70 passes that sufficient margin **subject to applicability of the previously derived assumptions**. This alone DOES NOT assert all Nash designs are interior; use full KKT and demand/output checks everywhere. Do not put a theorem-certified boundary on the whole rectangle solely from this condition.

## 2. Economic/game objects at EACH independent cell theta=(1,eta,.9,kappa)
H^SW=I; H^SU has edges AB=g (and diagonals 1); H^IS all offdiag g. X_ii=1, X_ij=(x_i+x_j)/2. B=rho H+(1-rho)X; M=I+B-eta H. Full equilibrium q solves Mq=d1; prices p_i-c=q_i. National W_i=CS+Pi_i with CS=q'Bq/2, Pi_i=3q_i^2-kappa(1-x_i)^2/2, and no lambda term.
Determine unique genuine SW-Nash **at that theta**, z(theta), and s(theta)=W_i^SW. Do NOT keep canonical z(0.8505,.758) fixed when moving parameters.
* Frozen panel F: x_i^F(H)=z(theta) for all countries and all policy H, maintaining original cost evaluated at that fixed design. SW baseline common to F and N.
* Endogenous panel N: solve full three-firm Nash residual x_i^N(H,g), including asymmetric SU member/outsider design, for each H/g. Under symmetric IS retain all-player Nash uniqueness check, do not replace with a planner's choice or rely merely on a symmetric stationary point.
Define m_j(g)=W_A^{SU}=W_B^{SU}, o_j(g)=W_C^{SU}; i_j(g)=W_i^{IS}, for j=F,N.

## 3. Government subgame solution (MUST NOT draw vote-feasibility alone)
For each g>0, both panels apply Stage22 original weak-acceptance vote rules:
* **IS(g) terminal** iff i_j(g)>= max{s,m_j(g),o_j(g)}. (B foresees accession; C and incumbent consent).
* Else **SU(g) terminal** iff m_j(g)>=s and enlarged coalition was rejected: i_j(g)<o_j(g) OR i_j(g)<m_j(g). (This condition is sufficient whenever IS eligibility above fails and m>=s; all comparisons are actual per-branch equilibrium payoffs.)
* Else **SW(g) terminal**. At g=0 every regime has no substantive compatibility differences; identify as SW (not a colored spurious IS phase).
Government A optimizes across ALL feasible depths g∈[0,1] anticipating this mapping. For each depth, let G_j(g)=i_j(g) if IS terminal, m_j(g) if SU terminal, otherwise s. Compute the GLOBAL maximizers (including g=0, policy acceptance boundary roots and extrema on all participation-feasible segments), then classify by the outcome of A's optimal offer:
  **IS** if unambiguous global winner is positive-depth IS,
  **SU** if unambiguous global winner is positive-depth SU,
  **SW** if the government's maximum is s and no strictly better substantive offer exists,
  **TIE/UNRESOLVED** if ambiguous regimes are optimal within numerical error or best-response validity/global maximization is unverified.
Never infer IS from the existence of some acceptable i(g), or SW from m'(0)<0. Both are conditional/local facts, NOT the maximized terminal outcome. Do NOT optimize social welfare instead of A's actual W_A.

### Numerical tolerance/proof distinction
- Voting uses WEAK acceptance at true equality; numerical implementation must distinguish certifiably >0, <-0 and a tie band (numerical tolerance relative to welfare scale). Indeterminate within tolerance = mark uncertainty, not silently force acceptance.
- Maxima are compared with error bounds from solver, g resolution, and branch/path continuation. If max payoff regimes are closer than known numerical accuracy, label TIE/UNRESOLVED.
- If any relevant Cournot q becomes nonpositive, firm x hits boundary (requiring KKT), uniqueness is unverified, M singular or solver lacks a valid branch, mark UNCERTIFIED (hatched) unless separately solved with proper KKT/global methods. Never use solver failure to imply that a government deviation is unprofitable.
- Local sign lines m'_j(0)=0 may be optional dotted overlays **labelled 'local consent slope zero'**, and explicitly NOT the SW/SU/IS phase boundary.

## 4. Resolution, search and validation
**Step P0 exploratory (already done privately; NONCERTIFIED):** 6x6 over eta [0.70,.86], kappa [.70,1.05] and 8x8 over eta [.742,.770], kappa [.70,1.05], with 31/51 sampled g-values. At the narrow 8x8, apparent qualitative counts: (F-SW,N-SW)=32; (F-IS,N-IS)=22; (F-IS,N-SW)=10; SU=0. This motivated the zoom; it does **NOT** prove all cells, absence of SU, precise boundary curves, uniqueness or global government-optimal g. Canonical test with 101 sampled g yields exploratory F-IS/N-SW, consistent with Stage22 exact certificate.
**Step P1 coarse production:** e.g. 41 kappa x 61 eta cells; at each cell warm-start from z(theta) but verify independent multi-start seeds and KKT, both SU/IS, multiple g seeds.
**Step P2 continuous-in-g optimization:** enumerate roots of acceptance boundaries i-s,i-m,i-o,m-s, and all interior stationary points of i(g),m(g) on each genuine feasible government regime segment. Include endpoints g=0,1 and one-sided discontinuity limits; use bracketed high precision/adaptive interval branch search. Uniform mesh in g is a DISCOVERY TOOL, not a certificate of global optimum.
**Step P3 adaptive refinement:** refine parameter cells where labels or certified participation margins change; bracket the 2D boundary without plotting an invented smooth analytic line. Downshift to gray hatching where residual uncertainty remains. Report both mesh and g-resolution convergence.
**Step P4 certification:** exact replay of canonical theta0 at (eta=.758,kappa=.8505), requiring F-IS/N-SW, z≈.7185927073 and previously verified g=.05 payoffs; independently spot-check additional interior of each drawn regime using high precision/multistart/KKT, plus a reproducible solver log. Only depict entire rectangle as 'certified equilibrium' if genuine global interval enclosures support it, which current Stage14 certificate does NOT. Otherwise manuscript labels it 'numerically classified illustrative regimes'.
**Step P5 guardrail:** SU may be absent from the given slice; show SU in legend but DO NOT artificially widen/recalibrate to manufacture it. If absence merely empirical, caption 'not identified in the displayed numerical slice', not 'SU never arises'. No plot representing a global exact network cutoff at eta=6/7 because that is ONLY the rho=1 limiting face, different from rho=.9 here.

## 5. Appearance / insertion
Proposed Figure 3: two aligned equal-axis panels (a) F and (b) N, 7.0-7.2in combined print width for two-column manuscript or column-sized stacked panels if JPET typesetting width differs. Colorblind-safe and grayscale-differentiable: SW light neutral gray with "SW" interior labels, SU amber with sparse diagonal hatch + "SU" labels, IS dark blue with contrasting "IS" labels; UNCERTIFIED white / gray crossed hatch; separate outline/legend for numerical ties. No interpolated smoothed boundary presented as theorem. Discrete raster cell fill (or exact vector polygons once verified) rather than interpolated gradients.
Dashed/thin boundaries are grid-dependent numeric approximations. Distinct black marker/star for theta0 and coordinates written in caption; add short annotation "fixed IS / endogenous SW" near canonical spot if no overlap. Same x/y ticks and limits in both panels, with eta decimal ticks to 3 places. For second plot do not move the canonical point or change rho/d/costs.
Insert after the main government's regime-result theorem and existing numeric Table2, BEFORE institutional direct-grand comparison or at the opening of Results illustration subsection, with cited cross-reference to Stage22 all-depth center cert. Do not add unrelated heatmaps or projection disguises.

## 6. Manuscript-ready English caption
**Figure 3. Equilibrium standardization regimes in the (kappa, eta) plane.**
'(a) Firms’ residual product designs are fixed at the fragmentation Nash design z(kappa,eta) associated with each parameter pair. (b) Firms instead reoptimize residual designs in Nash equilibrium after each contemplated compatibility arrangement. Both panels solve the same bilateral-first, inherited-depth governmental accession game, allowing the initiating government to optimize compatibility depth g over [0,1]. SW denotes fragmentation, SU a bilateral compatibility arrangement, and IS a three-country agreement. We set d=1, rho=0.9, and lambda=0, and vary kappa in [0.70,1.05] and eta in [0.742,0.772]. The marker identifies the previously certified reference parameters (kappa,eta)=(0.8505,0.758), at which the frozen-design game selects IS and the endogenous-design game selects SW. Shaded cells are numerical regime classifications, not independently certified global phase regions. Boundaries are resolution-dependent approximations; hatched cells indicate unresolved continuation equilibria, government maximization, or near-ties. The figure complements, but does not enlarge, the open-neighborhood result established in the text.'
Only adopt after actually computing color patches; do not pretend phase results beyond the certified center already obtained.

## 7. Supplementary figure
If economically useful after main figure: Appendix Figure A1 wide `eta in [.70,.86]` with identical kappa, rho and other policy assumptions, marked as wide-context numerically computed. Avoid a new C2 global-freehand line. No extension-lambda panel in main Figure 3.

## 8. Audit record and status
Inputs: Stage22 `reviews/STAGE22_ABC_PROPOSITIONS_AND_PROOFS.md`, Stage14 `reviews/STAGE14_THEOREMS_AND_PROOFS.md`, Stage23 `verification/stage23_independent_reconstruction.py` (pointwise local only), Stage25 v0.2 figure-architecture provenance; this spec explicitly reuses existing work.
The plotted phase map has NOT yet been generated or certified; only its scope, game classification, plot captions, validation and stop rules are fixed here. **Production figure remains pending.**
