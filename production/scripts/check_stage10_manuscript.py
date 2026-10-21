#!/usr/bin/env python3
"""Stage10: manuscript-facing structural audit; not a scientific proof referee."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper"
MAIN = PAPER / "main.tex"
SECTIONS = [
    "00_introduction","01_model","02_equilibrium","02a_analytic_design_results",
    "03_main_results","03a_policy_benchmark","04_welfare","05_robustness",
    "06_related_literature","07_discussion","A_proofs","A_analytic_proofs"
]
alltext = MAIN.read_text(encoding="utf-8")
errors = []
for section in SECTIONS:
    p = PAPER / "sections" / (section + ".tex")
    if not p.is_file():
        errors.append("Missing section: "+str(p));continue
    v = p.read_text(encoding="utf-8")
    alltext += "\n"+v
    if "\\input{sections/"+section+"}" not in MAIN.read_text(encoding="utf-8"):
        errors.append("Section omitted from main: "+section)
gen = PAPER / "generated" / "welfare_table.tex"
if not gen.is_file():
    errors.append("Missing deterministically generated welfare table; run make table")
else:
    alltext += "\n" + gen.read_text(encoding="utf-8")
consent = PAPER / "generated" / "consent_table.tex"
if not consent.is_file():
    errors.append("Missing Stage13 generated consent table; run make table")
else:
    alltext += "\n" + consent.read_text(encoding="utf-8")
    if r"\input{generated/consent_table.tex}" not in alltext:
        errors.append("Unreferenced Stage13 consent table")
bibliography = (PAPER/"references.bib").read_text(encoding="utf-8")
available_bib=set(re.findall(r"@\w+\s*\{\s*([^,\s}]+)",bibliography))
cited=set()
for match in re.finditer(r"\\cite[pt]?\s*(?:\[[^]]*\])*\s*\{([^}]+)\}",alltext,re.S):
    cited.update(x.strip() for x in match.group(1).split(","))
if not cited:
    errors.append("No live bibliography citations found")
for key in sorted(cited-available_bib):
    errors.append("Undefined citation key: "+key)

# This only checks ordinary LaTeX \label/\ref; full TeX crossref is also
# checked after compilation by the separate PDF job.
defined=re.findall(r"\\label\s*\{([^}]+)\}",alltext)
if len(defined)!=len(set(defined)):
    errors.append("Duplicate LaTeX label(s)")
referenced=set(re.findall(r"\\(?:eqref|ref|autoref)\s*\{([^}]+)\}",alltext))
for key in sorted(referenced-set(defined)):
    errors.append("Undefined LaTeX label: "+key)

for text in ("Stage 10 section reserved","Stage 9 production scaffold only",
             "The abstract and main text are deliberately reserved"):
    if text.lower() in alltext.lower():
        errors.append("Unreplaced production placeholder: "+text)
for path in SECTIONS:
    p=PAPER/"sections"/(path+".tex")
    if p.is_file() and "STAGE 10 SECTION RESERVED" in p.read_text("utf-8").upper():
        errors.append("Unwritten section "+path)

core = [
    r"\label{eq:utility}",r"\label{eq:Mq}",r"\label{eq:design-bridge}",
    r"\label{eq:member-path}",r"\label{eq:outsider-path}",
    r"\label{eq:rejection}",r"\label{eq:frozen-votes}",
    r"\label{eq:pareto}",r"\label{eq:failed-comparison}",
    r"\label{eq:app_krawczyk}",r"\label{tab:v2b-consent-margins}",r"\label{app:rosen-bound}"
]
for needle in core:
    if needle not in alltext:
        errors.append("Missing proof-critical bridge: "+needle)

if "9.09" not in alltext or "-0.000440395" not in alltext:
    errors.append("Frozen-positive nonlinear C margin or original negative test missing")
if "not" not in alltext.lower() or "Lean 4" not in alltext:
    errors.append("Proof-scope disclosure missing")

if errors:
    print("STAGE10 STRUCTURAL AUDIT FAILED")
    print("\n".join("- "+err for err in errors))
    sys.exit(1)
print("STAGE10 STRUCTURAL AUDIT PASS")
print("Live citations:", len(cited), "unique keys")
print("LaTeX labels:",len(defined),"and references:",len(referenced))
print("Sections:",len(SECTIONS),"plus generated welfare table")
print("Scope: source-form structural/reviewer bridge presence; NOT proof correctness")
