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
    t=re.sub(r"\\date\{[^\n]*\}",r"\\date{NORMALIZED}",t,count=1)
    t=re.sub(r"\\begin\{abstract\}[\s\S]*?\\end\{abstract\}",r"\begin{abstract}NORMALIZED\end{abstract}",t,count=1)
    t=re.sub(r"\\section\*\{Declarations[^\n]*[\s\S]*?(?=\\begin\{thebibliography\})","DECLARATIONS_NORMALIZED\n\n",t,count=1)
    return t
assert normalize(present)==normalize(baseline), "Unexpected change outside title-date/structured abstract/declarations"
for h in ("Introduction","Methods","Results","Conclusion"):
    assert r"\textbf{"+h+".}" in present
assert r"\date{}" in present
assert "Not for submission" not in present
assert present.count("[Author to confirm:")==2, "V2b funding/conflicts must remain unasserted before author signoff"
assert "[Author to review and confirm" in present, "AI disclosure must remain subject to author verification"
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
print("PENDING author funding, conflict, AI declaration signoff, journal upload confirmation")
