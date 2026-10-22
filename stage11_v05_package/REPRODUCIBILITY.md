# Stage 11 v0.5 — standalone reproducibility patch (2026-10-22)

The 23 files from the earlier v0.5 archive remain independently recoverable at git commit cae6059 and the legacy \`SOURCE_FILE_HASHES.json\`. This patch corrects the **distributed script locations**, supplies the archived v0.4 classifier inputs in \`verification/input_v04/\`, and adds a genuine end-to-end entry point. The patched files intentionally no longer match the historical immutable file hashes; do not use that legacy manifest to claim current byte identity.

## Commands

From anywhere (Python 3.12 and numpy, scipy, matplotlib required):

\`\`\`bash
python stage11_v05_package/run_reproducibility.py --mode smoke
python stage11_v05_package/run_reproducibility.py --mode full
\`\`\`

\`smoke\`: byte/count/paper-presence check through \`verification/verify_v05.py\`, the 11 previously false SW labels, both benchmark policies, and two near-zero vote-margin witnesses. \`full\`: all 41x41x2 classifier cells, IS-envelope checks on 1,550 cells, 1,812 SW micro-depth tests, numeric phase rendering and strict comparison with the shipped data. Recomputed outputs reside in \`verification/rerun_outputs/\` and are deliberately untracked; \`full\` is computationally intensive.

Individual source scripts also run **without relocating them**:

\`\`\`bash
python stage11_v05_package/verification/verify_v05.py
python stage11_v05_package/verification/stage11_fix_classifier.py
python stage11_v05_package/verification/stage11_dominance_check.py
python stage11_v05_package/verification/stress_swcells.py
python stage11_v05_package/verification/plot_figure3_v05.py
\`\`\`

The last three require a completed classifier run. All scripts use script-directory-relative paths, not the working directory. \`verify_github_package.py\` is a historical snapshot integrity checker, not an approval of changed script hashes; use \`run_reproducibility.py\` for the patched package.

**Proof clarification:** The main manuscript supplement now identifies SU's 2D symmetry reduction and IS's 1D interval-Newton certificate. Global Rosen uniqueness of the *three-firm* Nash guarantees that lifted solutions are fully strategic equilibrium continuations. This clarification does not broaden the certified original parameter region.

**Boundaries:** Figure 3 outside the rigorous benchmark neighborhood remains a numerical candidate map; a successful full computation cannot certify a continuum of depths or the whole 2D parameter rectangle. Formal Stage12 journal/submission gates remain separate.
