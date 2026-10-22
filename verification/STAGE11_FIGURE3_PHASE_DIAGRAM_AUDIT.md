# Stage 11 — independent Figure 3 phase-diagram audit

Date: 2026-10-22. Reviewer 4: computation, numerical optimization, and computer-assisted proof.

**Verdict: MAJOR BUT FIXABLE. Archived computations are reproducible, but the displayed map contains at least eleven false SW classifications. The benchmark comparison survives. A numerical phase map is not an all-depth interval certificate.**

## Source, coverage, and audit status

Actual v0.4 manuscript, Figure 3 PNG/PDF, Python model/plot/recompute sources, NPZ arrays, 28-case convergence JSON, design-spotcheck summary JSON, and QA record were read. The original ZIP is `stage25_jpet_v04_with_refined_phase.zip`, Library version 2. Repository base supplied to this reviewer: `1146745c548734370de190899ac43370649a3c29`.

The supplied numerical inputs are preserved unchanged in `verification/stage11/input_v04/`; independent scripts and results are alongside that directory. The PDF's page 11 and standalone Figure 3 were visually inspected. No manuscript or source numerical classifications were altered during this audit. We did **not** rerun the entire 1681-cell initial and 351-cell refinement exercise. We did independently reconstruct its mask/data bookkeeping, rerun all 28 logged changed cells at all three resolutions, and perform targeted independent optimization attacks.

## 1. What reproduces

| Object | Independent check | Result |
|---|---|---|
| Parameter lattice | NPZ endpoints, dimensions, spacing | 41 by 41; kappa .70 to 1.05, eta .742 to .772 |
| Frozen labels | NPZ `F` | SW 772, IS 909; SU/UN zero |
| Endogenous labels | NPZ `N` | SW 1051, IS 630; SU/UN zero |
| Initial 81-point labels | NPZ `oldF`, `oldN` | frozen SU 11, endogenous SU 12 |
| Targeted 321-point cells | Reconstructed transition mask and one binary dilation | Exactly 351 cells |
| Changed cells | NPZ comparison and JSON | Exactly 28 |
| Archived 81/321/641 outcomes | Reran unmodified `classify` for all 28 cases | All 84 comparisons match |
| Recorded 641 stability | Compare recomputation to stored 321 | All 28 stable |

The NPZ field `refine_mask` contains only the **28 changed cells**, not the 351-cell refinement mask. This is recoverable by reconstructing the original mask, but the field should be renamed or the full mask separately retained. There is no per-call log for every one of the 351 refined cells.

Reproduction environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0. Result: `verification/stage11/supplied_record_recheck.json` and its stdout log. Reproducibility of an algorithm is not validation of its optimization target.

## 2. Numerical algorithm: valid elements and limitations

The source correctly computes each parameter pair's own fragmentation root `z(eta,kappa)` and freezes that root only within the frozen panel. It keeps d=1, rho=.9, lambda=0 and government rules identical across panels. Welfare is one destination's CS plus the home firm's **three-market** operating profit net of design cost. It maximizes A's implemented national payoff, not world welfare. SU is solved as `(u,u,w)` rather than an incorrectly symmetric three-firm root. IS uses a symmetric root. Each equation is a unilateral firm FOC obtained by differentiating `q=M^{-1}1`, not a planner FOC.

The production classifier nevertheless checks only stationary equations, interiority, and FOC residuals; it does not itself establish all-firm Nash optimality, global uniqueness, positive quantities, or consumer concavity. These require separate evidence. Its 240-case summary JSON gives aggregate ranges but omits the generating spotcheck script and actual sampled cases. It cannot by itself reproduce that claim or the reported sufficient Rosen bound.

This audit supplied a separate full-three-variable evaluator with an analytic Jacobian. At 72 SU/IS cases (six parameter pairs, six depths including endpoints, both regimes), three asymmetric initial seeds produced 216 roots, agreeing to 1.67e-15. Maximum FOC residual was 3.05e-16; minimum quantity .576895; designs ranged .663588 to .847095; maximum sampled own second derivative was -.667177. Independent bounded unilateral payoff optimization, with endpoints, yielded maximum profitable-deviation gain 1.11e-15. Minimum sampled B eigenvalue was .0152905. This supports these continuations numerically; it does not establish Nash uniqueness or feasibility on the entire continuous rectangle or full strategy cube. Results: `phase_nash_spotchecks.json`.

At g=0 all physical regimes coincide: the within-depth routine provisionally labels the equality as IS, but its final gain check returns SW when no positive-gain depth is found. This convention does not create a positive-depth agreement; a revised algorithm should label the zero-depth outcome explicitly and retain any tiny positive gain separately.

Solver failures are **not** silently labeled SW: a failed IS or SU call yields UN/NaN, and the final `choose` returns UN if any depth is nonfinite. This is appropriately conservative. Exceptions are not explicitly logged/caught; those abort rather than establish nonexistence. The supplied arrays have no UN labels.

## 3. Major defect: narrow feasible IS windows are missed

The depth search is a finite mesh (`linspace(0,1,n)`), including 0 and 1. It does **not** locate the acceptance-boundary roots, search all interior extrema, or subdivide intervals where a feasible window lies wholly between mesh points. Refining only cells that changed at 81-to-321 and then confirming those cells at 641 cannot detect stable but wrong labels.

There are additional numerical conventions: acceptance tolerance 1e-8, gain-versus-SW threshold 1e-6, and tie set within 1e-6 of the numerical maximum. These can change labels near a true boundary; no tolerance sensitivity or certified error budget accompanies them. A positive IS welfare gain can be appreciable even when its binding outsider vote margin is tiny.

An independent analytic local audit of every stored SW cell found **seven frozen and four endogenous SW cells with strictly positive incident-welfare slope**. Independent 20001-point scans found an accepted positive-gain IS candidate at each of those eleven cells. The candidate alone invalidates SW as A's optimum; the scans do not prove that no still-better SU/IS candidate exists.

| Panel | eta | kappa values of false SW cells |
|---|---:|---|
| Frozen | .7555 | .93625, .945, .95375, .9625, .97125, .98, .98875 |
| Endogenous | .7600 | .945, .95375 |
| Endogenous | .76075 | .86625 |
| Endogenous | .7615 | .79625 |

Two examples were reconstructed with **80-decimal arithmetic**, independently of the supplied evaluator:

| Design | kappa | eta | g | i-s | i-m | i-o |
|---|---:|---:|---:|---:|---:|---:|
| Frozen | .93625 | .7555 | .0001 | 3.81355714348e-5 | 3.81347486213e-5 | 3.94704111296e-10 |
| Endogenous | .945 | .76 | .0001 | 3.70706802345e-5 | 3.70699896969e-5 | 1.39497667385e-10 |

All three acceptance gaps are positive and A gains relative to SW. The endogenous reconstruction solves all three firm FOCs and has maximum residual 7.91e-82. High-precision arithmetic is strong numerical counterevidence, **not** outward-rounded interval certification. Files: `high_precision_phase_counterexample.py/.json`, `high_precision_endogenous_counterexample.py/.json`. The first example also has m-s=8.22813497708e-10, so initial B acceptance is positive even if B ignored subsequent IS.

These are not just the 28 already corrected cells. They were SW before and after the archived refinement. The 321-point spacing is .003125; windows with useful candidates at g=.0001 or .00055 are simply not resolved. The all-cell local audit, independently recomputed Jacobian slopes, and eleven targeted scans are retained in `phase_independent_results.json` and `all_local_mismatch_rechecks.json`.

**Certification regression:** the prior Figure-3 numerical classification/QA gate must reopen. This does not by itself refute the benchmark all-depth theorem, invalidate the local design-incidence identity, or necessitate changing the economic model. It does refute the accuracy of the displayed classifications as solutions to the continuous-depth government's optimization.

## 4. Benchmark and SU disappearance

At the exact starred benchmark (.8505,.758), independently reconstructed fragmentation design is .7185927073221113. The local fixed slope D=.00676792412884 and endogenous slope mu=-.00830181999655 agree with the manuscript. A separate 20001-point scan finds frozen IS (sample best g=.0774, gain .0293635269) and endogenous SW. This is a numerical corroboration; the historical rigorous certificate is audited separately. The star is not an exact lattice point, and the caption/QA correctly acknowledge that it represents the separate benchmark.

The archived SU removal is reproducible: coarse-grid SU feasibility at one depth does not imply A chooses SU when a different depth delivers accepted IS. Refinement finds such better IS proposals in the former SU cells. All 28 stored revisions are reproduced. However, **zero SU at the refined sampled cells** remains an observation about this algorithm, not a theorem of no optimal SU in the rectangle, and not evidence that every SW/IS label is correct. The manuscript makes the no-SU scope distinction reasonably well, but presents the overall map too confidently as government-optimal.

## 5. Figure and layout QA

The panels share parameter bounds, scale, government game, and normalization. SW/IS labeling, star placement, legend and caption are coherent. Gray versus blue has a pronounced luminance contrast and the region labels preserve meaning in grayscale. The vector PDF embeds all fonts; `pdffonts` reports embedded Type 3 DejaVu fonts. A final journal production pass may prefer Type 42/TrueType embedding, but no present journal-specific violation is asserted. Source PNG is high resolution. Manuscript p.11 places the figure immediately before the institution section, without clipping, collisions or a wasted float-only page. The displayed numerical boundary is stepped rather than falsely smoothed. These presentation passes do not cure incorrect classifications.

## 6. Maximum defensible claim and minimal repair

Presently defensible: **the archived algorithm's finite-mesh outputs show large regions of differing agreement incentives, and independent checks preserve the benchmark Frozen-IS/Endogenous-SW contrast.** The exact plotted SW/IS boundary and its cell counts cannot be called validated solutions to continuous-depth optimization. At least eleven labels require correction; more are not excluded by this audit.

Minimum substantive repair before treating Figure 3 as a government-optimal numerical map:

1. Locate positive-depth acceptance-boundary roots of `i-s`, `i-m`, `i-o`, and `m-s`, with explicit handling of g=0 and tiny positive g. Use analytic local slopes as diagnostics for missed intervals.
2. Partition depth into implemented-regime intervals and evaluate A's objective at feasible endpoints, acceptance boundaries, and internal stationary candidates. When numerical signs are unresolved, retain an explicit UN classification rather than SW.
3. Recompute the affected boundary neighborhood under that method, retain candidate depth and all vote margins for every label, and run tolerance/high-precision checks where margins are small. The eleven counterexamples should be permanent regression cases.
4. Supply the actual Nash spotcheck generator/cases and the derivation/code underlying any uniform Rosen bound. No new global interval certification of the entire rectangle is required solely to present a correctly scoped numerical illustration.
5. Regenerate the figure from corrected data, amend counts/convergence narrative, and state remaining numerical error and scope limits. A fallback is to remove the phase map and retain only the independently checked benchmark illustration; that sacrifices breadth but does not alter the model or proven core.

A 1281/2561-point mesh alone is not the targeted fix: it can still miss even narrower feasible windows. Do not silently patch just eleven pixels.

## Referee 4 report

**Summary.** The v0.4 package is unusually candid about finite grids versus interval proof and correctly distinguishes fixed-depth SU feasibility from government-optimal SU. Its archived refinement results reproduce. Nevertheless, the classifier does not resolve participation boundaries, and stable false SW labels remain in both panels.

**Major concerns.** At least eleven economically incorrect SW labels; no continuous feasibility-boundary optimization; material undocumented 1e-8/1e-6 conventions; Nash spotcheck summary lacks reproducible case-level generator; no per-cell optimal-depth/margin ledger. Figure accuracy is MAJOR BUT FIXABLE and must reopen the numerical QA gate.

**Minor concerns.** `refine_mask` misnames the changed-cell mask; retain environment pins; optional Type42 PDF fonts; label the certified star as separately evaluated rather than an exact grid cell.

**Potentially fatal objections.** None to the paper's core established by this figure audit. If the paper required the exact continuous phase boundary or an absence-of-SU theorem as a headline discovery, the present evidence would be insufficient. It explicitly does not claim the latter. Failure to correct a known misleading map would become a publication-blocking integrity/accuracy problem.

**Recommended decision.** Major revision / CONDITIONAL GO on this component. Archived numerical reproducibility: PASS for the 84 rerun comparisons. Numerical equilibrium-map accuracy: FAIL in v0.4. Benchmark numerical consistency: PASS. All-rectangle rigorous certification: NOT ATTEMPTED and not required for a properly limited illustration.
