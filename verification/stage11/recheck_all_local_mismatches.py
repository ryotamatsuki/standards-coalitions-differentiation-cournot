"""Recheck every archived SW cell with a positive incident derivative."""
from pathlib import Path
import json
from phase_independent_audit import scan
p=Path(__file__).resolve().parent
r=json.loads((p/'phase_independent_results.json').read_text());out=[]
for c in r['local_mismatches']:
 out.append({**c,'independent_dense_scan':scan(c['eta'],c['kappa'])})
(p/'all_local_mismatch_rechecks.json').write_text(json.dumps(out,indent=2,allow_nan=False))
print('Rechecked',len(out),'positive-slope SW labels')
