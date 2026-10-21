# Stage13A independent reproducibility evidence

Audited input: `07b275fd5693d8160234bf2e318e24e2fa4878c2` (PR #9).

## Actual local executions

Pinned dependencies: `production/requirements-stage9.txt`; Python 3.12.14.

```bash
python -m venv .venv
.venv/bin/pip install -r production/requirements-stage9.txt
.venv/bin/python verification/v2b_stage13a_independent_audit.py --json verification/stage13a/independent_results.json
.venv/bin/python verification/v2b_stage04a_krawczyk_cleanroom.py
.venv/bin/python production/scripts/verify_freeze.py
```

* `independent_run.txt`: 28 exact identities, exact Fraction interval open-region inequalities, exact PSD vertex checks, explicit balanced benchmark and boundary/output counterexamples; PASS for corrected claims. **Literal PR #9 Eq.(9) FAILED**: a regression identity preserves its sign residual. The program's final PASS means the corrected audit checks and expected failure regression pass, not that the original display is correct.
* `independent_results.json`: exact rational interval endpoints, primitive-region coordinate definition, exact sufficient-condition witnesses, numerical diagnostics and expected wrong-formula outputs.
* `baseline_global_run.txt`: original canonical full-depth Krawczyk / frozen full-menu certificate; PASS. This reexecution is separate from the new independent derivation; it is not falsely represented as a new all-depth regional proof.
* `freeze_run.txt`: original v2 11-blob protection; PASS.

The dedicated remote workflow runs the independent checker and freeze guard. Actual remote status, commit SHA, job names and run URLs are recorded in the audit Draft PR description after observation. Workflow installation alone is not a CI result. Local nonlinear, Lean and LaTeX jobs were not reexecuted in this audit; if remote inherited workflows run, their observed results must be stated separately.

## Proof trust boundary

The independent symbolic path differentiates scalar Cramer quotients before imposing symmetry, without importing previous V2b programs. SymPy exact identities are algebra checks, not proof of the hypotheses. The new region uses an independent standard-library Fraction interval evaluator; every operation is exact, including endpoint addition. It rejects floats and intervals containing zero divisors. Numerical output conversion happens after sign checks. This avoids the old float-early coefficient and unrounded-endpoint-addition failures.

The new region is parameterized by (z,eta,rho,d), with kappa recovered from the SW Nash FOC and kappa_z>0. It maps to an open primitive region; its kappa enclosure must not be reinterpreted as an independent rectangular parameter interval. It certifies **local-in-depth** B/C. Only the unchanged single-witness certificate covers the full depth menu. All reviewed claims concern canonical phi=x; the earlier nonlinear same-depth failure remains in the inherited record.

No proof assistant was used for the new analytic results. No source-complete priority certificate, general optimal policy threshold, or all-parameter Nash theorem is supplied.
