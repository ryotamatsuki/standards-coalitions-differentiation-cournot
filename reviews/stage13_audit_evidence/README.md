# Evidence scope

These are audit files, not replacements of frozen production proofs. Target source: `8aeb27f4df47a759723b03ce77fbe53adf4bb1d1`.

- `independent_reconstruction.py`: no project economic-module imports; matrix/FOC/payoff reconstruction, point and asymmetric-start root diagnostics; float calculations are not proofs.
- `independent_results.json`: actual output under package versions in `environment.json`.
- `exact_shadow_runner.py`: in-process audit re-evaluation of nonlinear scripts with Rational constants evaluated as interval rationals and Gershgorin sums kept in intervals. Does not edit originals; same underlying algebra/partition and arithmetic libraries, not a new independent formal proof.
- `nonlinear_original_*.log`: execution PASS is not accepted as exact certification because coefficient/row rounding is unsound.
- `nonlinear_exact_shadow_*.log`: supports repair feasibility; does not silently replace Stage8 certificate.
- `rounding_counterexample.json`: exact-vs-float 71/500 non-inclusion. Reproduce in Python with `from mpmath import iv; iv.dps=40; print(iv.mpf(71/500),iv.mpf(71)/500)`.
- `generated_nonlinear_is.py`: inspected lambdify source containing non-dyadic coefficient divisions, shown as evidence of rounding.
- `canonical_interval.log`, `pareto_original.log`: new local executions of existing programs; not newly authored cleanroom full-domain algorithms.
- `envelope_decomposition.json`: finite-difference diagnostic at epsilon1e-5 from independent model; not a new economic theorem.
- `phase_a.md`, `proof_phase_a.md`, `editorial_phase_a.md`: exposure/first-impression ledger before code and prior stage verdicts. User prompt values were already known; PR metadata exposure is disclosed.
- `table_check.log`, `source_check.log`: structural/source consistency only. `make paper` was executed, 15-page PDF visually inspected. Build console-log whitespace was normalized; early LaTeX passes include expected unresolved references, final main.log had none. PDF hash in environment.json; PDF itself not added to audit-only PR.

Lean source was inspected and four proxy signs were crosschecked arithmetically; Lean executable absent, so no new Lean kernel build is claimed. No third-party copyrighted paper PDFs are redistributed.
