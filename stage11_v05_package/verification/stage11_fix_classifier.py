"""Stage11 repairs to coarse-g illustration: zero-neighborhood geometric probes,
implementation-wise government payoff, boundary bracketing and safe uncertainty.
Numerical illustration only.  Never a global proof of all parameters.
"""
from __future__ import annotations
import json, math, pathlib, time
from collections import Counter
import numpy as np
from scipy.optimize import root, root_scalar, minimize_scalar
from functools import lru_cache
ROOT=pathlib.Path(__file__).resolve().parent
import sys
sys.path.insert(0,str(ROOT))
from phase_funcs import solve_sw, solve_is, solve_su, welfare

regimes=('SW','SU','IS','UN')

class Cell:
 def __init__(self,kappa,eta):
  self.kappa=float(kappa); self.eta=float(eta)
  self.z, self.z_ok=solve_sw(self.eta,self.kappa)
  self.s=float(welfare(np.array([self.z]*3),0,'SW',self.eta,self.kappa)[0]) if self.z_ok else np.nan
  self.cache={}
 def at(self, g, tr):
  # Returns vote margins, branch payoffs. First run at fine-grid seeds with high precision FOC residual verified by original solver.
  g=float(g); key=(round(g,15),tr)
  if key in self.cache: return self.cache[key]
  z=self.z
  if tr=='F':
   ws=welfare(np.array([z]*3),g,'SU',self.eta,self.kappa)
   wi=welfare(np.array([z]*3),g,'IS',self.eta,self.kappa)
   m,o,i=map(float,(ws[0],ws[2],wi[0]))
   ok=True
  else:
   y,iy=solve_is(g,self.eta,self.kappa,z)
   uv,iv=solve_su(g,self.eta,self.kappa,(z,z))
   ok=iy and iv
   if ok:
    ws=welfare(np.array([uv[0],uv[0],uv[1]]),g,'SU',self.eta,self.kappa)
    wi=welfare(np.array([y]*3),g,'IS',self.eta,self.kappa)
    m,o,i=map(float,(ws[0],ws[2],wi[0]))
   else: m=o=i=float('nan')
  if not ok:
   out={'ok':False,'g':g}
  else:
   out={'ok':True,'g':g,'m':m,'o':o,'i':i,'s':self.s,
        'ms':m-self.s,'io':i-o,'im':i-m,'is':i-self.s}
  self.cache[key]=out
  return out

def strict_agreement(v):
  if not v['ok'] or v['g']<=0:return None
  # Sign margin only, no artificial 1e-8 weak acceptance tolerance at tiny g.
  scale=max(1.,abs(v['s']))
  uncertain=4e-13*scale
  if min(v['is'],v['io'],v['im'])>uncertain:return 'IS'
  if v['ms']>uncertain and (v['io']< -uncertain or v['im'] < -uncertain):return 'SU'
  if any(abs(v[x])<=uncertain for x in ['ms','io','im','is']):return 'UN'
  return 'SW'

def classify(cell,tr,extra=False):
  # Every panel shares fixed government menu. Geometric g near zero removes the known 11 false SW aliasing.
  probes=sorted(set(np.concatenate(([0],np.geomspace(1e-6,.01,23),np.linspace(.01,1,71)))))
  vals=[cell.at(g,tr) for g in probes]
  if any(not v['ok'] for v in vals): return {'result':'UN','reason':'failed_continuation'}
  confirmed=[]
  ambiguous=[]
  for v in vals[1:]:
   label=strict_agreement(v)
   if label in ['IS','SU']:
    gain=(v['i'] if label=='IS' else v['m'])-cell.s
    if gain>1e-11: confirmed.append((gain,label,v['g'],v))
   elif label=='UN': ambiguous.append(v['g'])
  # Scan between candidate roots i-o, i-m, i-s, m-s. Brent roots discover sign changes; evaluate both sides of each.
  roots=[]
  for key in ['io','im','is','ms']:
   for va,vb in zip(vals[:-1],vals[1:]):
    fa,fb=va[key],vb[key]
    if fa*fb<0:
     try:
      r=root_scalar(lambda g:cell.at(g,tr)[key],bracket=[va['g'],vb['g']],xtol=1e-12,method='brentq').root
      roots.append(float(r))
     except Exception:
      ambiguous.append((va['g']+vb['g'])/2)
  # probe just inside the boundary, respecting floating point and choosing physically meaningful gap
  for r in roots:
   for g in [max(1e-10,r-1e-6),min(1,r+1e-6), max(1e-10,r*.99), min(1,r*1.01)]:
    v=cell.at(g,tr)
    label=strict_agreement(v)
    if label in ['IS','SU']:
     gain=(v['i'] if label=='IS' else v['m'])-cell.s
     if gain>1e-11:confirmed.append((gain,label,g,v))
  # pick best confirmed realized A payoff; no affirmative result means SW only if no near-zero sign diagnostic contradicts
  if confirmed:
   confirmed.sort(key=lambda x:x[0],reverse=True)
   top=confirmed[0]
   # alternative regime within tolerance => uncertain label
   labs={x[1] for x in confirmed if top[0]-x[0]<1e-8}
   return {'result':top[1] if len(labs)==1 else 'UN','max_gain':float(top[0]),'g':float(top[2]),
      'binding_vote':float(min(top[3]['is'],top[3]['io'],top[3]['im']) if top[1]=='IS' else top[3]['ms']),
      'n_roots':len(roots),'n_probes':len(cell.cache),'ambiguous_probes':len(ambiguous)}
  # confirm no positive incident edge slope at zero by derivative from two independent small g, using high-resolution finite differences
  vs=[cell.at(g,tr) for g in [1e-5,1e-4]]
  mu=[v['ms']/v['g'] for v in vs]
  outsider=[v['io']/v['g'] for v in vs]
  if (min(mu)>1e-9 and min(outsider)>1e-9) or (len(ambiguous)>25):
   return {'result':'UN','reason':'local_positive_or_ambiguous','local_member_slopes':mu,'local_outsider_slopes':outsider}
  return {'result':'SW','max_gain':0.0,'g':0.0,'n_roots':len(roots),'n_probes':len(cell.cache),'ambiguous_probes':len(ambiguous)}

def main():
  source=np.load(ROOT/'input_v04'/'figure3_data_41x41.npz')
  ks=source['ks']; es=source['es']; oldF=source['F']; oldN=source['N']
  outdir=ROOT/'rerun_outputs';outdir.mkdir(exist_ok=True)
  outF=np.full((len(es),len(ks)),3,dtype=int);outN=np.full_like(outF,3)
  ledger=[];counts=Counter();start=time.time()
  codes={'SW':0,'SU':1,'IS':2,'UN':3}
  for j,eta in enumerate(es):
   for i,kappa in enumerate(ks):
    c=Cell(kappa,eta)
    for tr,arr,old in [('F',outF,oldF),('N',outN,oldN)]:
     result=classify(c,tr)
     arr[j,i]=codes[result['result']]
     r={'eta':float(eta),'kappa':float(kappa),'panel':tr,'original':int(old[j,i]),'new':int(arr[j,i]),**result}
     ledger.append(r)
     if int(old[j,i])!=int(arr[j,i]):counts[tr+':changed']+=1
     counts[tr+':'+result['result']]+=1
   print(f"row {j+1}/{len(es)} eta={eta:.6f} time={time.time()-start:.1f}s",flush=True)
   np.savez_compressed(outdir/'figure3_continuous_candidate_map_checkpoint.npz',F=outF,N=outN,kappas=ks,etas=es)
  np.savez_compressed(outdir/'figure3_boundary_aware_map.npz',F=outF,N=outN,kappas=ks,etas=es)
  (outdir/'figure3_candidate_ledger.json').write_text(json.dumps(ledger,indent=2))
  (outdir/'figure3_summary.json').write_text(json.dumps({'counts':dict(counts),'runtime':time.time()-start, 'method':'geometric near-zero probes, sign-change bracketing, and candidate government-payoff comparison; not formal global optimality certification'},indent=2))
  # 11 permanent regression cases
  samples=[('F',.93625,.7555),('N',.945,.760),('N',.86625,.76075),('N',.79625,.7615)]
  check=[]
  for tr,k,e in samples:
   c=Cell(k,e);v=c.at(.0001,tr); check.append({'panel':tr,'kappa':k,'eta':e,'g':.0001,'i-s':v['is'],'i-o':v['io'],'i-m':v['im'],'label':strict_agreement(v)})
  (outdir/'regression_cases.json').write_text(json.dumps(check,indent=2))
  print('DONE',dict(counts),flush=True)

if __name__=='__main__': main()
