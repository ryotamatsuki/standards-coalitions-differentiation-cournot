"""Independent Stage23 floating-point Nash and counterfactual audit.
Requires numpy and scipy. Fixed lambda=0 benchmark; global Nash certification
requires separate exact Rosen/Krawczyk checks. No journal policy claims.
"""
import numpy as np
from scipy.optimize import least_squares, minimize_scalar
d,eta,rho,k=1.0,379/500,9/10,1701/2000
beta=1-rho
z0=0.0
def solve(regime,g,lamb=0.0,frozen=None):
 H=np.eye(3)
 if regime=="SU":H[0,1]=H[1,0]=g
 if regime=="IS":H[:,:]=g;np.fill_diagonal(H,1)
 def stats(x):
  X=np.ones((3,3))
  for a in range(3):
   for b in range(3):
    if a!=b:X[a,b]=(x[a]+x[b])/2
  B=rho*H+beta*X;M=np.eye(3)+B-eta*H
  q=np.linalg.solve(M,np.full(3,d))
  CS=q@B@q/2
  p=3*q*q-k*(1-x)**2/2-lamb*(x-z0)**2/2
  return CS+p,p,CS,q,M
 def foc(x):
  w,p,cs,q,M=stats(x); R=np.linalg.inv(M)
  F=np.empty(3)
  for a in range(3):
   E=np.zeros((3,3))
   for b in range(3):
    if a!=b:E[a,b]=E[b,a]=beta/2
   dq=-(R@E@q)[a]
   F[a]=6*q[a]*dq+k*(1-x[a])-lamb*(x[a]-z0)
  return F
 x=np.full(3,frozen) if frozen is not None else least_squares(foc,np.full(3,.72),bounds=(np.zeros(3),np.ones(3)),xtol=1e-13,gtol=1e-13,ftol=1e-13).x
 if frozen is None:
  assert np.max(np.abs(foc(x)))<1e-8
  for a in range(3):
   xx=x.copy(); p=stats(x)[1][a]
   def obj(t):xx[a]=t;return -stats(xx)[1][a]
   assert minimize_scalar(obj,bounds=(0,1),method="bounded").fun>=-p-1e-8
 return x,stats(x)
x0,(s,ps,cs,qs,M)=solve("SW",0.0)
z0=x0[0]
print("baseline x, welfare, CS, profits",z0,s[0],cs,ps[0])
for frozen in [False,True]:
 for regime in ["SU","IS"]:
  x,(w,p,cs,q,M)=solve(regime,0.05,frozen=z0 if frozen else None)
  print(regime,"frozen=",frozen,"x=",x,"W=",w,"CS=",cs,"P=",p)
x,(w,p,cs,q,M)=solve("IS",.054333206815,lamb=5)
xx,(b,pb,csb,qb,Mb)=solve("SU",.054333206815,lamb=5)
print("lambda5",w[0],b[2],w[0]-b[2])
