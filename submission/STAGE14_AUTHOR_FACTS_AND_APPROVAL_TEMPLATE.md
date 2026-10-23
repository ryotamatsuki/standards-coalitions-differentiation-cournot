# JPET Stage 14 — verified author inputs (PRIVATE TEMPLATE)

**BLOCKED — not an attestation of any author facts.** Enter only accurate, author-approved facts. Do **not** commit a filled copy containing personal contact details or unpublished disclosures to a public repository unless intended for public release. Keep the completed JSON on a private machine or supply answers directly to the author at the last approval step. This template contains no inferred facts.

Fill every required string with the exact information you want in the published article (no brackets or placeholders). Set `author_approved_contents` to `true` only after you personally review the complete manuscript, every declaration and all AI-assisted work. This is **not** authorization to click Submit at Wiley.

Use this JSON shape as a starting point (store as an untracked local file; **never** put your filled personal details or declarations into a pull request):

```json
{
  "author_name": "",
  "affiliation_or_independent_status": "",
  "correspondence_email": "",
  "orcid": "",
  "funding_statement": "",
  "conflicts_statement": "",
  "data_code_availability_statement": "",
  "ai_assistance_statement": "",
  "ethics_and_permissions_statement": "",
  "acknowledgments_statement": "",
  "author_approved_contents": false
}
```

## Author decision points — no defaults are assumed

1. **Author and affiliation.** Confirm legal scholarly name and actual affiliation **at the time of research**, or a truthful independent-researcher designation. Do not imply an employer endorses the research without permission. Confirm email and ORCID (Wiley JPET current guidelines request ORCID).
2. **Funding and institutional resources.** Identify funding bodies, amounts/IDs if applicable, actual equipment/institutional support and absence or presence of financial support. If work touches public-service employment or activities, resolve any relevant disclosure and permission questions with the competent authority; no affiliation/clearance can be inferred from repository history.
3. **Conflicts.** State actual relevant financial, employment, advisory and nonfinancial interests, or a personally confirmed accurate absence. Do not use a false boilerplate `No conflicts`.
4. **Ethics and permissions.** Confirm that no human/animal research or protected data were used **if true**. Check third-party image rights, paper figures, contributor permissions and prior-publication policies.
5. **AI assistance.** Disclose tools and material uses in research or manuscript development according to Wiley policy, and describe substantive human verification performed. AI cannot be listed as an author. Do not claim checks you did not perform. Ordinary spelling/grammar editing alone is treated separately under the journal's published policy.
6. **Data/code.** Link a publicly **immutable** versioned archive (persistent DOI or versioned archive URL), its exact manuscript commit and the certificate/replay commit. A mutable default GitHub branch URL alone does not satisfy the archival gate. The paper has mathematical/numerical artifacts, not an empirical dataset unless independently established.
7. **Title, author order, contents, related manuscripts, originality.** Every author must approve the paper and no duplicative/concurrent submission can exist.
8. **Wiley portal.** Current author instructions primarily point to Research Exchange (`submission.wiley.com/journal/JPET` / `authors.wiley.com/journal/JPET`); legacy ScholarOne pages remain indexed and **are not** the default. Confirm the actual instructions displayed during upload.

## Review and processing

- Working manuscript remains `manuscript/stage13rl_jpet_revised.tex`; until required facts are provided, its title/date/declarations deliberately display **not for submission**.
- The private metadata rendering utility `scripts/stage14_render_submission.py` checks that all required facts are filled and approved, creates a **separate private output directory**, and does not modify the public working paper. It does not upload/submit.
- Once populated: `python scripts/stage14_render_submission.py /path/to/filled_private_metadata.json --output-dir /path/to/private/submission_build`, then `cd /path/to/private/submission_build && latexmk -pdf -halt-on-error -interaction=nonstopmode stage14_jpet_submission.tex`.
- The GitHub Actions package is a **preflight technical artifact**, not a submission-ready package while these declarations remain incomplete.
