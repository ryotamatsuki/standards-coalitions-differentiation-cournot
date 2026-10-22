# V2b Stage 11 — v0.5 verified complete source bundle

This folder is the **exact 23-file extraction** of `V2b_Stage11_v05_Corrected_Manuscript_and_Reproducibility.zip`. All blobs were sent to GitHub using base64 of original file bytes and checked against locally computed git-blob SHA1. Inspect `SOURCE_FILE_HASHES.json` for the original byte length, SHA256 and Git Blob SHA of every file. No byte normalization, abridgment, or reconstruction was used to populate this folder.

**Manuscript:** [v0.5 TeX](../manuscript/stage25_jpet_v05.tex), [v0.5 PDF](../manuscript/stage25_jpet_v05.pdf), [proof supplement](../manuscript/stage11_proof_supplement.tex), and [editable Figure 3](../manuscript/figure3_v05_tikz.tex). The identical original bytes are also archived under `manuscript/` in this folder. [Figure 3 vector](../figures/stage11_v05/figure3_v05_corrected.pdf) and [raster](../figures/stage11_v05/figure3_v05_corrected.png).

**Computational records:** `verification/` contains the complete original candidate ledger (3362 panel-cells), dominance checks, regression cases, corrected Python scripts, phase NPZ, plotting script, QA JSON and original local compile log. The original Python scripts may depend on the historical relative-layout convention: inspect `README.md` and `verification/verify_v05.py` and use the immutable Stage11 PR #27 replay code for strict mathematical proof. Existing CI smoke and PDF workflows live outside this archived folder.

**Scientific caution:** Figure 3 displays **exploratory numeric candidates**; SW shading is not a proved all-depth nonexistence claim for every 2D-grid cell. The rigorous center/open-neighborhood theorem rests on the separate 1000-interval replay documented in Stage11 PR #27. The manuscript is a working draft; Stage12 journal routing and submission QA remain separate.

**Safety:** this commit does not merge or mutate `main`, the frozen theory, or the Stage11 auditor source branch.
