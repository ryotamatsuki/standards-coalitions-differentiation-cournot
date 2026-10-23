# Stage 14 — JPET Submission Package Preparation and QA (23 October 2026)

**Stage status: TECHNICAL PREFLIGHT PASS / SUBMISSION GATE OPEN (not approved).**
**Draft PR #35:** https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/pull/35
**Input:** Stage13R-M PR #34 exact HEAD `492605b5938e857137a6721eb22150f294d84835`; independent branch `submission/stage14-jpet-finalization-20261023`. No change to main, PR #34, scientific source, uploaded Wiley manuscripts, or public research releases.

## 1. Source and authorship from actual prior submission correspondence

The author had previously provided and confirmed in ERE/JRS submission exchanges:

| Attribute | Value used in this Stage14 preflight paper |
|---|---|
| First and corresponding author | Ryota Matsuki |
| Research affiliation | Independent Researcher, Matsuyama, Ehime, Japan |
| Corresponding email | ryota.matsuki@gmail.com |
| ORCID | 0009-0005-2329-531X (independently validated checksum X) |
| Street postal address / phone | Not reproduced in public repository |

These verified *historical author metadata* were populated on the first manuscript page, prefilled in `submission/STAGE14_AUTHOR_FACTS_AND_APPROVAL_TEMPLATE.md`, and included in the explicitly unapproved cover-letter draft. They do not claim affiliation with or endorsement by an employer or any other institution.

Earlier JRS submission recorded no funding and no conflicts for **that distinct work**. Those are disclosed here as historical observations only; no assertion about V2b funding or conflicts has been transferred to the Stage14 manuscript.

**Submission-dependent statements remain blocked:** accurate V2b funding, relevant employment/institutional resources, interests, ethics/permissions, detailed AI-assistance use and verification, immutable archive citation, acknowledged contributors, author approval and actual Wiley portal-generated PDF. The working TeX deliberately retains the `Not for submission` date notice and conspicuous Declarations placeholders.

## 2. Specific edits, and scientific invariance

Stage14 applies only two prose corrections relative to PR #34:
- `\\citet{Kawabata2021} also establishes` → `... also establish`.
- `\\citet{Grossman2021} already studies` → `... already study`.

It also replaces the *title-page author placeholder* with author-verified data. `scripts/stage14_submission_preflight.py` compares **the entire Stage14 manuscript** against exact PR #34 fixed source after applying only those three substitutions, and rejects any other change.

The following are byte-for-byte unchanged: Abstract, Introduction's substantive economic-significance explanation, body other than the two subject–verb agreements, equations, theorems, lemmas, propositions, proofs, figure and table source and contents, Table1 `tab:map` [H] placement, 20 references, 2 `\\input` dependencies, published scientific evidence/proof certificate, and Theory Freeze. No rerun of original all-depth numerical proofs was needed for this content-only revision.

## 3. JPET current author rules checked

Official, live JPET Wiley [For Authors](https://onlinelibrary.wiley.com/page/journal/14679779/homepage/forauthors.html) (checked on October 23 2026):
- Uses [Wiley Research Exchange](https://submission.wiley.com/journal/JPET), not the historical/legacy ScholarOne URL.
- Supports initial **Free Format** and **single-anonymized** peer review. LaTeX Main Document requires corresponding PDF for Peer Review, with every `\\input` file supplied separately as a LaTeX Supplementary File.
- Requests author/affiliation/contact and ORCID, abstract max 250 words, no more than seven keywords, funding/conflict/data availability statements and article-appropriate ethics/permissions.
- Current guidelines refer to structured abstract while some historical/published theory articles have unstructured abstracts; pending live submission-form review, the author's existing Abstract is preserved and this ambiguity remains tracked as a *format gate*, not scientific failure.
- Wiley [AI research policy](https://www.wiley.com/en-us/publishing/article/ai-guidelines) requests appropriate disclosure of material use in manuscript drafting/organization (Acknowledgments), research analysis or literature/methodology (Methods), and AI-generated graphics (figure captions), based on what actually occurred. A prior AI declaration from another paper is not presumed to describe V2b accurately.

## 4. Reproducible packaging and privacy guard

Files committed exclusively to Stage14 Draft PR #35:
- Updated canonical `manuscript/stage13rl_jpet_revised.tex` and latest compiled `manuscript/stage13rl_jpet_revised.pdf`.
- `scripts/stage14_submission_preflight.py`: baseline-locked entire-source diff, citation/content invariance, fail-closed author status, optional integrity manifest and exact source/PDF ZIP.
- `scripts/stage14_render_submission.py`: local private author-data-to-LaTeX renderer requiring every actual declaration and an explicit `author_approved_contents=true`; it writes a *new private output outside this public repository* without mutating scientific source or submitting to Wiley.
- `submission/STAGE14_AUTHOR_FACTS_AND_APPROVAL_TEMPLATE.md`: truthful author facts filled, V2b-specific declarations intentionally blank; separate note of JRS historical statements.
- `submission/STAGE14_COVER_LETTER_DRAFT.md`: author byline filled but originality/permissions/consent declarations left as an explicit unsent author-gate.
- `submission/STAGE14_JPET_REQUIREMENTS_AND_SUBMISSION_README.md`: upload file-designation checklist and portal/format flags.
- `.github/workflows/stage14-jpet-preflight.yml`: only Stage14 branch PDF may be updated by CI; does not touch parent PR or submit.

Local renderer testing: with mock data and `author_approved_contents=false`, the renderer returned status code 2 and refused output; with an **explicitly fictitious** private test approval and complete dummy fields, it generated TeX with no submission placeholders and both required `\\input` dependencies. Dummy author data and fake declarations are **not** in GitHub or any user-facing ZIP.

## 5. CI artifact, binary identity and rendered pages

Dedicated GitHub Actions run **39885342753** (all steps SUCCESS): https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39885342753. All 20 bibliography entries resolved and are cited in main/supplement. No undefined citation/reference, multiply defined citation or Overfull box in the final LaTeX log.

**Current compiled preflight paper:** `manuscript/stage13rl_jpet_revised.pdf`, **23 pages**; **596,431 bytes**; complete Git Blob SHA-1 **`70bc07c8c355b4b05fe0daed5b2084502a2abb78`**; raw SHA-256 **`c980d27666ffff66eb5be954d3896980b1041d4d1af4e7f82b04170bd5a94d9c`**. Compiled manuscript GitHub source blob SHA-1 **`666d195ef4d82030dce9f5c4de4932c96583a863`**. PDF-only branch publish commit **`6b50e90705dac19820018fa6129a4612aa0488c4`**.

Run artifact **12472810641**, name `stage14-jpet-PREFLIGHT-NOT-FOR-SUBMISSION`, ZIP SHA256 **`bcfbb4aec98867075bae0ecfe4b1cc20d9b39e9d43cb5fcbf6d918b0a1f8d081`**. Downloaded actual CI archive and unpacked nested `submission/JPET_STAGE14_PREFLIGHT_DO_NOT_SUBMIT.zip`: **exact PDF bytes and SHA256 match** among run PDF, nested package PDF and GitHub committed PDF. Nested `SUBMISSION_MANIFEST.json` records author-declaration-complete=false, archive-doi-confirmed=false, upload-authorized=false; includes the 20-citation TeX, both LaTeX inputs, all 3 vector figure PDFs and local metadata renderer. The archive is **not** safe to upload to the journal as a finalized paper.

**Image review:** Rendered all 23 pages of the actual CI artifact. Visually checked title/Abstract and Introduction pp. 1–2; model pp.3–4; Theorem4 and Table1 pp. 9–10; Table2/Figure3 p.11; Related Literature/Conclusion pp.13–14; Table3 p.20; declarations pp.21–22; references pp.22–23. The Table1-in-theorem-proof defect from earlier PR is absent: the proof ends on p.10 before Table1; no table interrupts the final sentence. The title author name, affiliation, email and ORCID are clearly legible; no clipped text or overprints detected. Page count increased from 22 to 23 because the verified author byline and working declarations altered pagination; pages need not be artificially compressed. Final page 23 carries the final two bibliography entries. No page-break issue was classified as submission-blocking.

## 6. Status and specific remaining steps

**Completed:** Current Wiley venue workflow verified; historical verified author metadata recovered and embedded; correct grammar; exact mathematical/source invariance; author-data private renderer/approval gate; unsent cover-letter draft; locked source manifest; compiled 23-page PDF; artifact-to-repository PDF identity; visual page QA. No merge, journal submission, or journal acceptance represented.

**Required before an actual submission:** (1) author certifies V2b-specific funding and conflicts (despite prior JRS defaults); (2) author confirms ethics/permissions, actual AI assistance, acknowledgments and any public-service/affiliation authorization; (3) immutable source/certificate archive link and public status are supplied truthfully; (4) private final TeX is generated from confirmed author statements and independently recompiled and inspected, with any structured-Abstract portal requirement resolved; (5) exact portal upload preview and metadata are checked; (6) author explicitly instructs submission.

**Stage 14 technical package: PASS. Final JPET upload gate: BLOCKED until truthful author-specific facts and explicit approval.**
