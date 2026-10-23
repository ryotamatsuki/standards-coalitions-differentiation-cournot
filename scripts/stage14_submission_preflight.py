#!/usr/bin/env python3
"""Fail-closed Stage14 preflight: locked scientific source and reproducible draft package."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = "492605b5938e857137a6721eb22150f294d84835"
TEX = "manuscript/stage13rl_jpet_revised.tex"
PDF = "manuscript/stage13rl_jpet_revised.pdf"
SUP = "manuscript/stage13r_proof_supplement.tex"
ALLOWED = {
    TEX, PDF,
    "scripts/stage14_submission_preflight.py",
    "scripts/stage14_render_submission.py",
    ".github/workflows/stage14-jpet-preflight.yml",
    "submission/STAGE14_AUTHOR_FACTS_AND_APPROVAL_TEMPLATE.md",
    "submission/STAGE14_JPET_REQUIREMENTS_AND_SUBMISSION_README.md",
    "submission/STAGE14_COVER_LETTER_DRAFT.md",
    "submission/STAGE14_FINAL_PREP_AND_QA.md",
}
REQUIRED_COMPANIONS = [
    "manuscript/stage13r_proof_supplement.tex",
    "manuscript/stage13r_figure3_tikz.tex",
    "manuscript/stage13r_figure1.pdf",
    "manuscript/stage13r_figure2.pdf",
    "manuscript/stage13r_figure3.pdf",
]
grammar = [
    (r"\citet{Kawabata2021} also establishes", r"\citet{Kawabata2021} also establish"),
    (r"\citet{Grossman2021} already studies", r"\citet{Grossman2021} already study"),
]

def baseline_git(args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()

def pdf_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("--package", action="store_true")
    opts = arg.parse_args()
    old = baseline_git(["show", f"{BASE}:{TEX}"])
    new = (ROOT / TEX).read_text(encoding="utf-8").strip()
    expected = old
    for a,b in grammar:
        assert old.count(a) == 1, f"Baseline no longer matches sole grammar edit: {a}"
        expected = expected.replace(a,b)
    assert new == expected, "Stage14 must contain ONLY the two approved grammar agreements vs PR #34 HEAD"
    assert r"\begin{table}[H]" + "\n" + r"\centering\footnotesize" + "\n" + \
        r"\caption{Hierarchy, proven domains, and limits of the results}\label{tab:map}" in new
    assert "Review working draft---author details withheld" in new
    assert r"\textbf{Not for submission}" in new
    assert "[AUTHOR-CONFIRMED" in new and "[FINAL IMMUTABLE ARCHIVE" in new
    assert all((ROOT / f).exists() for f in REQUIRED_COMPANIONS)
    assert (ROOT / SUP).read_text(encoding="utf-8").strip() == baseline_git(["show",f"{BASE}:{SUP}"])
    bib = re.findall(r"(?m)^\\bibitem\[[^\n]*?\]\{([^}]+)\}\s*([^\n]+)$", new)
    assert len(bib)==20 and len(set(k for k,_ in bib))==20
    names = [value.split(",",1)[0].casefold() for _,value in bib]
    assert names == sorted(names)
    supp=(ROOT/SUP).read_text(encoding="utf-8")
    cites = re.findall(r"\\cite(?:t|p|author|year|yearpar)?(?:\[[^\]]*\])?\{([^}]+)\}",new+"\n"+supp)
    keys={x.strip() for group in cites for x in group.split(",")}
    assert keys=={k for k,_ in bib}, "Citation/bibliography mismatch"
    for env in ("equation","align","lemma","theorem","proposition","proof","split","table","figure"):
        pat = re.compile(r"\\begin\{"+env+r"\}(?:\[[^\]]*\])?[\s\S]*?\\end\{"+env+r"\}")
        assert pat.findall(old) == pat.findall(new), "Changed scientific block: "+env
    changed = set(baseline_git(["diff","--name-only",BASE,"HEAD"]).splitlines())
    assert changed <= ALLOWED, f"Unapproved modified scientific files: {changed-ALLOWED}"
    assert TEX in changed
    assert (ROOT/"scripts/stage14_render_submission.py").exists()
    txt = (ROOT / "submission/STAGE14_AUTHOR_FACTS_AND_APPROVAL_TEMPLATE.md").read_text()
    assert '"author_approved_contents": false' in txt, "Do not implicitly authorize author declarations"
    print("PASS: two language fixes only, model/proofs/figures/tables/bibliography unchanged, 20/20 citations")
    print("AUTHOR GATE: BLOCKED until personal attestation, immutable archive, live submission confirmation")

    if opts.package:
        pdf_path = ROOT / PDF
        assert pdf_path.exists() and pdf_path.stat().st_size > 100000, "Compiled review PDF absent"
        data=pdf_path.read_bytes()
        assert data.startswith(b"%PDF-")
        log=(ROOT/"manuscript/stage13rl_jpet_revised.log").read_text(encoding="utf-8")
        assert "Overfull \\hbox" not in log
        assert not re.search(r"(Citation .* undefined|Reference .* undefined|multiply defined)",log)
        files=[TEX,PDF,*REQUIRED_COMPANIONS,
               "submission/STAGE14_AUTHOR_FACTS_AND_APPROVAL_TEMPLATE.md",
               "submission/STAGE14_JPET_REQUIREMENTS_AND_SUBMISSION_README.md",
               "submission/STAGE14_COVER_LETTER_DRAFT.md",
               "scripts/stage14_render_submission.py",
               "scripts/stage14_submission_preflight.py"]
        branch=baseline_git(["rev-parse","HEAD"])
        manifest={
            "status":"PREFLIGHT_ONLY_NOT_FOR_SUBMISSION",
            "source_branch_head":branch,
            "reference_baseline_stage13rm":BASE,
            "compiled_pdf":"stage13rl_jpet_revised.pdf",
            "pdf_size_bytes":len(data),
            "pdf_git_blob_sha1":pdf_blob(data),
            "pdf_sha256":hashlib.sha256(data).hexdigest(),
            "required_author_declarations_complete":False,
            "immutable_repository_doi_confirmed":False,
            "author_upload_authorization_obtained":False,
            "file_sha256":{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files},
        }
        destination=ROOT / "submission/JPET_STAGE14_PREFLIGHT_DO_NOT_SUBMIT.zip"
        destination.parent.mkdir(exist_ok=True)
        with zipfile.ZipFile(destination,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
            for f in files: z.write(ROOT/f,arcname=f)
            z.writestr("SUBMISSION_MANIFEST.json",json.dumps(manifest,indent=2,ensure_ascii=False))
        print(json.dumps({"package":str(destination),"package_size":destination.stat().st_size,
            "pdf_size":len(data),"pdf_git_blob_sha1":pdf_blob(data),
            "pdf_sha256":manifest["pdf_sha256"],"head":branch},indent=2))

if __name__=="__main__":
    try: main()
    except (AssertionError,OSError,ValueError,subprocess.CalledProcessError) as exc:
        print(f"FAIL: {exc}",file=sys.stderr)
        sys.exit(1)
