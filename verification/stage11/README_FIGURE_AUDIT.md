# Independent Figure 3 audit reproduction

Run from repository root with Python 3.12, NumPy, SciPy, matplotlib, mpmath installed. Original model evaluator imports matplotlib even when only classifying. Audited versions: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0; mpmath 80-digit mode used only for numerical counterchecks, never claimed as interval proof.

```bash
OPENBLAS_NUM_THREADS=1 python3 verification/stage11/recheck_supplied_records.py
OPENBLAS_NUM_THREADS=1 python3 verification/stage11/phase_independent_audit.py
OPENBLAS_NUM_THREADS=1 python3 verification/stage11/recheck_all_local_mismatches.py
OPENBLAS_NUM_THREADS=1 python3 verification/stage11/phase_nash_spotchecks.py
python3 verification/stage11/high_precision_phase_counterexample.py
python3 verification/stage11/high_precision_endogenous_counterexample.py
```

The first command re-executes 28 archived cells at 81/321/641 depths (84 comparisons), using unchanged input source. The second derives local slopes at all stored SW cells from a separate full-three-firm analytic-Jacobian evaluator and scans benchmark/boundary cases at 20001 depth points; the third retains the dedicated eleven-case record. The fourth independently checks full-three-firm roots from asymmetric seeds and bounded unilateral best responses at 72 continuation cases. The final two commands assert positive participation gaps at 80-decimal precision and save the resulting values. All paths resolve relative to the scripts, with numerical source/data snapshots under `input_v04`; no Library credentials or external manuscript folder is required to reproduce these calculations.

The source `figure3_recompute_v04.py` can regenerate the entire historic map, but its output is known to contain missed narrow feasible windows. It is archived as evidence, not proposed as the repair. The audit did not rerun that whole exercise or repair the phase map. Preserve the input snapshot unchanged; write any future improved algorithm elsewhere.

Important result: archival reproducibility PASS does not imply optimal-map accuracy PASS. Seven frozen and four endogenous SW cells admit a positive-gain accepted IS candidate. A dense-grid candidate is not a proof of the globally optimal positive agreement type or a theorem of no SU. The standalone report is `verification/STAGE11_FIGURE3_PHASE_DIAGRAM_AUDIT.md`.
