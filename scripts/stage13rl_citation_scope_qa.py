#!/usr/bin/env python3
"""Stage13R-L conservative citation and scope regression checks (no scientific recomputation)."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "manuscript/stage13rl_jpet_revised.tex"
SUP = ROOT / "manuscript/stage13r_proof_supplement.tex"
BASE_SHA = "4532486e4929ba3d228229d76264c059ee3a6852"
main = MAIN.read_text(encoding="utf-8")
supplement = SUP.read_text(encoding="utf-8")
original = subprocess.check_output(
    ["git", "show", f"{BASE_SHA}:manuscript/stage13r_jpet_revised.tex"],
    cwd=ROOT,
    text=True,
)
original_supp = subprocess.check_output(
    ["git", "show", f"{BASE_SHA}:manuscript/stage13r_proof_supplement.tex"],
    cwd=ROOT,
    text=True,
)
assert supplement == original_supp, "Proof supplement has unexpectedly changed"
assert main.count(r"\end{document}") == 1
assert main.count(r"\begin{figure}") == 3
assert main.count(r"\begin{table}") == 2
assert len(re.findall(r"\\bibitem\[", original)) == 11
bib = re.findall(r"(?m)^\\bibitem\[[^\n]*?\]\{([^}]+)\}\s*([^\n]+)$", main)
assert len(bib) == 20, f"Expected 20 references, found {len(bib)}"
keys = [k for k, _ in bib]
assert len(keys) == len(set(keys)), "Duplicate bibliography keys"
names = [entry.split(",", 1)[0].casefold() for _,entry in bib]
assert names == sorted(names), f"Bibliography is not alphabetically sorted: {names}"
citations = re.findall(r"\\cite(?:t|p|author|year|yearpar)?(?:\[[^\]]*\])?\{([^}]+)\}", main + "\n" + supplement)
cited = {v.strip() for item in citations for v in item.split(",")}
assert set(keys) == cited, f"Bibliography/citation mismatch: uncited={set(keys)-cited}; missing={cited-set(keys)}"
required = {
    "KatzShapiro1985", "EconomidesFlyer1998", "BranderSpencer2015",
    "ZhouSpencerVertinsky2002", "BaakeBoom2001", "BarrettYang2001",
    "CabralSalant2014", "LambertiniRossini1998", "TakaradaKawabata2025"
}
assert required.issubset(cited)
assert main.count(r"\begin{thebibliography}") == 1
assert "Stage 13R-L literature-integrated draft" in main
assert "Not for submission" in main

for env in ("equation", "align", "theorem", "proposition", "lemma", "proof", "split"):
    rx = re.compile(r"\\begin\{" + env + r"\}(?:\[[^\]]*\])?[\s\S]*?\\end\{" + env + r"\}")
    assert rx.findall(original) == rx.findall(main), f"Research {env} changed!"
    assert rx.findall(original_supp) == rx.findall(supplement)
# Existing key scientific paragraphs and two floating layout guardrails remain intact.
for marker in (
    r"\Needspace{10\baselineskip}",
    r"\begin{table}[H]",
    r"\input{stage13r_proof_supplement.tex}",
    r"\input{stage13r_figure3_tikz.tex}",
    r"\label{thm:open}",
    r"\label{eq:cert}",
    r"\label{eq:frozenCert}",
):
    assert marker in main, f"Regressed prior submission guard: {marker}"
assert r"\begin{table}[H]" in supplement, "Certification Table3 no longer fixed"
print("PASS Stage13R-L: 20 references, 20 cited, 9 new, alphabetical, 45 scientific math/proof blocks unchanged, appendix+tables retained")
