# V2B-THEORY-FREEZE-2026-10-21-v2-CERT-REPAIR

**Type:** Stage 8 technical certificate reissue after Stage13 hostile proof audit; 2026-10-21 JST.  
**Parent freeze:** `V2B-THEORY-FREEZE-2026-10-21-v1`, preserved as an immutable historical Git blob and the archived Git commit.  
**Status:** **MATHEMATICAL PROOF REPAIR PASS at Stage4/4A; Stage7.5A continuation reassessed below; author journal/submission sign-off remains PENDING.** This is *not* a new theory-finding exercise and does not supersede the unresolved academic originality audit.

## Scope and rationale

Audit PR #4 identified **two certifier-implementation defects** in the *separately preregistered nonlinear design variant* phi(x)=x² only:
1. SymPy exact Rational was emitted as ordinary Python `p/q` before it touched an interval; Python binary64 rounding did not outwardly enclose the intended rational coefficient. The generated derivatives were also independently rounded. Consequently the old nominally PASS certificates could not be cited as exact for the frozen rational witness.
2. Gershgorin/Rosen row upper bound was computed via float endpoints and ordinary addition, not rigorous interval addition.

The **canonical phi=x economic model and canonical Stage4A certificate**, the 3-country governmental extensive form, payoff and cost definitions, parameter vector (1,379/500,9/10,1701/2000), all frozen findings, negative portability test and narrow institutional scope are **unchanged**. Proof software for the nonlinear variant is replaced only to restore soundness of original stated certification.

## Repaired arithmetic implementation

- New shared code `verification/v2b_exact_rational_interval.py` provides `interval_lambdify` using a custom SymPy PythonCodePrinter emitting every rational literal as `RAT(p,q)`. At runtime `RAT(p,q)=iv.mpf(p)/q`, including at intermediate common subexpression elimination nodes, so the coefficient encloses the true rational at the configured 40 decimal digits.
- `exact_interval` accepts only Fraction-coercible rational endpoints, constructs common-denominator integer intervals prior to mpmath's outward rounding, and refuses reversed intervals.
- A mandatory preflight checks coefficient enclosure for 71/500, 1/10, 621/500, 1701/2000, a composite rational, and reproduces the historical **non-intersection** between `iv.mpf(71/500)` and exact 71/500.
- Rosen Gershgorin computes `row=J_ii + sum_{j != i} abs((J_ij+J_ji)/2)` **entirely as interval arithmetic**; the upper endpoint is compared strictly to zero *before* float metrics are printed.
- Only numerical *root proposals*, trial preconditioners and display summaries use binary64; all definitive inclusion/signed-cell comparisons are interval-valued.

## Stage4/4A mathematical rerun

**Official code and recorded CI:** [GitHub Actions run 39571673076](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39571673076), both jobs SUCCESS, ref `repair/stage13-exact-interval-recertification-20261021` before manuscript/document additions.

- Full asymmetric `(x_A,x_B,x_C,g) in [0,1]^4` Rosen: SW 1 box, SU 1 box, IS 5 boxes / 4 splits, all strict upper rows negative. Worst IS upper `-0.09496342972119372`.
- Nonlinear SU root-face proof: `(u,v) in (0.60,0.67)x(0.60,0.65)`; IS scalar `y in (0.60,0.73)`, all `g in [0,1]`.
- Full nonlinear government derivatives: 100 exact closed g cells, 0 adaptive splits, member upper `-0.014278736686089652`, C accession-vs-outsider upper `-0.01657547425035518`.
- **Unchanged preregistered failure:** frozen nonlinear C accession at the originally specified `g=0.05` remains STRICTLY NEGATIVE `[-.0004403948341162623,-.0004403948309408524]`.
- **Existential alternate depth `g=.005`:** frozen C gain `[.00000090988090427044,.00000090988408551711]` strictly positive. International restricted-design offer beats SW and the entire 4,000-cell SU policy envelope.
- **Hypothetical endogenous IS `g=.05`:** per-country Pareto gain `[.016601146798306146,.016601147409436319]` >0.
- These reproduce the prior audit's exact shadow rerun, but are now reissued by **production proof scripts themselves**; both repaired scripts run in GitHub CI from the actual PR source.

## Stage7.5A portability re-review / negative results preserved

The two sampled functions are still phi=x (canonical) and phi=x² (nonlinear pre-registered functional diagnostic). Exact same parameter witness; nonlinear result is existential at **different depth**, not same-depth robustness. The failed original g=.05 frozen C test remains a failure, and the g=.005 advantage is ~9.1e-7, hence fragile. No certification for arbitrary phi, theta, bargaining institutions or country asymmetries. Claim class unchanged: **INSTITUTION-SPECIFIC** with bounded two-map existential support, **NOT GENERIC PORTABILITY**.

The corresponding previous Stage7.5A reasoning **does not change** because no game primitives, equilibria, signs or witnesses changed; its code-based support is now correctly bounded to the revised exact-interval certificates. The source-level priority issue Cheng–Huang (2025) and the editorial-significance question are **NOT resolved** by this technical fix.

## Stage8 freeze provenance, change control and trust boundary

Old freeze document `docs/V2B_THEORY_FREEZE_2026-10-21_v1.md` and its Git blob are **not edited**. This new document and `production/freeze_manifest.json` establish the successor *proof-certification* identity. All other seven old frozen blobs retain their original hashes. Two nonlinear proof scripts carry new hashes tracked in v2.

This is a ***technical recertification record***, not the author's final independent intellectual verification or a journal submission authorization. AI-assisted analysis and computer/CI validation are distinguishable from author sign-off. The trust base includes SymPy's expression printer and mpmath interval kernels; it is not Lean formal verification or a second independent interval library.

### Acceptance conditions and unresolved matters

- **Technical arithmetic validation:** PASS (run above).
- **New exact blob-protection via v2 manifest and make freeze:** recorded separately by successor CI, must PASS before integrating to protected branch.
- **Later Stage9/10/13 PDF/citation/bridge regression:** successor CI pending at document creation; cannot infer success.
- **Author certification of substantive manuscript and new documentation:** PENDING.
- **Stage6/13 source-absorption audit of Cheng–Huang (2025) full primary propositions:** UNRESOLVED, independent of correctness of computer-assisted proof.
- **Stage14:** BLOCKED until both the remaining scientific editorial issues and author-required declarations are closed.

### Provenance links

- Hostile audit PR #4: https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/pull/4
- Technical repair PR #5: https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/pull/5
- Two code changes are permanently visible in the staged Git branch and successor manifest.
