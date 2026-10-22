# Stage 13R: Figures, tables and JPET submission compliance

Reviewed manuscript SHA: `c7b52ac10a701c682479e8f57c1343ceed1df719`. Date: 23 October 2026 JST. Simulated reviewer/editor assessment, not a decision by JPET.

## All-page visual review

All 20 canonical PDF pages were rendered individually at up to 1,400 pixels on the long edge and inspected as images. Text extraction was not used as a substitute for layout inspection. A separate three-pass local pdfLaTeX build compiled the unchanged source in scratch: 20 pages, no undefined references/citations or overfull warnings on the final pass. The build was not substituted for the canonical PDF; font/toolchain metadata mean byte equality is not expected.

| PDF page | What was inspected | Observation/action |
|---|---|---|
| 1 | Title, working metadata, abstract, keywords/JEL, opening | Legible. Remove draft metadata at submission. Abstract is 187 words, seven keywords. |
| 2 | Introduction, headline equation, roadmap | Legible; contribution pitch has excessive caution, not a layout defect. |
| 3 | Model matrices, utility, cost | Equations fit; dense but readable. Clarify economic meaning rather than enlarge type. |
| 4 | Welfare, timing, payoff definitions, consent | No unresolved labels; continuation logic needs clear terminology. |
| 5 | Figure 1, end of previous paragraph, Cournot formulas | Boxes fit; unnecessary word hyphenation in labels. Diagram is a timing summary, not full branching tree. |
| 6 | Nash Jacobian, Lemma 1, fixed-design definition | Legible. Block split into next page is ordinary, not a correctness issue. |
| 7 | D, C,V, Lemma 2, interpretation | Clear equations; add economic algebra in appendix rather than crowd page. |
| 8 | Figure 2, local theorem, start global theorem | Readable. Theorem 4 begins near bottom and continues on p.9; prefer a full theorem start after revision if practical. |
| 9 | Global theorem continuation and proof | No clipping; long certification paragraphs are a presentation issue. |
| 10 | Tables 1–2, numerical explanation | Table 2 interrupts a sentence; 13R-16. Table 1 small but readable. |
| 11 | Figure 3, direct-grand proposition/proof | Map legible; candidate status should appear within plot, not only caption. |
| 12 | Institutional discussion, lambda definition/proposition | No collision; theorem continues to p.13 ordinarily. |
| 13 | Lambda proof, network boundary, literature | Text readable; late literature repetition burdens flow. |
| 14 | Conclusion, Appendix A | Equations fit. Add short gradient derivation and reflow later. |
| 15 | Appendix B/C, start full-cube proof | Long formulas remain legible; cutoff coefficient needs derivation. |
| 16 | Contraction, derivative bounds, Rosen inequality, Appendix E | No equation overflow; appendix heading wraps across lines. Optional shorter heading. |
| 17 | Nash lift, interval methods, derivative/candidate bounds | Legible, but output precision and prose hierarchy need simplification. |
| 18 | Closed feasible set, replication mapping, Appendix F | Long paths use breakable formatting; no missing reference. |
| 19 | Face witness and strategic strip | Dense but readable; reusing M,J,H,V for welfare gaps increases notation burden. |
| 20 | End of strip, declarations, all nine references | References readable; placeholders are actual submission blockers. |

No cropped equation, unreadable symbol, label overlap, missing figure, or unresolved citation was demonstrated. Not every page break must be repaired; only the disruptive sentence/table break is a substantive layout recommendation.

## Every exhibit

| Exhibit | Economic function | Decision / implementation |
|---|---|---|
| Figure 1 (p.5) | Separate government agenda from private continuation | KEEP; shorten boxes, retain vote-order explanation in prose. Figure alone need not encode every off-path branch. |
| Figure 2 (p.8) | Local identifying comparison | KEEP as a compact local comparison; condition 0<D<L remains visible. |
| Figure 3 (p.11) | Explore how permitting redesign changes the numerical search outcome | KEEP with visible candidate/search labels and legend. All archived cells match TikZ rectangles. No certified area or universal no-SU statement. |
| Table 1 (p.10) | Organize main/local/institution/boundary claims | KEEP; add theorem/proposition numbers and reduce caution repetition. Do not delete the underlying conditions. |
| Table 2 (p.10) | Compare national rejection options at the same g | KEEP; every number independently reproduces. Complete the interpretation after table; avoid floats inside a sentence. |

Figures 1–2 already use black lines/labels. Figure 3’s dark blue and light gray remain distinct in grayscale in the observed rendering; a legend and candidate labels are still needed because grayscale readability does not communicate evidential status. Do not claim grayscale failure without evidence. Final label sizes must be rechecked after standalone export.

## Current official rules: decision log

Primary source, retrieved during this audit: [JPET Author Guidelines](https://onlinelibrary.wiley.com/page/journal/14679779/homepage/forauthors.html), especially “Free Format,” main-file guidance, submission versus post-acceptance LaTeX guidance, peer review and AI paragraphs. No archived page was substituted for the current page.

| Status | Verified rule or unresolved question | Current action |
|---|---|---|
| Required | Abstract ≤250 words; ≤7 keywords; ORCID; author identity/affiliation/contact; applicable disclosures | Word/keyword limits pass. Author fields and declarations remain incomplete. |
| Required if submitting LaTeX | Source plus compiled peer-review PDF and referenced files | Prepare the complete dependency set. |
| Initial submission flexible | Free Format permits embedded figures/tables and consistent reference style | Current TikZ embedding alone is not an established initial-submission violation. |
| Recommended | NJD template | Optional initial reformatting; prioritize clarity. |
| Post-acceptance | Editable sources and separate EPS/PDF/TIFF graphics; avoid embedded LaTeX drawing code | Export all three figures, not only Figure 3. |
| Confirmed review model | Single-anonymized | Do not withhold author identity merely to imitate double-anonymized review. |
| Confirmed AI policy | Substantive assistance must be disclosed; author remains accountable | Author confirms actual tasks/tools and review. |
| Ambiguous on current page | Generic structured-abstract/Materials-and-Methods instructions coexist with theory-oriented guidance | Preserve theory sections; resolve final packaging interpretation without inventing empirical content. |
| Unconfirmed | Exact portal field behavior, production interpretation of all TeX-generated graphics, any unpublished editorial preferences | Verify at final QA; no submission attempted here. |

The structured-abstract wording is genuinely on the current official page; do not dismiss it as a proved obsolete rule. The inspected recent theoretical articles use ordinary prose abstracts and theory-specific sections. This supports an unstructured theory abstract as the working editorial recommendation, not certainty about what a future portal validator or editor will demand. If run-in headings are required, classify the same research question/model/results/conclusion without adding experiments, participants, data collection or a fictitious empirical Methods section. Mark the ambiguity unresolved until final submission-package QA or editorial clarification.

## Concrete separate-figure workflow

The no-embedded-drawing recommendation belongs to the production-stage LaTeX list, while separate-figure requests also occur in general sections. The explicit Free Format permission prevents treating the latter as a categorical ban on an integrated review PDF. For a safe final package, prepare independent vector PDF figures and captions anyway.

Use a scratch `standalone` document with `tikz` and the currently required libraries. For Figure 3, input the existing figure file; for Figures 1–2, extract the corresponding `tikzpicture` environments. Compile each wrapper and crop its bounding box, then use `\includegraphics` in the submission/production copy. Export EPS from vector PDF if specifically requested; TIFF is unnecessary for these vector diagrams unless requested. This conversion is proposed, not performed in the protected manuscript. If the production office rejects graphics generated with TeX at all, recreate Figure 3 from the same map array in Matplotlib and diagrams in a vector editor, then compare all data/labels and benchmark coordinates. A standalone PDF does not by itself prove compliance with an interpretation excluding all TeX-generated graphics.

## Author-only facts and insertion locations

The conditional English template is in `editorial/STAGE13R_PROPOSED_ENGLISH_REVISIONS.md`, linked to 13R-18. It deliberately leaves facts undecided.

| Item | Author must supply/confirm | Location |
|---|---|---|
| Name/affiliation/contact | Actual author(s), institution where work was done or independent-researcher designation, correspondence | Title page and portal |
| ORCID | Real verified identifier; no invented identifier | Portal/title metadata as requested |
| Funding | All real support or truthful no-specific-grant statement | Acknowledgments/declarations |
| Conflicts | Actual conflict or truthful none statement | Declaration and portal |
| Data | No empirical collection if accurate; acknowledge generated computational data | Data availability |
| Code | Frozen accessible release, manuscript SHA, certificate SHA, environment and reproduction commands | Code availability and supplement |
| AI | Actual tools and tasks, including drafting/code/math assistance if used, and responsibility | Acknowledgments or appropriate declaration |
| Acknowledgments | Actual human contributions and permission to be named | Before references |
| Research ethics | Theoretical/computational nature if accurate; no fabricated IRB approval | Applicable statement/portal |
| Exclusive submission | Author confirms no simultaneous submission of the same manuscript | Cover letter/portal |

Do not infer any of these facts from the user’s job or biography. Do not copy a generic “no new data” statement from an analytical paper when this work generated numerical maps and certificates. ORCID, archive URL and declarations cannot be completed by prose polishing alone.

## Submission package and closeout

For the next stage, prepare the revised main PDF and editable source, mathematical supplement, computational sources/environment/expected outputs, standalone figures and captions, verified references, author declarations and cover letter. Separate supporting material clearly if the portal requests it; do not remove proof-critical arguments from the review package. Confirm every source input is included and cross-references survive the package structure.

Do not upload this working draft. Close the register’s required and strongly recommended items, obtain truthful author facts, render the actual revised PDF, check the upload-generated review PDF, and stop before final submission unless separately authorized. This audit itself performs no journal submission.
