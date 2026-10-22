import json, pathlib, sys
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent))
from stage11_fix_classifier import Cell,strict_agreement
led=json.loads((ROOT/'figure3_candidate_ledger.json').read_text())
flag=[];count=0
for r in led:
 if r['result']!='SW':continue
 c=Cell(r['kappa'],r['eta']);tr=r['panel'];count+=1
 vs=[c.at(g,tr) for g in (1e-7,1e-6,1e-5,1e-4,1e-3,.002,.004,.008)]
 if any(v['ok'] and strict_agreement(v)=='IS' and v['is']>1e-11 for v in vs):
  flag.append({'eta':r['eta'],'kappa':r['kappa'],'panel':tr, 'newly_found_g':[v['g'] for v in vs if v['ok'] and strict_agreement(v)=='IS' and v['is']>1e-11]})
print(json.dumps({'checked_SW_cells':count,'additional_accepted_IS_found':len(flag),'flagged':flag[:20]},indent=2))
(ROOT/'extra_SW_stress.json').write_text(json.dumps({'checked_SW_cells':count,'additional_accepted_IS_found':len(flag),'flagged':flag},indent=2))
