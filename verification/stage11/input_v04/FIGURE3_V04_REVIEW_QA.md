# Stage25 v0.4 — Figure 3 literature-facing review and numerical QA

## Exposition audit / placement
The v0.3 PDF places Figure 3 on p.11 after numerical Table 2 on p.10, but it was a separate float-only page with an overly long caption. In v0.4, the figure remains immediately after the numeric illustration and before the institutional comparison, uses a shorter caption, and is placed inline (`float` [H]) so the following institutional section begins on the same page. PDF 17 pages; page 10 is the main diagram explanation / SU diagnostic paragraph, page 11 contains the diagram and institutional argument.

## Interpretation and substantive correction
The v0.3 narrow SU bands were artifacts of the coarse government-depth grid in several cells; copying them to a refined figure without checking would overstate the evidence. The g search must find a government-optimal proposal and its accepted terminal outcome; a terminal SU possible at some g does NOT imply that SU maximizes government A's payoff across all g.

## Updated numerical experiment
- Primitive parameters: x-axis kappa [0.70,1.05] sampled 41 points; y-axis eta [0.742,0.772] sampled 41 points; d=1, rho=.9, lambda=0; inherited-depth AB-first government game; g in [0,1].
- Each (kappa,eta) has its **own** no-agreement residual Nash z(kappa,eta) in the frozen panel. Endogenous panel re-solves firms for SU and IS at each considered g. Same national CS + home-firm *worldwide* profits, same governmental votes and depth choice.
- First pass uses 81 g samples across ALL 1681 parameter cells (prior v0.3 used 15x15 cells / 61 g). Near different labels / phase transitions, targeted 321-g refinements cover 351 cells. Of these, 28 classifications differ from 81-g labels, all 28 retain their 321-g regime in a 641-g recheck.
- First pass reported 11 frozen-SU and 12 endogenous-SU cells, but targeted 321-g refinement reclassified ALL of those as SW/IS. **Final map = frozen SW 772, frozen IS 909; endogenous SW 1051, endogenous IS 630; zero SU at sampled cells**. This is finite numerical nonobservation, NOT an analytical no-SU theorem or certified global 2D result.
- Benchmark (kappa,eta)=(.8505,.758) is not exactly a point on the plotted 41x41 lattice; it is superimposed as an independently checked original-center star. At that exact center the Stage22 historical all-depth theorem proves Frozen IS and Endogenous SW. Independent sample of g-grid 61,161,321 also returns those outcomes.
- Nash output checks: at 20 selected (kappa,eta) pairs × 6 depths × two active policy regimes = 240 test cases, each with independent full three-firm FOC solver using three initial seeds, residual maximum 3.1e-14, x range [0.637,0.867], q_min=.572>0 and zero detected alternative FOC equilibria. The sufficient full-cube Rosen uniqueness bound peaks at .61977 below minimum kappa=.70 on displayed rectangle. This does not certify every g or every parameter point; full interval proof remains at historical center only.
- Numerical limitations: policy optimization still based on finite depth grids, with targeted checks; unobserved narrow regions, hidden corners or non-regular strategies are not globally excluded across the continuous parameter rectangle. Boundaries are stepwise numerical classifications; interpolation smoothing is intentionally excluded.

## Final proof and production QA
- LaTeX compiles on two successive pdflatex passes (17-page PDF, no missing-reference/overfull warnings); Figure 3 is drawn as embedded vector PDF; image and caption inspected on p.11 at publication-like zoom.
- Mechanism theorem, open primitive-neighborhood theorem, and C1/C2 are unchanged. No new theorem or false prior-art novelty claims have been inserted.
- The SU diagnostic now explains exactly why fixed-depth feasibility is not government-optimal SU and why grid-alias SU regions were removed.
- No submission-ready / paper-priority verdict granted. Stage11 hostile manuscript audit remains to be done.
