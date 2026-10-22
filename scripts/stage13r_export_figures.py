#!/usr/bin/env python3
"""Export standalone vector versions of unchanged Stage13R manuscript TikZ figures."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1] / "manuscript"
manuscript = (root / "stage13r_jpet_revised.tex").read_text(encoding="utf-8")
figures = re.findall(r"\\begin\{figure\}(.*?)\\end\{figure\}", manuscript, re.S)
assert len(figures) == 3, f"Expected 3 figures, got {len(figures)}"
preamble = r"""\documentclass[tikz,border=5pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb}
\usetikzlibrary{arrows.meta,positioning,calc,fit,shapes.geometric}
\newcommand{\SW}{\mathrm{SW}}
\newcommand{\SU}{\mathrm{SU}}
\newcommand{\IS}{\mathrm{IS}}
\newcommand{\N}{\mathrm{N}}
\newcommand{\F}{\mathrm{F}}
\begin{document}
"""
for i, figure in enumerate(figures[:2], start=1):
    match = re.search(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", figure, re.S)
    assert match, f"Figure {i} has no TikZ."
    (root / f"stage13r_figure{i}.tex").write_text(
        preamble + match.group(0) + "\n\\end{document}\n", encoding="utf-8")
(root / "stage13r_figure3.tex").write_text(
    preamble + "\\input{stage13r_figure3_tikz.tex}\n\\end{document}\n", encoding="utf-8")
print("PASS: three standalone figure LaTeX wrappers generated; paper source unchanged")
