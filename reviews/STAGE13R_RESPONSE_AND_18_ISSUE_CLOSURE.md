# Stage13R hostile referee response ledger — JPET revision

Input referee: Draft PR #31, reviewed Stage13 commit `c7b52ac10a701c682479e8f57c1343ceed1df719`. Repair branch: `revision/stage13r-jpet-full-response-20261023`, based on PR31 and no changes to main, Theory Freeze or verified scientific calculation scripts.

**Status semantics:** IMPLEMENTED = changes made to current revised source; PENDING AUTHOR = cannot responsibly supply declarations or certify journal submission readiness; QA PENDING until the final branch build, visual inspection and release verification. No original Stage13 sources are overwritten. This report is an author-facing revision map, not simulated acceptance by JPET.

| Issue | Tier | Concrete edit & where | Independent check needed | Status |
|---|---:|---|---|---|
| **13R-01** | 1 | Introduce substitution vs network benefit in §2 after `eq:matrices`, within-destination network quantities, quasi-linear preferences, distinguish `rho,eta,g,x`, new §1 opening | algebraic model consistency; no changed `M` | IMPLEMENTED |
| **13R-02** | 1 | Rewrite §4.2 national mechanism: rise in member similarity, private cost savings, domestic CS and rival export-profit incidence; §5 table discussion maps to B's decision | sign of `u',v'` only at benchmark, no broad comparative statics claim | IMPLEMENTED |
| **13R-03** | 1 | Add stand-alone `m-s` vs outsider accession `i-o` passage before local theorem; distinguish actual upstream vote conditional on continuation | respect `eq:consent` backward induction | IMPLEMENTED |
| **13R-04** | 1 | Replace literal incorrect same-government-payoffs assertion with same **primitives/goals/rules but different reduced payoff functions** | grep for conflicting payoffs phrasing | IMPLEMENTED |
| **13R-05** | 1 | Rebuild open-region theorem proof as Step1 full 3-firm Nash, Step2 all-g derivative integration/frozen global envelope/closed optimum, Step3 uniform open primitive continuation; Appendix certificate table | no loss of mathematically nontrivial bridge; exact bounds conservatively weakened | IMPLEMENTED |
| **13R-06** | 1 | Add Appendix A `eq:designQuantityBridge` and `eq:crossProfitBridge`, derive national gradient and loss's correct positive `V` contribution | check unilateral derivatives and quantities | IMPLEMENTED |
| **13R-07** | 2 | Shorten §3 private-equilibrium heading/explanation; restrict Appendix F welfare-gap variables to `Delta_m,Delta_a,Delta_i,Delta_b` avoiding matrix `M,J,H,V` conflicts | no altered signs, matrix symbols in other appendices unchanged | IMPLEMENTED |
| **13R-08** | 2 | Add Rosen (1965) and Rump (2010) to references and cite relevant concave-game and interval-proof methods in supplement | journal metadata and `natbib` citation compilation | IMPLEMENTED |
| **13R-09** | 2 | Appendix C near-face derivative `eta_c'(1)=211/196` with partial derivatives; Appendix F inward Nash design expansion `1-x_i=6beta q_i^0 a_i/kappa+O(beta²)` and boundary note | distinguish rho=1 face from active design rho<1 and rho=.9 plot | IMPLEMENTED |
| **13R-10** | 1 | §1 explicit Takarada 2020 Proposition 2 and 5–6 distinction: consumption externality/compliance cost + core, vs sovereign controlled private-design comparison; §8 compress | do not claim first standards obstruction or full unreviewed propositions | IMPLEMENTED |
| **13R-11** | 2 | Remove repeated defensive priority evaluations and research-audit process diction, compact §6 and §8 | scope and no invented general bargaining theorem retained | IMPLEMENTED |
| **13R-12** | 2 | Replace entire abstract with single results-led 160–180-word version | ≤250 words under current JPET guide; no new result | IMPLEMENTED |
| **13R-13** | 2 | Shorten institutional/boundary headings and entire conclusion; keep local friction and limited rho near-face scope | theorem locations and conditions remain identifiable | IMPLEMENTED |
| **13R-14** | 2 | Rename in-panel Figure3 SW/IS to **No offer found / IS candidate**, and correct caption and surrounding text | check figure geometric rectangles/polygons unchanged; archived 3362 cells are **numerical** | IMPLEMENTED |
| **13R-15** | 3 | Shorten Figure1 caption but keep same sequence and causal Figure2 | standalone production artwork visually inspect | IMPLEMENTED |
| **13R-16** | 2 | Add theorem/proposition crossrefs to Table1 and actual B/C rejection interpretation after Table2 | make sure wider result names don't overflow table | IMPLEMENTED; PDF QA PENDING |
| **13R-17** | 1 | Write `replication/STAGE13R_REPRODUCIBILITY.md` with exact historical source/replay commit, environment, 1000 intervals, expected output and hash references; preserve no-all-slice guarantee | archive DOI/immutable submission release URL must be inserted into declarations by author | IMPLEMENTED PROVENANCE; IMMUTABLE PUBLIC RELEASE PENDING |
| **13R-18** | 1 | Replace generic declarations with explicit author-verification fields, funding/COI/AI-use/data-code status, ORCID/contact; standalone PDF artwork workflow; no invented declarations | human author must actually confirm each item; portal-generated final PDF inspection | **PARTIAL; PENDING AUTHOR** |

## Submission decision / non-negotiable stop condition

**Manuscript-side requested editorial modifications are implemented but NOT all final-submission conditions are completed.** JPET portal upload/submit remains blocked until: (a) independent revised LaTeX/PDF+vector-figure CI PASS and visual QA; (b) author-confirmed identity/affiliation/ORCID/correspondence, funding, COI, acknowledgment, AI systems+tasks and human accountability; (c) immutable code/data release and final SHA linked in article; (d) JPET live portal-generated reviewer PDF, cross-references, figures, declarations; (e) final author approval. No model extension or theorem upgrade is required by this editorial audit. If a logical counterexample emerges, reopen the earliest affected research stage.

## Reference source and validation
- Stage11 mathematical interval evidence / 1000 all-real-depth boxes: source commit `54ac8389f2c45d56b2e587a62c62f226cc121f95`.
- Stage11 numerical 41x41 and known 11 regressions: current verified `stage11_v05_package/` with GitHub Actions run `39785976411`.
- Stage13R original PR31 contains 18 detailed issues and exact adopted English before edits.
- Stage13R revised work is in `manuscript/stage13r_jpet_revised.tex`, `stage13r_proof_supplement.tex`, `stage13r_figure3_tikz.tex`, plus standalone exported figure PDFs if build is successful. CI `.github/workflows/stage13r-jpet-build.yml` publishes exact build results.
