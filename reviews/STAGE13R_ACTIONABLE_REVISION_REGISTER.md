# Stage 13R: Actionable revision register

Reviewed manuscript SHA: `c7b52ac10a701c682479e8f57c1343ceed1df719`. Date: 23 October 2026 JST. Simulated editorial/referee judgment, not a JPET decision. Original manuscript, figures, scientific code and Theory Freeze are unchanged. Locations refer to the canonical 20-page PDF and frozen TeX.

This is the controlling issue list. Categories are simulated referee judgments. No FATAL error was established. Tier 1 means required before submission; Tier 2 strongly improves submission quality; Tier 3 is optional. An editorial Tier 1 issue need not be a mathematical error. Exact English blocks below are adopted proposals, not edits to the frozen manuscript. Where an action requires a figure label, citation, or author fact, the non-prose instructions form part of the implementation specification.

| Issue | Severity | Tier | Location | Dependency |
|---|---|---|---|---|
| 13R-01 | MAJOR | 1 | pp.1,3; §1 first paragraph; §2.1, eqs.(2)–(3), main TeX L37,58–71 | None |
| 13R-02 | MAJOR | 1 | p.7 §4.2 economic interpretation; pp.8–9 §5; main L222–223,289 | 13R-01 |
| 13R-03 | MODERATE | 1 | pp.8–9; Theorem 3 and explanation; main L258–268,289 | 13R-02 |
| 13R-04 | MODERATE | 1 | p.8 after Theorem 3; main L268 | None |
| 13R-05 | MAJOR | 1 | pp.8–9 Theorem 4 proof; pp.16–18 Appendix E; main L283–300; supplement L26–79 | 13R-03,13R-06 |
| 13R-06 | MODERATE | 1 | p.7 eqs.(16)–(18); p.14 Appendix A final paragraph; main L198–219,428 | 13R-01 |
| 13R-07 | MODERATE | 2 | pp.5–6 §3; p.12 §7.1; pp.15,19 Appendices B,F | 13R-05 |
| 13R-08 | MODERATE | 2 | pp.16–18 Appendices D,E; references p.20 | 13R-05 |
| 13R-09 | MODERATE | 2 | p.15 Appendix C final sentence; pp.18–20 Appendix F; main L456; supplement L99–112 | 13R-07 |
| 13R-10 | MAJOR | 1 | pp.2,13 §1/§8; main L41,395–402 | 13R-02 |
| 13R-11 | MODERATE | 2 | pp.2,6–9,11–14; main L41,50,52,180,219,223,281,302,364,371,398,400,407 | 13R-05,13R-10 |
| 13R-12 | MODERATE | 2 | p.1 Abstract; main L30–32 | 13R-02,13R-03 |
| 13R-13 | MODERATE | 2 | pp.12–14 §§7–9; main L370–407 | 13R-10,13R-11 |
| 13R-14 | MODERATE | 2 | p.11 Figure 3; §5.1 main L340–347; TikZ labels | 13R-05 |
| 13R-15 | MINOR | 3 | p.5 Figure 1; p.8 Figure 2; main L105–132,228–252 | 13R-02 |
| 13R-16 | MODERATE | 2 | p.10 Tables 1–2; main L307–338 | 13R-02,13R-03 |
| 13R-17 | MODERATE | 1 | p.18 Appendix E replication map; p.20 declarations; supplement L67–79 | 13R-05 |
| 13R-18 | MAJOR | 1 | pp.1,20; title/declarations; submission package; main L25–27,460–464 | 13R-17 |

## 13R-01

**Severity:** MAJOR

**Location:** pp.1,3; §1 first paragraph; §2.1, eqs.(2)–(3), main TeX L37,58–71

**Original:** A common compatibility standard can increase the value of consumption across jurisdictions.

**Problem:** Compatibility is described as a network benefit without explaining that increasing g also raises substitution in B; the international wording can suggest cross-destination network quantities absent from the displayed utility.

**Why it matters:** A referee cannot evaluate whether the public policy and the demand specification represent the same economic object.

**Evidence:** B_g=rho H_g, M_g=(rho-eta)H_g; eq.(3) has quantities in one destination market.

**Recommended action:** Insert the demand interpretation after eq.(2); make the opening about compatibility between goods from different origins. Add numeraire and expectation timing clarification.

**Proposed revised English:**

Each firm chooses residual similarity x_i; a higher x_i saves the cost of differentiation. The government chooses the depth g of compatibility between goods supplied from member countries. A deeper agreement has two effects in demand: it increases cross-product substitution through B and expands the network interaction through H. The parameter rho weights the public component of substitution, while eta measures the network benefit. Hence greater compatibility need not raise every country’s welfare even before firms adjust their designs. Network quantities in the model are measured within each destination market; the same origin-based compatibility links apply in all three markets.

**Expected improvement:** Explains the key primitive trade-off while preserving the demand system.

**Risk of revision:** Do not introduce a global network or alter H, B, or expectations.

**Priority:** Tier 1 — Required before submission

**Dependencies:** None

**Verification:** Read the revised definition against each off-diagonal demand coefficient.

## 13R-02

**Severity:** MAJOR

**Location:** p.7 §4.2 economic interpretation; pp.8–9 §5; main L222–223,289

**Original:** Standardization changes the privately desirable residual characteristics.

**Problem:** The private response direction and the government rejection sequence remain implicit. Repeating that the envelope theorem fails does not explain why redesign occurs or how it blocks the initial proposal.

**Why it matters:** This is the principal editorial significance risk: the result can look like a numerical derivative reversal rather than a theory of consent.

**Evidence:** Appendix B positive forcing and M-matrix imply u'>v'>0 at the center; eqs.(7),(18),(21).

**Recommended action:** Replace the interpretation with the adopted mechanism paragraph; add the adopted backward-induction paragraph after the main result.

**Proposed revised English:**

Near fragmentation at the benchmark, a deeper bilateral agreement reduces the member firms’ private return to maintaining costly residual differentiation. Their equilibrium similarity choices rise, and the outsider also adjusts its design. Each firm accounts for its own design cost and operating profit, but not for the resulting loss of domestic consumer surplus. Moreover, a home firm’s first-order condition does not remove the effects of its rivals’ design changes on its worldwide profits. Together these responses subtract from the member’s fixed-design welfare gain. When this induced loss exceeds the direct gain, both the stand-alone bilateral margin and, by three-country symmetry, the outsider’s accession margin become negative.

**Expected improvement:** Connects cost-saving redesign, quantity effects and national incidence to government behavior.

**Risk of revision:** Restrict the response-direction interpretation to the certified/local setting.

**Priority:** Tier 1 — Required before submission

**Dependencies:** 13R-01

**Verification:** Confirm the signs with Appendix B; trace the last vote backward to initial B acceptance.

## 13R-03

**Severity:** MODERATE

**Location:** pp.8–9; Theorem 3 and explanation; main L258–268,289

**Original:** the bilateral-member and outsider-accession conditions fail

**Problem:** m-s is a stand-alone bilateral margin, not generally the initial acceptance payoff when B anticipates successful integration. The theorem is correct with its other conditions, but the shorthand obscures backward induction.

**Why it matters:** A game theorist may mistakenly infer that B compares m with s even when integration follows.

**Evidence:** §2.2 explicitly says initial acceptance compares the actual continuation; eq.(7).

**Recommended action:** Introduce the two comparisons before Theorem 3 and use “stand-alone bilateral margin” in its statement. Retain the other slope assumptions and proof.

**Proposed revised English:**

The local result separates two comparisons. The inequality m(g)>s asks whether a bilateral arrangement is preferable to fragmentation if it remains bilateral. The inequality i(g)>o(g) asks whether the outsider wants to enlarge that arrangement. Neither comparison alone describes the initial acceptance vote, which depends on the anticipated accession continuation. The following theorem combines these margins with the incumbent approval and integrated-welfare conditions.

**Expected improvement:** Distinguishes economic margins from actual voting strategies.

**Risk of revision:** Do not replace the extensive-form gate with a simultaneous or myopic rule.

**Priority:** Tier 1 — Required before submission

**Dependencies:** 13R-02

**Verification:** At histories with successful accession verify that B compares i with s, not m with s.

## 13R-04

**Severity:** MODERATE

**Location:** p.8 after Theorem 3; main L268

**Original:** Both treatments use the same governmental strategies and payoffs

**Problem:** The phrase says reduced payoffs are unchanged even though their change is the result of the paper.

**Why it matters:** A literal contradiction weakens the identifying comparison.

**Evidence:** m_F and m_N have opposite slopes in eq.(18).

**Recommended action:** Replace the sentence with the adopted distinction between primitives/objectives/rules and induced payoff functions.

**Proposed revised English:**

Both treatments preserve the economic primitives, governments’ welfare objectives, and the proposal and voting rules. They differ in the constraint on firms’ post-policy design choices and therefore in the induced government payoff functions.

**Expected improvement:** Removes a conceptual wording inconsistency.

**Risk of revision:** Low: no equation changes.

**Priority:** Tier 1 — Required before submission

**Dependencies:** None

**Verification:** Search for all “same payoffs” claims and distinguish primitive objectives from reduced payoffs.

## 13R-05

**Severity:** MAJOR

**Location:** pp.8–9 Theorem 4 proof; pp.16–18 Appendix E; main L283–300; supplement L26–79

**Original:** Proof architecture and certified bounds

**Problem:** The main proof combines computational objects, 13-digit output, earlier audit language and continuity in long paragraphs. Correct ingredients are present, but a referee must build the dependency structure themselves.

**Why it matters:** The central theorem needs an intelligible proof without requiring the reader first to reverse-engineer the repository.

**Evidence:** Fresh 1,000-interval replay; Appendix D uniqueness and Appendix E closed feasible set; accepted frozen candidate beats the full bilateral envelope.

**Recommended action:** Use three named steps in the main proof, add one compact certificate table in Appendix E, and retain the full inclusion formulas and symmetry lift. Round displayed bounds conservatively, e.g. m_N'<-0.00797, (i_N-o_N)'<-0.01503.

**Proposed revised English:**

The proof has three steps. First, Appendix D establishes positive quantities and a unique design Nash equilibrium on the full strategy cube; symmetry then permits the reduced bilateral and integrated systems. Second, interval inclusions cover every depth in [0,1] and bound the endogenous derivatives of m and i-o strictly below zero. Since both welfare gaps vanish at zero depth, integration makes the corresponding level gaps negative at every positive depth. In the fixed-design counterfactual, a strictly accepted integrated proposal at g=1/20 dominates fragmentation and an upper bound on the bilateral payoff at every depth. Maximizing integrated welfare over the closed accepted-depth set therefore implements integration. Third, the uniform regularity and strict welfare margins persist in a sufficiently small common neighborhood of the primitives. This gives the open-set result without assigning a numerical radius to that neighborhood.

**Expected improvement:** Makes what is proved by analysis, computation, and continuity separately assessable.

**Risk of revision:** Never replace all-depth certification by sampled g values; retain uniform margins near zero.

**Priority:** Tier 1 — Required before submission

**Dependencies:** 13R-03,13R-06

**Verification:** Replay exact targets after editing; confirm the accepted IS maximization is on a closed feasible set.

## 13R-06

**Severity:** MODERATE

**Location:** p.7 eqs.(16)–(18); p.14 Appendix A final paragraph; main L198–219,428

**Original:** Direct differentiation and substitution ... yield

**Problem:** The most important economic derivative is asserted in the main text and again summarized in the appendix without showing the short output-derivative-to-welfare calculation.

**Why it matters:** The chain rule proof is clear only after the national gradient is independently understood; the gap increases referee effort.

**Evidence:** Fresh full-matrix calculation gives W_A,x=(-0.0338879983,-0.1397089653,-0.1397089653); algebra yields the adopted equations.

**Recommended action:** Add the three short derivative identities to Appendix A. Keep C and V interpretation in the body.

**Proposed revised English:**

At the symmetric no-agreement Nash, a unilateral increase in x_j changes outputs according to
\[
(q_{x_j})_j=-\frac{\beta\alpha q_0}{PL},\qquad
(q_{x_j})_k=-\frac{\beta(\alpha-2t)q_0}{2PL}\quad(k\ne j).
\]
Consequently \(\partial_{x_j}CS=-C\) for every j. For the resident firm, its own design derivative is zero by its Nash first-order condition, whereas
\[
\partial_{x_k}\Pi_j=6q_0(q_{x_k})_j=-V\quad(k\ne j).
\]
Adding consumer surplus to resident profit yields Equation (16), and the chain rule then gives Equation (18).

**Expected improvement:** Provides the missing economic algebra rather than more generic proof narration.

**Risk of revision:** Preserve the positive V term in the loss and the unilateral derivative convention.

**Priority:** Tier 1 — Required before submission

**Dependencies:** 13R-01

**Verification:** Symbolically substitute q0=d/L and compare with C,V; re-evaluate the national gradient.

## 13R-07

**Severity:** MODERATE

**Location:** pp.5–6 §3; p.12 §7.1; pp.15,19 Appendices B,F

**Original:** The implicit Nash response rather than a planner response

**Problem:** Repeated cautions and u′ versus nu near-homographs create unnecessary notation load. Appendix F also reuses M,J,H,V with different meanings from the model.

**Why it matters:** These are avoidable interruptions for a reader already following the equilibrium system.

**Evidence:** Main eqs.(2),(12),(17),(24); Appendix F uses M(g,p),J(g,p),H(g,p),V(g,p).

**Recommended action:** Use “Private design equilibrium” as the subsection heading; retain one unilateral-FOC warning. In Appendix F use Δ_m, Δ_a, Δ_i, Δ_b for payoff gaps; list them once. Retain u′,v′ in equations if changing them risks cross-reference churn.

**Proposed revised English:**

For the restricted network-boundary argument, write \(\Delta_m=m-s\), \(\Delta_a=i-o\), \(\Delta_i=i-s\), and \(\Delta_b=i-m\). This notation distinguishes welfare gaps from the Cournot matrix M, the firm-design Jacobian J, and the compatibility matrix H used elsewhere. The member and outsider design responses remain u′ and v′; the outsider welfare derivative is nu.

**Expected improvement:** Keeps conceptual distinctions without repeatedly teaching the reader what not to do.

**Risk of revision:** Renaming must be mechanical and scoped; do not alter any derivative matrix.

**Priority:** Tier 2 — Strongly recommended

**Dependencies:** 13R-05

**Verification:** Search every changed symbol and compile; verify Appendix F inequalities are unchanged.

## 13R-08

**Severity:** MODERATE

**Location:** pp.16–18 Appendices D,E; references p.20

**Original:** strong-monotonicity/Rosen argument

**Problem:** The proof invokes named game and interval methods without bibliographic support.

**Why it matters:** An external referee needs a standard reference for theorem conditions, distinct from an internal audit report.

**Evidence:** Verified Rosen 1965 source and Rump 2010 DOI; full-cube analytic inequality is already supplied.

**Recommended action:** Cite Rosen and Rump at the relevant proof steps; keep the sufficient bound and state its domain, rather than suggesting citations replace proof.

**Proposed revised English:**

Appendix D uses the strict concavity and diagonal strict concavity argument for concave games in Rosen (1965). Appendix E uses interval inclusion methods of the kind surveyed by Rump (2010). The analytical uniqueness argument and the interval root inclusions perform distinct tasks: the former excludes other full-game Nash equilibria, and the latter encloses the interior continuation and its derivatives over the depth interval.

**Expected improvement:** Places the technical argument in standard economic and numerical-analysis practice.

**Risk of revision:** Citations do not certify this implementation or replace root inclusion evidence.

**Priority:** Tier 2 — Strongly recommended

**Dependencies:** 13R-05

**Verification:** Check reference metadata and ensure both sources are cited in the text.

## 13R-09

**Severity:** MODERATE

**Location:** p.15 Appendix C final sentence; pp.18–20 Appendix F; main L456; supplement L99–112

**Original:** eta_c(rho)=6/7+(211/196)(rho-1)+O((1-rho)^2)

**Problem:** The first-order coefficient appears without a derivation. The active-strip proof is compact and treats an equilibrium approaching the boundary x=1 without explicitly showing inward continuation.

**Why it matters:** A correct auxiliary boundary can still be hard to audit; it must not look like a universal phase theorem.

**Evidence:** Independent symbolic calculation: mu_eta=2401d²/512 and -mu_rho/mu_eta=211/196. At beta=0 the first-order loss is zero.

**Recommended action:** Add the adopted derivative calculation; state fixed d,kappa and 0<eta<1. Add the inward first-order design displacement for beta>0 or reference its explicit FOC expansion.

**Proposed revised English:**

For fixed d,kappa>0, restrict attention to 0<eta<1. At the critical face point, the first-order response of t=(1-rho)z to rho is -1 because z=1 at rho=1. Moreover the induced-design loss is of order (1-rho)^2. Direct differentiation gives
\[
\partial_\eta\mu=\frac{2401d^2}{512},\qquad
\partial_\rho\mu=-\frac{2401d^2}{512}\frac{211}{196}.
\]
The implicit-function theorem therefore gives eta_c'(1)=211/196. This expansion describes the restricted near-face cutoff, not the rho=0.9 numerical slice.

**Expected improvement:** Makes the reported coefficient traceable while retaining the restricted strip.

**Risk of revision:** Do not transfer this expansion to rho=0.9 or infer a global adjustment-cost cutoff.

**Priority:** Tier 2 — Strongly recommended

**Dependencies:** 13R-07

**Verification:** Verify expansion symbolically; ensure no dimension or parameter domain was broadened.

## 13R-10

**Severity:** MAJOR

**Location:** pp.2,13 §1/§8; main L41,395–402

**Original:** its broader economic priority and generality should not be exaggerated

**Problem:** The closest-paper distinction is stated defensively rather than through its actual primitives and propositions.

**Why it matters:** A JPET editor familiar with Takarada et al. can otherwise read this as another outsider-veto paper.

**Evidence:** Publisher full text checked: Takarada §§2,4–5 and Propositions 2,5,6. Their standards correct negative externalities and alter compliance costs; their solution concept is the core.

**Recommended action:** Adopt the precise Takarada paragraph and merge the principal contribution comparison into the Introduction. Retain other background citations compactly. Do not claim exhaustive priority over unread supplements.

**Proposed revised English:**

Takarada et al. (2020) analyze standards that reduce negative consumption externalities while raising compliance costs. Their Proposition 2 makes regional harmonization beneficial to both members and the outsider; Propositions 5–6 relate outsider opposition and core stability to transboundary externalities. Here the governmental agreement procedure is held fixed across the design comparison, and downstream residual-design responses can also eliminate the members’ stand-alone gain from a bilateral agreement. Our equilibrium concept is the specified extensive-form procedure, not the core. Accordingly, the contribution is neither the generic possibility of outsider opposition nor a new proof that regionalism can obstruct multilateralism.

**Expected improvement:** Shows why loss of the members’ bilateral gain and the controlled redesign comparison differ from the predecessor.

**Risk of revision:** Different solution concepts do not by themselves establish novelty; do not claim their firms never adapt in any sense.

**Priority:** Tier 1 — Required before submission

**Dependencies:** 13R-02

**Verification:** Verify each sentence against predecessor §§2,4–5; keep main-text and supplement evidence levels distinct.

## 13R-11

**Severity:** MODERATE

**Location:** pp.2,6–9,11–14; main L41,50,52,180,219,223,281,302,364,371,398,400,407

**Original:** not a new economic discovery

**Problem:** Repeated self-assessments and research-process language displace positive explanations.

**Why it matters:** The prose sounds like responses to earlier agents rather than a finished scholarly argument.

**Evidence:** Scope is already explicitly defined in Theorems 3–4, §6 and figure caption; repetition is not needed for rigor.

**Recommended action:** Delete the novelty self-rating after Lemma 1; retain its accession meaning. Replace “previously certified/independently checked/manuscript-facing” with statements of results and stable appendix references. Keep one institutional-scope paragraph and each result’s essential quantifier.

**Proposed revised English:**

The contribution is a controlled comparison of national consent with and without downstream residual redesign. Firms’ own-profit optimality leaves two national effects: the response of domestic consumer surplus and the response of the home firm’s profits to its rivals’ designs. We derive these effects and show that they can overturn the direct benefit of compatibility. Three-country symmetry links the member’s stand-alone welfare derivative to the outsider’s accession derivative. The all-depth result then rules out restoration of agreement by choosing a different inherited depth. Thus the economic result concerns the implementation of cooperation under a specified procedure, rather than the welfare chain rule alone.

**Expected improvement:** Keeps humility in claim scope while allowing the substantive discovery to lead.

**Risk of revision:** Do not delete local/all-depth qualifiers, conditions, or the exploratory-map warning.

**Priority:** Tier 2 — Strongly recommended

**Dependencies:** 13R-05,13R-10

**Verification:** Compare all theorem quantifiers before/after; every deleted caution must be covered by one explicit scope statement.

## 13R-12

**Severity:** MODERATE

**Location:** p.1 Abstract; main L30–32

**Original:** Adjustment costs and network intensity delineate additional, explicitly limited boundaries.

**Problem:** The abstract is compliant in length but ends with secondary boundary bookkeeping and a literature disclaimer rather than the main public-economic implication.

**Why it matters:** Abstract readers should immediately understand the policy comparison and its institutional domain.

**Evidence:** Python counts 187 whitespace-delimited words in current abstract; no 250-word breach was found.

**Recommended action:** Adopt the single replacement abstract. Retain an ordinary theory abstract; structured-heading uncertainty is handled in 13R-18.

**Proposed revised English:**

Can firms’ product redesign change whether governments agree on compatibility standards? We study three countries whose firms choose costly residual differentiation before competing in quantities. Governments negotiate compatibility through a bilateral-first procedure in which subsequent accession inherits the original depth. We compare this game with a counterfactual that fixes product designs at their no-agreement Nash levels. Private redesign affects domestic consumer surplus and the home firm’s worldwide profits; these national effects are not eliminated by the firm’s own-profit first-order condition. Under explicit sufficient conditions, redesign reverses both a bilateral member’s stand-alone welfare gain and the outsider’s gain from accession. A computer-assisted proof establishes an open parameter neighborhood in which the government-optimal outcome switches from integration with fixed designs to fragmentation with endogenous designs. Yet a direct multilateral proposal can benefit all three countries. The result identifies how private design responses and inherited agreement terms jointly determine national consent, rather than a general obstacle to compatibility cooperation.

**Expected improvement:** Emphasizes national consent and the implemented outcome without strengthening the theorem.

**Risk of revision:** Do not turn an open-neighborhood existence result into an arbitrary-parameter claim.

**Priority:** Tier 2 — Strongly recommended

**Dependencies:** 13R-02,13R-03

**Verification:** Count words and compare each assertion with Theorems 3–4 and Proposition 5.

## 13R-13

**Severity:** MODERATE

**Location:** pp.12–14 §§7–9; main L370–407

**Original:** Relationship to the literature and interpretation

**Problem:** A second late contribution pitch and an abrupt technical network-face paragraph dilute the route-to-agreement finding. Conclusion repeats caution language.

**Why it matters:** Readers should finish with the economic implication, not another priority defense.

**Evidence:** §1 already introduces the closest literature; §6 provides the essential institutional interpretation.

**Recommended action:** Merge §8’s substantive comparison into §1; keep the lambda proposition with a short interpretation, compress §7.2 to a boundary paragraph and appendix link; adopt the replacement conclusion.

**Proposed revised English:**

Governments’ willingness to coordinate compatibility can depend on how firms redesign the product characteristics left outside the agreement. In our model, private design optimality does not eliminate the effects on domestic consumers or the effects of rivals’ designs on the resident firm’s worldwide profits. These national effects can reverse the consent predicted by a fixed-design comparison.

The distinction changes the implemented government outcome in a nonempty open neighborhood of the benchmark parameters. Fixed designs support an optimal integrated proposal, while endogenous designs produce fragmentation throughout the depth menu under inherited-depth bilateral accession. A direct integrated proposal can nevertheless improve every country’s welfare. The economic implication is that evaluating compatibility requires both a private-design continuation and a specified rejection option. The result does not select among unrestricted bargaining institutions or quantify actual agreement gains.

**Expected improvement:** Shortens the narrative without deleting a supporting proof or result.

**Risk of revision:** Preserve all citations still supporting claims; moving text requires cross-reference updates.

**Priority:** Tier 2 — Strongly recommended

**Dependencies:** 13R-10,13R-11

**Verification:** Outline read: question → model → incidence → implemented outcome → institution → boundaries → conclusion.

## 13R-14

**Severity:** MODERATE

**Location:** p.11 Figure 3; §5.1 main L340–347; TikZ labels

**Original:** SW

**Problem:** The plot labels look like categorical proven regimes even though light cells mean no successful offer found. The caption qualifies this, but the visual can travel without its surrounding text.

**Why it matters:** A reader may incorrectly infer certified two-dimensional nonexistence or a no-SU theorem.

**Evidence:** All 41×41 cells in both panels reconcile to the archived numeric array, but that is data-to-figure consistency, not exhaustive depth certification.

**Recommended action:** Replace in-panel SW by “No offer found” and IS by “IS candidate”; add a visible legend and adopted caption; put detailed search settings and artifact SHA in supplement.

**Proposed revised English:**

Numerical search outcomes with fixed designs (left) and endogenous designs (right), for d=1, rho=0.9, and lambda=0. Dark shading: an accepted integrated candidate dominates the computed bilateral candidates. Light shading: no profitable accepted offer found. In-panel labels describe search outcomes, not proven regimes. The star marks the separately certified benchmark (kappa,eta)=(0.8505,0.758). No optimal bilateral outcome was identified in this search. Boundaries are exploratory; no certified neighborhood is plotted.

**Expected improvement:** Makes the epistemic status visible within the figure itself.

**Risk of revision:** Do not shade an unquantified certified neighborhood; preserve the center star only.

**Priority:** Tier 2 — Strongly recommended

**Dependencies:** 13R-05

**Verification:** Inspect at final width and grayscale; verify all cells and star positions again if regenerated.

## 13R-15

**Severity:** MINOR

**Location:** p.5 Figure 1; p.8 Figure 2; main L105–132,228–252

**Original:** Firms simultaneously select Nash residual designs

**Problem:** Figure 1 boxes force distracting hyphenation; Figure 2 mostly restates the equations and is optional.

**Why it matters:** This is a reading-efficiency issue, not a layout failure or proof flaw.

**Evidence:** Visual inspection of all 20 pages; no clipped labels or overlapping boxes established.

**Recommended action:** Shorten boxes to “Firms choose residual designs”, “Cournot competition”, “National welfare”, “Government decisions”. Retain Figure 2 as the compact local comparison, with its existing local-scope qualification.

**Proposed revised English:**

Figure 1. Government timing and continuation payoffs. A proposes bilateral depth, B votes while anticipating accession, and C and the incumbents decide enlargement at the inherited depth. For every terminal policy pattern, firms choose residual designs and then compete in quantities; governments anticipate the resulting national welfare. Box labels: “Firms choose residual designs”; “Cournot competition”; “National welfare”; “Government decisions”.

**Expected improvement:** Improves display clarity without increasing the figure count.

**Risk of revision:** Removing Figure 2 requires updating its cross-reference; no scientific content should depend on it.

**Priority:** Tier 3 — Optional

**Dependencies:** 13R-02

**Verification:** Render at submission width and read all labels without zoom.

## 13R-16

**Severity:** MODERATE

**Location:** p.10 Tables 1–2; main L307–338

**Original:** Although i_N-s is positive ... [Table 2 interrupts sentence]

**Problem:** Table 2 splits one sentence across its float. Table 1 repeats many scope cautions and lacks displayed proposition numbers.

**Why it matters:** The float interrupts the explanation of the economic contrast at the exact point where the reader needs the rejection options.

**Evidence:** Canonical PDF p.10, independently reproduced table values.

**Recommended action:** Place the complete two-sentence interpretation immediately after Table 2. Retain Table 1, add theorem/proposition numbers, and shorten its repeated scope language; keep every result condition explicit.

**Proposed revised English:**

At g=0.05, an integrated agreement improves every country’s welfare relative to fragmentation under either design treatment. With endogenous design, however, the outsider prefers the bilateral outside option to integration; anticipating failed accession, the initial member rejects the bilateral arrangement because its stand-alone payoff is below fragmentation. These values illustrate the consent comparisons in the model and are not calibrated welfare estimates.

**Expected improvement:** Makes the numerical example an economic explanation rather than a detached table.

**Risk of revision:** Do not present the uncalibrated gaps as empirical percentages or exact welfare losses.

**Priority:** Tier 2 — Strongly recommended

**Dependencies:** 13R-02,13R-03

**Verification:** Verify numbers round to nine decimals and that no sentence crosses the table.

## 13R-17

**Severity:** MODERATE

**Location:** p.18 Appendix E replication map; p.20 declarations; supplement L67–79

**Original:** The commands, run from the repository root, are

**Problem:** The immutable source mapping is useful, but installation/precision/software details and a final release link are not self-contained in the article package.

**Why it matters:** A reviewer needs a runnable environment and must distinguish manuscript SHA from certificate SHA.

**Evidence:** Current primary executables are byte-identical to 54ac8389...; clean invocation initially lacked mpmath, then passed after installation.

**Recommended action:** Supply the existing interval requirements file plus exact successful versions, precision, commands, hashes and expected output in a compact supplementary README. Link a frozen release in the article.

**Proposed revised English:**

The computer-assisted step certifies roots of the unilateral design conditions and welfare-derivative bounds, rather than a grid of government outcomes. For each of 1,000 adjacent depth intervals, the bilateral system uses a two-variable Krawczyk inclusion and the integrated system uses a scalar interval-Newton inclusion. Global Nash uniqueness identifies these enclosed roots with the full three-firm equilibrium, including unilateral deviations that break policy symmetry. The certification table reports conservative outward bounds; the economic inference follows by integrating the welfare derivatives and applying the government consent inequalities.

**Expected improvement:** Makes proof reproduction practical without treating previous PASS prose as evidence.

**Risk of revision:** Do not overwrite the historical certificate source or imply the exploratory map is certified by its replay.

**Priority:** Tier 1 — Required before submission

**Dependencies:** 13R-05

**Verification:** Fresh environment install and one complete replay; compare hashes and expected margins.

## 13R-18

**Severity:** MAJOR

**Location:** pp.1,20; title/declarations; submission package; main L25–27,460–464

**Original:** Review working draft—author details withheld

**Problem:** Author details and disclosures remain placeholders. Figure production and structured-abstract instructions require stage-sensitive interpretation rather than blanket compliance claims.

**Why it matters:** The current file is not ready for submission even if its science is correct.

**Evidence:** Current JPET author guidance checked directly; decision log in compliance audit. No portal submission was attempted.

**Recommended action:** Have the author supply verified identity, affiliation, contact, ORCID, funding, conflicts, acknowledgment, AI-use details and archive identity. Use the adopted conditional declaration template; prepare separate production graphics; resolve ambiguous format instructions in final package QA.

**Proposed revised English:**

Author: [author-confirmed full name]. Affiliation where the research was conducted: [author-confirmed affiliation or independent-researcher designation]. Correspondence: [author-confirmed email]. ORCID: [verified ORCID].

Funding: [state all actual support; if accurate, “This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.”]

Conflicts of interest: [author-confirmed disclosure; if accurate, “The author declares no conflicts of interest.”]

Data and code availability: “The computational sources, generated numerical results, and reproduction instructions supporting this study are available at [archived release URL], manuscript commit [SHA], and certificate-source commit [SHA].” Add “No empirical dataset was collected” only if accurate; do not use “no data were generated” for a paper generating numerical arrays.

AI assistance (complete with actual tools, dates/versions where known, and tasks): “During the preparation of this work, the author used [tools] for [drafting, code assistance, symbolic or numerical checks, as applicable]. The author reviewed the resulting text, code, and calculations and takes responsibility for the final manuscript and its claims.” This sentence may be used only after the review it states has occurred; it does not itself establish independent human verification.

Acknowledgments: [actual contributions and permissions, or omit if none]. Research ethics: [if accurate: “This theoretical and computational study involved no human participants or animal research.”]

**Expected improvement:** Closes actual submission omissions without fabricating author-only facts.

**Risk of revision:** Do not infer employment affiliation, absence of funding/conflict, or completed human verification from conversation history.

**Priority:** Tier 1 — Required before submission

**Dependencies:** 13R-17

**Verification:** Author confirms every factual declaration; inspect actual upload fields and generated peer-review PDF before submission.
