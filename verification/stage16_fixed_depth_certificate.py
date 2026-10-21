#!/usr/bin/env python3
"""Independent exact Fraction+Krawczyk certificate: g=1/20, stdlib only."""
from fractions import Fraction as Q
class I:
 def __init__(self,a,b=None):
  self.l,self.h=(a.l,a.h) if isinstance(a,I) else (Q(a),Q(a if b is None else b))
  assert self.l<=self.h
 def c(self,x):return x if isinstance(x,I) else I(x)
 def __add__(self,x):
  x=self.c(x);return I(self.l+x.l,self.h+x.h)
 __radd__=__add__
 def __neg__(self):return I(-self.h,-self.l)
 def __sub__(self,x):return self+-self.c(x)
 def __rsub__(self,x):return self.c(x)+-self
 def __mul__(self,x):
  x=self.c(x);p=[u*v for u in (self.l,self.h) for v in (x.l,x.h)];return I(min(p),max(p))
 __rmul__=__mul__
 def __truediv__(self,x):
  x=self.c(x);assert x.l*x.h>0;return self*I(1/x.h,1/x.l)
 def __rtruediv__(self,x):return self.c(x)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  if not n:return I(1)
  p=[self.l**n,self.h**n]
  if n%2==0 and self.l<=0<=self.h:p.append(Q(0))
  return I(min(p),max(p))
 def mid(self):return (self.l+self.h)/2
 def show(self):return (float(self.l),float(self.h))
ETA=Q(379,500); RHO=Q(9,10); K=Q(1701,2000)
BETA=1-RHO;DELTA=RHO-ETA;A=2-ETA;G=Q(1,20)
def sz(z):
 t=BETA*z;return K*(1-z)-6*BETA*A/((A-t)*(A+2*t)**3)
l,r=Q(7,10),Q(3,4)
for _ in range(106):
 m=(l+r)/2
 if sz(m)>0:l=m
 else:r=m
assert sz(l)>0>sz(r) and r-l<Q(1,10**30)
Z=I(l,r)
def mat(x,mode):
 h={(0,1):G if mode in ('SU','IS') else 0,(0,2):G if mode=='IS' else 0,(1,2):G if mode=='IS' else 0}
 B=[[I(1 if i==j else RHO*h[min(i,j),max(i,j)]+BETA*(x[i]+x[j])/2) for j in range(3)] for i in range(3)]
 M=[[I(A if i==j else DELTA*h[min(i,j),max(i,j)]+BETA*(x[i]+x[j])/2) for j in range(3)] for i in range(3)]
 return B,M
def inv(m):
 a,b,c,e=m[0][0],m[0][1],m[0][2],m[1][2]
 d=a**3+2*b*c*e-a*(b*b+c*c+e*e);assert d.l>0
 return [[v/d for v in row] for row in [[a*a-e*e,c*e-a*b,b*e-a*c],[c*e-a*b,a*a-c*c,b*c-a*e],[b*e-a*c,b*c-a*e,a*a-b*b]]]
def mv(m,v):return [sum((m[i][j]*v[j] for j in range(3)),I(0)) for i in range(3)]
def evalx(x,mode,lam,jac=False):
 B,M=mat(x,mode);R=inv(M);q=mv(R,[I(1)]*3)
 E=[[[I(BETA/2 if i!=k and (i==j or k==j) else 0) for k in range(3)] for i in range(3)] for j in range(3)]
 dx=[[-v for v in mv(R,mv(E[j],q))] for j in range(3)]
 F=[6*q[i]*dx[i][i]+K*(1-x[i])-lam*(x[i]-Z) for i in range(3)]
 if not jac:return F
 J=[]
 for i in range(3):
  row=[]
  for j in range(3):
   xij=mv(R,mv(E[j],mv(R,mv(E[i],q))))
   xji=mv(R,mv(E[i],mv(R,mv(E[j],q))))
   row.append(6*(dx[j][i]*dx[i][i]+q[i]*(xij[i]+xji[i]))-(K+lam if i==j else 0))
  J.append(row)
 return F,J
CENTERS={(2,'SU'):('0.71943493680857','0.71902020859959'),(2,'IS'):('0.72068343123925',),
 (4,'SU'):('0.71908258425354','0.71883911218911'),(4,'IS'):('0.71980691959296',),
 (5,'SU'):('0.71899784128711','0.71879603574198'),(5,'IS'):('0.71959650360396',)}
def red(y,mode,lam,jac=False):
 x=[y[0],y[0],y[1]] if mode=='SU' else [y[0]]*3
 if not jac:
  f=evalx(x,mode,lam);return [f[0],f[2]] if mode=='SU' else [f[0]]
 f,j=evalx(x,mode,lam,True)
 return ([f[0],f[2]],[[j[0][0]+j[0][1],j[0][2]],[j[2][0]+j[2][1],j[2][2]]]) if mode=='SU' else ([f[0]],[[sum(j[0],I(0))]])
def rootbox(mode,lam,band=False):
 vals=CENTERS[(5 if band else int(lam),mode)]
 center=[Q(v) for v in vals];rad=Q(1,10**5 if band else 10**7)
 cube=[I(v-rad,v+rad) for v in center]
 f=red([I(v) for v in center],mode,lam)
 _,j=red(cube,mode,lam,True);_,jc=red([I(v) for v in center],mode,lam,True)
 mat0=[[v.mid() for v in row] for row in jc]
 if len(center)==1:invj=[[1/mat0[0][0]]]
 else:
  (a,b),(c,d)=mat0;dt=a*d-b*c;invj=[[d/dt,-b/dt],[-c/dt,a/dt]]
 for i in range(len(center)):
  k=I(center[i])-sum((invj[i][jj]*f[jj] for jj in range(len(center))),I(0))
  for jj in range(len(center)):
   co=I(int(i==jj))-sum((invj[i][h]*j[h][jj] for h in range(len(center))),I(0))
   k+=co*I(-rad,rad)
  assert cube[i].l<k.l and k.h<cube[i].h and 0<cube[i].l<cube[i].h<1
 assert ((I(K)+lam).l if isinstance(lam,I) else K+lam)>54*BETA**2/(ETA**2*A**2)
 return [cube[0],cube[0],cube[1]] if mode=='SU' else [cube[0]]*3
def welfare(x,mode,lam):
 B,M=mat(x,mode);q=mv(inv(M),[I(1)]*3)
 assert all(v.l>0 for v in q)
 cs=sum((q[i]*B[i][j]*q[j] for i in range(3) for j in range(3)),I(0))/2
 return [cs+3*q[i]**2-K*(1-x[i])**2/2-lam*(x[i]-Z)**2/2 for i in range(3)]
SW=welfare([Z]*3,'SW',Q(0))[0]
def verify(lam,band=False):
 S=welfare(rootbox('SU',lam,band),'SU',lam)
 F=welfare(rootbox('IS',lam,band),'IS',lam)
 v={'bilateral':S[0]-SW,'outsider':F[2]-S[2],
    'incumbent':F[0]-S[0],'grand':F[0]-SW}
 print('lambda', '[4.99,5.01]' if band else lam,{k:x.show() for k,x in v.items()})
 if band or lam==5:assert all(x.l>0 for x in v.values())
 if lam==4:assert v['outsider'].h<0
 if lam==2:assert v['bilateral'].l>0 and v['outsider'].h<0
for t in (Q(2),Q(4),Q(5)):verify(t)
verify(I(Q(499,100),Q(501,100)),True)
print('PASS exact finite-depth votes at g=1/20 and uniform lambda band')
