# Stage 11 — Exposition, proof visibility, and minimum revision plan

## Scope and method

The exact v0.4 source (SHA256 `4d42ee2c30e72e9a7f81f4eed6847d8e73870b76f3b87f94abea72ebbd99572b`) and all 17 PDF pages were read. All pages were rendered with Poppler; the page containing Figure 3 was additionally viewed at full rendered size. This is an audit, not an edited manuscript. Original TeX/PDF, numerical figure, main and Theory Freeze are unchanged. Proposed wording below is not a new theorem.

## Overall reading judgment

The question and controlled comparison arrive early, and the paper correctly distinguishes local derivatives, the all-depth certified witness, and numerical exploration. The main conceptual bridge is already visible: own-private-profit optimization does not remove consumer effects or rival-design effects on home worldwide profits. Lemma 1 explicitly counts incident and nonincident edges; this passes the specialist-reader standard. Equations (14)–(18) preserve the corrected **plus** rival-profit incidence.

The largest reading problem is Appendix D: it instructs a future author to assemble certificates rather than giving a complete certificate proposition and runnable immutable supplement. The second is treating Figure 3 as an optimized regime map despite actual missed accepted proposals. A narrower caption alone does not repair incorrect cell classifications while retaining that interpretation. Repeated discussion of editors, prior audit stages and 'our answer cannot rest' should become ordinary economic exposition.

## Claim-to-proof and exhibit map

| Object | Location in v0.4 | Referee assessment | Required action |
|---|---|---|---|
| Demand, fixed expectations, Cournot FOC, CS | §2.1, §3.1; eqs. (2)–(5),(8) | BRIDGE NEEDED | State parameter domain and consumer concavity argument; show fixed expectations are held fixed only at quantity deviation, fulfilled in continuation. |
| Actual private design, not common optimization | §3.2, eqs. (10)–(12) | BRIDGE NEEDED | Display `q_xj=-M^{-1}M_xj q` and `F_i=6q_i q_i,xi + kappa(1-x_i)`; state sufficient own-concavity and full-cube uniqueness certificate. |
| Edge-count lemma | §4.1, Lemma 1, eq. (13) | ROUTINE/PASS | Keep in main text. Two incident edges plus one nonincident edge directly justify every derivative identity. |
| Incidence lemma | §4.2, Lemma 2, eqs. (14)–(18), Appendix A | PASS with short bridge advisable | Keep the national-gradient vector and plus sign; add matrix derivative and own-FOC substitution in Appendix A. Root's independent exact script verifies 20 identities. |
| Local reversal (A-local) | §5, Theorem 3, eq. (19) | PASS under stated regularity | Preserve local quantifier and derivative-to-level proof. Do not market `0<D<L` itself as a new general theorem. |
| Open-region optimal-regime reversal (A-global) | §5, Theorem 4, eqs. (20)–(22), Appendix D | APPENDIX DETAIL NEEDED | Add exact targets, complete full-cube Nash and quantity argument, interval construction and immutable source/run identifiers. Show compact feasible-IS-set maximization and strict SU envelope domination. |
| Institutional comparison B | §6, Proposition 5 | BRIDGE NEEDED | State voting implementation and tie-breaking on all histories; distinguish SU rejection continuation from direct-grand SW continuation. Keep proposition as interpretation of A. |
| Local design-friction cutoff C1 | §7.1, Proposition 6, Appendix B | PASS; scope already accurate | Retain unique local cutoff, not global regime threshold. Define forcing and Jacobian before use, avoid u/nu visual confusion. |
| Network face and near-face strip C2 | §7.2, eqs. (25)–(27), Appendix C | APPENDIX DETAIL NEEDED | Move bulk to Appendix; include actual polynomial inequalities and nearby-strip proof rather than citing an internal Stage file. `rho=1` is design-inactive. |
| Figure 1 | p5 timing; §2.2 | Useful, minor compression possible | Explicit rejection arrows/labels can strengthen extensive form. It currently displays a sequence, not a full voting game tree. |
| Figure 2 | p7 causal diagram | Useful but partially repeats eq. (18) | Keep if it helps reader distinguish fixed/endogenous treatments; shorten adjacent repetitions. It depicts local signs only. |
| Figure 3 | p11, §5.1 | MAJOR BUT FIXABLE | Recompute continuous-depth boundary candidates, retain unresolved cells and regenerate plot. See numerical report and concrete counterexamples. |
| Table 1 | p10 hierarchy | Useful scope map, dense small type | Keep local/global/institution limits; shorten content after C2 Appendix move. |
| Table 2 | p10 national gaps | Useful and independently reproduced | Keep uncalibrated units and signs. Do not infer empirical importance from 0.70%. |

## Concrete English replacements and insertions

### 1. Give the residual attribute economic content (§2.1)

**Before:** “a larger x_i is a higher level of the model's residual attribute”.

**After:** “Residual design represents costly differentiation. A higher x_i increases substitution with rival products through X_ij=(x_i+x_j)/2 and lowers the design cost K_i. It therefore represents cheaper residual similarity, while a lower x_i purchases differentiation. The government's compatibility depth g specifies a separate component of the product relationship.”

This is a description of the existing equations, not a new primitive or an empirical identification.

### 2. Explain the response rather than naming the incidence (§4.2)

**Before:** “Standardization changes the privately desirable residual characteristics.”

**After:** “At the reference parameters, compatibility lowers output and weakens the private return to costly differentiation. Firms consequently choose higher, cheaper residual similarity. Each firm's first-order condition cancels its own marginal private-profit effect, but leaves domestic consumer effects and the effect of rivals' redesign on its worldwide earnings. These national effects can overturn consent even when a direct grand agreement remains beneficial.”

Qualify the first sentence to the demonstrated parameter region; it is not a universal comparative-static statement.

### 3. Make the consent rule a derived continuation (§2.2)

**Before:** “Country C may then join at the same inherited depth; accession requires the approval of C and incumbents. When indifferent, a government accepts.”

**After:** “After B accepts, C and the incumbents vote on enlargement at the inherited depth g. If enlargement is rejected, AB remains in SU. Every government votes to accept when its final payoff is unchanged, including at off-path histories. Thus enlargement succeeds if i(g)≥m(g) and i(g)≥o(g). B anticipates this continuation and accepts an enlarging offer only if i(g)≥s; if enlargement fails, B accepts only if m(g)≥s. Hence integration requires i(g)≥max{s,m(g),o(g)}.”

Either specify sequential voting with this continuation or state the simultaneous voting implementation and tie-breaking sufficiently precisely. The tie rule is material: a potential coordination objection without it must not be represented as an established defect of the actual draft, which already states acceptance when indifferent.

### 4. Replace the promise of future proof packaging (Appendix D)

**Before:** “The following records ... must accompany the submission package and be checked against the precise text of the theorem”.

**After, once integrated:** “The supplementary certificate fixes the rational primitives in (20). For every g∈[0,1], it encloses the full three-firm Nash continuation, proves positive quantities and a uniform uniqueness margin, and bounds the two derivatives in (21). The certificate uses 1000 accepted depth intervals with outward rational arithmetic. Integration from the common zero-depth payoffs proves the endogenous participation inequalities. For frozen design, the accepted g=1/20 grand offer strictly exceeds the all-depth bilateral envelope in (22). The supplement records the exact source revision, interval construction, commands and output hashes.”

Add the actual Nash-system/Krawczyk/Rosen mathematical definitions and the compactness/continuity argument. A working command and successful log are necessary evidence, not substitutes for those definitions. Use the precise details in the proof audit; do not describe floating-point phase exploration as this certificate.

### 5. Correct the Figure 3 result (§5.1 and caption)

**Before:** “Figure 3 maps the government-optimal terminal regime”.

**Required action before replacement:** The map currently misses positive-depth accepted IS offers in at least 11 saved SW cells. Refinement to 641 equally spaced depths does not close this. Root acceptance boundaries, include endpoints and candidate interior welfare optima on each feasible branch, check one-sided limits, and label unresolved/tolerance-sensitive cells. Regenerate the map and all counts from the corrected evaluator. Preserve original inputs and logs.

**After, only if corrected:** “Figure 3 numerically approximates the initiating government's preferred terminal regime. Acceptance boundaries and candidate interior welfare maxima are evaluated separately; unresolved cells are shown explicitly. This numerical map does not extend the strict interval certificate beyond its stated domain.”

An alternative minimal full-paper route is to remove Figure 3 and its phase claims while retaining Table 2 and the certified benchmark. That is an editorial choice requiring the author to accept the reduced exhibit scope; it does not establish a corrected phase map. The audit's required Figure 3 inspection is already complete and must remain archived either way.

### 6. Replace audit-facing novelty prose (§8)

**Before:** “An editor can still reasonably ask whether ... Our answer cannot rest merely on a new derivative formula”.

**After:** “The increment relative to standards-coalition and regulatory-design models is the controlled participation comparison: holding the government procedure fixed, private design changes the national participation constraints and the government-optimal terminal agreement. The result is conditional on inherited-depth accession; a direct grand offer remains feasible.”

Retain an explicit focused comparison with Takarada/Kawabata and Grossman–McCalman–Staiger. The eight-study comparison belongs in a compact literature table or supplement, with unavailable propositions marked unresolved. Do not replace a material novelty uncertainty by stronger wording.

## Scope and placement of supporting results

* **B:** keep in main text immediately after A and interpretation; it demonstrates the institution boundary and prevents a misleading broad cooperation-failure claim. Do not count it as an independent generic coalition discovery.
* **C1:** keep a short proposition in main text if desired, with the M-matrix derivation in Appendix. It directly clarifies why costly adjustment restores local participation. The current restriction to a local cutoff is valuable and must remain.
* **C2:** retain a short limiting-case paragraph; move formulas and nearby-strip detail to Appendix. At rho=1 the strategic private-design channel vanishes, so this is a boundary check rather than corroboration of active redesign. Preserve all research records.
* **Introduction/Conclusion:** remove announcement of how many figures the paper uses and repeated defensive novelty disclaimers. Retain one precise novelty statement and one institutional limit. Conclusion introduces no material new theorem and is acceptably short.

## Visual QA

Figures 1–3 and Tables 1–2 appear within the 17-page PDF without observed clipping or broken equation references. Figure 3 sits in the numerical-results discussion before §6 and has common axes, correct benchmark star, direct regime labels and vector artwork. Gray/blue fills differ in brightness and direct labels help grayscale interpretation; confirm on final production proof. Table 1 and diagram text are compact; review at final journal size. No layout defect discovered here competes in seriousness with the numerical classifications. This audit did not recompile or rewrite the TeX.

## Minimum mandatory repair order and stop rules

1. **Numerical integrity, Stage 9/10 rerun then Stage 11:** replace grid-only regime identification or remove the phase-map claim. Recheck the 11 demonstrated misses, 28 historical changed cells, center and new computed boundary cases; preserve UN rather than treating failed solves as SW. No entire-plane interval proof is required.
2. **Proof visibility, Stage 10/13 exposition then Stage 11:** integrate the complete all-depth certificate supplement and nearby-network proof, exact historical source and replay output, full-cube equilibrium/positive-output margin, voting continuation and optimal-offer existence. No new model is needed for these repairs.
3. **Economic exposition and focused novelty:** give x its costly-differentiation meaning; state protocol scope once; compare to actual strongest propositions. If unavailable CH/BFG material reveals a concrete absorber, reopen Stage 6. Missing access itself is not an absorption finding.
4. **Author responsibility and publication:** author checks exact revision and final claims; formal Stage 12 remains separate from this JPET-oriented attack. Do not change main, frozen theory, bargaining primitives, or add a renegotiation equilibrium in this repair.

Future research, not required here: unrestricted bargaining, transfers, endogenous institutional selection, estimated magnitudes, arbitrary demand or country-number generality. A valid institution-specific result can stand without these. Stop repairs once the stated question, verified proof scope and numerical claims agree; do not expand the research indefinitely to protect a preferred journal.
