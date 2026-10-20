#!/usr/bin/env python3
"""Stage 4/4A repair: nonlinear residual design all-depth coalition certificate.

Diagnostic alternative PRE-REGISTERED in:
reviews/V2B_STAGE07_DESIGN_PORTABILITY_PREREG_2026-10-21.md
X_ij=(x_i^2+x_j^2)/2 (i != j), parameters FIXED eta=379/500,
rho=9/10, kappa=1701/2000, a-c=1. Firms choose x after government
compatibility and before Cournot in three identical national markets.

Mathematical claims (computer-assisted rational interval arithmetic):
  1. Unique interior symmetric SU/IS design continuation at every real g,
     using Poincare-Miranda sign faces and global Rosen uniqueness (from
     v2b_alt_quadratic_rosen_interval.py).
  2. SU member total welfare derivative <0 over all g in [0,1].
  3. International-vs-SU-outsider welfare derivative <0 over all g.
  4. Holding firm design fixed at SW Nash, IS at g=1/200=.005 satisfies
     C participation, A/B approval and beats SW and ALL frozen SU policies.
  5. When firms REOPTIMIZE, IS at g=.05 is strictly Pareto better than SW,
     yet unreachable under canonical A/B-first consent.

IMPORTANT: the original preregistered FROZEN C consent at g=.05 FAILED,
and remains FAILED. The g=.005 point was identified during the earlier
preregistered all-g numerical scan. This code certifies the separate
existential (some positive g) question; it does NOT revise the failed
fixed-g=.05 test post-hoc or authorize parameter tuning.
"""
from fractions import Fraction as Q
from scipy.optimize import root, brentq
from mpmath import iv
import numpy as np
import sympy as sp
from time import perf_counter
iv.dps=40

u,v,g=sp.symbols('u v g',real=True)
y=sp.symbols('y',real=True)
eta=sp.Rational(379,500)
rho=sp.Rational(9,10)
kappa=sp.Rational(1701,2000)
beta=1-rho
A=2-eta
m=(rho-eta)*g+beta*u**2
n=beta*(u**2+v**2)/2
D=A*(A+m)-2*n*n
qm=(A-n)/D
qo=(A+m-2*n)/D
inv11=(A/D+1/(A-m))/2
inv12=(A/D-1/(A-m))/2
inv13=-n/D

# Own design deviations are unilateral, NOT a joint symmetric u change.
dqm=-beta*u*(inv11*(qm+qo)+qm*(inv12+inv13))
dqo=-2*beta*v*((A+m)*qm-n*qo)/D
fm=kappa*(1-u)+6*qm*dqm
fo=kappa*(1-v)+6*qo*dqo
CS=(1+rho*g+beta*u*u)*qm**2+qo**2/2+2*n*qm*qo
WM=CS+3*qm**2-kappa*(1-u)**2/2
WO=CS+3*qo**2-kappa*(1-v)**2/2
su_expr=[fm,fo,WM,WO]+[sp.diff(z,t) for z in (fm,fo,WM,WO)
                        for t in (u,v,g)]
su_interval=sp.lambdify((u,v,g),su_expr,modules='math',cse=True)
su_numeric=sp.lambdify((u,v,g),(fm,fo),modules='numpy',cse=True)

t=(rho-eta)*g+beta*y**2
q=1/(A+2*t)
fi=kappa*(1-y)-12*beta*y*A/((A-t)*(A+2*t)**3)
WI=(sp.Rational(9,2)+3*(rho*g+beta*y**2))*q**2-kappa*(1-y)**2/2
is_expr=[fi,WI,sp.diff(fi,y),sp.diff(fi,g),sp.diff(WI,y),sp.diff(WI,g)]
is_interval=sp.lambdify((y,g),is_expr,modules='math',cse=True)
is_numeric=sp.lambdify((y,g),fi,modules='numpy',cse=True)

def exact(a,b=None):
    """Closed outward-rounded interval from rational endpoints only."""
    if b is None:b=a
    a,b=Q(a),Q(b)
    return iv.mpf([a.numerator*b.denominator,
                   b.numerator*a.denominator])/(a.denominator*b.denominator)
def pos(z):return z.a>0
def neg(z):return z.b<0

def SU(U,V,G):return su_interval(U,V,G)
def IS(Y,G):return is_interval(Y,G)

def global_interior_roots():
    """Uniform Nash face signs across every real g in [0,1]."""
    start=perf_counter()
    ul,uh=Q(60,100),Q(67,100)
    vl,vh=Q(60,100),Q(65,100)
    for i,bound in ((0,ul),(0,uh),(1,vl),(1,vh)):
        lo,hi=(vl,vh) if i==0 else (ul,uh)
        for j in range(40):
            counterpart=exact(lo+(hi-lo)*j/40,lo+(hi-lo)*(j+1)/40)
            for k in range(100):
                G=exact(Q(k,100),Q(k+1,100))
                val=(SU(exact(bound),counterpart,G)[0] if i==0
                     else SU(counterpart,exact(bound),G)[1])
                assert (pos(val) if bound in (ul,vl) else neg(val)),\
                    ('SU Nash face unresolved',i,bound,j,k,val)
    for boundary,lower in ((Q(60,100),True),(Q(73,100),False)):
        for k in range(100):
            v0=IS(exact(boundary),exact(Q(k,100),Q(k+1,100)))[0]
            assert (pos(v0) if lower else neg(v0)),\
                ('IS Nash face unresolved',boundary,k,v0)
    print('CERTIFIED: SU Nash in (0.60,0.67)x(0.60,0.65) and '
          'IS Nash in (0.60,0.73) for all g; seconds',
          perf_counter()-start,flush=True)

def derivatives_su(w):
    determinant=w[4]*w[8]-w[5]*w[7]
    if not (pos(determinant) or neg(determinant)):return None
    du=(-w[6]*w[8]+w[5]*w[9])/determinant
    dv=(w[6]*w[7]-w[4]*w[9])/determinant
    return (w[12]+w[10]*du+w[11]*dv,
            w[15]+w[13]*du+w[14]*dv)

def roots_at(gval):
    z=root(lambda x:su_numeric(x[0],x[1],gval),
           [0.63,0.62],tol=1e-12)
    assert np.max(np.abs(z.fun))<1e-10
    yval=brentq(lambda z:is_numeric(z,gval),.6,.73,xtol=1e-14)
    # NUMERICAL ROOTS ARE GUESSES for a small certifying rectangle only.
    return tuple(Q(str(round(float(a),12))) for a in (z.x[0],z.x[1],yval))

def all_policy_depths():
    """100 closed rational g-cells: inclusion signs and derivative bounds."""
    st=perf_counter()
    stack=[(Q(k,100),Q(k+1,100)) for k in range(100)]
    accepted=0;divisions=0;maximum_m=-1e10;maximum_c=-1e10
    while stack:
        lo,hi=stack.pop()
        G=exact(lo,hi)
        us,vs,ys=roots_at(float((lo+hi)/2))
        eps=Q(25,10000)
        U,V,Y=(exact(z-eps,z+eps) for z in (us,vs,ys))
        w=SU(U,V,G); z=IS(Y,G)
        boundary=[
            SU(exact(us-eps),V,G)[0],
            SU(exact(us+eps),V,G)[0],
            SU(U,exact(vs-eps),G)[1],
            SU(U,exact(vs+eps),G)[1],
            IS(exact(ys-eps),G)[0],
            IS(exact(ys+eps),G)[0]
        ]
        inward=(pos(boundary[0]) and neg(boundary[1])
                and pos(boundary[2]) and neg(boundary[3])
                and pos(boundary[4]) and neg(boundary[5]))
        if inward:
            deriv=derivatives_su(w)
            if deriv is not None and neg(z[2]):
                isprime=z[5]-z[4]*z[3]/z[2]
                cprime=isprime-deriv[1]
                if neg(deriv[0]) and neg(cprime):
                    accepted+=1
                    maximum_m=max(maximum_m,float(deriv[0].b))
                    maximum_c=max(maximum_c,float(cprime.b))
                    continue
        divisions+=1
        if divisions>20000:
            raise AssertionError(('Unresolved universal policy cell',lo,hi))
        md=(lo+hi)/2
        stack.extend(((lo,md),(md,hi)))
    print('CERTIFIED ALL REAL g in [0,1] — SU member W derivative <0, '
          'IS-vs-C outsider derivative <0.',
          'closed g cells:',accepted,'adaptive splits:',divisions,
          'largest derivative upper bounds:',maximum_m,maximum_c,
          'seconds:',perf_counter()-st,flush=True)
    assert maximum_m<0 and maximum_c<0

def frozen_agreement():
    """Do not overwrite preregistered failure at g=.05. Certify EXISTENCE at .005."""
    st=perf_counter()
    swroot=brentq(lambda z:is_numeric(z,0),.60,.73,xtol=3e-15)
    lower=Q(str(round(swroot-8e-13,12)))
    upper=Q(str(round(swroot+8e-13,12)))
    assert pos(IS(exact(lower),exact(0))[0])
    assert neg(IS(exact(upper),exact(0))[0])
    X=exact(lower,upper)
    Wsw=IS(X,exact(0))[1]

    gfail=exact(Q(1,20)) # original g=.05, PRE-REGISTERED FAILURE
    su_failed=SU(X,X,gfail)
    is_failed=IS(X,gfail)
    assert neg(is_failed[1]-su_failed[3]),\
        'Original preregistered g=.05 C participation failure MUST remain.'
    print('ORIGINAL g=.05 fixed-design C accession FAILS:',
          is_failed[1]-su_failed[3],flush=True)

    small_g=exact(Q(1,200)) # .005, from earlier pre-registered g scan
    m,o=SU(X,X,small_g)[2:4]
    iw=IS(X,small_g)[1]
    assert pos(iw-o),('C no longer accepts',iw-o)
    assert pos(iw-m),('A/B reject accession',iw-m)
    assert pos(iw-Wsw),('B rejects or A prefers SW',iw-Wsw)
    # ALL possible terminal SU depths, not a g grid of candidate equilibria:
    upper_su=float('-inf')
    for j in range(4000):
        candidate=SU(X,X,exact(Q(j,4000),Q(j+1,4000)))[2]
        upper_su=max(upper_su,float(candidate.b))
        assert iw.a>candidate.b,('SU dominates IS in some policy cell',j)
    print('CERTIFIED frozen-design international agreement at g=1/200:',
          'C advantage',iw-o,
          'IS minus SW',iw-Wsw,
          'IS welfare lower',float(iw.a),
          'frozen SU full-domain upper',upper_su,
          'seconds',perf_counter()-st,flush=True)
    assert float(iw.a)>upper_su

def endogenous_pareto():
    gpoint=exact(Q(1,20))
    y0=roots_at(.05)[2]
    ylo=y0-Q(1,10**10)
    yhi=y0+Q(1,10**10)
    assert pos(IS(exact(ylo),gpoint)[0])
    assert neg(IS(exact(yhi),gpoint)[0])
    sw0=roots_at(0)[2]
    xlo=sw0-Q(1,10**10)
    xhi=sw0+Q(1,10**10)
    assert pos(IS(exact(xlo),exact(0))[0])
    assert neg(IS(exact(xhi),exact(0))[0])
    gap=IS(exact(ylo,yhi),gpoint)[1]-IS(exact(xlo,xhi),exact(0))[1]
    assert pos(gap)
    print('CERTIFIED: even after endogenous design, IS at .05 '
          'strictly Pareto improves on SW by',gap,flush=True)

if __name__=='__main__':
    global_interior_roots()
    all_policy_depths()
    frozen_agreement()
    endogenous_pareto()
    print('PASS: nonlinear design existential coalition reversal at same parameter witness')
    print('NON-PASS REMAINS: frozen C accession at fixed original g=.05.')
    print('NOT CERTIFIED: unrestricted functional forms, arbitrary parameters, '
          'alternative bargaining regimes or journal-level originality.')
