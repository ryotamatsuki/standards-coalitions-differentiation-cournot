# Stage9 frozen V2b reproduction. Requires Python3.12, make and optional TeXLive / Lean.
# Never run historical V1 checker as if it certifies V2b.
PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: freeze table table-check fast-proofs full-proofs lean paper clean help

freeze:
	$(PYTHON) production/scripts/verify_freeze.py

table: freeze
	$(PYTHON) production/scripts/generate_welfare_table.py --write

table-check: freeze
	$(PYTHON) production/scripts/generate_welfare_table.py --check

fast-proofs: freeze
	$(PYTHON) verification/v2b_stage06_pareto_holdout.py
	$(PYTHON) verification/v2b_stage07_welfare_institutions.py

full-proofs: fast-proofs
	$(PYTHON) verification/v2b_stage04a_krawczyk_cleanroom.py
	$(PYTHON) verification/v2b_alt_quadratic_rosen_interval.py
	$(PYTHON) verification/v2b_alt_quadratic_policy_interval.py

lean: freeze
	lean formal/V2bWelfareCore.lean

paper: table
	cd paper && $(LATEXMK) -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex

clean:
	cd paper && $(LATEXMK) -C -outdir=build main.tex || true
	rm -rf paper/build paper/generated

help:
	@echo "Install: python3 -m pip install -r production/requirements-stage9.txt"
	@echo "make freeze       protect frozen theory and proof code Git blobs"
	@echo "make table        regenerate V2b equilibrium welfare table"
	@echo "make table-check  verify deterministic rerender, after table"
	@echo "make fast-proofs  quick checked interval welfare and direct evaluator"
	@echo "make full-proofs  separate Stage4A complete rational interval certificates"
	@echo "make lean         selected exact-rational Lean4 core (pinned lean-toolchain)"
	@echo "make paper        bootstrap LaTeX production scaffold (TeXLive/latexmk)"
