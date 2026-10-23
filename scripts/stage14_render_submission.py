#!/usr/bin/env python3
"""Render a private JPET submission TeX from verified author facts; never submit/upload."""
import argparse
import json
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "manuscript/stage13rl_jpet_revised.tex"
INCLUDES = ("stage13r_proof_supplement.tex", "stage13r_figure3_tikz.tex")
FIELDS = (
    "author_name",
    "affiliation_or_independent_status",
    "correspondence_email",
    "orcid",
    "funding_statement",
    "conflicts_statement",
    "data_code_availability_statement",
    "ai_assistance_statement",
    "ethics_and_permissions_statement",
)
META_BLACKLIST = re.compile(
    r"\b(?:TODO|TBD|TO CONFIRM|AUTHOR.CONFIRMED|PLACEHOLDER|INSERT HERE|UNKNOWN)\b",
    re.IGNORECASE,
)

def tex_escape(value: str) -> str:
    mapping = {
        "\\": r"\textbackslash{}",
        "{": r"\{",
        "}": r"\}",
        "%": r"\%",
        "&": r"\&",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "^": r"\textasciicircum{}",
        "~": r"\textasciitilde{}",
    }
    return "".join(mapping.get(c, c) for c in value)

def require_metadata(path: Path) -> dict:
    values = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(values, dict):
        raise ValueError("Metadata must be a JSON object.")
    absent = [
        k for k in FIELDS if not isinstance(values.get(k), str)
        or not values[k].strip()
        or META_BLACKLIST.search(values[k])
    ]
    if absent:
        raise ValueError("Missing or unconfirmed required fields: " + ", ".join(absent))
    if values.get("author_approved_contents") is not True:
        raise ValueError("The author must explicitly confirm all manuscript contents and declarations.")
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", values["correspondence_email"]):
        raise ValueError("Correspondence email has invalid syntax.")
    if not re.fullmatch(r"(?:https://orcid\.org/)?\d{4}-\d{4}-\d{4}-[\dX]{4}", values["orcid"], re.I):
        raise ValueError("ORCID must be a fully specified XXXX-XXXX-XXXX-XXXX identifier.")
    return values

def author_tex(data):
    return (
        r"\author{" + tex_escape(data["author_name"]) + r"\\" + "\n"
        + tex_escape(data["affiliation_or_independent_status"]) + r"\\" + "\n"
        + r"\texttt{" + tex_escape(data["correspondence_email"]) + r"}\\" + "\n"
        + "ORCID: " + tex_escape(data["orcid"]) + "}"
    )

def declarations_tex(data):
    def item(label, key):
        return r"\noindent\textbf{" + label + r":} " + tex_escape(data[key].strip()) + "\n\n"
    out = "\\section*{Declarations}\n"
    out += item("Funding", "funding_statement")
    out += item("Conflicts of interest", "conflicts_statement")
    out += item("Data and code availability", "data_code_availability_statement")
    out += item("Research ethics and permissions", "ethics_and_permissions_statement")
    out += r"\section*{Acknowledgments}" + "\n"
    out += item("Generative AI assistance", "ai_assistance_statement")
    if (ack := data.get("acknowledgments_statement", "")).strip():
        out += tex_escape(ack) + "\n\n"
    return out

def render(data: dict, outdir: Path):
    src = TEX.read_text(encoding="utf-8")
    orig_author = r"\author{Ryota Matsuki\\Independent Researcher, Matsuyama, Ehime, Japan\\\texttt{ryota.matsuki@gmail.com}\\ORCID: 0009-0005-2329-531X}"
    orig_date = r"\date{23 October 2026\quad |\quad Stage 13R-M economic-significance editorial revision\quad |\quad \textbf{Not for submission}}"
    if src.count(orig_author) != 1 or src.count(orig_date) != 1:
        raise ValueError("Canonical source changed: author/date replacement anchors do not match.")
    src = src.replace(orig_author, author_tex(data)).replace(orig_date, r"\date{}")
    start = src.index(r"\section*{Declarations (author verification required before submission)}")
    end = src.index(r"\begin{thebibliography}", start)
    src = src[:start] + declarations_tex(data) + src[end:]
    if "Not for submission" in src or "[AUTHOR" in src or "[FINAL IMMUTABLE" in src:
        raise ValueError("Unresolved submission source marker.")
    outdir.mkdir(parents=True, exist_ok=True)
    dest = outdir / "stage14_jpet_submission.tex"
    if dest.resolve() == TEX.resolve() or ROOT in outdir.resolve().parents:
        raise ValueError("Keep final, identifying metadata OUTSIDE the public GitHub repository.")
    dest.write_text(src, encoding="utf-8")
    for fn in INCLUDES:
        shutil.copy2(ROOT / "manuscript" / fn, outdir / fn)
    print(f"Author-approved TeX assembled locally: {dest}")
    print("Next step: compile and visually inspect the exact PDF; upload only after separate author authorization.")

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("metadata_json", type=Path)
    p.add_argument("--output-dir", required=True, type=Path)
    a = p.parse_args()
    data = require_metadata(a.metadata_json)
    render(data, a.output_dir)

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, json.JSONDecodeError) as ex:
        print(f"BLOCKED: {ex}", file=sys.stderr)
        sys.exit(2)
