# Stage 11 — Materials, workflow application and provenance

Date: 2026-10-22 JST. Repository input SHA `1146745c548734370de190899ac43370649a3c29`. Workflow stable tag v2.9, commit `338677e9566e6bf63a455de81da4ac47153b4e69`. Audit-only branch: `audit/stage11-jpet-v04-20261022`, based on the specified manuscript branch. No edits to that branch, main, Theory Freeze or v0.4 source.

## Order and independence

1. Resolved the exact supplied ZIP, version 2, from Library and unpacked it. Local workspace did not contain a manuscript at task start.
2. Read complete v0.4 LaTeX before historical verdicts, proof ledgers, numerical code or prior-art audit records. Wrote `reviews/STAGE11_BLIND_FIRST_IMPRESSION.md` before opening those records.
3. Inspected the actual 17-page PDF and all named figures/tables/appendices/references; rendered every page for layout inspection.
4. Commissioned the four explicitly requested independent referee perspectives. They read the manuscript first, then relevant sources and code. Their evidence is reconciled by the root auditor, not counted as a majority vote.
5. Performed fresh symbolic matrix derivation, fresh numerical full-firm evaluation, historical rigorous source replays, source/data reconciliation and targeted phase-map attacks.

“Blind” means the historical detailed verdicts/proofs were not read before the first manuscript impression. The user request and visible conversation context were available; this was not a fully blinded experiment. Referee agents inherited that context and task instructions. Different AI instances are an independence measure for reasoning, **not external human review**. Replay of production certificate code is labeled replay; scripts independently derived from primitives are identified separately. No unperformed test is marked PASS.

## A. Manuscript materials secured

| Requested item | Access/result |
|---|---|
| Exact ZIP | `source_v04/stage25_jpet_v04_with_refined_phase.zip`, byte-preserved; SHA256 in INPUT_MANIFEST.json |
| Full v0.4 TeX | Read all model/theorem/proof/appendix/reference text; 58,513 bytes; byte-identical to tracked `manuscript/stage25_jpet_v04.tex` |
| Full PDF | Actual 17-page PDF, 485,409 bytes; byte-identical to tracked manuscript PDF; `pdfinfo` and Poppler render used |
| Figure 1 | Embedded TikZ in TeX and actual PDF p5; no separate image needed |
| Figure 2 | Embedded TikZ in TeX and actual PDF p7; no separate image needed |
| Figure 3 | Original vector PDF/PNG and page11; vector PDF byte-identical to tracked manuscript figure |
| Table 1 / Table 2 | TeX and actual PDF p10; numerical table independently checked at the center |
| All statements/proofs, Appendix A–D, references | Read; proof gaps distinguished from actual mathematical errors |
| SHA256SUMS.json / README.md | Archive entries preserved; independent hashes in INPUT_MANIFEST.json take precedence over unaudited descriptive claims |

The exact file list, sizes and SHA256 values for **all 13 archive entries** are enumerated individually in INPUT_MANIFEST.json. Full archive contents are retained, not reconstructed from GitHub summaries. GitHub had in fact synchronized the exact TeX/PDF/Figure3 by the input SHA, contrary to the older possible-unsynced warning; independent byte comparisons confirmed this.

## B. Proof and historical evidence

| Requested item | Actual access and limit |
|---|---|
| `reviews/STAGE22_ABC_PROPOSITIONS_AND_PROOFS.md` | Read; A/B/C scope and written open-neighborhood/continuity argument audited |
| `reviews/STAGE14_THEOREMS_AND_PROOFS.md` | Read; used as source index, not adopted verdict |
| Stage14 Krawczyk/Rosen code | Historical source `verification/v2b_stage04a_krawczyk_cleanroom.py` read and successfully replayed; independent full-cube proof additionally supplied |
| Named `canonical_global_rerun.log` / `pareto_rerun.log` | **Absent** in checkout; Stage14 source_manifest retains hash references. Original absent log bytes were not inspected. Fresh actual runs are separately named `canonical_global_replay.log` and `pareto_replay.log` |
| Stage21 network theorem | `reviews/STAGE21_NO_SU_MISSING_MIDDLE_THEOREM.md` and `verification/stage21_no_su_phase_theorem.py` inspected; exact-face executable replayed, restricted-strip written proof checked |
| Stage23 independent reconstruction | Source and `verification/stage23_local_reconstruction_log.json` inspected; not confused with all-g proof |
| Stage23 historical Actions rerun | Historical provenance read; **no new CI rerun commissioned or claimed** in this audit. Local interval replay is the new evidence |
| Stage24 literature/contribution audit | Eight-layer matrix and related source ledgers read after initial manuscript assessment; actual primary articles revisited selectively |
| Original nonlinear diagnostic / portability | Existing Stage7.5A certificate, negative same-depth p=2 record and formal scope map inspected; no new nonlinear or arbitrary-function theorem claimed |
| Lean certificate | `production/THEOREM_CERTIFICATE_MAP.md` scope inspected: rational proxy arithmetic only; full design Nash/all-depth government theorem not Lean-encoded. **No new Lean build** or full formal certification claimed |

All newly executed mathematical source hashes and dependency versions are in `math_execution_environment.json`. Existing freeze is untouched.

## C. Figure 3 materials: all secured, none inferred

| Archive item | Actual use and limitations |
|---|---|
| `phase_model_functions.py` | Full original evaluator inspected; mirrored unchanged in input_v04 |
| `figure3_recompute_v04.py` | Full original source inspected; reconstructs selected refinement and 641 records; full 1681-cell computation not rerun |
| `figure3_data_41x41.npz` | Arrays/axes/classification counts read; old/final grids and masks reconciled |
| `figure3_depth_convergence_641.json` | All 28 stored records read, and all 84 combinations of 81/321/641 depths independently replayed |
| `figure3_design_nash_spotchecks.json` | Read; aggregate summary only. Original 240-case generator/case list **not in archive**, so original sampling claim not independently reproduced. New 72-case/216-root checks and actual cases saved separately |
| `figure3_plot_source.py` | Inspected; hardcoded production source paths noted; exact original preserved. Future regeneration requires documented path adaptation |
| `FIGURE3_V04_REVIEW_QA.md` | Read; not treated as proof. All claims tested to the stated extent |
| Figure3 PDF/PNG | Visual inspection and PDF font information; actual paper placement checked |
| 351 boundary refinement | Reconstructed mask yields 351; no per-call record for all351, and entire sweep not rerun. NPZ refine_mask names only28 changed cells |
| SU disappearance | Historical changes reproduce, but no continuous-depth absence theorem is inferred. Stable SW errors remain in11 cells |

Independent targeted scans, full-three-firm spotchecks and 80-digit counterexamples are documented in the Figure 3 report and README_FIGURE_AUDIT.md. A high-precision float is not an interval proof.

## D. Workflow checklist application

The stable package uses `NOVELTY_KILL_CHECKLIST.md` and `PORTABILITY_FALSIFICATION_CHECKLIST.md` for some of the user's descriptive checklist titles; those are the mapped documents, not invented missing files.

| Requested check | Applied evidence | Current state / inapplicable portion |
|---|---|---|
| Stage11 Robustness/Referee Attack Gate | Four reports; primitive reconstruction; concrete numerical attack; known-model mapping; institutional counterfactual | CONDITIONAL GO; actual numeric regression recorded, no blanket inherited certification |
| Reviewer Verifiability | Exposition map and full local theorem reconstruction in proof report | Local chain PASS; all-depth/strip article-facing supplement CONDITIONAL |
| Theorem Certification | Quantity/full-cube Nash/Rosen; exact J/F forcing algebra; local-to-level implication; interval all-depth; C1/face replay | PASS within quantified baseline domains; no whole-phase-plane or unrestricted-bargaining certification |
| Novelty / theorem absorption | Eight-study structural/mechanism/proposition map; reduced-form chain-rule attack; final GMS propositions | CONDITIONAL; no direct mapping found, explicitly incomplete Klimenko/BFG/CH texts |
| Contribution robustness / portability | Existing frozen scope checked against title/abstract/theorems; direct-grand procedure undermines bargaining-invariant reading | INSTITUTION-SPECIFIC; no new broad portability study because none is promised/authorized |
| Economic contribution and question completeness | One-sentence question, 100–150 word pitches, strongest objection, all-depth policy consequence, narrow diagnosis-only case | Specialized value supported; unrestricted bargaining/empirics future paper, not essential follow-up for stated question |
| Exposition streamlining | Exact locations, keep/move/delete recommendations, English replacements, conceptual-bridge map | CONDITIONAL; no manuscript rewrite during audit |
| Figure/Table | Full PDF inspected, table values checked, figure inputs/logs audited, false-SW counterexamples | Figures1/2/Tables presentation broadly PASS; Figure3 accuracy FAIL; final journal artwork package N/A at Stage11 |
| AI provenance / author accountability | Actor taxonomy below; separate original/replay/new scripts and raw inputs; original author record inspected as historical evidence | Audit provenance documented. **No new AUTHOR verification/sign-off claimed**; final disclosure/submission sign-off deferred to appropriate stage |

No new Stage12 journal selection, Stage14 submission package, deployment, journal submission, empirical test or full formal proof was performed. Current JPET scope and the closest articles were checked only to assess the requested hypothetical-editor objection. No new model or unrestricted literature search was undertaken.

## E. Material AI-use and verification actors

| Date | Actor | Purpose and input | Adopted output | Verification/evidence boundary |
|---|---|---|---|---|
| 2026-10-22 | AI: Codex/GPT-6 family, root | Full v0.4 manuscript first, later records/code/sources | First impression, exact symbolic check, integrated verdict, exposition plan | 20 symbolic identities checked by COMPUTATION; editorial interpretation remains AI judgment |
| 2026-10-22 | AI: four separate referee agents | Same task context plus manuscript, assigned primary-source/code subsets | Referees1–4, proof/literature/numerical reports | Distinct derivation paths where documented; neither external human review nor complete blind replication |
| 2026-10-22 | COMPUTATION | Archived interval source at fixed SHA | New full-depth/Pareto/C1/network replay logs | Replays, not independent algorithms or new Lean proof; manuscript-object mapping checked separately |
| 2026-10-22 | COMPUTATION | Independent matrix/symbolic primitives | Local exact identities, full-cube rational bounds, full-firm roots | Exact and floating portions explicitly separated; roots/spotchecks do not certify entire phase plane |
| 2026-10-22 | COMPUTATION | Original NPZ/code and new full-three-firm evaluator | 84 archived comparisons reproduce; 11 false SW labels, 80-digit examples | Numerical counterevidence, no claim of all-plane interval proof or corrected map |
| pending | AUTHOR | Exact future revised manuscript/supplement | Not yet supplied | Audit acceptance, user instruction or successful code is not substituted for personal derivation/sign-off |

No passwords, credentials, private email, signed URLs or externally copied full copyrighted articles are included. The original user-supplied manuscript bundle is archived as requested; prior-art sources are cited by public primary URLs and exact locations instead of redistributed. New local audit code/materials are git-backed project work, so no duplicate Library save is required.
