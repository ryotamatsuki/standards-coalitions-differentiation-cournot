"""80-digit independent three-firm Nash reconstruction at endogenous SW-mislabel cell.
High precision numerical evidence; not an interval proof.
"""
import mpmath as mp,json
from pathlib import Path
mp.mp.dps=80
rho=mp.mpf('.9');eta=mp.mpf('.76');kappa=mp.mpf('.945');g=mp.mpf('.0001');beta=1-rho

def econ(x,h,reg):
 H=mp.eye(3)
 if reg=='SU':H[0,1]=H[1,0]=h
 if reg=='IS':
  for j in range(3):
   for i in range(3):
    if i!=j:H[i,j]=h
 X=mp.matrix(3)
 for j in range(3):
  for i in range(3):X[i,j]=1 if i==j else (x[i]+x[j])/2
 B=rho*H+beta*X;M=mp.eye(3)+B-eta*H;q=mp.lu_solve(M,mp.matrix([1,1,1]));cs=(q.T*B*q)[0]/2
 return q,M,[cs+3*q[i]**2-kappa*(1-x[i])**2/2 for i in range(3)]
def solve(h,reg):
 def f(a,b,c):
  x=[a,b,c];q,M,_=econ(x,h,reg);out=[]
  for i in range(3):
   E=mp.zeros(3)
   for j in range(3):
    if j!=i:E[i,j]=E[j,i]=beta/2
   dq=mp.lu_solve(M,-E*q)
   out.append(6*q[i]*dq[i]+kappa*(1-x[i]))
  return out
 x=mp.findroot(f,(mp.mpf('.7'),)*3)
 return econ(x,h,reg)[2],x,max(abs(v) for v in f(*x))
sw,z,r0=solve(0,'SW');su,x1,r1=solve(g,'SU');is_,x2,r2=solve(g,'IS');s=sw[0];m=su[0];o=su[2];i=is_[0]
assert min(i-s,i-m,i-o)>0
r={key:mp.nstr(v,60) for key,v in {'kappa':kappa,'eta':eta,'g':g,'z':z[0],'m-s':m-s,'i-s':i-s,'i-m':i-m,'i-o':i-o,'max_Nash_FOC_residual':max(r0,r1,r2)}.items()}
r['method']='80-digit mpmath full-three-variable Nash system; not interval certification'
print(json.dumps(r,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2))
