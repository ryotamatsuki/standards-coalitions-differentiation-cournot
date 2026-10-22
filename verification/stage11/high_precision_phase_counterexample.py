"""80-decimal numerical check of strict accepted-IS counterexample to Figure 3 SW cell.
This is arbitrary precision arithmetic, not outward-rounded interval certification.
"""
import mpmath as mp,json
from pathlib import Path
mp.mp.dps=80
rho=mp.mpf('.9');d=mp.mpf('1')
def point(k,e,g):
 k,e,g=map(mp.mpf,[k,e,g]);a=2-e;b=1-rho
 def f(z):
  t=b*z;return k*(1-z)-6*b*a/((a-t)*(a+2*t)**3)
 z=mp.findroot(f,(mp.mpf('.6'),mp.mpf('.9')))
 def w(reg):
  H=mp.eye(3)
  if reg=='SU':H[0,1]=H[1,0]=g
  if reg=='IS':
   for j in range(3):
    for i in range(3):
     if i!=j:H[i,j]=g
  X=mp.matrix(3)
  for j in range(3):
   for i in range(3):X[i,j]=1 if i==j else z
  B=rho*H+b*X;M=mp.eye(3)+B-e*H;q=mp.lu_solve(M,mp.matrix([1,1,1]));cs=(q.T*B*q)[0]/2
  return [cs+3*q[i]**2-k*(1-z)**2/2 for i in range(3)]
 s=w('SW')[0];m,_,o=w('SU');i=w('IS')[0]
 assert min(i-s,i-m,i-o)>0
 return {key:mp.nstr(v,60) for key,v in {'kappa':k,'eta':e,'g':g,'z':z,'m-s':m-s,'i-s':i-s,'i-m':i-m,'i-o':i-o}.items()}
r={'precision_decimal_digits':mp.mp.dps,'method':'mpmath findroot and LU; not interval proof','points':[point('.93625','.7555','.0001'),point('.945','.7555','.00055')]}
print(json.dumps(r,indent=2));Path(__file__).with_name('high_precision_phase_counterexample.json').write_text(json.dumps(r,indent=2))
