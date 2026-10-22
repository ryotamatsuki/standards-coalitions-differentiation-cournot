# V2b Stage25 v0.4 — Figure3 integration, prose/placement review, SU aliasing correction
Date: 2026-10-22 JST. **Pre-Stage11 authoring review, not a journal decision or a theorem certificate.**

## Critical factual correction to v0.3
v0.3's 15x15 primitive grid / 61 g-depth search showed SU-colored pixels in the endogenous panel. **Those SU bands were not robust numerical outcomes.** A more resolved 41x41 (kappa,eta) grid with 81 g proposals, followed by 321 g-depth reoptimizations for 351 near-transition cells, yielded **NO SU-classified cells** in either treatment. Initially 11 frozen-SU and 12 endogenous-SU cells became SW or IS upon g-grid refinement. Across the entire rectangle 28 primitive cells changed label (81→321), and all 28 preserved the refined category under an additional 641-depth recheck.

Retain the principled distinction: SU at a **fixed g** requires member payoff m(g)>=s plus failed enlargement (i(g)<m(g) or i(g)<o(g)); this is NOT sufficient for SU to be **optimal** when government A may choose a different g producing IS. Lack of observed SU in a finite grid is NOT a general no-SU proposition, nor an exact global phase theorem.

## Validated figure setup
- x-axis kappa∈[.70,1.05], 41 points; y-axis eta∈[.742,.772], 41 points.
- d=1, rho=.9, lambda=0; bilateral-first inherited-depth government protocol, A chooses g∈[0,1].
- Frozen x=z(kappa,eta) at EACH primitive pair, not frozen at the central point's z; endogenous design reoptimizes private Nash x^SU and x^IS at each policy.
- Center theta0 (kappa,eta)=(.8505,.758) is star, **NOT** an actual lattice point; the original independent, historically all-depth-certified center contrast F:IS and N:SW is separately preserved.
- Final numeric labels on 1681 cells: frozen SW=772, IS=909, SU=0; endogenous SW=1051, IS=630, SU=0. Numeric phase contours are stepped/discrete, not falsely smooth or exact.
- A separate independent 3-firm Nash full-FOC multi-start check was performed at 240 (parameter,regime,g) cases, three seeds each: no alternative roots found, max FOC residual 3.1e-14; 0.637≤x≤0.867, q_min=.572>0 in those samples. On this displayed rectangle the sufficient Rosen-margin bound peaks ≈.619762 below min kappa=.70, but the numerical data themselves are not comprehensive interval certificates.

## Manuscript review and actual edits
- Figure location remained immediately after Table 2 and before institutional scope section (p11).
- v0.3 Figure3 was a float-only full page and ~145-word caption; v0.4 shortened caption, moved the economic interpretation and SU disappearance into manuscript text, placed embedded Figure3 before §6 using [H], leaving §6 text on SAME page 11.
- English prose now explains member/outsider votes, government maximization across g, why SU availability at one g does not imply an optimal SU, and why grid aliasing necessitated correction.
- Figure has two comparable panels F/N, axes/ticks, grayscale-distinct blue vs gray, certified-center star, minimal separate SU note ('not detected in refined slice'). The graphic has no imaginary SU stripe or invented smooth cutoff.
- v0.4 LaTeX compiled successfully twice; 17 pages, no unresolved references or overfull warnings. PDF pp10–11 rendered and visually inspected; corrected hairline grid artifacts by rendering region raster through imshow with vector text/axes.
- No changes to Stage22 frozen theory, all-depth interval claims, local-vs-global quantifiers, literature priority claims, or JPET provisional target. Formal Stage11 independent adversarial reading still pending.

## Provenance and user deliverables
Full actual TeX, PDF, Figure3 vector-PDF and PNG, classification data NPZ, 641-depth convergence JSON, 240 Nash spotcheck JSON, Python model and replot/recompute scripts, and written QA are supplied as a downloadable bundle `stage25_jpet_v04_with_refined_phase.zip` created in ChatGPT's working container.
**The GitHub repo stores this documented QA and figure spec, but the updated TeX/PDF/NPZ bytes have not yet been synced to GitHub.** Do not assert otherwise or call this paper submission-ready.

Status: **Stage10 display architecture repaired; v0.4 manuscript diagram and SU commentary integrated; global numeric phase certification and Stage11 hostile referee pending.**
