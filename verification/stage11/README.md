# Stage 11 hostile audit — reproduction entry point

Read `reviews/STAGE11_EXECUTIVE_EDITORIAL_VERDICT.md` first. This directory preserves the original v0.4 ZIP, copied numeric input, independent code, numerical counterexamples and successful proof-source replays. It does **not** contain a corrected phase diagram or a revised manuscript.

Input source SHA, exact archive/file hashes and workflow tag are in INPUT_MANIFEST.json. Requirements used: Python3.12.14; NumPy2.3.5; SciPy1.17.0; SymPy1.14.0; mpmath1.3.0; matplotlib is needed by the archived classifier even in nonplotting runs. See math_execution_environment.json for source hashes.

From repository root:

```bash
python3 verification/stage11/independent_incidence_symbolic.py
python3 verification/stage11/independent_matrix_audit.py
python3 verification/v2b_stage04a_krawczyk_cleanroom.py
python3 verification/v2b_stage06_pareto_holdout.py
python3 verification/stage14rs_adjustment_cost.py
python3 verification/stage21_no_su_phase_theorem.py
```

The first script checks20 exact local identities from matrix inversion, without importing historical evaluators. The second derives/diagnoses the full3-firm system and exact domain bounds independently. The remaining commands replay historical all-depth, Pareto, local-friction and network-face certificates; their actual new stdout files are `*_replay.log`. These replays do not certify the Figure3 parameter rectangle. No Lean build was executed.

For all numerical phase attacks and the84 archived depth-comparison rechecks, use README_FIGURE_AUDIT.md. New tests of the old code intentionally reproduce a known incorrect map and must not be read as a corrected solver. The11 counterexamples establish only that those SW labels are false; finding one accepted better proposal does not solve the global optimal positive-agreement type.

`AUDIT_PROTOCOL_AND_MATERIALS.md` lists every requested material, access gap, applied workflow checklist and verification actor. `source_v04/` contains the exact ZIP; `input_v04/` provides portable numeric source/data snapshots. Original TeX/PDF/Figure3 vector PDF are already tracked under manuscript/ and independently byte-matched against the ZIP. Figures1/2 and Tables1/2 are embedded in the TeX.

No benchmark, Theory Freeze, production classifier, manuscript or main-branch source was modified. Repaired algorithms and any final supplementary package must be created as a separately reviewable next change; do not overwrite these negative records.
