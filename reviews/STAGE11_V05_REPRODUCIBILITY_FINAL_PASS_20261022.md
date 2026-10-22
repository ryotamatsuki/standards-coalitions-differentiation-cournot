# V2b Stage11 v0.5r1 — final standalone reproducibility closeout (2026-10-22 JST)

## Verdict
**Reproduction-package integrity and scientific numerical replay: PASS**, on the corrected, distributable repository layout. The original v0.5 release remains available in earlier Git history, while this repair patches its broken relative paths without changing the original model or Stage22 Theory Freeze.

### Authoritative GitHub Actions evidence
- **Full standalone job: SUCCESS**, [run 39785976411](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39785976411).  `stage11_v05_package/run_reproducibility.py --mode smoke` and `--mode full` run directly from the published package layout, with no missing-path failure. The workflow uses Python 3.12, NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8.
- **Updated full 21-page manuscript PDF: SUCCESS**, [run 39785976404](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39785976404). Current manuscript PDF: `manuscript/stage25_jpet_v05.pdf`, rebuilt from updated `manuscript/stage11_proof_supplement.tex`. The original **20-page PDF** remains in `stage11_v05_package/manuscript/` as an immutable historical v0.5 release artifact. Do NOT claim these two PDFs are byte-identical.

### Completed mandatory tests
| Test | Final result | Evidence |
|---|---|---|
| Patched package blob integrity | **PASS** | `verify_github_package.py` with `CURRENT_BLOB_MANIFEST_V05R1.json`; legacy 23-file `SOURCE_FILE_HASHES.json` retained for historical archive |
| Published `verify_v05.py` script without old paths | **PASS** | `verification/verify_v05.py` reads its actual package-local data + manuscript; `pdfinfo` optional, PDF magic checked even without it |
| Published `stage11_fix_classifier.py` without old paths | **PASS** | reads `verification/input_v04/figure3_data_41x41.npz`, writes `verification/rerun_outputs/` |
| 11 previously misclassified SW cells | **PASS** | seven frozen, four endogenous, all return candidate IS with positive feasible depth |
| Exact canonical point's two policy treatments | **PASS** | fixed-design IS and endogenous-design SW |
| 41x41 lattice for both treatments | **PASS** | **3362/3362** resulting saved numerical regime labels exactly reproduced |
| IS candidate bilateral-envelope tests | **PASS** | **1550 checked, zero contrary cases; min tested gap 0.00003967743602961704** |
| SW candidate micro-depth tests | **PASS** | **1812 checked, 0 additional accepted IS found** |
| Candidate map plot regeneration | **PASS** | `plot_figure3_v05.py` writes image and PDF under `verification/rerun_outputs/` |
| LaTeX proof supplement source/compiled PDF | **PASS** | GitHub Actions compiles and pushes current **21-page** manuscript after deterministic branch reconciliation |
| SU / IS interval methods transparency | **PASS** | `stage11_proof_supplement.tex` explains SU 2D Krawczyk on (u,v), IS 1D interval-Newton on y, and lift to full 3-firm Nash using Rosen full-cube uniqueness |
| No modification of main or Theory Freeze | **PASS** | only Stage11 PR #28 draft branch changed |

### Reproduction commands
From any working directory with the repo checkout:
```sh
python stage11_v05_package/verify_github_package.py
python stage11_v05_package/run_reproducibility.py --mode smoke
OPENBLAS_NUM_THREADS=1 python stage11_v05_package/run_reproducibility.py --mode full
```
The latter reruns each 2D numerical candidate cell and the associated checks. It is intentionally computationally intensive. Full logs and generated outputs are uploaded as GitHub Actions artifacts for run 39785976411. Shipped inputs/archived results are not overwritten by these reproductions.

### Explicit surviving limits
1. The displayed Figure3 two-dimensional phase classification remains **numerical and exploratory**; these successful tests do NOT certify all parameter/depth combinations by intervals.
2. The exact all-depth central mechanism's 1000-interval mathematical certificate is independent and already replayed in Stage11 PR #27; this numerical workflow does not reprove it.
3. The broader novelty evidence gaps for inaccessible historical supplements remain acknowledged. Stage12 journal placement and submission QA remain separate.
4. Updated current package content differs intentionally from original v0.5 byte-for-byte hashes. The historical archive is preserved; the current package uses its own SHA1 Git blob manifest. The edited proof supplement now contributes to a 21-page current article.

**Result:** the user's two originally failing scripts now work from the published hierarchy, and the single command demonstrably re-executes the entire numerical candidate analysis successfully on GitHub. No outstanding reproduction-blocking items were found in this validation run.
