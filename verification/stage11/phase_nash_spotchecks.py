"""Independent full-three-variable roots, asymmetric seeds, unilateral best responses.
Finite numerical checks do not prove global unique Nash over the rectangle.
"""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import root,minimize_scalar
from phase_independent_audit import system,quantities,solve
points=[(.742,.70),(.772,1.05),(.758,.8505),(.76,.945),(.7555,.93625),(.7615,.79625)]
out=[]
for eta,kappa in points:
 for g in [0.,.0001,.05,.25,.75,1.]:
  for reg in ['SU','IS']:
   sols=[]
   for seed in [[.3,.5,.9],[.9,.2,.6],[.7,.7,.7]]:
    sol=root(lambda x:system(x,g,reg,eta,kappa,False),seed,jac=lambda x:system(x,g,reg,eta,kappa)[1],tol=1e-11)
    if max(abs(system(sol.x,g,reg,eta,kappa,False)))>1e-9:raise RuntimeError('stationary failure')
    sols.append(sol.x)
   x=sols[0];q,B,M=quantities(x,g,reg,eta)
   F,J=system(x,g,reg,eta,kappa)
   maxprof=0
   for i in range(3):
    def pi(t):
     xx=x.copy();xx[i]=t;qq,_,_=quantities(xx,g,reg,eta)
     return 3*qq[i]**2-kappa*(1-t)**2/2
    opt=minimize_scalar(lambda t:-pi(t),bounds=(0,1),method='bounded',options={'xatol':1e-13})
    maxprof=max(maxprof,max(pi(0),pi(1),pi(opt.x))-pi(x[i]))
   out.append({'eta':eta,'kappa':kappa,'g':g,'regime':reg,'x':x.tolist(),'q_min':float(min(q)),'B_eigen_min':float(min(np.linalg.eigvalsh(B))),'foc_residual':float(max(abs(F))),'seed_max_difference':float(max(max(abs(v-x)) for v in sols)),'unilateral_max_profit_gain':float(maxprof),'own_profit_second_derivative_max':float(max(np.diag(J))),'symmetric_J_eigen_max':float(max(np.linalg.eigvalsh((J+J.T)/2)))})
p=Path(__file__).with_name('phase_nash_spotchecks.json');p.write_text(json.dumps(out,indent=2))
print(json.dumps({'cases':len(out),'roots':len(out)*3,'min_x':min(min(v['x']) for v in out),'max_x':max(max(v['x']) for v in out),'min_q':min(v['q_min'] for v in out),'max_FOC':max(v['foc_residual'] for v in out),'max_seed_difference':max(v['seed_max_difference'] for v in out),'max_unilateral_gain':max(v['unilateral_max_profit_gain'] for v in out),'max_own_second_derivative':max(v['own_profit_second_derivative_max'] for v in out),'min_B_eigen':min(v['B_eigen_min'] for v in out)},indent=2))
