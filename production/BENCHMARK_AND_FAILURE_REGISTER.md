# Stage9 benchmark, failure and regression ledger
**Authoritative version:** V2B-THEORY-FREEZE-2026-10-21-v1. Entries are fixed baseline facts for reproducibility, not new research findings.

## Counterfactual definitions (never conflate)

| ID | Regime | Meaning and valid comparison |
|---|---|---|
| B0 SW | All technical H_ij=0 off-diagonal, residual substitution X retained | Real on-path substantive outcome at θ0 with firms choosing x |
| B1 SU(AB,g) | H_AB=g, C outside, firms reoptimize | Off-path continuation at g>0 in the original government game, still needed for veto and welfare |
| B2 IS(ABC,g) | All cross H_ij=g, firms reoptimize | Off-path/hypothetical positive g given Stage1–3 sequential consent; not government SPNE |
| B3 frozen SW design | Every x_i fixed at unique x^SW* after **every** government history | Restricted-strategy alternate GAME; cannot describe as actual original-firm Nash |
| B4 hypothetical direct ABC offer | Simultaneous unanimity on IS(g=.05) or fallback SW | **Different** institutional agenda; not a feasible deviation in original A/B-first game |
| B5 nonlinear φ=x² | Only X changes to (x_i²+x_j²)/2, unchanged θ0 and country game | Pre-registered single functional-form diagnostic, not canonical V2b |

## Regression checks (PASS means exactly described scope)

- Frozen source IDs are immutable per production/freeze_manifest.json. The make freeze target checks all 9 pinned Git blobs.
- p=1 SW national W≈2.422078421718, SU(.05) A W≈2.421604947547, C W≈2.440259596858, IS(.05) W≈2.439013049624; world IS(.05)>SU(.05)>SW. The make table target recalculates and compares against those anchors.
- p=1 all g>0 endogenous SU member <SW and C outside SU>IS via Stage4A Krawczyk certificate, not a finite sample.
- p=1 frozen design some positive-depth IS g=.05 beats EVERY SU proposal and SW (full SU envelope).
- p=2 Stage4 full 3x3 asymmetric Rosen over x∈[0,1]^3 and all g; p=2 Stage4A all-g implicit government derivatives negative.
- p=2 original *pre-registered identical g=.05* frozen C acceptance: **FAIL** (gain ≈−0.000440395). Must remain visible even though existential different-depth test passed.
- p=2 *g=.005 frozen C acceptance*: tiny strict positive ≈9.1×10⁻⁷; Stage4A rational interval proof and Lean **proxy** welfare sign.
- p=1/p=2 hypothetical endogenous IS(.05) Pareto beats SW. Does **not** imply efficient implementable government policy.
- Lean pointwise arithmetic uses source-declared xSWproxy, xISproxy; Lean does **not** prove that those rationals equal Nash roots.
- V1 z_i≥g, product homogeneity mixed with standards: REJECTED for current paper, retained only in archival docs.

## Failed or limited experiments are part of the record

1. Original p=2 φ=x² fixed-depth g=.05 C participation -> **FAILED**; changing witness g after exploration does not reclassify the preregistered fixed-g outcome.
2. Earlier original proof CI run with a name typo -> FAILED, subsequent exact source fix and CI rerun -> PASS; history retained.
3. First Lean run with plain by decide hit kernel reduction limits -> FAILED, switched to decide +kernel, existing four theorems unchanged; clean CI PASS.
4. V2a product-multiplicative heterogeneity had multi-Nash risk; not V2b portability evidence.
5. Real-world A/B/C historical veto from ChaoJi or GSM not established. Those cases are institutional motivation, not theorem verification.
6. Published Cabral–Salant theorem full text and Baake–Boom original coverage remain incomplete; source access does not imply academic originality.

## Change control
Failure to reproduce a certified numerical interval, hidden NaN, missing proof evidence, source drift, or a new original theorem that directly absorbs the result means **gate re-open**, not silently modifying costs, interpolation powers, government agenda, parameter bounds or manifest.
