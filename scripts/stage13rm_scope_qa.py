#!/usr/bin/env python3
"""Stage 13R-M: strictly isolate editorial changes from the Stage 13R-L baseline."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "51f5494d616167894e351cd226aadc8f9036cdf8"
TEX = "manuscript/stage13rl_jpet_revised.tex"
SUP = "manuscript/stage13r_proof_supplement.tex"
text = (ROOT / TEX).read_text(encoding="utf-8")
supp = (ROOT / SUP).read_text(encoding="utf-8")
original = subprocess.check_output(["git", "show", f"{BASE}:{TEX}"], cwd=ROOT, text=True)
old_supp = subprocess.check_output(["git", "show", f"{BASE}:{SUP}"], cwd=ROOT, text=True)
assert supp == old_supp, "Proof supplement edited"
assert text.count(r"\end{document}") == 1
assert text.count(r"\begin{table}[H]"+ "\n" + r"\centering\footnotesize"+ "\n" + r"\caption{Hierarchy, proven domains, and limits of the results}\label{tab:map}") == 1, "Table 1 must have [H]"
assert r"\section{Introduction}" in text
assert r"\section{Relationship to the literature and interpretation}" in text
assert r"\section{Conclusion}" in text

# Mask ONLY the permitted prose sections and the version date; the rest must match byte for byte.
def mask_allowed(s):
    starts_ends = [
        (r"\section{Introduction}", r"\section{Economic environment and the accession protocol}"),
        (r"\section{Relationship to the literature and interpretation}", r"\section{Conclusion}"),
        (r"\section{Conclusion}", r"\appendix"),
    ]
    for start, end in starts_ends:
        a = s.index(start) + len(start)
        b = s.index(end, a)
        s = s[:a] + "\n% SECTION PROSE ONLY\n" + s[b:]
    # Sole permitted non-prose correction: Table 1/tab:map float specifier [tbp] -> [H].
    # Normalize the specified table header only, so any changed table content, position,
    # math, figures or unrelated float specifiers still fail the byte-comparison.
    old_map = r"\begin{table}[tbp]" + "\n" + r"\centering\footnotesize" + "\n" + \
        r"\caption{Hierarchy, proven domains, and limits of the results}\label{tab:map}"
    new_map = old_map.replace(r"\begin{table}[tbp]", r"\begin{table}[H]")
    assert s.count(old_map) + s.count(new_map) == 1, \
        "Exactly one unchanged Table 1/tab:map header is required"
    s = s.replace(new_map, old_map)
    s = s.replace("Stage 13R-L literature-integrated draft", "STAGE-EDITORIAL-VERSION")
    s = s.replace("Stage 13R-M economic-significance editorial revision", "STAGE-EDITORIAL-VERSION")
    return s

assert mask_allowed(text) == mask_allowed(original), \
    "Non-editorial manuscript content unexpectedly changed (including the Abstract, equations, graphs or tables)"
assert text[text.index(r"\begin{thebibliography}"):text.index(r"\end{thebibliography}")+len(r"\end{thebibliography}")] == \
    original[original.index(r"\begin{thebibliography}"):original.index(r"\end{thebibliography}")+len(r"\end{thebibliography}")], \
    "Stage13R-L bibliography not identical"

bib = re.findall(r"(?m)^\\bibitem\[[^\n]*?\]\{([^}]+)\}\s*([^\n]+)$", text)
assert len(bib) == 20, f"Expected 20 bibliographic entries, got {len(bib)}"
keys = [key for key,_ in bib]
assert len(set(keys)) == 20, "Duplicate bib key"
names = [entry.split(",",1)[0].casefold() for _,entry in bib]
assert names == sorted(names), "Bibliography not alphabetical"
cited_raw = re.findall(r"\\cite(?:t|p|author|year|yearpar)?(?:\[[^\]]*\])?\{([^}]+)\}", text+"\n"+supp)
cited = {key.strip() for item in cited_raw for key in item.split(",")}
assert set(keys) == cited, f"missing={cited-set(keys)}, uncited={set(keys)-cited}"
for key in ("KatzShapiro1985","EconomidesFlyer1998","BranderSpencer2015",
            "ZhouSpencerVertinsky2002","BaakeBoom2001","BarrettYang2001",
            "CabralSalant2014","LambertiniRossini1998","TakaradaKawabata2025"):
    assert key in cited
for environment in ("equation","align","theorem","proposition","lemma","proof","split"):
    pattern = re.compile(r"\\begin\{"+environment+r"\}(?:\[[^\]]*\])?[\s\S]*?\\end\{"+environment+r"\}")
    assert pattern.findall(original) == pattern.findall(text), f"Changed scientific {environment}"
for marker in (r"\Needspace{10\baselineskip}", r"\begin{table}[H]",
               r"\input{stage13r_proof_supplement.tex}",
               r"\input{stage13r_figure3_tikz.tex}",
               r"\label{thm:open}", r"\label{eq:cert}", r"\label{eq:frozenCert}"):
    assert marker in text
assert r"\begin{table}[H]" in supp
assert "an assessment that holds residual designs" in text
assert "an empirical question" in text
assert "the \\emph{same} bilateral-first accession procedure" in text

# Guard all repository files, including proofs, numeric scripts, theory freeze and figures.
allowed = {
    TEX, "manuscript/stage13rl_jpet_revised.pdf",
    "scripts/stage13rm_scope_qa.py",
    ".github/workflows/stage13rm-economic-significance-build.yml",
    "reviews/STAGE13RM_ECONOMIC_SIGNIFICANCE_AND_SCOPE_QA.md",
    "reviews/STAGE13R_FINAL_POST_REVISION_QA.md",
}
modified = subprocess.check_output(["git","diff","--name-only",BASE,"HEAD"],cwd=ROOT,text=True).splitlines()
assert set(modified).issubset(allowed), f"Unexpected scientific or other files changed: {set(modified)-allowed}"
assert TEX in modified
print("PASS Stage13R-M: prose scope isolated; 20/20 cited; equations, proofs, tables, figures, model, scientific files, supplement and source bibliography unchanged")
