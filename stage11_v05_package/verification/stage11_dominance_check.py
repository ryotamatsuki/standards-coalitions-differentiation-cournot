"""Independent numeric upper-envelope stress check for all plotted IS points.
This is not an interval certificate, but guards against a hidden more-profitable SU continuation."""
import json, pathlib, numpy as np
from scipy.optimize import minimize_scalar
from stage11_fix_classifier import Cell
R=pathlib.Path(__file__).resolve().parent
outdir=R/'rerun_outputs'
ledger=json.loads((outdir/'figure3_candidate_ledger.json').read_text())
checked=[]; switched=[]; mins=[]
for n,p in enumerate(ledger):
 if p['result']!='IS':continue
 c=Cell(p['kappa'],p['eta']); tr=p['panel'];
 # available IS candidate from boundary-aware previous run is a lower bound for optimal IS
 i_low=p['max_gain']
 gs=sorted(set(np.r_[np.geomspace(1e-5,.05,12),np.linspace(0,1,31),[p['g']]]))
 vals=[c.at(float(g),tr) for g in gs]
 if any(not v['ok'] for v in vals):
  switched.append({**p,'reason':'root_failure'});continue
 ms=np.array([v['ms'] for v in vals]);j=int(ms.argmax());
 g_peak=float(gs[j]);m_best=float(ms[j]);
 if 0<j<len(gs)-1:
  sol=minimize_scalar(lambda g:-c.at(g,tr)['ms'],bounds=(gs[j-1],gs[j+1]),method='bounded',options={'xatol':1e-11})
  if sol.success:m_best=max(m_best,-float(sol.fun))
 margin=i_low-m_best
 checked.append({'panel':tr,'kappa':p['kappa'],'eta':p['eta'],'is_gain_lower':i_low,'bilateral_gain_upper_numeric':m_best,'gap':margin})
 if margin<1e-7:
  switched.append({**p,'reason':'no_bilateral_envelope_domination','gap':margin})
 mins.append(margin)
 if n%250==0:print('progress',n,'checked',len(checked),'switch',len(switched),flush=True)
res={'checked':len(checked),'not_confirmed':len(switched),'min_domination_margin':float(min(mins)) if mins else None}
(outdir/'dominance_check.json').write_text(json.dumps({'summary':res,'noncertified':switched,'cases':checked},indent=2))
print(res)
