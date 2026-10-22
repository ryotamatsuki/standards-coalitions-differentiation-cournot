"""Independent v0.4 Figure 3 audit. Numerical evidence, not interval proof.
No imports from the supplied phase evaluator; derivatives use full three-firm systems.
"""
from pathlib import Path
import json,sys,time
import numpy as np
from scipy.optimize import brentq,root,minimize_scalar

SRC=Path(__file__).resolve().parent/'input_v04'
OUT=Path(__file__).resolve().parent
rho=.9; beta=1-rho; d=1.

def quantities(x,g,reg,eta):
 x=np.asarray(x);g=np.asarray(g)
 H=np.broadcast_to(np.eye(3),x.shape[:-1]+(3,3)).copy()
 if reg=='IS':
  H+=g[...,None,None]*(np.ones((3,3))-np.eye(3))
 elif reg=='SU':H[...,0,1]=H[...,1,0]=g
 X=(x[..., :,None]+x[...,None,:])/2
 X[...,range(3),range(3)]=1
 B=rho*H+beta*X; M=np.eye(3)+B-eta*H
 q=np.linalg.solve(M,np.ones_like(x)[...,None])[...,0]
 return q,B,M

E=np.zeros((3,3,3))
for i in range(3):
 for j in range(3):
  if j!=i:E[i,i,j]=E[i,j,i]=beta/2

def system(x,g,reg,eta,kappa,need_jac=True):
 q,B,M=quantities(x,g,reg,eta)
 inv=np.linalg.inv(M)
 dq=np.stack([-np.einsum('...ij,jk,...k->...i',inv,E[j],q) for j in range(3)],axis=-1)
 F=6*q*np.diagonal(dq,axis1=-2,axis2=-1)+kappa*(1-x)
 if not need_jac:return F
 J=np.zeros(x.shape[:-1]+(3,3))
 for i in range(3):
  for j in range(3):
   d2=-np.einsum('...ab,bc,...c->...a',inv,E[i],dq[...,j])-np.einsum('...ab,bc,...c->...a',inv,E[j],dq[...,i])
   J[...,i,j]=6*(dq[...,i,j]*dq[...,i,i]+q[...,i]*d2[...,i])-kappa*(i==j)
 return F,J

def solve(g,reg,eta,kappa,seed=.72):
 g=np.asarray(g);x=np.broadcast_to(np.asarray(seed),g.shape+(3,)).copy()
 if np.asarray(seed).ndim==0:x[:]=seed
 for it in range(20):
  F,J=system(x,g,reg,eta,kappa)
  if np.max(np.abs(F))<2e-13:break
  x-=np.linalg.solve(J,F[...,None])[...,0]
 if np.max(np.abs(system(x,g,reg,eta,kappa,False)))>1e-10:raise RuntimeError('Nash residual')
 return x

def welfare(x,g,reg,eta,kappa):
 q,B,M=quantities(x,g,reg,eta)
 cs=.5*np.einsum('...i,...ij,...j->...',q,B,q)
 return cs[...,None]+3*q*q-kappa*(1-x)**2/2

def evals(g,eta,kappa,frozen):
 z=solve(0,'SW',eta,kappa)
 xsu=np.broadcast_to(z,np.asarray(g).shape+(3,)) if frozen else solve(g,'SU',eta,kappa)
 xis=np.broadcast_to(z,np.asarray(g).shape+(3,)) if frozen else solve(g,'IS',eta,kappa)
 s=float(welfare(z,0,'SW',eta,kappa)[0])
 wsu=welfare(xsu,g,'SU',eta,kappa);wi=welfare(xis,g,'IS',eta,kappa)
 return s,wsu[...,0],wsu[...,2],wi[...,0]

def scan(eta,kappa,n=20001):
 out={};gs=np.linspace(0,1,n)
 for frozen in [True,False]:
  s,m,o,i=evals(gs,eta,kappa,frozen)
  isok=(i>=s)&(i>=m)&(i>=o)
  suok=(~isok)&(m>=s)
  gain=np.where(isok,i-s,np.where(suok,m-s,0))
  j=np.argmax(gain)
  out['frozen' if frozen else 'endogenous']={'label':'SW' if gain[j]<=1e-12 else ('IS' if isok[j] else 'SU'),'g':float(gs[j]),'gain':float(gain[j]),'min_IS_vote_margin':float(min(i[j]-s,i[j]-m[j],i[j]-o[j])),'best_SU_gain':(float(np.max(m[suok]-s)) if np.any(suok) else None),'n':n}
 return out

def local(eta,kappa):
 z=solve(0,'SW',eta,kappa); zz=z[0];a=2-eta;t=beta*zz;L=a+2*t;P=a-t;delta=rho-eta
 D=rho/L**2-delta/L**3*(2*(1+2*t)+6*a/P)
 h=1e-5
 s,m,o,i=evals(np.array([0,h]),eta,kappa,False)
 # Estimate is secondary to independent Jacobian and primitive derivatives.
 F,J=system(z,0,'SU',eta,kappa)
 Fg=(system(z,h,'SU',eta,kappa,False)-system(z,-h,'SU',eta,kappa,False))/(2*h)
 xg=-np.linalg.solve(J,Fg)
 C=beta*(eta+2*t)/L**3;V=3*beta*(a-2*t)/(P*L**3)
 mu=D-C*sum(xg)-V*(xg[1]+xg[2])
 return {'z':float(zz),'D':float(D),'mu':float(mu),'xg':xg.tolist()}

if __name__=='__main__':
 data=np.load(SRC/'figure3_data_41x41.npz');r={'metadata':{},'local_mismatches':[],'points':[]}
 for j,eta in enumerate(data['es']):
  for k,kappa in enumerate(data['ks']):
   l=local(float(eta),float(kappa))
   for name,slope in [('F',l['D']),('N',l['mu'])]:
    if data[name][j,k]==0 and slope>1e-8:r['local_mismatches'].append({'panel':name,'j':j,'i':k,'eta':float(eta),'kappa':float(kappa),'slope':slope})
 print('SW with positive incident slope',len(r['local_mismatches']),flush=True)
 (OUT/'phase_independent_results.json').write_text(json.dumps(r,indent=2))
 points=[(.758,.8505),(.7555,1.05),(.75625,.7),(.76,.9625),(.76225,.74375)]
 for v in r['local_mismatches']:points.append((v['eta'],v['kappa']))
 for eta,kappa in points:
  p={'eta':eta,'kappa':kappa,'local':local(eta,kappa),'scan':scan(eta,kappa)}
  r['points'].append(p);print(json.dumps(p),flush=True)
  (OUT/'phase_independent_results.json').write_text(json.dumps(r,indent=2))
