# Stage 13 — Full-Paper Integration / Exposition Streamlining Gate
**Date:** 2026-10-21 JST. **Workflow:** research-paper-workflow v2.9.  
**Manuscript:** *International Standards Coalitions and Endogenous Product Design*  
**Primary target:** *Review of Industrial Organization* original research article (Stage12 provisional).  
**Theory authority:** `V2B-THEORY-FREEZE-2026-10-21-v1`, exact witness `(1,379/500,9/10,1701/2000)`.  
**Final assessment: CONDITIONAL GO to Stage14 submission-QA preparation, not publication/submission GO.** Manuscript/exposition integration passes its mechanical and internal-consistency criteria. Exact-proposition full reading of Cheng–Huang (2025) and author/portal approvals remain open as explicit blockers.

## 1. Stage11/12 first-order changes and results

1. **Source comparison was prioritized before editing:** see `literature/V2B_STAGE13_CHENG_HUANG_ABSORPTION_2026-10-21.md`. Cheng–Huang 2025 establishes endogenous quality, firm compatibility veto, incompatibility under network effects, and compatibility welfare gains. Direct government A/B-first, C application/inherited g and *frozen-government-forecast reversal* are not observed in the publisher preview; complete main propositions still **UNAVAILABLE / UNRESOLVED**. The published Appendix 2 text was partially inspectable, including the firm veto/no-veto deviation comparison. We do **not** assert exhaustive source absorption PASS. Buccella–Fanti–Gori 2024 quality/compatibility work was added and the existence of its 2026 corrigendum logged; corrigendum theorem content not silently assumed.
2. **Source-scoped contribution framed without inflation:** no priority for endogenous quality, firm veto, inefficient incompatibility, regional outsider obstruction, standardization/investment tension or coalition solution method. Specific retained result is an *institution-dependent national participation forecast reversal* when private post-commitment residual design is reoptimized versus frozen at SW.
3. **Deterministically generated same-depth comparison:** `production/scripts/generate_consent_table.py` at canonical `g=1/20`; `make table` generates `paper/generated/consent_table.tex`; `make table-check` reruns exact regression anchors and relative sign checks. Its three columns represent `m-s`, `i-o`, `i-s` with both endogenous and frozen SW design choices. Numeric source is *floating point with Stage4A anchors*, not a new all-g certificate.
4. **Global Nash proof made reader-checkable:** `paper/sections/A_proofs.tex` derives norm bounds `||M^-1||∞≤1/.758`, `||q||∞≤1/1.242`, first/second derivatives of Cournot quantities, resulting operating-profit Hessian <0.203092 and strict Rosen margin >0.2412 for all asymmetric designs. Section `02_equilibrium.tex` links this to Rosen before invoking interval root inclusion. This is an exposition-level analytic derivation at frozen theta, **not** a new general theorem or new model.
5. **RIA-facing discussion and disclosures:** a testable **conditional diagnostic** identifies what observed negotiated depth, residual product design and outsider opportunity must be measured; no claim of empirical validation. A clear computation/AI-assisted research paragraph states use and the limits of Lean/interval certification. Author-specific facts are explicitly pending in `journal/STAGE13_AUTHOR_DECLARATIONS_PENDING_2026-10-21.md`.

## 2. Section-purity / content role audit

| Component | Dominant role | Necessity | Integrator finding |
|---|---|---|---|
| Abstract and Introduction | Economic question, strict result, prior boundary, reader map | CORE | Opens directly on missing international agreement despite Pareto welfare, identifies AB-first/frozen-vs-endogenous forecast; no novelty for firm veto |
| Model | Five stage government/firm Cournot game, utility/matrices/costs/welfare, tie and SW benchmark | CORE | Primitives consolidated, inherited-g at C application explicit; no spurious $x_i\ge g$ |
| Market/design equilibrium | $Mq=1$, FOCs, global full-design uniqueness | CORE | Key unilateral $q_{x_i}$ bridge and analytic Rosen appendix retained |
| Main results | All-g government veto proposition and frozen-design counterfactual, backward induction | CORE | New one-table canonical comparison reduces reader search; all-g proof remains certified program |
| Welfare | Conditional IS Pareto gain, government CS/export-rent decomposition, original welfare table | CORE | Distinguishes conditional allocation from realized political outcome |
| Nonlinear robustness | Precisely phi=x² existential portability plus *failed* same g=.05 consent | CORE (one bounded subsection) | Negative preregistered result retained; no new p interval or functions |
| Relation to Existing Theory | Concept clusters: government SU/outsiders; private firm compatibility/quality; timing and national forecast | CORE | Cheng–Huang and Buccella included, strong Takarada–Kawabata overlap given substance; source limit stated |
| Discussion | Institution mapping, falsifiability, policy vs feasible treaty distinction, formal/AI scope | HELPFUL | Does not silently claim ISO voting, GSM/ChaoJi historical veto, implementation or economic calibration |
| Conclusion | Answer only | CORE | No new theorem/policy beyond closed scope |
| Proof appendix | SU/IS algebra, norm bound, rational-policy root enclosure, nonlinear and Lean trust boundary | APPENDIX | Necessary for specialist verifiability; long implementation algebra kept in code |

### Main-text necessity choices
**Keep CORE:** two controlled government proposition statements, exact theta, all-depth quantifiers, proof-critical derivative bridge, same-g positive/negative national participation comparison, Pareto gain, failed nonlinear same-depth g test, source limitations.  
**Keep HELPFUL:** short actual-application diagnostic and funding/AI transparency context.  
**APPENDIX:** analytical Rosen Hessian bound, SU inverse, polynomial root enclosure and program mapping.  
**DELETE/REPLACE:** previous author-by-author related-work repetitions, unproved “standard bound” reference, narrow-reader-cost numerical inline interval with overflow, overly long code filenames in a prose run.  
**No theorem weakened by deletion or content moved across freeze.**

## 3. Actual manuscript reader-arrival audit

**Observed on Stage13 integrated branch CI SHA `ecedfe57c8a9f40053cc8c7dc46f394e9741a5f7`**: [Stage10 manuscript workflow run 39556013651](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39556013651), source-consistency PASS + reviewer PDF PASS, **15 physical pages**, no Overfull hbox. Source order and final LaTeX pass indicate the following **approximate printed page entrances**, not universal journal limits: Introduction pp1–2; Model pp2–3; Equilibrium p4; Main Results p5 (consent table around pp6–7); Welfare p7; Nonlinear Robustness p8; Closest Literature pp9–10; Discussion p11; Appendix from p12; references from p14. These are final LaTeX process page-flush diagnostics; a precise printed-page-header mapping should be checked visually again in Stage14 generated PDF.

**Arrival criterion:** question and main claim on opening page, all game primitives by p3, first government result by p5, quantitative consent contrast near its paired propositions, broad literature only after theorem/welfare arguments. This meets the paper's theory-first Stage10 exposition targets. No costly literature review precedes the mechanism.

## 4. Five-exhibit / scarcity audit

The manuscript uses **only two numerical tables** and no decorative figure:
1. **Consent margins at common g=.05**, generated, essential: frozen vs endogenous A/B and C participation signs with off-path IS gain; point illustration only.
2. **Conditional SW/SU/IS consumer and world welfare**, generated, essential: shows why local national blocking and Pareto-positive global compatibility can coexist.

The two headline propositions and the bounded nonlinear result supply the other essential exhibit *functions* without needing separately plotted pictures. A full timing diagram could shorten prose but adds little beyond the five-stage model paragraph, so **no figure added**. Welfare-vs-g grid plot excluded because it may falsely suggest a finite sample proves the all-g theorem. No second nonlinear table because the ~9.1e-7 positive acceptance margin and failed same-depth -0.000440395 are already precisely stated.

## 5. Compression-without-damage verification

- **Quantifiers:** `forall g in (0,1]` only in theta0 and the named two functions; separate g=.05 baseline, g=.005 nonlinear frozen.
- **Identity:** true design Nash and frozen restricted-strategy game distinguished in title/text/table.
- **Welfare:** conditional endogenous IS(.05) beats SW for every country; does *not* assert first best, governmental SPNE, or that IS Pareto beats every SU country allocation.
- **Network demand:** $B=\rho H+(1-\rho)X$, $M=I+B-\eta H$, expected use held fixed during Cournot deviations, CS=$q'Bq/2$.
- **Firm profit:** three markets' operating $3q_i^2$ and single $κ(1-x_i)^2/2$ expenditure.
- **Proof bridges:** firm unilateral matrix derivative; total government $W_g+W_xx'$; all-g rational policy intervals; numerical sample not proof; Rosen analytic inverse bound.
- **Prior art:** CH published article visible material and uninspected propositions carefully separated; GS non-SU can mean mutual recognition unlike V2b SW.
- **Machine formalization:** Lean only four rational proxy comparisons, not Nash/SPNE; SymPy/mpmath trust remains visible.
- **Negative findings:** original preregistered p2 frozen C entry at g=.05 remains negative.
- **Substantive Stage8 model files:** not edited (9-blobs protected by CI).
- **Citation and label QA:** deterministic Stage10 source checker PASS including `app:rosen-bound` and generated table label; BibTeX succeeds with new citations, no unresolved final PDF references.
- **Typesetting:** 15-page initial `article` layout; no Overfull hbox in final run; bibliography links can show underfull lines (harmless layout defect to inspect at Stage14).

## 6. RIO requirements integration and remaining substantive blockers

**Integrated:** English abstract within the provisional 150–250 range, five keywords and preliminary JEL categories, regenerated reproducible tables, separately mapped prior citations, AI/proof-scope paragraph, versioned reproducibility programs.

**Unverified / author action:** exact journal-specific anonymity model and title page designation; names/affiliations/corresponding author/ORCID; actual funding/competing-interest/contribution attestations; data/code availability wording and published deposit release; current full Springer requirements and authenticated portal file/figure classification; source archive and LaTeX class, cover letter, fees, preprints, system-generated PDF details. See `journal/STAGE13_AUTHOR_DECLARATIONS_PENDING_2026-10-21.md` and Stage12 RIO ledger. Do not invent these fields or declare submission-ready.

**Material novelty blocker:** Complete Cheng–Huang 2025 main-text Propositions 1–4, including their generality/timing restrictions, not obtained. The accessible abstract and Appendix2 prove firm veto and endogenous quality are known but do not certify the precise V2b government forecast chain absent. This must remain **PRIORITY_UNRESOLVED** until full-text examination or explicit editorial risk acceptance; by Stage14 fail-closed policy, unresolved material novelty means **NO SUBMIT**, and source-identified absorption triggers rollback to Stage6 / Stage11, not cosmetic exposition.

**Additional bibliography due diligence:** Buccella et al. 2024 has 2026 published corrigendum; if any corrected proposition is relied upon, examine corrigendum; no such proposition is invoked as theorem here.

## 7. CI/reproducibility evidence and change control

- Base source is Stage12 branch; changed only `paper/main.tex`, selected sections, `paper/references.bib`, Makefile and production check/generator scripts, plus Stage13 scholarly audit and journal metadata files.
- **No changes** to the Stage8 nine-blob frozen manifest objects or corresponding files.
- The initial intermediate Stage13 commits generated source-check failures because the table and appendix labels were not yet registered; static QA was extended. A short-lived erroneous section-file interchange during overfull-line remediation was immediately restored from the previous verified commit before final CI. Preserve Git history rather than rewriting incidents as clean first-pass success.
- CI run `39556013651` at `ecedfe57c8a9f40053cc8c7dc46f394e9741a5f7`: Stage8 freeze verification PASS; generated welfare table + new consent table WRITE/CHECK PASS; manuscript citation/crossref QA PASS; LaTeX/BibTeX reviewer PDF **15 pages PASS**; final log no overfull; earlier incomplete commit failures not erased. Later Stage13 documentation-only additions contain no manuscript code or frozen source edits.
- This is not a second cleanroom proof of the full continuous policy function; prior full Stage4A interval certification remains the mathematical source. Numeric table computation is illustrative.

## 8. Stage13 verdict and Stage14 contract

**Verdict: CONDITIONAL GO — manuscript integrated and printable; NOT SUBMISSION READY.** Stage14 may begin its policy/portal/package QA, but it cannot assign `SUBMISSION QA PASS` until the material primary-text overlap question, author attestation and portal requirements are closed.

**Stage14 actions (in order):**
1. Obtain complete published Cheng–Huang 2025 and reproduce theorem-level primitive/timing/veto/frozen-design absorption map. If exact/main theorem absorption found, rollback Stage6/11; otherwise evidence-grade closure.
2. Verify/update RIO guide and authenticated review/anonymity file designation rules; prepare correct title page/main file and author-reviewed declaration texts.
3. Clean source archive containing all LaTeX sections/BibTeX/generated tables and required class/assets, exclude internal private documents, recompile from clean extraction, verify portal-created PDF page-by-page.
4. Rebuild and timestamp unchanged frozen Stage8 certificate and generation logs; provide reproducible interval output digest / exact verification commands.
5. Secure actual human author approval of theorem, source comparisons, bibliography, AI disclosure, statements and final submission commit; without this do not submit.

**Do not add a new economic theorem, tweak theta/g to improve rhetoric, or silently claim stronger generality just to satisfy the first-choice RIO outlet.**