# Stage 13R-M — Economic Significance, Motivation and Scope QA

## 2026-10-23 Stage13R-M Table 1 placement correction — FINAL PASS

An independent PDF review identified a pre-existing float-order defect: `Table 1` (`tab:map`) was inserted at the top of page 10 between the words “a finite cover then establish” (page 9) and “the asserted nonempty open neighborhood” (page 10), splitting the final sentence of the proof of Theorem 4. This flaw predates Stage13R-M and was missed in prior layout QA.

**Minimal source fix:** Change only the `tab:map` float header from `\\begin{table}[tbp]` to `\\begin{table}[H]` in `manuscript/stage13rl_jpet_revised.tex`. All Table 1 values and text, theorem/proof text, mathematical environments, figures, bibliography and the economic-significance revision remain identical. Source edit commit `d0b742f01212418ace3c6b49f399c559f6d8a4d3`. The editorial QA script was tightened to require exactly this Table 1 `[H]` float and normalize **only that exact table header** while comparing the otherwise unchanged full source against PR #33's fixed input; script update `79cc21a295dbe019ac1af1ab5a17c51fb479b59e`.

**Successful dedicated rebuild and artifact QA:** GitHub Actions run [`39882473382`](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39882473382), all steps SUCCESS (source-level exclusions, bibliography, latexmk, log diagnostics, PDF artifact publication, isolated-branch PDF commit). The superseded intermediate run `39882467176` failed as expected under the older QA script before its one-position exception was added; it is **not** the final verification run.

**Current authoritative PDF after this fix:** `manuscript/stage13rl_jpet_revised.pdf` on PR #34, **22 pages**, **574,053 bytes**, **complete Git Blob SHA-1 `943d27b473fdf8039cb3d410a1d59aae4d6443af`**, SHA-256 of raw PDF `1707e4699228c86f4b58fbf494c7175b39900821e91faf5c8ae4f6a51af28468`. Workflow ZIP artifact `12470973368`, archived ZIP sha256 `10948f7fd9a4a58d57f1a8bf92bfe0529ce5f41a2540b6ed01a1d9661ab65cd7`. Actual extracted artifact PDF and GitHub committed PDF have the same full SHA-1 Git blob and exact byte size. The old PR #34 PDF also happened to have **574,053 bytes** but had a **different SHA** (`15778b46f8ca6f466b4a81cdaf2a4ffe17bedbbe`); that binary is historical and must not be distributed as the new PDF.

**Image and text-order inspection:** Full page images of pages 9–11 checked, with page 10 text order independently inspected using `pdftotext -layout`. Theorem 4's proof continues at top of page 10, **finishes before the explanatory Table 1 lead-in paragraph and Table 1 itself**. The end of the proof still spans the ordinary page 9–10 boundary, but **no table interrupts the proof or its sentence**. Table 1 and Table 2 now appear on page 10 after the proof. Zero unresolved/multiply-defined citations/references or Overfull hbox found in exact compiled log. Page count is unchanged. The prior Theorem 4 heading, Table 2 and Table 3 placement safeguards remain unaffected.

**Conclusion:** The sole Table 1 float-placement regression is corrected. Previous editorial and scientific invariance checks continue to PASS. PR remains Draft, unmerged and unsubmitted. Stage13R-M editorial/layout gate PASS; Stage14 author/archival/portal/submission gates remain distinct.



**Date:** 2026-10-23 JST. **Decision:** PASS — bounded editorial significance revision and production QA; **NOT** paper submission, new theoretical results, empirical validation or novelty certification.

## Source lineage and isolated workflow
- Repository: `ryotamatsuki/standards-coalitions-differentiation-cournot`.
- Baseline Stage13R-L **Draft PR #33**, immutable input HEAD `51f5494d616167894e351cd226aadc8f9036cdf8`.
- New **Draft PR #34**, base `literature/stage13rl-reference-integration-20261023`, head `editorial/stage13rm-economic-significance-20261023`. The edit did not mutate PR #33, PR #32, or main, and no merge/submission was made.
- Canonical files edited in place within the new branch: `manuscript/stage13rl_jpet_revised.tex` and its newly compiled `manuscript/stage13rl_jpet_revised.pdf`. No second paper filename.
- Editorial source commit: `09cf738c3b3d9d200650501f2cd98a73fbfc2ad7`. Stage13RM QA-script commit: `b88d9ab75808683dff0e2dadfa6017f60f4b625b`. CI-workflow source commit: `f23b83fb10b11fd27413f39a59b1b242a9c92099`. GitHub Actions PDF-only commit: `e540b1ec2d8fca8ba3ba6c5ffdcf7c3b025c8b6a`. These source and binary commits precede addition of QA prose records.

## Adopted economic-significance message
In an economy where firms **can** reoptimize post-policy residual product designs, omitting that available response from a fixed-design assessment can change the **predicted implemented agreement**, not only the predicted national welfare gain from a proposed standard. In the **same** inherited-depth bilateral-first government game, the fixed-design counterfactual supports approved proposer-optimal integration, while endogenous-design Nash yields fragmentation at all positive depths on the certified benchmark and a nonempty open primitive neighborhood. Governments in each model correctly anticipate the relevant firm continuation; **no governmental misbelief or information failure is modeled**.

The welfare channel is specific: firm own-profit design optimality cancels only the firm's own-design own-profit first-order term, leaving domestic consumer-surplus incidence and resident worldwide-profit effects of rivals' redesign. The national loss can reverse the bilateral-member stand-alone incentive and the outsider's accession incentive. A direct-grand offer changes the relevant rejection alternative, not the baseline government's endogenous choice of negotiation institutions. The ex post bilateral path is **not** falsely described as having actually formed before failing enlargement; C's anticipated refusal causes B to reject at the earlier stage.

## Exact original/new English and rationale

### E1. Introduction — implemented agreement and economic significance

**Original (PR #33):**

```tex
The main result concerns the implemented agreement, not just a marginal derivative. On a nonempty open neighborhood of the benchmark primitives, the fixed-design counterfactual supports a government-optimal integrated agreement, whereas endogenous design yields fragmentation at every positive depth under bilateral-first accession. A direct integrated proposal nevertheless improves every country's welfare. The two routes impose different rejection options: an entrant to an existing bilateral standard compares integration with that bilateral standard, whereas a direct multilateral proposal is compared with fragmentation.
```

**Revised (PR #34):**

```tex
The main result concerns the implemented agreement, not just a marginal derivative. On a nonempty open neighborhood of the benchmark primitives, the fixed-design counterfactual supports a government-optimal integrated agreement, whereas endogenous design yields fragmentation at every positive depth under the \emph{same} bilateral-first accession procedure. This is a qualitative difference in predicted agreement formation, not merely in the predicted welfare gains from a given standard. When firms can reoptimize, an assessment that holds residual designs at their no-agreement levels can predict integration where the endogenous-design game instead implements fragmentation. The all-depth result rules out restoring agreement simply by changing the inherited depth. Yet a direct integrated proposal can improve every country's welfare relative to fragmentation. An entrant to an existing bilateral standard compares integration with remaining outside that standard, whereas a direct multilateral proposal is evaluated against fragmentation.
```

**Why:** Replaces a result-only paragraph with the qualitative consequence for analytical predictions; explicitly conditions omission on firms' ability to redesign, retains same protocol, all-depth/open-neighborhood and distinct rejection options.

### E2. Introduction — national incidence mechanism

**Original (PR #33):**

```tex
Private design optimality cancels the derivative of a firm's own profit with respect to its own design, but not the effects on domestic consumers or the resident firm's profits from rivals' designs. These effects can outweigh the fixed-design gain. Three-country symmetry links the member's stand-alone welfare derivative to the outsider's accession derivative; the all-depth theorem then excludes simply selecting a different inherited depth.
```

**Revised (PR #34):**

```tex
Private design optimality cancels the derivative of a firm's own profit with respect to its own design, but not the effects on domestic consumers or the resident firm's profits from rivals' designs. These national-welfare effects can exceed the fixed-design gain. Three-country symmetry then links the resulting reversal of the member's stand-alone bilateral consent margin to a reversal of the outsider's accession margin.
```

**Why:** Retains the existing D−L equation unchanged; removes repeated all-depth statement and explicitly connects domestic consumers/rivals' profits to two consent margins.

### E3. Related Literature — government standards and outsiders

**Original (PR #33):**

```tex
\section{Relationship to the literature and interpretation}\label{sec:literature}
International compatibility standards and their institutional consequences have an established literature. \citet{GandalShy2001} and \citet{Klimenko2009} study international compatibility with network effects; \citet{Costinot2008} examines alternative rules for international product standards. \citet{BarrettYang2001} show that nonconformity with an international standard can be rational. In government-cooperation settings, \citet{Takarada2020}, \citet{Kawabata2021}, and the mutual-recognition discussion paper of \citet{TakaradaKawabata2025} demonstrate why regional arrangements and an outsider's welfare can impede wider agreement. Those obstructions are not new. Our question is whether \emph{post-policy private design adjustment}, with the government's proposal and voting rules held fixed, changes the national consent conditions that determine the outcome.
```

**Revised (PR #34):**

```tex
\section{Relationship to the literature and interpretation}\label{sec:literature}
International compatibility standards and their institutional consequences have an established literature. \citet{GandalShy2001} and \citet{Klimenko2009} study international compatibility with network effects; \citet{Costinot2008} examines alternative rules for international product standards. \citet{BarrettYang2001} show that nonconformity with an international standard can be rational. In government-cooperation settings, \citet{Takarada2020}, \citet{Kawabata2021}, and the mutual-recognition discussion paper of \citet{TakaradaKawabata2025} demonstrate why regional arrangements and an outsider's welfare can impede wider agreement. These studies already establish that cooperation can be obstructed and that outsiders' welfare matters. Our comparison instead asks whether allowing \emph{post-policy private redesign}, rather than fixing firms' no-agreement designs, changes agreement formation while the government proposal, inherited-depth and voting rules remain identical.
```

**Why:** Credits existing explanations of blocked cooperation; sharpens fixed-vs-endogenous prediction under identical agenda/ballots without implying entire phenomenon is novel.

### E4. Related Literature — firm coalitions and attribute choice

**Original (PR #33):**

```tex
Private standard coalitions and attribute choices are also established objects of network economics. \citet{EconomidesFlyer1998} analyze firms' technical-standards coalitions under opposing network benefits and product-market competition. \citet{BaakeBoom2001} distinguish intrinsic product quality from compatibility decisions, while \citet{Buccella2023} and \citet{Cheng2025} examine firm-level compatibility and quality incentives, including veto behavior. The distinction between attributes and compatibility is therefore not itself our contribution. In our game, a government's welfare includes domestic consumers and its resident firm's profits across markets; a firm's subsequent residual-design Nash response changes the payoffs associated with both the member's bilateral outside option and the outsider's accession vote.
```

**Revised (PR #34):**

```tex
Private standard coalitions and attribute choices are also established objects of network economics. \citet{EconomidesFlyer1998} analyze firms' technical-standards coalitions under opposing network benefits and product-market competition. \citet{BaakeBoom2001} distinguish intrinsic product quality from compatibility decisions, while \citet{Buccella2023} and \citet{Cheng2025} examine firm-level compatibility and quality incentives, including veto behavior. The distinction between attributes and compatibility is therefore not itself our contribution. We trace the firms' subsequent design Nash response through domestic consumer surplus and the resident firm's profits across markets into two distinct national consent margins: the bilateral member's stand-alone gain and the outsider's incentive to accede. A firm's own-profit design condition does not eliminate these national effects.
```

**Why:** Connects private design Nash to consumer surplus, resident worldwide profit and the two national consent constraints instead of a mere actor distinction.

### E5. Related Literature — investments and controlled novelty boundary

**Original (PR #33):**

```tex
Standards and regulatory choices can induce other private responses. \citet{CabralSalant2014} examine standards regulation and private R\&D incentives; \citet{LambertiniRossini1998} study endogenous common standards alongside technology and quality choices in a 1998 working paper. \citet{Grossman2021} analyzes international regulatory cooperation when firms choose product characteristics. Thus neither endogenous product attributes nor the possible conflict between private investment and standards policy originates here. \citet{BranderSpencer2015} provide the related strategic-trade treatment of costly horizontal differentiation, and \citet{ZhouSpencerVertinsky2002} study trade policy with endogenous quality and export-profit consequences. Against these precedents, our narrower result traces residual redesign through domestic consumer surplus and the resident firm's worldwide earnings into \emph{national accession and bilateral-member consent}, and establishes a frozen-versus-endogenous government-optimal reversal at a certified parameter benchmark and within its open neighborhood. The direct-grand comparison isolates its dependence on inherited-depth accession, not a universal barrier to multilateral cooperation.
```

**Revised (PR #34):**

```tex
Standards and regulatory choices can induce other private responses. \citet{CabralSalant2014} examine standards regulation and private R\&D incentives; \citet{LambertiniRossini1998} study endogenous common standards alongside technology and quality choices in a 1998 working paper. \citet{Grossman2021} analyzes international regulatory cooperation when firms choose product characteristics. Thus neither endogenous product attributes nor the possible conflict between private investment and standards policy originates here. \citet{BranderSpencer2015} provide the related strategic-trade treatment of costly horizontal differentiation, and \citet{ZhouSpencerVertinsky2002} study trade policy with endogenous quality and export-profit consequences. Relative to these precedents, the controlled contribution is a reversal of the \emph{implemented agreement} when an available private-design response is omitted from an otherwise identical government procedure. At the certified benchmark and in a nonempty open neighborhood, the reversal survives the entire positive-depth menu, not merely a marginal comparison. The direct-grand counterfactual makes the role of the entrant's rejection option explicit; it does not establish a universal failure of multilateral cooperation.
```

**Why:** Preserves all literature and limits claims to all-depth certified benchmark/open set and a counterfactual direct-grand comparison; avoids overclaiming global universality.

### E6. Conclusion — analytical lesson and empirical boundary

**Original (PR #33):**

```tex
\section{Conclusion}
Governments' willingness to coordinate compatibility can depend on how firms redesign the product characteristics left outside an agreement. Private design optimality does not eliminate the effects on domestic consumers or the effects of rivals' designs on the resident firm's worldwide profits. These national effects can reverse the consent predicted by a fixed-design comparison.

On a nonempty open neighborhood of the benchmark primitives, fixed designs support a government-optimal integrated proposal, while endogenous design yields fragmentation throughout the positive-depth menu under inherited-depth bilateral accession. A direct integrated proposal can nevertheless improve every country's welfare. Evaluating compatibility therefore requires both a private-design continuation and a specified rejection option. The model does not select among unrestricted bargaining institutions or quantify actual agreement gains.
```

**Revised (PR #34):**

```tex
\section{Conclusion}
Ignoring an available post-policy private-design response can change the predicted formation of a compatibility agreement, not merely its predicted welfare gain. Firms optimize their own profits, but their residual redesign affects domestic consumers and the resident firm's worldwide earnings through rivals' choices. These national effects can reverse both the stand-alone bilateral-member gain and the outsider's incentive to accede.

At the benchmark and in a nonempty open primitive neighborhood, a fixed-design assessment supports government-optimal integration whereas endogenous design yields fragmentation at every positive depth under the \emph{same} inherited-depth bilateral-first procedure. Yet a direct integrated offer can improve every country relative to fragmentation, because the rejection alternatives differ. Predicting agreement formation in this setting therefore requires both firms' equilibrium continuation and governments' specified outside options. The model neither selects an optimal bargaining institution nor estimates real-world agreement gains; whether the mechanism is quantitatively important in particular industries remains an empirical question.
```

**Why:** Explains predictive implications and the rejection-option mechanism; distinguishes a theoretical equilibrium prediction from an empirical estimate and unrestricted-bargaining proof.

### E7. Version label only
- Original: `Stage 13R-L literature-integrated draft`.
- Revised: `Stage 13R-M economic-significance editorial revision`.
- Rationale: distinguish the new PDF/source from the historical original without multiplying main manuscript filenames.

## Consolidation / redundancies removed
- Removed a repeat of the full-depth claim after the D−L display in the Introduction; the earlier result paragraph now owns the all-depth implication.
- Related Literature now performs a distinct **literature-boundary** function and does not simply restate the Introduction's full mechanism.
- Conclusion carries the policy-assessment meaning without claiming actual governments are systematically mistaken or standardization is generally blocked.
- Abstract was untouched because it already accurately presents the mechanism and institutional limitation.

## Primary-institutional-source decision
No WTO/TBT source was newly cited. Existing `Simcoe2012` already gives a bounded real-world committee-process motivation; the WTO sources would add general institutional authority but no evidence of the present inherited-depth voting sequence or design-driven reversal. Existing 20 references are retained as chosen at Stage13R-L; unverified Maggi–Mrázová/Cheng–Huang full-text comparisons remain separate research questions.

## Six adversarial editorial checks
| Question | Result | Evidence in revised manuscript |
|---|---|---|
| Q1. Is firm adjustment changing results trivial? | **PASS within specified model** | Intro identifies **qualitative agreement formation** rather than only a welfare magnitude; the unchanged D−L mechanism and the two national consent margins explain the channel; Theorem 4 certifies the full depth menu. Not a claim of broad originality for endogenous behavior per se. |
| Q2. Why not agree if everyone beats fragmentation? | **PASS** | Revised Intro distinguishes outsider's bilateral rejection payoff from direct-grand fragmentation; Section 6 and Proposition 5 unchanged. |
| Q3. Why not choose another depth? | **PASS** | Intro expressly states all-depth failure and nonempty open neighborhood; Theorem 4 bounds both derivatives for all positive depths at the benchmark. |
| Q4. Is the conclusion protocol-dependent? | **PASS** | Explicit inherited-depth limitation; direct-grand offer is a **separate agenda counterfactual**, not a solved optimal bargaining institution. |
| Q5. Did we establish actual policy importance empirically? | **PASS** | Conclusion calls sector-specific quantitative importance an **empirical question**; illustration continues to call units uncalibrated. |
| Q6. How does this differ from the literature? | **PASS subject to earlier open prior-art issues** | All 20 citations retained; literature paragraphs contrast known firm/institution mechanisms with **controlled identical-procedure** change in national participation payoffs. No full general novelty certification asserted. |

## Exact scientific non-change, bibliography and workflow QA
- Dedicated `scripts/stage13rm_scope_qa.py` masks only the three permitted prose sections and revision label before comparing the entire remaining TeX with baseline `51f5494...` **byte for byte**. The Abstract, mathematical formulae, theorems, lemmas, propositions, proof blocks, tables, figures, policy/game definitions, full bibliography and all appendix source outside those sections are unchanged.
- `manuscript/stage13r_proof_supplement.tex` is byte-for-byte identical to the baseline, as verified by `git show`.
- The same QA rejects any changed repository files outside the canonical TeX/PDF, this editorial QA script, the isolated CI workflow and the two QA-report Markdown files. Thus scientific computation programs, figure source/PDFs, numerical data and Theory Freeze remain unchanged. The automatic repository PR-wide CI triggers are separate from this dedicated editorial test and do not imply scientific edits.
- All **20 existing bibliography entries** are alphabetized and unchanged; all 20 correspond to citations in the article or unchanged supplement. No unresolved/multiply defined citations, references, overfull lines or duplicate items observed.
- New workflow `.github/workflows/stage13rm-economic-significance-build.yml` triggers only on the editorial branch and commits only `manuscript/stage13rl_jpet_revised.pdf` to `editorial/stage13rm-economic-significance-20261023`, never to the parent PR #33 or main.
- Dedicated GitHub Actions run **39880887967**: https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39880887967. Every stage completed **SUCCESS**, including strict source-scope comparison, latexmk, log QA, artifact upload and branch PDF commit.

## PDF identity and direct page-image verification
- PDF: `manuscript/stage13rl_jpet_revised.pdf`, **22 pages** and **574,053 bytes**.
- Complete Git Blob SHA-1: **`15778b46f8ca6f466b4a81cdaf2a4ffe17bedbbe`**.
- Exact successful build ZIP: `stage13rm-economic-significance-pdf`, artifact **12470059131**, SHA256 `a1bd974d24e908ed90144dfaee1c7ad7c0e86f33d425ca64260a2d5982f52ffd`.
- The actual extracted CI PDF had 574,053 bytes and Git blob `15778b46...`, which equals GitHub's stored binary blob for the same path in PR #34 HEAD immediately after CI. **Byte identity PASS**; the old 572,923-byte/22-page PDF from PR #33 is historical, not this revision.
- Real PDF pages were rendered and visually inspected: **1–2** (Abstract and Introduction), **13–14** (complete Related Literature and Conclusion), **21–22** (complete bibliography), **9–10** (Theorem 4 and Table 2), **18–19** (certification and Table 3).
- Layout PASS: Theorem 4 heading and first substantive text remain together on page 9; Table 2 on page 10 precedes its full explanatory paragraph; Table 3 on page 19 does not split a displayed equation from its defining 'where' text. No overprints, clipped references, newly orphaned subsection headings or improper float movement detected.
- Figure PDFs unchanged: Figure 1 `9977c9a04ce0a59c5bcd561e855cc81322dd9d0a`; Figure 2 `44d631aaf5c3a02929370e065cd9672b3fa8a2ab`; Figure 3 `60da45c9356e540f2f0a304958bf25eb8f5ec6e2`. Figure 3 remains exploratory and not a proven global phase diagram.

## Remaining work, independently gated
1. Verify actual author identity/affiliation/contact/ORCID and the genuine funding, conflict, acknowledgments, research ethics and AI-assistance declarations; do not fabricate author inputs.
2. Publish an immutable version of the final replay source/data and record the public archive and exact paper/certificate commits.
3. Inspect current journal portal requirements and portal-generated review PDF and obtain express author approval before submission.
4. An inaccessible/updated prior-art full text or other uncompleted absorption comparison remains a distinct research/novelty issue, **not** resolved by editorial polishing.

**Stage13R-M gate: EDITORIAL AND PDF-QA PASS; submission gate still BLOCKED pending author and publication tasks.**
