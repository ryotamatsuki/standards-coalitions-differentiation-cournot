# JPET final layout, vector figures and AI disclosure — editorial QA

Date: 2026-10-23 JST. **Task scope: exactly three editorial items. Scientific claims frozen; no Wiley submission or GitHub merge.**

## Input authority
- Parent Draft PR: #36, branch `submission/stage14-jpet-author-check-20261023`, exact parent HEAD `32120775fed53bd6d191c532e827b2de2e211bb4`.
- Original GitHub TeX: `manuscript/JPET_submission_author_check.tex`, Git blob **`8ef3b6836277c0b388af0a0c3e42b15cea3b1d7f`**, size 62,159 bytes.
- User's latest `JPET_V2b_submission_abstract_revised_20261023.zip` contains `JPET_submission_final.tex` with **identical Git blob SHA `8ef3b6836277c0b388af0a0c3e42b15cea3b1d7f`** and a 23-page PDF. The latest one-paragraph 172-word Abstract, byline, 20 references, funding/COI and existing AI disclosures were therefore maintained.
- The released standalone vector PDFs match corresponding GitHub blobs bit-for-bit:
  - `stage13r_figure1.pdf`: `9977c9a04ce0a59c5bcd561e855cc81322dd9d0a`
  - `stage13r_figure2.pdf`: `44d631aaf5c3a02929370e065cd9672b3fa8a2ab`
  - `stage13r_figure3.pdf`: `60da45c9356e540f2f0a304958bf25eb8f5ec6e2`
- New editing branch: `submission/jpet-final-layout-graphics-disclosure-20261023`. Main, parent branch and draft PR #36 untouched.

## Exact editorial changes

**1. Layout:** Previously `Conclusion → \appendix A–F → AI / Declarations / Acknowledgments → References`; now `Conclusion → Research workflow and use of generative AI → Acknowledgments (including confirmed no external funding) → Declarations (COI, data/code, ethics) → References → \clearpage → \appendix A–F`. AI/disclosure headings are unnumbered. Bibliography's 20 entries remain verbatim and the input supplement includes the same remaining Appendix D–F sections.

**2. Graphics:** In Figure 1 / 2 / 3, original TikZ environments are replaced by existing original **vector PDFs** loaded as `\includegraphics` with widths `0.92\linewidth`, `0.85\linewidth`, and `0.98\linewidth` respectively. Same figure environments, float options, labels, captions and source data. The Figure 3 exploratory categories IS candidate / No offer found and uncertainty caveats remain unchanged. No TikZ drawing package or TikZ input is required for journal-paper compilation. The original `stage13r_figure3_tikz.tex` remains in the repository and in the replication/editing subfolder of the ZIP.

**3. Author disclosure:** Research workflow and AI-assisted critiques/derivations/code, manuscript-creation acknowledgment, confirmed *no external funding*, confirmed *no competing interests*, ethics and fixed commit source/data availability are retained, without duplicated funding disclosure or fictional human verification.

## Scientific and structural invariance

- All text in sections from Introduction through Conclusion is **exactly unchanged except figure environments**; compare after normalizing precisely three graphics environments. All Appendix A–F source is **byte-for-byte unchanged** after its move. The 20-entry bibliography and two included scientific TeX sources also remain byte-for-byte unchanged.
- Original and new LaTeX `.aux` files compiled from the complete corresponding original/current sources: **67 labels are identical and all 67 displayed numbers are unchanged**, including all appendix labels A–F and theorem/equation/figure/table numbering. Citations (20/20) unchanged.
- Local isolated LaTeX build PASS, **23 pages**, zero Overfull hbox, missing citations or references. At least 142 PDF links checked for PDF structure. Figure pages: 1 on p.5, 2 on p.8, 3 on p.11; theoretical main result/table passages pp.9–11; workflow/disclosures and start of references p.15; Appendix starts p.17. Table 3 remains in Appendix E. The length is an observed result, not a page-count requirement.
- Actual page images visually checked: first page, Figures 1–3, main theorem with Tables 1/2, disclosures/reference transition and Appendix/secondary certificate tables. No displaced table or orphaned theorem heading observed. Graphic PDFs were inspected as vector PDF renders and have no duplicated captions/figure numbers.
- Full scientific code and Theory Freeze were not modified or re-run for this editorial-only change.

## Local exact-source candidate identity

- Main `manuscript/JPET_submission_author_check.tex` **59,251 bytes**, Git blob `2e485def8e126c1312fb74ba05b6a7b8bd9e52d9`; SHA-256 `7ab00cd273f6c56f7c42891afa628822ff1b144401fbc138e31ee7ec3e55364b`.
- Local build `JPET_submission_final.pdf` 23 pages and 681,947 bytes. Local build SHA-256 `91a3bd6122a159df9cc5e026b5120e5caf00688c9d760cb140ddd4b16aae2451`.
- GitHub CI-built binary bytes may differ from local TeX toolchain, so the final downloadable package uses **the exact GitHub CI PDF**, checked against the copy saved to this isolated branch. The final Git blob and package SHA are reported by CI metadata and can be inspected at the PR and artifact.

## Status and limits

All requested editorial changes and local validation PASS. Final Guild/Wiley portal preview, declarations of originality or concurrent submissions, author signoff and actual Submit remain separate and were not carried out. Main manuscript and figures are complete for file-level preparation, not an assertion of journal acceptance.

## Sources checked
- [Official JPET instructions](https://onlinelibrary.wiley.com/page/journal/14679779/homepage/forauthors.html) distinguish free-format initial submission and **post-acceptance** LaTeX figure guidance.
- [Lee (2026) article / reference layout comparator](https://doi.org/10.1111/jpet.70128) shows Acknowledgments then appendix in the HTML; publisher PDF differs in some bibliographic placement, so Reference-before-Appendix is an **editorial choice**, not a JPET-wide mandatory ordering.
- [Wiley AI guidance](https://www.wiley.com/en-us/publishing/article/ai-guidelines).