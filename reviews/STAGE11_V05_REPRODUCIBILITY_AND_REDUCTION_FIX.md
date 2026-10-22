# Stage 11: distributed v0.5 path fix and SU/IS proof transparency

## Origin
PR #28 commit \`cae6059\` preserved exact old 23 archive bytes but 2 shipped scripts did not run in the published directory hierarchy. The original archive and its legacy hash list remain a **historical record**, not a manifest of subsequent edits.

## Actual changes
- Corrected \`stage11_fix_classifier.py\` to read package-local \`verification/input_v04/figure3_data_41x41.npz\` and write regenerated arrays/logs only in \`verification/rerun_outputs/\`.
- Corrected \`verify_v05.py\` to load saved maps and dominance data from \`verification/\`, original map from \`verification/input_v04/\`, and PDF/TeX from \`manuscript/\`, using the existing \`verification/build_log.txt\`; outputs recheck JSON only to \`rerun_outputs/\`.
- Changed dominance, SW stress and figure replot tools to use the same rerun_outputs directory. Preserved archived original case/result/figure files.
- Added \`run_reproducibility.py\` smoke and full modes, real compute+array comparison, no synthetic PASS from hash check only.
- Supplement clarifies SU reduction (u,u,v) from A/B exchange symmetry, IS scalar (y,y,y) from S3 symmetry; the scalar interval-Newton implementation differs from SU's Krawczyk. The all-three-firm strict Nash argument remains independent of the reduction.

## Required replay checks
1. Run the standalone smoke tests after checkout: \`python stage11_v05_package/run_reproducibility.py --mode smoke\`.
2. Run full analysis: \`python stage11_v05_package/run_reproducibility.py --mode full\`. This may take several minutes. Check regenerated arrays **exactly equal** stored labels, 1,550 IS candidate comparisons and 1,812 SW candidate micro-depth tests. Save actual CI run status, rather than asserting completion before execution.
3. Compile the updated \`manuscript/stage25_jpet_v05.tex\` on GitHub CI; its generated PDF replaces the earlier original PDF and may have a different page count due to proof text. Do not claim file-byte identity to the old 20-page PDF.
4. Check all eight baseline versioned scripts/outputs are retained and theory/main untouched.

## Research-status limit
Passed smoke/integrity tests or a green CI only validates deterministic reproduction, not an exact global numerical phase diagram nor JPET readiness.
