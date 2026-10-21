# Stage16 — Actual government depth and welfare: certified vs numerical

Distinct government objects:
- **Feasibility:** for a fixed g, member approves AB against SW, C approves IS against AB at inherited g, incumbents approve IS against AB. This is EXACTLY CERTIFIED for g=.05, lambda in [4.99,5.01].
- **Proposer optimal depth:** among the complete feasible government menu over g in [0,1], choose a subgame-perfect optimal offer accounting for all votes and rejection continuations. A positive strictly feasible offer does NOT identify this argmax.
- **World welfare optimum:** unconstrained planner's maximum; never equate to above.

Numerical-only independent root/scan/optimization at theta0 with lambda=5:
- First outsider-vote root at g≈0.0543332068142; for smaller depths near zero, the C accession margin is positive. This value has not been proven the GLOBAL greatest feasible depth; disjoint positive islands have not been ruled out.
- IS welfare per country minus SW at the first outsider root ≈0.02058599317, or 0.84993% of s=2.42207842172.
- Unconstrained terminal bilateral SU member gain numeric maximum ~0.00022056271 at g~0.0933524.
- Local government optimization over the first accepted IS interval numerically selects the *boundary* g≈0.0543332; this is suggestive, not rigorously proved SPNE argmax. At exact equality C is indifferent, so tie-breaking matters; strict proposals g<cap are admissible.
- At fixed certified offer g=.05, each country's realized IS-SW improvement lies in [0.01899962417, 0.01899996167] (0.78443%–0.78445% of SW).
- Even without global optimization proof, existence of a strictly accepted offer g=.05 and a proposer who can select it makes an agreement payoff attainable. This does not alone certify that *every* optimal-subgame-perfect outcome is IS rather than SU without a full SU envelope comparison.

Follow-up condition: to claim a unique government equilibrium depth, certify full continuous g [0,1] menus, strict best response inequalities, boundary/tie-breaking and no disconnected feasible islands, using interval branch continuation. No handpicked grid, optimizer output or small depth threshold licenses global institutional taxonomy.
