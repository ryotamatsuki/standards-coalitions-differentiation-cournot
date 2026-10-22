#!/usr/bin/env python3
"""Stage19: exact rational sufficient-condition audit for private/social design wedge.
No imports from preceding V2b scripts; no NumPy, SymPy or SciPy required.
Analyzes grand coalition at a fixed g, with a symmetric constrained planner.
"""
from fractions import Fraction as Q

class I:
    def __init__(self, a, b=None):
        if isinstance(a,I): self.l,self.h=a.l,a.h
        else: self.l,self.h=Q(a),Q(a if b is None else b)
        assert self.l<=self.h
    @staticmethod
    def c(x): return x if isinstance(x,I) else I(x)
    def __add__(self,v):
        v=self.c(v);return I(self.l+v.l,self.h+v.h)
    __radd__=__add__
    def __neg__(self):return I(-self.h,-self.l)
    def __sub__(self,v):return self+-self.c(v)
    def __rsub__(self,v):return self.c(v)+-self
    def __mul__(self,v):
        v=self.c(v);vals=[a*b for a in (self.l,self.h) for b in (v.l,v.h)]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,v):
        v=self.c(v);assert not v.l<=0<=v.h
        return self*I(1/v.h,1/v.l)
    def __rtruediv__(self,v):return self.c(v)/self
    def __pow__(self,n):
        assert n in (0,2,3,4)
        if n==0:return I(1)
        if n==3:return I(self.l**3,self.h**3)
        if n==2:
            vals=[self.l**2,self.h**2]
            if self.l<=0<=self.h:vals.append(Q(0))
            return I(min(vals),max(vals))
        return (self**2)**2
    def fmt(self):return (float(self.l),float(self.h))

eta=Q(379,500)
rho=Q(9,10)
beta=1-rho
delta=rho-eta
alpha=2-eta
kappa=Q(1701,2000)
d=Q(1)
lam=Q(5)
assert Q(2,5)<eta<rho<1 and delta>0
assert kappa>180*beta**2*d**2/alpha**4
assert kappa>54*beta**2*d**2/(eta**2*alpha**2)
assert kappa>30*beta**2*d**2/alpha**2
assert 6-15*eta<0
print('PASS: global parameter inequalities eta>2/5, symmetric welfare concavity, firm Rosen margin, design response regularity')

def sf(z):
    t=beta*z
    return kappa*(1-z)-6*beta*alpha*d*d/((alpha-t)*(alpha+2*t)**3)
zl,zh=Q(7,10),Q(3,4)
for _ in range(150):
    m=(zl+zh)/2
    if sf(m)>0:zl=m
    else:zh=m
assert sf(zl)>0>sf(zh) and zh-zl<Q(1,10**30)
z=I(zl,zh)
g=I(Q('0.05433320681'),Q('0.05433320682'))

def pieces(y):
    t=delta*g+beta*y
    b=rho*g+beta*y
    L=alpha+2*t
    N=Q(9,2)+3*b
    return t,b,L,N
def nash_foc(y):
    t,b,L,N=pieces(y)
    return kappa*(1-y)-lam*(y-z)-6*beta*alpha*d*d/((alpha-t)*L**3)
def social_symmetric_derivative(y):
    t,b,L,N=pieces(y)
    return beta*d*d*(3/L**2-4*N/L**3)+kappa*(1-y)-lam*(y-z)
def social_welfare(y):
    t,b,L,N=pieces(y)
    return N*d*d/L**2-kappa*(1-y)**2/2-lam*(y-z)**2/2
def indirect_wedge(y):
    t,b,L,N=pieces(y)
    return beta*d*d/L**3*(3*L-4*N+6*alpha/(alpha-t))
def G(y):
    t,b,L,N=pieces(y)
    return 6*beta*alpha*d*d*(5*alpha-8*t)/((alpha-t)**2*L**4)

nl,nh=I(Q('0.71968163')),I(Q('0.71968164'))
pl,ph=I(Q('0.66267728')),I(Q('0.66267730'))
assert nash_foc(nl).l>0 and nash_foc(nh).h<0
assert social_symmetric_derivative(pl).l>0 and social_symmetric_derivative(ph).h<0
assert nh.l>ph.h
Nash=I(nl.l,nh.h)
Plan=I(pl.l,ph.h)
w=indirect_wedge(Nash)
assert w.h<0
assert (kappa+lam-beta*G(Nash)).l>0
dyg=delta*G(Nash)/(kappa+lam-beta*G(Nash))
assert dyg.l>0
indirect=w*dyg
assert indirect.h<0
gain=social_welfare(Plan)-social_welfare(Nash)
assert gain.l>0
print('PASS: strict Nash over-similarity and symmetric welfare improvement at Stage18 optimal g bracket')
print('  z=',z.fmt())
print('  g bracket=',g.fmt())
print('  Nash similarity=',Nash.fmt())
print('  symmetric-planner similarity=',Plan.fmt())
print('  Nash minus planner similarity=',(Nash-Plan).fmt())
print('  welfare gain under re-designed symmetric plan=',gain.fmt())
print('  planner derivative at Nash=',w.fmt())
print('  induced policy-welfare slope (W_y*y_g)=',indirect.fmt())
print('SCOPE: planner is symmetric and holds g fixed; not unrestricted global planner or all-parameter optimal government depth.')
