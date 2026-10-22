# Stage 25 v0.4 — canonical GitHub synchronization manifest

**Synchronized 2026-10-22 JST.** Original v0.4 bytes are copied from the delivered `stage25_jpet_v04_with_refined_phase.zip`, **not** regenerated, edited, or shortened. This manifest supersedes the older "TeX/PDF not yet GitHub-synced" statements in Stage25 working QA documents.

## Checked-in files (all under manuscript/)
- [Full 17-page manuscript LaTeX](stage25_jpet_v04.tex) — 58,513 bytes, SHA-256 `4d42ee2c30e72e9a7f81f4eed6847d8e73870b76f3b87f94abea72ebbd99572b`, Git blob SHA `11113b98c2d5f104d0da9ab5e9493ad7d8b5f201`.
- [Original compiled v0.4 PDF](stage25_jpet_v04.pdf) — 485,409 bytes, SHA-256 `06f7e717a0c49c1bfcbd71cccceffd8c0dca893fd67dafba572d288a87952e6b`, Git blob SHA `64da98d50ef530f080af2a5b3aeecad05e6e4dfd`.
- [Figure 3 vector PDF referenced by TeX](figure3_v04_kappa_eta_phase.pdf) — 23,450 bytes, SHA-256 `c8f385b9152005725baf147f7fc9702a29bcb6e4d054ddb03d58a4d8c790d79d`, Git blob SHA `9048341fe9cddc0cfa154b6e4c10613e3c749ed0`.

The TeX explicitly uses `\\includegraphics{figure3_v04_kappa_eta_phase.pdf}`; the figure is in the **same** folder so a LaTeX build from `manuscript/` can locate it without external attachments. Existing package/TeX may require ordinary TeX Live packages (`tikz,amsmath,natbib,...`).

## Git and QA
- PR #26: https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/pull/26 ; **Draft**, not merged.
- Binary source commit: `c91d1f12f67a3973739bbe61747fc946ac20cf27`; the manifest itself is a later commit.
- Git tree was read from GitHub, and **three exact blob SHA values and sizes matched the local original bytes**. No truncated or converted PDF was used.
- All existing Stage22 theory/Stage23–24 audit provenance unchanged; only the existing manuscript branch received the new files.

## Limitations
- This check proves file-byte identity and location in Git; it is **not** a new mathematical proof, independent LaTeX rebuild on GitHub CI, or JPET submission approval.
- v0.4 numerical Figure3 source and numeric evidence are still contained in the locally available v0.4 user ZIP and previous Stage25 QA records. The figure's embedded PDF required for **compiling** the paper is Git-tracked.
- Stage11 reviewers should read the **exact** Git-tracked `stage25_jpet_v04.tex`, `stage25_jpet_v04.pdf`, and Figure3 PDF, rather than the earlier Stage23 working draft or Stage25 synopsis.
