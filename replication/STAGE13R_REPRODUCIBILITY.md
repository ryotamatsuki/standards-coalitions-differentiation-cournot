# Stage13R: reproducibility and proof-certificate submission index

This index is for the Stage13R JPET **working** revision and does not claim external peer review or journal submission readiness.

## 1. Distinct evidence and scope
- **Central all-depth theorem**: exact reference primitives `(d,eta,rho,kappa)=(1,379/500,9/10,1701/2000)`, and a qualitative nonempty primitive neighborhood under AB-first inherited-depth accession. The proof uses the full three-firm global Nash uniqueness argument, **two-variable SU Krawczyk** and **scalar IS interval Newton**, then uniformly negative welfare-derivative bounds. It is NOT a finite-depth grid.
- **Figure 3**: 41x41 *numerical proposal search* in `(kappa,eta)` at `d=1,rho=.9,lambda=0`; gray = no better accepted offer detected; blue = accepted IS candidate beating the **computed** SU envelope. It is NOT a theorem-level classification, nor a proof of universal absence of SU.
- **Frozen counterfactual**: design held at the fragmentation Nash for each primitive point, cost `K_i(z)` retained. Governments' induced reduced payoff functions therefore differ between treatments although government objectives and protocol are identical.
- **Direct grand**: a different rejection continuation (SW, not established SU), not an unrestricted equilibrium selection theorem.

## 2. Pinned underlying source and reference replay
Certificate source pinned to historic Stage11 audit commit **`54ac8389f2c45d56b2e587a62c62f226cc121f95`** (same scripts at Stage13 manuscript reference).
| Purpose | Command (repository root) | Expected |
|---|---|---|
| Complete g interval theorem | `python verification/v2b_stage04a_krawczyk_cleanroom.py` | `KRAWCZYK SIGN CERT SUCCESS accepted= 1000 splits= 0`; max derivative upper bounds below `-0.007970192997334808`, `-0.015038883337750794` |
| Grand Pareto | `python verification/v2b_stage06_pareto_holdout.py` | Strict lower gain `>0.0169346278736` |
| Friction local cutoff | `python verification/stage14rs_adjustment_cost.py` | Exact sign bracket `0.93538<lambda_c<0.93539` |
| Network face | `python verification/stage21_no_su_phase_theorem.py` | Exact rho=1 SW/IS threshold eta=6/7, not unrestricted rho |
| Full numerical candidate map | `OPENBLAS_NUM_THREADS=1 python stage11_v05_package/run_reproducibility.py --mode full` | 3362/3362 saved candidate labels, 11 prior false-SW corrections, 1550 IS samples (0 numerical reversals), 1812 SW micro-depth tests (0 new candidates) |
| Package integrity | `python stage11_v05_package/verify_github_package.py` | Git blob digest/expected data PASS |

GitHub CI prior reference runs: full numerical [39785976411](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39785976411) SUCCESS; canonical 21-page Stage11 PDF [39785976404](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39785976404) SUCCESS. Stage13R independent article+figure CI has a separate workflow `.github/workflows/stage13r-jpet-build.yml`.

**Research-code pin:** SHA256 `25c92e800a255ddfd0712f3a9095f83a2a69c70addcf0d16f75fc7b65289fd74` for Krawczyk source; `7134e55cd6dcb3e3f0f6cc8af27c698240364c4f0670ef37c0324231b4757a28` for Pareto source (Stage13R audit PR31). Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0, mpmath 1.3.0; interval source `iv.dps=35`, Pareto `iv.dps=40`. See `verification/stage11/math_execution_environment.json` for source hashes and versions.

## 3. Publication package assembly
Current files are `manuscript/stage13r_jpet_revised.tex`, `manuscript/stage13r_proof_supplement.tex`, `manuscript/stage13r_figure3_tikz.tex`. The figure export script `scripts/stage13r_export_figures.py` generates standalone cropped vector PDF Figures 1–3, preserving the original geometry; compare artwork against article figures and figure 3 archived 41x41 candidate labels before final publication. Separate Figures 1–3 and LaTeX are included in the branch-level CI build if successful.

**Archive status:** an immutable public deposited release DOI/URL and human verified contributor declarations are **not** yet established. No DOI is invented and no source revision is called a frozen public release until it exists. At Stage14 insert exact revision SHA, archived URL and author-approved data/code statement in the manuscript.

## 4. QA boundaries
Changes after the audited Stage13 include prose, proof exposition, reference citations, candidate-map label, declaration template and vector-artwork packaging. Original model, fixed-dimension FOCs, theorem constraints, certified primitives and numerical scientific code are not modified. Rebuild and visually inspect any new PDF. If exact claims/numeric values change, re-open the scientific certification gate rather than accepting a typography-only check.
