# JPET Stage13R — author-controlled submission data and final checks

**Blocking status:** These cannot be asserted by an AI editor from a GitHub repository or external user profile. They must be affirmatively confirmed by the actual author before submission. A placeholder is NOT a submission-compliant declaration.

| Input needed | What the author must confirm | Location to amend |
|---|---|---|
| Author name | Exact publication name and attribution; any coauthors and their explicit contributions/permission | Title page; article metadata |
| Research affiliation | Institution where research was conducted, or author-chosen independent-researcher label; do not infer employment affiliation | Title page |
| Correspondence | Valid email intended for publication and submission account | Title page / journal portal |
| ORCID | Author-confirmed ORCID iD | Journal portal / title page |
| Funding | Specific grants, salary/in-kind institutional resource relevant to this study, or accurate no-grant statement; funder names and grant IDs | Declarations |
| Competing interests | Any financial, organizational or professional interest requiring journal disclosure, or author-approved none | Declarations |
| Acknowledgments | Actual contributors, help, permission to acknowledge, or omit | Declarations |
| AI use | Tool names/versions where known, tasks (concept development, writing, coding, verification), author's actual independent review/validation performed, and conformity with current Wiley policy | Declarations |
| Data/code archive | Public archive/release DOI or immutable URL containing sources, numerical outputs, environment, reproduced logs and links to certificate evidence, with final SHA | Declarations + Appendix |
| Ethics | Whether no human/animal research statement is accurate and required; any other applicable oversight | Declarations/portal |
| Copyright & originality | Confirm unpublished status, no simultaneous submission, figures and third-party content rights | submission portal |
| Final authorization | Explicit approval of exact final PDF, supplementary files and cover letter before any journal upload/submit | Stage14 exit |

## Conditional draft language; use only after author verification

Funding, only if true: "This research received no specific grant from funding agencies in the public, commercial or not-for-profit sectors." 
Conflicts, only if true: "The author declares no conflicts of interest."
AI, only if fully true: "During preparation of this article, the author used [verified tool names] for [verified tasks]. The author reviewed the outputs and assumes responsibility for the content, code and scientific conclusions."
Availability, after archive exists: "The model, code, generated numerical data, and replication instructions are available at [immutable release identifier], manuscript revision [SHA], with original computer-assisted proof at [source SHA]."

Do not fill with defaults, infer truth from ChatGPT usage, or assert a human review that has not occurred. Current Stage13R manuscript deliberately contains conspicuous bracketed placeholders and "Not for submission" heading. Stage14 must check actual JPET publisher rules and the upload-generated review PDF.

## Production graphics
`scripts/stage13r_export_figures.py` creates standalone TikZ wrappers for the same Figure 1/2 diagrams and Figure 3 numerical slice. `.github/workflows/stage13r-jpet-build.yml` compiles vector PDF artwork separately on the revision branch and publishes it only when the CI passes. These are distinct from the original exploratory numerical generator; no phase classification recomputation is implied by exporting the graphic.

**Editorial recommendation:** author identity/declarations and immutable public archive are the remaining human-controlled mandatory work. Scientific model extensions are NOT a prerequisite from Stage13R.
