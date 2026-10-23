#!/usr/bin/env python3
"""JPET Stage14 author's near-final proof: FAIL unless scientific manuscript is frozen."""
from pathlib import Path
import re,subprocess
root=Path(__file__).resolve().parents[1]
BASE="cbe47a3777fdd193289eff0583f9d5d8d16e43d1"
TEX="manuscript/JPET_submission_author_check.tex"
baseline=subprocess.check_output(["git","show",BASE+":manuscript/stage13rl_jpet_revised.tex"],cwd=root,text=True)
present=(root/TEX).read_text()
def normalize(t):
    fig_notice = r" \emph{Figure layout generated with AI-assisted LaTeX/TikZ code.}"
    t = t.replace(fig_notice, "")
    t = re.sub(r"\\section\*\{Use of generative AI in the research process\}[\s\S]*?(?=\\section\*\{Declarations\})", "", t, count=1)
    t=re.sub(r"\\date\{[^\n]*\}",r"\\date{NORMALIZED}",t,count=1)
    t=re.sub(r"\\begin\{abstract\}[\s\S]*?\\end\{abstract\}","ABSTRACT_NORMALIZED",t,count=1)
    t=re.sub(r"\\section\*\{Declarations[^\n]*[\s\S]*?(?=\\begin\{thebibliography\})","DECLARATIONS_NORMALIZED\n\n",t,count=1)
    return t
assert normalize(present)==normalize(baseline), "Unexpected change outside title-date/structured abstract/declarations"
for h in ("Introduction","Methods","Results","Conclusion"):
    assert r"\textbf{"+h+".}" in present
assert r"\date{}" in present
assert "Not for submission" not in present
assert r"\textbf{Funding.} The author received no external funding for this research." in present
assert r"\textbf{Competing interests.} The author declares no competing interests." in present
assert "[Author to confirm" not in present and "[Author to review and confirm" not in present
assert present.count(r"\emph{Figure layout generated with AI-assisted LaTeX/TikZ code.}") == 3
assert r"\section*{Use of generative AI in the research process}" in present
assert "not independent human verification" in present
assert "not on language-model outputs as evidence" in present
assert "cbe47a3777fdd193289eff0583f9d5d8d16e43d1" in present
for f in ("stage13r_proof_supplement.tex","stage13r_figure3_tikz.tex"):
    a=subprocess.check_output(["git","show",BASE+":manuscript/"+f],cwd=root)
    assert a==(root/"manuscript"/f).read_bytes(), "Scientific input changed: "+f
bib=re.findall(r"(?m)^\\bibitem\[[^\n]*?\]\{([^}]+)\}",present)
assert len(bib)==20 and len(set(bib))==20
supp=(root/"manuscript/stage13r_proof_supplement.tex").read_text()
cites=re.findall(r"\\cite(?:t|p|author|year|yearpar)?(?:\[[^\]]*\])?\{([^}]+)\}",present+"\n"+supp)
citekeys={y.strip() for x in cites for y in x.split(",")}
assert set(bib)==citekeys, "Incomplete 20/20 citation coverage"
print("PASS source-lock: date/abstract/declarations only; 20/20 references; ALL scientific content unchanged")
print("DECLARATIONS: V2b funding and competing interests confirmed; AI uses transparently described")
print("PENDING: author examination of final proof, live publisher-generated PDF and explicit submission authorization")
