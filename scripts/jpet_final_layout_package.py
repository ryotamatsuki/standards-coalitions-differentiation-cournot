#!/usr/bin/env python3
"""Build a self-contained JPET package from the EXACT compiled PDF in this branch."""
from pathlib import Path
from hashlib import sha256
import json,os,shutil,zipfile
root=Path(__file__).resolve().parents[1]
ms=root/"manuscript"
dest=root/"submission"/"JPET_V2b_final_layout_submission.zip"
assert (ms/"JPET_submission_author_check.pdf").is_file()
pdf=(ms/"JPET_submission_author_check.pdf").read_bytes()
assert pdf[:5]==b"%PDF-" and len(pdf)>100000
shutil.copyfile(ms/"JPET_submission_author_check.tex",ms/"JPET_submission_final.tex")
shutil.copyfile(ms/"JPET_submission_author_check.pdf",ms/"JPET_submission_final.pdf")
files={}
for name in ("JPET_submission_final.tex","JPET_submission_final.pdf","stage13r_figure1.pdf","stage13r_figure2.pdf","stage13r_figure3.pdf","stage13r_proof_supplement.tex"):
    data=(ms/name).read_bytes()
    files[name]=data
files["editing_sources/stage13r_figure3_tikz.tex"]=(ms/"stage13r_figure3_tikz.tex").read_bytes()
files["reviews/JPET_FINAL_LAYOUT_GRAPHICS_AND_DISCLOSURE_QA.md"]=(root/"reviews"/"JPET_FINAL_LAYOUT_GRAPHICS_AND_DISCLOSURE_QA.md").read_bytes()
cover=root/"submission"/"STAGE14_COVER_LETTER_DRAFT.md"
if cover.exists(): files["Cover_letter_DRAFT_NOT_AUTHOR_APPROVED.md"]=cover.read_bytes()
info=("JPET manuscript package — review and author-signoff only; not submitted.\n"
"Compile in this folder with: latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode JPET_submission_final.tex\n"
"Upload main .tex + paired review PDF; upload the two input/graphics sources as additional LaTeX files as required by Wiley portal.\n"
"All three figure PDFs are used by \\includegraphics; not generic Supporting Information.\n"
"editing_sources contains legacy Figure 3 TikZ for reproduction; manuscript compilation DOES NOT require TikZ.\n"
"Funding and competing interests were confirmed by the author. No journal upload or merge performed.\n")
files["README_SUBMISSION.txt"]=info.encode()
manifest={"origin_git_base":"32120775fed53bd6d191c532e827b2de2e211bb4","source_blob_sha":"2e485def8e126c1312fb74ba05b6a7b8bd9e52d9","files":{k:{"sha256":sha256(v).hexdigest(),"size_bytes":len(v)} for k,v in files.items()},"state":"author review required, not submitted"}
files["SUBMISSION_MANIFEST.json"]=json.dumps(manifest,indent=2,ensure_ascii=False).encode()
checks="\n".join(sha256(v).hexdigest()+"  "+n for n,v in sorted(files.items()))+"\n"
files["SHA256SUMS.txt"]=checks.encode()
dest.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(dest,"w",zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for n,data in sorted(files.items()):
        z.writestr("JPET_V2b_final_layout/"+n,data)
with zipfile.ZipFile(dest) as z:
    for n,data in files.items():
        assert z.read("JPET_V2b_final_layout/"+n)==data
print("PDF_BYTES",len(pdf),"PDF_SHA256",sha256(pdf).hexdigest())
print("ZIP_BYTES",dest.stat().st_size,"ZIP_SHA256",sha256(dest.read_bytes()).hexdigest())
print("ZIP_CONTENTS",len(files),"TEX_SHA256",sha256(files["JPET_submission_final.tex"]).hexdigest())
