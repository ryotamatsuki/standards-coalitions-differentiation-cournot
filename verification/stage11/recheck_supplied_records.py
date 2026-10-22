"""Re-execute archived 28 convergence cases using unmodified source evaluator."""
import sys,json,time
from pathlib import Path
import numpy as np
src=Path(__file__).resolve().parent/'input_v04'
sys.path.insert(0,str(src))
from phase_model_functions import classify,codes
records=json.loads((src/'figure3_depth_convergence_641.json').read_text());out=[]
for n,r in enumerate(records):
 z={'i':r['i'],'j':r['j'],'eta':r['eta'],'kappa':r['kappa'],'results':{}}
 for count,key in [(81,'original81'),(321,'refined321'),(641,'refined641')]:
  a,b,_=classify(r['eta'],r['kappa'],np.linspace(0,1,count));v=[codes[a],codes[b]]
  z['results'][str(count)]={'actual':v,'expected':r[key],'match':v==r[key]}
 out.append(z)
 print(n+1,'/',len(records),z,flush=True)
 Path(__file__).with_name('supplied_record_recheck.json').write_text(json.dumps(out,indent=2))
