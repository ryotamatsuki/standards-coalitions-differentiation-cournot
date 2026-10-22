#!/usr/bin/env python3
"""Exact Fraction / parametric Krawczyk proof of unique government-optimal g at lambda=5.
No external dependencies. Predecessor global bilateral envelope is PR17.
"""
from fractions import Fraction as Q
class I:
 __slots__=('l','h')
 def __init__(self,a,b=None):
  if isinstance(a,I):self.l,self.h=a.l,a.h
  else:self.l,self.h=Q(a),Q(a if b is None else b)
  assert self.l<=self.h
 @staticmethod
 def cv(x):return x if isinstance(x,I) else I(x)
 def __add__(self,v):
  v=self.cv(v);return I(self.l+v.l,self.h+v.h)
 __radd__=__add__
 def __neg__(self):return I(-self.h,-self.l)
 def __sub__(self,v):return self+-self.cv(v)
 def __rsub__(self,v):return self.cv(v)+-self
 def __mul__(self,v):
  v=self.cv(v);p=[a*b for a in (self.l,self.h) for b in (v.l,v.h)]
  return I(min(p),max(p))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=self.cv(v);assert v.l*v.h>0
  return self*I(1/v.h,1/v.l)
 def __rtruediv__(self,v):return self.cv(v)/self
 def __pow__(self,n):
  assert n in (0,2,3)
  if n==0:return I(1)
  if n==2:return I(0 if self.l<=0<=self.h else min(self.l**2,self.h**2),max(self.l**2,self.h**2))
  return I(self.l**3,self.h**3)
 def mid(self):return (self.l+self.h)/2
 def __repr__(self):return f'[{float(self.l):.9g},{float(self.h):.9g}]'
class AD:
 __slots__=('v','d')
 def __init__(self,v,d=None):
  self.v=I(v);self.d=[I(0) for _ in range(3)] if d is None else d
 @staticmethod
 def cv(x):return x if isinstance(x,AD) else AD(x)
 def __add__(self,v):
  v=self.cv(v);return AD(self.v+v.v,[a+b for a,b in zip(self.d,v.d)])
 __radd__=__add__
 def __neg__(self):return AD(-self.v,[-x for x in self.d])
 def __sub__(self,v):return self+-self.cv(v)
 def __rsub__(self,v):return self.cv(v)+-self
 def __mul__(self,v):
  v=self.cv(v);return AD(self.v*v.v,[a*v.v+self.v*b for a,b in zip(self.d,v.d)])
 __rmul__=__mul__
 def __truediv__(self,v):
  v=self.cv(v);x=self.v/v.v
  return AD(x,[(a-x*b)/v.v for a,b in zip(self.d,v.d)])
 def __rtruediv__(self,v):return self.cv(v)/self
 def __pow__(self,n):
  assert n in (2,3)
  return AD(self.v**n,[n*(self.v**(n-1) if n>2 else self.v)*v for v in self.d])
a=Q(621,500);be=Q(1,10);delta=Q(71,500);rho=Q(9,10)
k=Q(1701,2000);lam=Q(5)
zl,zh=Q('0.7'),Q('0.75')
def fz(z):
 t=be*z
 return k*(1-z)-6*be*a/((a-t)*(a+2*t)**3)
for _ in range(150):
 mid=(zl+zh)/2
 if fz(mid)>0:zl=mid
 else:zh=mid
assert fz(zl)>0>fz(zh)
Z=I(zl,zh)
def model(U,V,G,mode):
 t=delta*G+be*U
 h=be*(U+V)/2 if mode=='SU' else t
 B=rho*G+be*U
 T=a*(a+t)-2*h*h
 qm=(a-h)/T;qo=(a+t-2*h)/T
 raa=(a*a-h*h)/((a-t)*T)
 dqa=-be/2*(raa*qo+(a-h)*qm/T)
 dqc=-be*((a+t)*qm-h*qo)/T
 Fu=6*qm*dqa+k*(1-U)-lam*(U-Z)
 Fv=6*qo*dqc+k*(1-V)-lam*(V-Z)
 cs=(1+B)*qm*qm+qo*qo/2+2*(B if mode=='IS' else h)*qm*qo
 Wa=cs+3*qm*qm-k*(1-U)**2/2-lam*(U-Z)**2/2
 Wc=cs+3*qo*qo-k*(1-V)**2/2-lam*(V-Z)**2/2
 return Fu,Fv,Wa,Wc
def evaluate(u,v,g,mode):
 U=AD(u,[I(1),I(0),I(0)])
 V=AD(v,[I(0),I(1),I(0)])
 G=AD(g,[I(0),I(0),I(1)])
 return model(U,V,G,mode)
def approx_center(g,mode):
 # Fixed-precision exact rational Newton: seeds are NOT certificates.
 z=Q('0.7185927073221112')
 x=[z+Q('.018')*g] if mode=='IS' else [z+Q('.008')*g,z+Q('.004')*g]
 D=10**20
 for _ in range(5):
  f=evaluate(I(x[0]),I(x[0] if mode=='IS' else x[1]),I(g),mode)
  if mode=='IS':
   j=(f[0].d[0]+f[0].d[1]).mid()
   x=[Q(round((x[0]-f[0].v.mid()/j)*D),D)]
  else:
   p,r=f[0].d[0].mid(),f[0].d[1].mid()
   s,t=f[1].d[0].mid(),f[1].d[1].mid()
   den=p*t-r*s
   A=(t*f[0].v.mid()-r*f[1].v.mid())/den
   B=(-s*f[0].v.mid()+p*f[1].v.mid())/den
   x=[Q(round((x[0]-A)*D),D),Q(round((x[1]-B)*D),D)]
 return x
def enclose(g1,g2,mode):
 mid=(g1+g2)/2;x=approx_center(mid,mode);n=len(x)
 radius=Q(1,10**6)+(g2-g1)/40
 box=[I(v-radius,v+radius) for v in x]
 F=evaluate(box[0],box[0] if mode=='IS' else box[1],I(g1,g2),mode)
 Fc=evaluate(I(x[0]),I(x[0] if mode=='IS' else x[1]),I(g1,g2),mode)
 Jm=evaluate(I(x[0]),I(x[0] if mode=='IS' else x[1]),I(mid),mode)
 idx=(0,) if mode=='IS' else (0,1)
 J=[[F[i].d[j]+(F[i].d[1] if mode=='IS' else I(0)) for j in idx] for i in idx]
 J0=[[Jm[i].d[j]+(Jm[i].d[1] if mode=='IS' else I(0)) for j in idx] for i in idx]
 if n==1:R=[[I(1)/J0[0][0].mid()]]
 else:
  aa,bb=J0[0];cc,dd=J0[1]
  d=aa.mid()*dd.mid()-bb.mid()*cc.mid()
  R=[[I(dd.mid()/d),I(-bb.mid()/d)],[I(-cc.mid()/d),I(aa.mid()/d)]]
 for i in range(n):
  image=I(x[i])-sum((R[i][j]*Fc[idx[j]].v for j in range(n)),I(0))
  for j in range(n):
   h=I(int(i==j))-sum((R[i][l]*J[l][j] for l in range(n)),I(0))
   image+=h*I(-radius,radius)
  assert box[i].l<image.l and image.h<box[i].h,(mode,g1,g2,i)
 if mode=='IS':
  slope=-(F[0].d[2]/(F[0].d[0]+F[0].d[1]))
  wi=F[2].d[2]+(F[2].d[0]+F[2].d[1])*slope
  return F,wi,wi
 ja,jb=F[0].d[0],F[0].d[1]
 jc,jd=F[1].d[0],F[1].d[1]
 det=ja*jd-jb*jc
 ug=(-jd*F[0].d[2]+jb*F[1].d[2])/det
 vg=(jc*F[0].d[2]-ja*F[1].d[2])/det
 wa=F[2].d[2]+F[2].d[0]*ug+F[2].d[1]*vg
 wc=F[3].d[2]+F[3].d[0]*ug+F[3].d[1]*vg
 return F,wa,wc
def certify(left,right,predicate):
 stack=[(Q(left),Q(right),0)];done=0
 while stack:
  lo,hi,depth=stack.pop()
  try:
   grand,di,dci=enclose(lo,hi,'IS')
   bilateral,_,dco=enclose(lo,hi,'SU')
   cp=dci-dco
   if predicate=='Cpositive':pass_test=cp.l>0
   elif predicate=='Cnegative':pass_test=cp.h<0
   elif predicate=='bounded':pass_test=cp.l>Q('-.01') and cp.h<Q('.01')
   elif predicate=='Ipositive':pass_test=di.l>0
   else:raise ValueError(predicate)
   if pass_test:done+=1;continue
  except (ArithmeticError,AssertionError,ZeroDivisionError):pass
  assert depth<20,('undischarged',predicate,lo,hi)
  mid=(lo+hi)/2
  stack.extend(((lo,mid,depth+1),(mid,hi,depth+1)))
 print('PASS',predicate,float(Q(left)),float(Q(right)),'cells',done)
 return done
D=10**35;rad=Q(1,10**23)
def rnd(v):return Q(round(v*D),D)
def refine(g,mode):
 x=approx_center(g,mode)
 for _ in range(4):
  f=evaluate(I(x[0]),I(x[0] if mode=='IS' else x[1]),I(g),mode)
  if mode=='IS':
   j=(f[0].d[0]+f[0].d[1]).mid()
   x=[rnd(x[0]-f[0].v.mid()/j)]
  else:
   aa,bb=f[0].d[0].mid(),f[0].d[1].mid()
   cc,dd=f[1].d[0].mid(),f[1].d[1].mid()
   dt=aa*dd-bb*cc
   dx=(dd*f[0].v.mid()-bb*f[1].v.mid())/dt
   dy=(-cc*f[0].v.mid()+aa*f[1].v.mid())/dt
   x=[rnd(x[0]-dx),rnd(x[1]-dy)]
 return x
def point(g,mode):
 x=refine(g,mode);n=len(x)
 box=[I(t-rad,t+rad) for t in x]
 f=evaluate(box[0],box[0] if mode=='IS' else box[1],I(g),mode)
 fc=evaluate(I(x[0]),I(x[0] if mode=='IS' else x[1]),I(g),mode)
 idx=(0,) if mode=='IS' else (0,1)
 J=[[f[i].d[j]+(f[i].d[1] if mode=='IS' else I(0)) for j in idx] for i in idx]
 if n==1:R=[[I(1)/J[0][0].mid()]]
 else:
  aa,bb=J[0];cc,dd=J[1]
  det=aa.mid()*dd.mid()-bb.mid()*cc.mid()
  R=[[I(dd.mid()/det),I(-bb.mid()/det)],[I(-cc.mid()/det),I(aa.mid()/det)]]
 for i in range(n):
  image=I(x[i])-sum((R[i][j]*fc[j].v for j in range(n)),I(0))
  for j in range(n):
   h=I(int(i==j))-sum((R[i][l]*J[l][j] for l in range(n)),I(0))
   image+=h*I(-rad,rad)
  assert box[i].l<image.l and image.h<box[i].h
 return f
def main():
 assert fz(zl)>0 and fz(zh)<0 and zh-zl<Q(1,10**30)
 for x,y,c in [('0','.02','Cpositive'),('.02','.04','bounded'),
               ('.04','1','Cnegative'),('0','.06','Ipositive')]:
  certify(x,y,c)
 c03=point(Q('.03'),'IS')[3].v-point(Q('.03'),'SU')[3].v
 assert c03.l>Q('.0001')
 # MVT with |Phi'|<.01 over [.02,.04], distance from .03 <= .01:
 assert c03.l-Q('.0001')>0
 lo,hi=Q('.05433320681'),Q('.05433320682')
 pos=point(lo,'IS')[3].v-point(lo,'SU')[3].v
 neg=point(hi,'IS')[3].v-point(hi,'SU')[3].v
 assert pos.l>0 and neg.h<0
 I0,_,_=enclose(lo,hi,'IS')
 S0,_,_=enclose(lo,hi,'SU')
 SW=point(Q(0),'IS')[2].v
 assert (S0[2].v-SW).l>0
 assert (I0[2].v-S0[2].v).l>0
 assert (I0[2].v-SW).l>0
 print('PASS: unique binding root in (0.05433320681,0.05433320682)')
 print('PASS: national votes at bound, monotone IS objective, global outsider domain')
 print('UNDER WEAK-ACCEPTANCE TIE RULE: g* is unique attained optimal depth')
 print('NOTE: global SU envelope comparison inherited from certified PR17.')
if __name__=='__main__':main()
