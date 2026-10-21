#!/usr/bin/env python3
"""Independent rational-interval check: V2b one-parameter adjustment-cost extension.
Local policy-depth slopes only; NOT a global-lambda SPNE proof.
Uses only Python standard library.
"""
from fractions import Fraction as Q

class I:
    def __init__(self, lo, hi=None):
        self.lo=Q(lo); self.hi=Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def cv(x): return x if isinstance(x,I) else I(x)
    def __add__(self,o):
        o=self.cv(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-self.cv(o)
    def __rsub__(self,o): return self.cv(o)+-self
    def __mul__(self,o):
        o=self.cv(o);v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.cv(o);assert o.lo*o.hi>0
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return self.cv(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        vals=[self.lo**n,self.hi**n]
        if n%2==0 and self.lo<=0<=self.hi:vals.append(Q(0))
        return I(min(vals),max(vals))
    def bounds(self):return tuple(float(v) for v in (self.lo,self.hi))

eta0=Q(379,500);rho0=Q(9,10);kap0=Q(1701,2000)
zl,zh=Q('0.71859270732'),Q('0.71859270733')
def F(z):
    a=2-eta0;b=1-rho0;t=b*z
    return kap0*(1-z)-6*b*a/((a-t)*(a+2*t)**3)
assert F(zl)>0>F(zh)

def check(lam):
    e=I(eta0);rho=I(rho0);k=I(kap0);z=I(zl,zh)
    b=1-rho;a=2-e;de=rho-e;t=b*z;P=a-t;L=a+2*t
    ell=-k+6*b*b*(a-2*t)*(2*a+t)/(P*P*L**4)
    h=3*b*b*(3*a-2*t)/(P*L**4)
    p=6*de*b*(a-2*t)*(2*a+t)/(P*P*L**4)
    r=6*de*b*(a*a-2*a*t+4*t*t)/(P*P*L**4)
    C=b*(e+2*t)/L**3
    V=3*b*(a-2*t)/(P*L**3)
    D=rho/L**2-de*(2*(1+2*t)/L**3+6*a/(P*L**3))
    A=I(lam)-ell
    assert (A-2*h).lo>0
    den=(A+h)*(A-2*h)
    u=(A*p+h*r)/den
    v=(2*h*p+(A-h)*r)/den
    loss=C*(2*u+v)+V*(u+v)
    m=D-loss
    outside=rho/L**2-2*de*(1+2*t)/L**3+12*de*t/(P*L**3)-C*(2*u+v)-V*(2*u)
    return dict(member=m,outsider=outside,grand=2*m+outside,up=u,vp=v,ell=ell,h=h,p=p,r=r)

a0=check(Q(0));aL=check(Q('0.93538'))
aH=check(Q('0.93539'));a1=check(Q(1))
assert a0['ell'].hi<0 and a0['h'].lo>0
assert (-a0['ell']-2*a0['h']).lo>0
assert a0['p'].lo>0 and a0['r'].lo>0
assert a0['member'].hi<0 and a0['grand'].lo>0
assert aL['member'].hi<0 and aH['member'].lo>0
assert a1['member'].lo>0 and a1['outsider'].lo>0 and a1['grand'].lo>0
for label,res in [('lambda0',a0),('lambda_lower',aL),('lambda_upper',aH),('lambda1',a1)]:
    print(label, {k:res[k].bounds() for k in ('member','outsider','grand','up','vp')})
print('PASS: exact rational sign certificates at true SW Nash root')
print('SCOPE: unique local crossing by M-matrix monotonicity; global policy-depth threshold unproved')
