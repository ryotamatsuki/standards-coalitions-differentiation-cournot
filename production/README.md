# V2b Stage 9 — Production and reproducibility

**AUTHORITATIVE MODEL:** [Stage 8 frozen specification](../docs/V2B_THEORY_FREEZE_2026-10-21_v1.md), ID \`V2B-THEORY-FREEZE-2026-10-21-v1\`. This production scaffold is **not** a manuscript, submission, or approval of a more general theory.

## Quick start (Python 3.12)

\`\`\`sh
python3 -m pip install -r production/requirements-stage9.txt
make freeze
make table
make table-check
make fast-proofs
\`\`\`

Additional complete proof check: \`make full-proofs\` (computationally intensive: full \`g\` interval certification and asymmetric firm Rosen domain).

LaTeX: install TeXLive, BibTeX and \`latexmk\`, then \`make paper\`. Produces \`paper/build/main.pdf\` locally; that build is deliberately a **Stage 9 shell** with placeholders for Stage 10 prose. The welfare table \`paper/generated/welfare_table.tex\` is recomputed from \`verification/v2b_stage07_welfare_institutions.py\` and is ignored by Git. **The government game does NOT implement the SU/IS table rows at this witness:** these are conditional continuation welfare comparisons. Do not confuse them with policy SPNE outcomes.

Lean: install the pinned toolchain from root \`lean-toolchain\` (Lean4 v4.24.0); \`make lean\` only validates FOUR rational-proxy payoff inequalities, **not** equilibrium Nash roots or full government SPNE.

## What gets rerun and trusted

| Level | Asset | Assertion scope |
|---|---|---|
| Economic version guard | \`production/freeze_manifest.json\`, \`scripts/verify_freeze.py\` | Exact **Git blob object ID** of Stage8 frozen specification and high-stakes code, not all arbitrary repository files |
| Pointwise payoff calculation | \`scripts/generate_welfare_table.py\`, \`verification/v2b_stage07_welfare_institutions.py\` | Three downstream equilibrium welfare rows at g=.05 in canonical linear φ=x V2b |
| Rational interval baseline proof | \`verification/v2b_stage04a_krawczyk_cleanroom.py\` | All-g endo SU and C joining signs, frozen-design benchmark, unilateral design gradients; separate math/provenance |
| Nonlinear diagnostic | \`verification/v2b_alt_quadratic_rosen_interval.py\`, \`verification/v2b_alt_quadratic_policy_interval.py\` | Nonlinear φ=x² one-witness all-g claims, NOT same-g φ=x comparison or arbitrary functional forms |
| Rational welfare | \`verification/v2b_stage06_pareto_holdout.py\` | Strict pointwise endogenous IS(.05)>SW for φ=x, not first-best or implementability |
| Lean formal core | \`formal/V2bWelfareCore.lean\` | Four comparisons at rational **proxy** designs, not at provably true Nash roots in Lean |
| Bibliography | \`paper/references.bib\` | Starter entries from original-source audit; Stage10 must verify publication versions and natural in-text attribution |

CI: \`.github/workflows/stage09-reproducibility.yml\`; frozen file modifications fail the read-only source-integrity check and require economic change control, NOT updating the manifest by convenience. Existing Stage4A/Lean CI retain their own history.

### Failure handling
- Solver nonconvergence ≠ government no-agreement. CI must FAIL on unresolved interval bounds.
- \`git\` blob SHA-1 integrity check guards **changes from the frozen content snapshot**; it is not a security authenticator for an untrusted GitHub admin.
- Python version pins are **exact package versions**, not a full transitive/OS or cryptographically hash-locked environment. Record \`pip freeze\`, workflow URL/SHA and runner information before final submission.
- Lean4 source uses \`decide +kernel\` but encodes pointwise fractions, and output status should never be promoted to a full-model theorem.
- Original pre-registered φ=x² frozen C entry at g=.05 remains **FAIL**; φ=x² existential feasibility instead at g=.005 has a ~9.1e-7 positive margin.
- The original published Gandal–Shy PDF supplied privately is intentionally not redistributed; no license to commit it is assumed.

### From Stage9 to Stage10

\`paper/sections/*.tex\` contain explicit editorial placeholders; Stage10 must replace them following model → equilibrium → main results → welfare → robustness → related results → discussion/intro while independently checking readable bridge equations, exact theorem assumptions and publication metadata. No author names, affiliations or journal-specific formatting are invented in this scaffold.

**Old repo archives:** \`docs/MODEL_SPECIFICATION.md\`, \`docs/EQUILIBRIUM_LEDGER.md\`, \`verification/symbolic_audit.py\` are V1 and MUST NOT be used as certification for frozen V2b.
