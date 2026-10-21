# V2b Stage 9 — Repository / Reproducibility Setup Gate
**Date:** 2026-10-21 JST. **Workflow:** research-paper-workflow v2.9, Stage 9.
**Canonical verdict: GO — REPRODUCIBLE PRODUCTION SCAFFOLD ESTABLISHED.** Next: Stage 10 section-by-section manuscript construction, **not** journal submission. No new or changed economic model, government stage, parameter or theorem is introduced here.

## A. Entry gate and no-model-change checks

- Stage8 frozen authoritative text: docs/V2B_THEORY_FREEZE_2026-10-21_v1.md, blob **ca16f0d4699364c7466d463c40e01cb5eaa2d8e5**.
- Frozen target: V2B-THEORY-FREEZE-2026-10-21-v1.
- Version guard: production/freeze_manifest.json enumerates **9 frozen Git blobs** (the V2b canonical freeze doc, Lean formal source, Lean toolchain pin, canonical and nonlinear firm/government certificates and welfare inputs). production/scripts/verify_freeze.py uses actual Git-object SHA-1 encoding from checked-out bytes; **PASS**. This guards accidental mutation; any intentional frozen-theory changes require Stage4A/7.5A impact re-audit and a NEW freeze.
- Historic V1 source docs docs/MODEL_SPECIFICATION.md and docs/EQUILIBRIUM_LEDGER.md were not modified into new math: they are explicitly labeled archival and excluded from the V2b production scaffold. The canonical research question remains an **INSTITUTION-SPECIFIC existential coalition-reversal result**.

## B. Delivered production components

| Component | Files | Coverage |
|---|---|---|
| Modular LaTeX skeleton | paper/main.tex, paper/sections/01_model.tex through 07_discussion.tex, paper/sections/A_proofs.tex | Compilable chapter architecture with **Stage10-pending editorial placeholders**, no invented manuscript argument |
| Initial original-source BibTeX | paper/references.bib | Gandal–Shy 2001, Cabral–Salant 2014, Buchholz–Hattori 2024, Takarada–Kawabata 2025 DP701, Rosen 1965; journal-vs-WP differences and remaining source checks disclosed |
| Reproducible welfare table | production/scripts/generate_welfare_table.py, generated paper/generated/welfare_table.tex (NOT committed; regenerated) | Executes frozen Stage7 independent welfare evaluator, rechecks specific numeric regression anchors and government/welfare rankings; explicitly labels SU/IS as conditional downstream outcomes, NOT on-path agreements |
| Frozen source guard | production/freeze_manifest.json, production/scripts/verify_freeze.py | Exact content matches 9 Stage8 source Git blobs |
| Python environment | production/requirements-stage9.txt | Python 3.12: numpy==2.2.6, scipy==1.15.3, sympy==1.13.3, mpmath==1.3.0. **Exact direct dependency pins**, NOT transitive/wheel hash locks |
| Make targets | Makefile | freeze, table, table-check, fast-proofs, full-proofs, lean, paper, clean; no automatic paper-theory edits |
| Formal proof | formal/V2bWelfareCore.lean, root lean-toolchain | Pinned Lean4 v4.24.0 and full original proof input unchanged; 4 rational-proxy strict welfare inequalities, **not** all-g Nash/SPNE Lean proof |
| Machine-check / CI | .github/workflows/stage09-reproducibility.yml | 5 jobs: freeze integrity, canonical math+table, nonlinear math, Lean4 kernel, LaTeX/BibTeX scaffold build |
| Audit map | production/THEOREM_CERTIFICATE_MAP.md | T1–T7 frozen propositions and limits linked to analytic, interval, numerical and Lean proof support |
| Benchmark/negative outcome registry | production/BENCHMARK_AND_FAILURE_REGISTER.md | SW/SU/IS, frozen x, hypothetical treaty, p=2 failed g=.05 test and successful g=.005 certified existence; prior CI failures preserved |
| User-facing runbook | production/README.md | Local setup, command line, per-result provenance, stage10 instructions and reproducibility limits |

## C. Github Actions independent reproduction

**Final passing run:** https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39524698485 . Source head commit at time of run: \`0ee946387d0139462262be2c9ae9b837a9824986\`.

| Job | Actual CI outcome | What it proves / does not prove |
|---|---|---|
| Verify Stage8 economic freeze | **PASS** | 9 frozen blobs unchanged |
| Baseline exact-witness mathematical checks | **PASS** | Independent Stage4A Krawczyk interval certificate, strict rational SW/IS Pareto and full country welfare evaluator, deterministic table match |
| Independent nonlinear design Nash and policy certificate | **PASS** | Separate full asymmetric design-game Rosen checker and continuous-g government interval proof for φ=x² |
| Lean kernel check — rational-proxy core only | **PASS** | Four arithmetic comparison statements for rational design proxies, no full Nash/SPNE formal theorem |
| Build Stage9 bibliography and PDF shell | **PASS** | Fresh Ubuntu apt TeXLive packages, fresh Python pinned env; latexmk/PDF and BibTeX build succeeds from the generated table |

CI build artifact named **v2b-stage09-scaffold-not-a-manuscript**, produced PDF about 242 kB compressed artifact and 7-day retention until 2026-10-28 JST ~10:01. To download use the GitHub Actions run Artifacts section. **Do not label this Stage9 shell as a substantive draft**; sections and abstract still contain editor placeholders.

**Negative CI regression preserved:** first Stage9 run https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39524532077 had 4 non-LaTeX jobs PASS and failed LaTeX for a generated \footnotesize token immediately joined to following text. production/scripts/generate_welfare_table.py was corrected by inserting whitespace after LaTeX \footnotesize; frozen theory and welfare numbers unchanged. Re-run 39524698485 passed all five jobs. No false PASS on the initial run. Other older Stage4A/Lean historical failed runs remain separately retained.

## D. Reproduction contract and residual limits

From repo root with Python 3.12, \`python3 -m pip install -r production/requirements-stage9.txt\` then \`make freeze\`, \`make table\`, \`make table-check\`, \`make fast-proofs\`; the global continuum audit is \`make full-proofs\`. For full PDF shell \`make paper\` after TeXLive/latexmk, and \`make lean\` after pinned Lean 4 installed. The CI is the latest executed reference. A full independent human mathematical proof and all-equilibrium Lean formalization are NOT claimed by build success.

Generality ceiling unchanged: exactly 2 specified φ design maps and one rational θ; all g policy in the **fixed A/B-first** institution; no arbitrary φ/negotiation or guaranteed journal novelty. The genuine failed nonlinear same-depth g=.05 pre-registered test remains FAIL. Original privately supplied Gandal–Shy full published PDF was **NOT** redistributed in public GitHub.

**PDF visual inspection:** automated TeX build, PDF nonempty check and complete BibTeX processing were successful; **no separate visual page-by-page human inspection is claimed at Stage9**. Page-by-page referee-oriented presentation will be reviewed after actual Stage10 prose replaces editorial placeholders.

## E. Next stage — Stage 10 only

Produce model, equilibrium, theorem propositions with exact quantifiers, proofs, welfare, robustness, institution bridge and related-literature exposition **directly from frozen Stage8 specification and theorem ↔ certificate map**. Before finalizing Introduction establish Stage10 Exposition Architecture and reviewer-verifiability map; no old V1 copy. Do NOT simply rewrite the original freeze to make prose appear nicer; theory changes trigger rollback. Do not invent author name/affiliation, appendix verification status, final journal or accepted disclosure policies.

**Stage9 GO recorded; Stage10 is next, NOT yet substantive manuscript done.**
