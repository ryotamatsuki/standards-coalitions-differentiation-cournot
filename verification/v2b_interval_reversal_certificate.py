#!/usr/bin/env python3
"""Interval-arithmetic certificate for V2b coalition-regime reversal.

Covers ALL real g in [0,1] at the exact rational witness
eta=379/500, rho=9/10, kappa=1701/2000, a-c=1.
A successful run supplies proof enclosures, not finite-grid evidence.

Dependencies: sympy, mpmath, numpy, scipy.
"""
from fractions import Fraction as Q
from math import lcm
from itertools import product
import numpy as np
import sympy as sp
from mpmath import iv
from scipy.optimize import root, brentq

iv.dps = 30
u, v, g = sp.symbols("u v g", real=True)
eta, rho, kap = sp.symbols("eta rho kap", real=True)
beta, A = 1-rho, 2-eta
m = (rho-eta)*g+beta*u
n = beta*(u+v)/2
D = A*(A+m)-2*n*n
qm = (A-n)/D
qo = (A+m-2*n)/D
inv11 = (1/(A-m)+A/D)/2
inv12 = (-1/(A-m)+A/D)/2
inv13 = -n/D
dqi = -beta/2*(inv11*(qm+qo)+qm*(inv12+inv13))
dqo = -beta*((A+m)*qm-n*qo)/D
Fm = kap*(1-u)+6*qm*dqi
Fo = kap*(1-v)+6*qo*dqo
CS = (1+rho*g+beta*u)*qm**2+qo**2/2+beta*(u+v)*qm*qo
WM = CS+3*qm**2-kap*(1-u)**2/2
WO = CS+3*qo**2-kap*(1-v)**2/2
vars = (u,v,g)
exprs = [Fm,Fo,WM,WO]+[sp.diff(Fm,z) for z in vars] + [sp.diff(Fo,z) for z in vars]+[sp.diff(WM,z) for z in vars]+[sp.diff(WO,z) for z in vars]
su_iv = sp.lambdify((u,v,g,eta,rho,kap),exprs,modules="math",cse=True)
su_num = sp.lambdify((u,v,g,eta,rho,kap),[Fm,Fo],modules="numpy",cse=True)

y = sp.symbols("y", real=True)
t = (rho-eta)*g+beta*y
qi = 1/(A+2*t)
Fi = kap*(1-y)-6*beta*A/((A-t)*(A+2*t)**3)
Wi = (sp.Rational(9,2)+3*(rho*g+beta*y))*qi**2-kap*(1-y)**2/2
is_expr = [Fi,Wi,sp.diff(Fi,y),sp.diff(Fi,g),sp.diff(Wi,y),sp.diff(Wi,g)]
is_iv = sp.lambdify((y,g,eta,rho,kap),is_expr,modules="math",cse=True)
is_num = sp.lambdify((y,g,eta,rho,kap),Fi,modules="numpy",cse=True)

E,R,K = iv.mpf(379)/500,iv.mpf(9)/10,iv.mpf(1701)/2000
assert Q(1701,2000)>81*(1-Q(9,10))**2
assert Q(379,500)<Q(9,10)  # M >= I and uniform positive-output safety

def enc(ab):
    """Outward-rounded closed interval with EXACT rational endpoints."""
    lo,hi=ab
    den=lcm(lo.denominator,hi.denominator)
    return iv.mpf([lo.numerator*(den//lo.denominator),
                   hi.numerator*(den//hi.denominator)])/iv.mpf(den)

def sb(U,V,G):
    return su_iv(U,V,G,E,R,K)

def ib(Y,G):
    return is_iv(Y,G,E,R,K)

def lo(z): return float(z.a)
def hi(z): return float(z.b)
def right(z): return z.b < 0
def left(z): return z.a > 0

def slopes(w):
    """Implicit derivatives of symmetric SU Nash choice and member/outsider welfare."""
    det=w[4]*w[8]-w[5]*w[7]
    if not (left(det) or right(det)): return None
    du=(-w[6]*w[8]+w[5]*w[9])/det
    dv=(w[6]*w[7]-w[4]*w[9])/det
    member=w[12]+w[10]*du+w[11]*dv
    outsider=w[15]+w[13]*du+w[14]*dv
    return member,outsider

def certify_SU():
    """Uniform bounds for the entire (u,v,g) rectangle, not sampled roots."""
    a,b=Q(7,10),Q(4,5)
    report=[]
    for idx,z0 in ((0,a),(0,b),(1,a),(1,b)):
        vals=[]
        for j in range(40):
            for k in range(80):
                T=enc((a+Q(j,400),a+Q(j+1,400)))
                G=enc((Q(k,80),Q(k+1,80)))
                z=enc((z0,z0))
                p=sb(z,T,G)[0] if idx==0 else sb(T,z,G)[1]
                vals.append((lo(p),hi(p)))
                assert left(p) if z0==a else right(p), (idx,z0,j,k,p)
        report.append((min(t[0] for t in vals),max(t[1] for t in vals)))
    print("SU rectangle inward face intervals:",report,flush=True)

    stack=[((a,b),(a,b),(Q(0),Q(1)))]
    pass_count=0;split_count=0;largest_hi=float("-inf")
    while stack:
        box=stack.pop()
        U,V,G=map(enc,box)
        raw=slopes(sb(U,V,G))
        if raw is not None and right(raw[0]):
            pass_count+=1
            largest_hi=max(largest_hi,hi(raw[0]))
            continue
        split_count+=1
        assert split_count<250000, ("insufficient partition budget",box)
        widths=[float(z[1]-z[0])/span for z,span in zip(box,(.1,.1,1.))]
        i=int(np.argmax(widths))
        a0,b0=box[i];mid=(a0+b0)/2
        for sub in ((a0,mid),(mid,b0)):
            nextbox=list(box);nextbox[i]=sub;stack.append(tuple(nextbox))
    print(f"CERTIFIED: SU member welfare derivative < 0 for all g; "
          f"{pass_count} cells, {split_count} subdivisions, "
          f"max interval upper bound {largest_hi:.12g}",flush=True)

def numeric_roots(gval):
    """Root approximations choose rectangles only; interval face tests certify them."""
    z=root(lambda x:su_num(x[0],x[1],gval,.758,.9,.8505),[.74,.73],tol=1e-12)
    assert np.max(np.abs(z.fun))<1e-10
    x=brentq(lambda t:is_num(t,gval,.758,.9,.8505),.6,.95,xtol=1e-14)
    return tuple(float(v) for v in z.x)+(float(x),)

def certify_C():
    """Interval-Newton style root boxes plus implicit derivative sign for I-O."""
    N=100
    rs=[numeric_roots(j/N) for j in range(N+1)]
    stack=[(Q(j,N),Q(j+1,N),rs[j],rs[j+1]) for j in range(N)]
    accepted=0;split_count=0;max_upper=-float("inf")
    while stack:
        a,b,L,Rr=stack.pop()
        eps=Q(1,100000)+(b-a)/15
        boxes=[]
        for j in range(3):
            nums=[Q(str(L[j])),Q(str(Rr[j]))]
            boxes.append((min(nums)-eps,max(nums)+eps))
        U,V,Y=map(enc,boxes); G=enc((a,b))
        faces=[
            sb(enc((boxes[0][0],boxes[0][0])),V,G)[0],
            sb(enc((boxes[0][1],boxes[0][1])),V,G)[0],
            sb(U,enc((boxes[1][0],boxes[1][0])),G)[1],
            sb(U,enc((boxes[1][1],boxes[1][1])),G)[1],
            ib(enc((boxes[2][0],boxes[2][0])),G)[0],
            ib(enc((boxes[2][1],boxes[2][1])),G)[0]
        ]
        inwards=all(left(faces[i]) for i in (0,2,4)) and all(right(faces[i]) for i in (1,3,5))
        if inwards:
            su=sb(U,V,G);is_=ib(Y,G)
            ds=slopes(su)
            if ds is not None and (left(is_[2]) or right(is_[2])):
                international=is_[5]-is_[4]*is_[3]/is_[2]
                c_gain=international-ds[1]
                if right(c_gain):
                    accepted+=1;max_upper=max(max_upper,hi(c_gain))
                    continue
        split_count+=1
        assert split_count<250000,("unable to certify",a,b)
        mid=(a+b)/2;middle=numeric_roots(float(mid))
        stack.extend([(mid,b,middle,Rr),(a,mid,L,middle)])
    print(f"CERTIFIED: C entry-gain derivative < 0 for all g; "
          f"{accepted} cells, {split_count} subdivisions, "
          f"max upper bound {max_upper:.12g}",flush=True)

def frozen_outcomes(G, X):
    AA=2-E; bb=1-R; n=bb*X; m=(R-E)*G+bb*X
    den=AA*(AA+m)-2*n*n
    q_m=(AA-n)/den
    q_o=(AA+m-2*n)/den
    CS=(1+R*G+bb*X)*q_m**2+q_o**2/2+2*bb*X*q_m*q_o
    member=CS+3*q_m**2-K*(1-X)**2/2
    outsider=CS+3*q_o**2-K*(1-X)**2/2
    q=1/(AA+2*m)
    international=(iv.mpf(9)/2+3*(R*G+bb*X))*q**2-K*(1-X)**2/2
    return member,outsider,international

def certify_frozen():
    l,h=Q(71859270731,10**11),Q(71859270734,10**11)
    assert left(ib(enc((l,l)),enc((Q(0),Q(0))))[0])
    assert right(ib(enc((h,h)),enc((Q(0),Q(0))))[0])
    X=enc((l,h))
    q=1/(2-E+2*(1-R)*X)
    Wsw=(iv.mpf(9)/2+3*(1-R)*X)*q*q-K*(1-X)**2/2
    G=enc((Q(1,20),Q(1,20)))
    M,O,I=frozen_outcomes(G,X)
    assert left(I-O) and left(I-M) and left(I-Wsw)
    upper_m=-float("inf")
    for j in range(50):
        m,_,_=frozen_outcomes(enc((Q(j,50),Q(j+1,50))),X)
        upper_m=max(upper_m,hi(m))
    assert lo(I)>upper_m
    print("CERTIFIED: frozen-x IS at g=0.05 feasible and dominates all SW/SU policies",
          "lower C advantage",lo(I-O),"best SU upper",upper_m,
          "IS lower",lo(I),flush=True)

if __name__=="__main__":
    certify_SU()
    certify_C()
    certify_frozen()
    print("PASS: conditional V2b positive-depth IS vs endogenous SW-equivalent regime reversal")
