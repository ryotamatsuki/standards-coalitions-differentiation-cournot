# V2b Stage13 hostile review — repair implementation and renewed certification (2026-10-21)

## Verdict and route

**REOPEN STAGE13 -> mathematical certification defects P1/P2 repaired; concrete exposition defects V1/V2/E1/V3/V4/E3 repaired; economic contribution N1/E2 remains CONDITIONAL; Stage14 SUBMISSION QA remains BLOCKED.**  
This is an evidence-bound closeout, not a claim that all Stage13 hostile review has been passed, and not an authorization to submit or merge a stale freeze without author intellectual sign-off.

**Source:** Hostile audit PR [#4](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/pull/4) and detailed report `reviews/V2B_STAGE13_ADVERSARIAL_ECONOMIC_AND_PROOF_AUDIT_2026-10-21.md`.  
**Fix:** stacked repair PR [#5](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/pull/5), based on PR#4 audit branch, retaining published audit and leaving original theory primitive files intact.

## 1. Remediation ledger by independent auditor ID

| Auditor ID | Diagnosis | Implemented repair | Closure state |
|---|---|---|---|
| **P1** (MAJOR) | SymPy rational constants pre-rounded to binary64 | `verification/v2b_exact_rational_interval.py` custom printer outputs `RAT(p,q)` backed by `iv.mpf(p)/q`; both nonlinear certificate programs use exact compiled functions; mandatory rational-constant test detects original 71/500 failure | **CLOSED FOR SOURCE + STAGE4A EXACT RUN** |
| **P2** (MAJOR) | Rosen Gershgorin row float endpoint addition without outward rounding | Entire diagonal plus two absolute symmetrized off-diagonal terms summed as interval objects; only outward endpoint is tested for strict negativity; conversion to float is display-only | **CLOSED FOR SOURCE + STAGE4A EXACT RUN** |
| **V1** | Canonical Krawczyk root box, rationalization and scalar Newton not explained | Appendix specifies 1000 closed cells, 12-decimal rationalized root centers/preconditioner, radius 1/5000, 35 digit outward arithmetic, exact inclusion criterion, scalar interval Newton and 0<root<1 | **CLOSED IN TEXT** (independent separate proof library not added) |
| **V2** | Nonlinear Rosen+Poincare–Miranda+government derivative missing bridge | Appendix reports SU/IS global face boxes, 100x40 partition, 100 policy cells, local half-width 1/400, 1/1/5 Rosen boxes, strict upper derivative bounds, and exact rational/interval arithmetic boundary | **CLOSED IN TEXT AFTER STAGE4A RUN** |
| **E1** | Negative exporter response misrepresented as own-firm redesign effect | Welfare section now displays Nash envelope identity `Pi_{A,x_A}=0`, separately reports domestic consumer effect about -0.005216220 and competitors' effect on home firm profits about -0.009853524 | **CLOSED IN TEXT** |
| **V3** | Incorrect assertion positive-depth feasible set closed | The proof uses compact weak-acceptance set **including g=0**. Feasible strict positive candidate beating zero/SU ensures proposer optimum is positive-depth IS; no claim g=.05 maximizes | **CLOSED IN TEXT** |
| **V4** | B positive semidefinite assertion without bridge | Short appendix proof via 16 exact-rational vertex principal-minor checks, affine dependence, convex PSD cone; valid for z=x² as well; does not claim positive definiteness at extreme profiles | **CLOSED IN TEXT** |
| **E3** | m-s confused with B's initial acceptance | Results now clarify terminal SU vs SW, B's anticipated IS vs SW, C's IS vs SU outsider and A/B approval | **CLOSED IN TEXT** |
| **N1** | Full Cheng–Huang (2025) proposition-level absorption unresolved | Existing partial primary-source audit remains, open-access search reattempt on 2026-10-21 found publisher preview and first article page only; no accessible complete published Props 1-5. Reconfirmed strong conceptual overlap. | **UNRESOLVED; MATERIAL NOVELTY GATE** |
| **E2** | Specific one-vector example's publication value weak | Explicitly cited **Brander & Spencer (2022)** RIO study showing endogenous horizontal differentiation reverses classic Bertrand/Cournot price/profit ordering; related theory now admits general fixed-vs-endogenous reversals are already prior art. Residual novelty framed only as national government participation forecast under fixed AB-first unchanged-depth agenda. | **CONDITIONAL EDITORIAL VALUE, NOT CURED BY ADDING CITATIONS** |
| **E4/E5** | Some internal editorial language or redundant exposition | De-emphasized generic reversal, preserved failed same-depth nonlinear test; final detailed style pass still useful | **MINOR REMAINS** |

## 2. Stage4/4A re-certification — actual production programs

**Execution evidence:** https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39571673076

- Both rebuilt proof scripts at revised source passed with the actual `verification/v2b_exact_rational_interval.py` coefficient helper; this is distinct from the audit-only monkeypatch runner.
- Rosen entire cube: `SW 1 box/0 split: upper -0.6190518323885061`; `SU 1/0: -0.3585422656810925`; `IS 5/4: -0.09496342972119372`.
- SU uniform interior rectangle `(0.60,0.67)x(0.60,0.65)`, IS `(0.60,0.73)` with all real g in [0,1].
- Total incentive signs certified over 100 exact closed depth cells with zero splits, upper `m'=-0.014278736686089652`, `(i-o)'=-0.01657547425035518`.
- **FAILED preregistered p2 g=.05 frozen C margin retained**: [-.0004403948341162623,-.0004403948309408524] <0.
- **Existential p2 g=.005 frozen C margin**: [.00000090988090427044,.00000090988408551711] >0, and full-depth SU supremum verified via 4000 cells.
- **Conditional p2 endogenous IS(.05) vs SW national gain**: [.01660114679830615,.01660114740943632] >0.
- The canonical p=1 original Stage4A remains frozen. Original and repaired versions do not broaden theta, function class, agenda or theorem quantifiers.

**Limit:** proof trusts mpmath interval kernels/SymPy custom printer and checks; it is not a formal Lean reconstruction of the entire continuous equilibrium result nor an independently coded second interval library.

## 3. Stage7.5A re-review and Stage8 controlled freeze

**Stage7.5A**: all passed p2 proof signs, original failed same-g test, small witness acceptance slack, and institutional counterfactual remain unchanged. Thus the strongest economic contribution classification is still **INSTITUTION-SPECIFIC / MODEL-SPECIFIC EXISTENCE**, with two explicitly tested design maps and **no universal functional-portability claim**. Numerics and re-certified code do not establish economic significance or priority. The relevant CI for the separate preregistered nonlinear diagnostic and four Lean rational-proxy facts was re-triggered; a successful Lean proxy is NOT a substitute for true Nash/continuum certificate.

**Stage8 technical freeze reissue**: `docs/V2B_THEORY_FREEZE_2026-10-21_v2.md` documents the repaired dependencies; `production/freeze_manifest.json` names **v2-CERT-REPAIR** and pins the two repaired nonlinear proof programs, exact rational helper and the new v2 record, while retaining each historically unmodified canonical/Lean/V1 blob. `production/scripts/verify_freeze.py` accepts only the explicit original and reissued identities and checks immutable historical anchors. Original frozen v1 document is unchanged, preserving auditability of the discovered defect and its correction. The v2 manifest/guard **actually PASSED** in [Stage9 run 39572860438](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39572860438) (specific first job `Verify Stage8 economic freeze`), and the same run's independent nonlinear and baseline proof jobs succeeded. This does not make the human author an independent mathematical verifier.

**Caution:** an intermediate Stage9 PDF step failed on a newly added paragraph due to literal `\n` commands rather than line breaks; the typo was corrected on the repair branch in commit `cfd0a94646e3169c9e4b39c8c5f840ff8a0495a0`. The failure is retained in the public CI history. A later, corrected Stage10 source-check and actual 17-page PDF build both PASSED in [workflow 39573190208](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39573190208), from repaired manuscript commit cfd0a94646e3169c9e4b39c8c5f840ff8a0495a0; no overfull boxes were found. This is a regenerated draft, not the portal-generated final submission PDF. The companion [Stage9 run 39573197466](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39573197466) showed all five jobs SUCCESS: v2 blob freeze guard, canonical checks, repaired nonlinear math, limited Lean rational-proxy and bibliography/source-build.

## 4. Manuscript-facing proof and economic bridge status

- **Economic mechanism:** FOC envelope now explicitly identifies why a firm's own adjustment has zero direct first-order profit effect; the rivals' design choices and consumers drive the country's negative indirect welfare term. This directly addresses the original audit's most important missing economic intuition.
- **Government votes:** terminal-SU margin vs initial government's true continuation, inherited depth, and compact offer maximization distinguished.
- **Cournot/utility:** exact rational positive-semidefinite B proof added; original network expectations and national welfare account retained.
- **Machine certificate mapping:** Krawczyk geometry, rationalization, scalar Newton, complete nonlinear root-face / Rosen / implicit derivative route now included in the Appendix.
- **Novelty:** independent article Brander–Spencer (2022) introduced into References and Related Theory. Known reversal of Bertrand/Cournot order due to endogenous differentiation explicitly disclaimed as new; the national-government-specific controlled forecast comparison remains a narrowly defensible candidate.
- **No new economics:** fixed θ, no alternative policy institution, no transfers, no new parameter search. Both pre-registered p2 failure and direct-grand-offer-success alternative are still disclosed.

## 5. Honest editorial decision and stop rule

**Economic claim (maximum):** Within the specified A/B-first, fixed-depth inherited accession game and exact θ witness, fixing the firms' residual product attributes at the fragmented-market Nash values can incorrectly predict a feasible international coalition. Allowing post-policy redesign reverses the national consent incentives for all positive depth while a conditional direct grand offer improves every country over fragmentation. **No claim about an actual ISO/IEC vote, real country rejection, all-standard failure, broad portability, an optimal policy remedy, or generic innovation reversal.**

**Open source-level problem:** Published Cheng–Huang (2025) main-text propositions inaccessible through the public Springer preview and available snippets. Government/firm actor, inherited-depth AB→C protocol and frozen-vs-optimized **country** participation are not seen in accessible parts, but this does NOT prove absence of a more general parent theorem. Buccella et al. 2026 corrigendum content similarly remains paywalled. A source-complete priority certification cannot be signed. On actual absorption evidence, rollback to Stage6; if residual contribution fails editor importance threshold, return to Stage7.5 for candid reframe/research-note decision.

**GO status:** **Technical P1/P2 Stage4A re-certified; Stage13 writing improved and proof bridges installed. Overall Stage13 adversarial verdict still CONDITIONAL due to N1/E2. No Stage14 submission QA PASS and no journal submission.**