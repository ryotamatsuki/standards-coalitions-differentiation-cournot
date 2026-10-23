#!/usr/bin/env python3
"""Fail-closed JPET layout-only release audit. Requires full git history."""
import re,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
base="32120775fed53bd6d191c532e827b2de2e211bb4"
path="manuscript/JPET_submission_author_check.tex"
old=subprocess.check_output(["git","show",base+":"+path],cwd=root,text=True)
new=(root/path).read_text()
assert len(old)==62159 and len(new)==59251,(len(old),len(new))
assert old.split(r"\begin{abstract}")[1].split(r"\end{abstract}")[0]==new.split(r"\begin{abstract}")[1].split(r"\end{abstract}")[0]
indices=[new.index(x) for x in (r"\section{Conclusion}",r"\section*{Research workflow and use of generative AI}",r"\section*{Acknowledgments}",r"\section*{Declarations}",r"\begin{thebibliography}",r"\appendix")]
assert indices==sorted(indices) and len(set(indices))==6
assert new.count(r"\appendix")==1
assert new.count("The author received no external funding for this research.")==1
assert new.count("The author declares no competing interests.")==1
assert new.count(r"\begin{figure}")==3 and new.count(r"\includegraphics")==3
assert r"\begin{tikzpicture}" not in new and r"\usepackage{tikz}" not in new
figpat=r"\\begin\{figure\}\[[^]]+\][\s\S]*?\\end\{figure\}"
for i,label,scale in ((1,"fig:timing",".92"),(2,"fig:mechanism",".85"),(3,"fig:phase",".98")):
    fn=f"stage13r_figure{i}.pdf"
    assert new.count(r"\includegraphics[width="+scale+r"\linewidth]{"+fn+"}")==1
    assert (root/"manuscript"/fn).read_bytes()==subprocess.check_output(["git","show",base+":manuscript/"+fn],cwd=root)
    of=next(m.group(0) for m in re.finditer(figpat,old) if r"\label{"+label+"}" in m.group(0))
    nf=next(m.group(0) for m in re.finditer(figpat,new) if r"\label{"+label+"}" in m.group(0))
    assert re.search(r"\\caption\{([^\n]+)\}",of).group(1)==re.search(r"\\caption\{([^\n]+)\}",nf).group(1)
    assert re.search(r"\\label\{([^}]+)\}",of).group(1)==re.search(r"\\label\{([^}]+)\}",nf).group(1)
    assert re.search(r"\\begin\{figure\}\[([^]]+)\]",of).group(1)==re.search(r"\\begin\{figure\}\[([^]]+)\]",nf).group(1)
def figless(s):return re.sub(figpat,"FIGURE_FROZEN",s)
before=old[:old.index(r"\appendix")].replace("\\usepackage{tikz}\n\\usetikzlibrary{arrows.meta,positioning,calc,fit,shapes.geometric}\n","")
after=new[:new.index(r"\section*{Research workflow and use of generative AI}")]
assert figless(before)==figless(after),"Nonfigure scientific text changed"
oapp=old[old.index(r"\appendix"):old.index(r"\section*{Use of generative AI in the research process}")]
napp=new[new.index(r"\appendix"):new.index(r"\end{document}")]
assert oapp==napp,"Appendix math or order changed"
def bib(s):return s[s.index(r"\begin{thebibliography}"):s.index(r"\end{thebibliography}")+len(r"\end{thebibliography}")]
assert bib(old)==bib(new),"Bibliography changed"
for fn in ("stage13r_proof_supplement.tex","stage13r_figure3_tikz.tex"):
    assert (root/"manuscript"/fn).read_bytes()==subprocess.check_output(["git","show",base+":manuscript/"+fn],cwd=root)
assert new.count("AI-assisted LaTeX/TikZ code.")==3
keys=re.findall(r"\\bibitem\[[^\n]+?\]\{([^}]+)\}",new)
cites=re.findall(r"\\cite(?:t|p|author|year|yearpar)?(?:\[[^\]]*\])?\{([^}]+)\}",new+"\n"+(root/"manuscript/stage13r_proof_supplement.tex").read_text())
assert len(keys)==20 and len(set(keys))==20 and set(keys)=={z.strip() for x in cites for z in x.split(",")}
labels=lambda t:set(re.findall(r"\\label\{([^}]+)\}",t))
assert labels(old)==labels(new)
print("PASS: scientific manuscript, six appendix sections and two scientific inputs frozen")
print("PASS: original figures and captions preserved; all three PDF blobs identical to base")
print("PASS: 20 citations; unchanged abstract; funding, COI, AI disclosures separated correctly")