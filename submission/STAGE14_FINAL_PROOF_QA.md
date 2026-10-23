# JPET Stage 14 Final Disclosures — research, authorship and reproducibility QA

Updated **23 October 2026**, based on user-confirmed V2b funding and conflicts and a review of the prior V2b research history.

## Assessment

**Economics and scientific manuscript locked; author declarations funding and COI complete; AI research/method/visual disclosures updated.** No final upload to Wiley and no merger to base. The remaining final steps are author review of this version and the Research Exchange publisher-generated preview and specific author confirmations of originality/other submissions/permissions as applicable.

## Grounded disclosure contents

- **Funding:** user personally confirms no external funding for V2b. Manuscript says: `The author received no external funding for this research.`
- **Competing interests:** user personally confirms no competing interests for V2b. Manuscript says: `The author declares no competing interests.`
- **AI research workflow:** Research ideas, specifications, theorem/proof strategies, sym/numeric/interval-code development and debugging, screening sources, simulated adversarial reviews and revisions/rejections of incorrect proposed results were AI-assisted through OpenAI ChatGPT (2026), under author direction. Separate Acknowledgments disclose English drafting/editing and LaTeX development. Three figure legends explicitly identify AI-assisted LaTeX/TikZ layout.
- **Independent human checks:** `reviews/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD_V2B_2026-10-21.md` states that **no author-independent reproduction of all derivations or numerical proofs is documented**. The manuscript does not claim it, and specifically distinguishes reproducible code from independent refereeing/formal verification.
- **Wiley policy:** [JPET author guidance](https://onlinelibrary.wiley.com/page/journal/14679779/homepage/forauthors.html) requires transparent AI manuscript-development disclosure; [Wiley guidance](https://www.wiley.com/en-us/publishing/article/ai-guidelines) places research-method/coding/literature help with research methods, prose editing in Acknowledgments, and AI-influenced figure creation in captions.
- **Other tools:** OpenAI ChatGPT is directly supported by past interactions. Other model/tool vendor names and versions are not invented.
- **Research ethics/data availability:** Theoretical/computational, no empirical dataset or human participant study; code linked to fixed public Git SHA `cbe47a3777fdd193289eff0583f9d5d8d16e43d1`.

## Unchanged scientific material

The source lock `scripts/stage14_jpet_submission_proof_qa.py` normalizes only (a) the draft date, (b) Abstract's structural labels, (c) declarations and AI methods/Acknowledgments, and (d) **exactly three AI figure-layout provenance suffixes**. It verifies that the resulting complete scientific body matches Stage14 preflight parent `cbe47a3777fdd193289eff0583f9d5d8d16e43d1`. The original proof supplement and Figure3 TikZ input files match the baseline, and all 20 bibliography entries remain cited. No model parameters, equations, inequalities, manuscript results, proofs, numerical source or figure data changed.

## Technical PDF review (local and GitHub)

- GitHub source `manuscript/JPET_submission_author_check.tex`, Git blob SHA-1 `372b8bfaebf38db3f70802bc506caa9d32891af5` (final AI prose plus confirmed funding/COI), 62,076 source bytes.
- Local exact-source LaTeX build **PASS**, 23 pages; no undefined citation, unresolved reference, or Overfull hbox warning. Full PDF compilation and pdfinfo checked.
- Layout: checked the first page and all changed-end pages 20–23; AI methods disclosure fits entirely on page 21; declarations and acknowledgments begin cleanly on page 22; 20-entry reference list ends page 23. Existing table placement around Theorem 4 remains unchanged.
- The branch's dedicated GitHub CI run is evaluated independently. Any successful CI-generated PDF hash must be compared against the GitHub stored binary; LaTeX builds may differ in bytes across TeXLive environments.

## Journal upload status

**No journal upload performed.** The following are portal/author actions, not missing scientific analysis: inspect final proof and ensure the prose describes the author's intended research conduct; confirm originality and no concurrent duplicate submissions; ensure any workplace permissions/reused figures and metadata are accurate; upload required main TeX/PDF and two input TeX files; inspect journal-generated PDF; explicitly authorize and execute final Submit. The author has already confirmed the funding/COI facts, so do not ask again.
