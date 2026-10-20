# Independent math checks — scope

Run `python -m pip install -r requirements.txt && python verification/symbolic_audit.py`.

The test checks:
- SW / SU / IS **selected continuation** Cournot linear equations;
- consumer surplus and government welfare identities;
- analytic derivatives;
- fixed-depth accession polynomial;
- interior IS welfare optimum;
- quartic cutoff root;
- eta=.82 C's rejection of same-depth IS;
- eta=.9 symmetric fixed-adoption-cost SU numerical witness, including an optimization over C's gross accession gains.

The checks intentionally **do not** certify:
- every off-path Cournot game with q_i≥0;
- globally unique firms' differentiation Nash equilibria, especially asymmetric strategies;
- existence and uniqueness of SPNE under every bargaining tie rule;
- robustness/novelty/empirical external validity.

For all these blockers, consult `reviews/OPEN_PROOF_OBLIGATIONS.md`.

Archive-machine observation: an equivalent source file was executed under SymPy 1.14.0, with all assertions passing, during archival on 2026-10-21. The in-repository script has CI coverage to independently reproduce the checks.
