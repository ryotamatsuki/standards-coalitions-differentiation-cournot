#!/usr/bin/env python3
"""Stage-4 primitive-first independent diagnostic (NOT independent Stage 4A).

No imports from prior V2b production solvers. This is a second algebraic
implementation, with numerical spot checks. Full continuum sign certification
remains in v2b_interval_reversal_certificate.py.
"""
from itertools import product
import numpy as np
from scipy.optimize import root, minimize_scalar, brentq

ETA=379/500
RHO=9/10
KAPPA=1701/2000
BETA=1-RHO

def primitive(regime,g,x):
    x=np.asarray(x,float)
    H=np.eye(3)
    if regime=="SU": H[0,1]=H[1,0]=g
    elif regime=="IS": H+=g*(np.ones((3,3))-np.eye(3))
    else: assert regime=="SW"
    X=np.eye(3)
    for i,j in product(range(3),repeat=2):
        if i!=j: X[i,j]=(x[i]+x[j])/2
    B=RHO*H+BETA*X
    M=np.eye(3)+B-ETA*H
    q=np.linalg.solve(M,np.ones(3))
    profit=3*q*q-KAPPA*(1-x)**2/2
    welfare=(q@B@q)/2+profit
    return q,profit,welfare,M,B,H,X

def grad(regime,g,x):
    q,_,_,M,*_=primitive(regime,g,x)
    df=[]
    for i in range(3):
        Mi=np.zeros((3,3))
        for j in range(3):
            if i!=j: Mi[i,j]=Mi[j,i]=BETA/2
        dq=np.linalg.solve(M,-Mi@q)
        df.append(6*q[i]*dq[i]+KAPPA*(1-x[i]))
    return np.array(df)

def solve_design(regime,g):
    s=root(lambda x:grad(regime,g,x),[.73,.73,.73],tol=1e-12)
    assert np.linalg.norm(grad(regime,g,s.x),ord=np.inf)<1e-9
    assert np.all((s.x>0)&(s.x<1))
    for i in range(3):
        def unilateral(z):
            x=s.x.copy();x[i]=z
            return primitive(regime,g,x)[1][i]
        b=minimize_scalar(lambda z:-unilateral(z),bounds=(0,1),method="bounded",
                          options={"xatol":1e-12})
        assert -b.fun-unilateral(s.x[i])<1e-8
    return s.x,primitive(regime,g,s.x)[2]

def run():
    # Exact rational inequality kappa>81(1-rho)^2 and Cournot positivity:
    assert KAPPA>81*BETA**2
    assert 2*(1-ETA)/(2-ETA)<1
    vertices=list(product([0.,1.],repeat=3))
    for reg in ("SW","SU","IS"):
        for depth in (0.,1.):
            for x in vertices:
                q,_,_,M,_,_,X=primitive(reg,depth,x)
                assert np.linalg.eigvalsh(X).min()>-1e-12
                assert np.linalg.eigvalsh(M).min()>1-1e-12
                assert q.min()>0
    rng=np.random.default_rng(2626)
    largest_error=0.
    for reg in ("SW","SU","IS"):
        for _ in range(35):
            depth=float(rng.uniform());x=rng.uniform(.02,.98,3)
            for i in range(3):
                h=1e-6;p=x.copy();m=x.copy();p[i]+=h;m[i]-=h
                fd=(primitive(reg,depth,p)[1][i]-primitive(reg,depth,m)[1][i])/(2*h)
                largest_error=max(largest_error,abs(fd-grad(reg,depth,x)[i]))
    assert largest_error<1e-7
    xsw,Wsw=solve_design("SW",0)
    assert abs(xsw[0]-.718592707322)<1e-8
    print("SW equilibrium:",xsw, Wsw, "gradient max discrepancy",largest_error)
    allg=np.linspace(0,1,101)
    max_su_gain=-float("inf");max_c_gain=-float("inf")
    for g in allg[1:]:
        _,WSU=solve_design("SU",float(g))
        _,WIS=solve_design("IS",float(g))
        max_su_gain=max(max_su_gain,WSU[0]-Wsw[0])
        max_c_gain=max(max_c_gain,WIS[0]-WSU[2])
    assert max_su_gain<0 and max_c_gain<0
    print("Numerical independent diagnostic, endogenous max SU gain",max_su_gain)
    print("Numerical independent diagnostic, endogenous max C gain",max_c_gain)
    fg=1/20
    FS=primitive("SU",fg,xsw)[2]
    FI=primitive("IS",fg,xsw)[2]
    assert FI[0]>FS[2] and FI[0]>FS[0] and FI[0]>Wsw[0]
    supSU=max(primitive("SU",float(g),xsw)[2][0] for g in np.linspace(0,1,2001))
    assert FI[0]>supSU
    print("Frozen x, g=.05: IS",FI[0],"C outside SU",FS[2],
          "largest sampled SU",supSU)
    print("PASS: independent Stage-4 finite-point consistency and BR checks")
    print("NOT A PROOF of full-continuum government inequalities or Stage 4A independence.")

if __name__=="__main__":run()
