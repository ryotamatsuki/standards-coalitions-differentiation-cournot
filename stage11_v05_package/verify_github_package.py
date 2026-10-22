"""Verify the CURRENT patched v0.5 package using Git object SHA-1 and file sizes.
The immutable SOURCE_FILE_HASHES.json still describes the older 23-file release;
that ledger is deliberately not substituted for the repaired revision.
"""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'CURRENT_BLOB_MANIFEST_V05R1.json').read_text())
problems=[]
for rel,expected in manifest['files'].items():
    p=root/rel
    if not p.is_file():
        problems.append('MISSING: '+rel)
        continue
    raw=p.read_bytes()
    sha=hashlib.sha1(('blob '+str(len(raw))+'\\0').replace('\\0','\0').encode()+raw).hexdigest()
    if len(raw)!=expected['size'] or sha!=expected['blob_sha1']:
        problems.append('MISMATCH: '+rel)
if problems: raise SystemExit('\n'.join(problems))
pdf=(root/'manuscript/stage25_jpet_v05.pdf').read_bytes()
assert pdf.startswith(b'%PDF-')
try:
    import numpy as np
except ImportError:
    print('SKIP optional NumPy phase counts')
else:
    d=np.load(root/'verification/figure3_boundary_aware_map.npz')
    a={'F_SW':int((d['F']==0).sum()),'F_IS':int((d['F']==2).sum()),'N_SW':int((d['N']==0).sum()),'N_IS':int((d['N']==2).sum())}
    assert a=={'F_SW':765,'F_IS':916,'N_SW':1047,'N_IS':634},a
print('PASS patched package Git blob checks:',len(manifest['files']),'files; PDF signature and candidate phase counts')
print('NOTE: numerical reproduction requires run_reproducibility.py; no global phase theorem is certified.')
