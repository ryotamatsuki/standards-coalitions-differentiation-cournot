#!/usr/bin/env python3
"""Stage 7.5 bounded pre-registered NONLINEAR design diagnostic.

The exact test was preregistered BEFORE this implementation at:
reviews/V2B_STAGE07_DESIGN_PORTABILITY_PREREG_2026-10-21.md

Baseline is unchanged. Only diagnostic X_ij=(x_i**2+x_j**2)/2.
Re-solves q and 3-firm Nash (never substitutes into baseline equilibrium).
This code is an EXPLORATORY diagnostic, NOT a certified all-g theorem.
"""
import numpy as np
from scipy.optimize import root, minimize_scalar, brentq

ETA,RHO,KAPPA=379/500,9/10,1701/2000
BETA=1-RHO
GTEST=.05

def evaluate(regime, g, x):
    x=np.asarray(x,float)
    H=np.eye(3)
    if regime=="SU":H[0,1]=H[1,0]=g
    elif regime=="IS": H+=g*(np.ones((3,3))-np.eye(3))
    else: assert regime=="SW"
    X=np.eye(3)
    for i in range(3):
        for j in range(i+1,3):
            X[i,j]=X[j,i]=(x[i]**2+x[j]**2)/2
    B=RHO*H+BETA*X
    M=np.eye(3)+B-ETA*H
    q=np.linalg.solve(M,np.ones(3))
    grads=[]
    for i in range(3):
        Mi=np.zeros((3,3))
        for j in range(3):
            if i!=j:Mi[i,j]=Mi[j,i]=BETA*x[i]
        qi_der=(-np.linalg.solve(M,Mi@q))[i]
        grads.append(6*q[i]*qi_der+KAPPA*(1-x[i]))
    CS=.5*q@B@q
    profits=3*q*q-KAPPA*(1-x)**2/2
    return np.asarray(grads),q,CS+profits,profits

def solve(regime,g,x0):
    r=root(lambda x:evaluate(regime,g,x)[0],x0,tol=1e-12)
    assert np.max(np.abs(evaluate(regime,g,r.x)[0])) < 1e-9
    assert min(r.x)>0 and max(r.x)<1
    return r.x,evaluate(regime,g,r.x)[2]

def unilateral_check(regime,g,x):
    base=evaluate(regime,g,x)[3]
    for i in range(3):
        def profit(z):
            d=x.copy();d[i]=z
            return evaluate(regime,g,d)[3][i]
        grid=np.linspace(0,1,121)
        vals=np.asarray([profit(z) for z in grid])
        winners=[(vals[0],0),(vals[-1],1)]
        for j in range(1,120):
            if vals[j]>=vals[j-1] and vals[j]>=vals[j+1]:
                p=minimize_scalar(lambda z:-profit(z),
                                  bounds=(grid[j-1],grid[j+1]),
                                  method="bounded",options={"xatol":1e-11})
                winners.append((-p.fun,p.x))
        gain=max(v for v,z in winners)-base[i]
        assert gain<2e-7,(regime,g,i,gain)

def main():
    s0,w0=solve("SW",0,np.full(3,.6))
    unilateral_check("SW",0,s0)
    cases={}
    for regime in ("SU","IS"):
        x,w=solve(regime,GTEST,s0)
        cases[regime]=(x,w)
        unilateral_check(regime,GTEST,x)
    xs,ws=cases["SU"];xi,wi=cases["IS"]
    fixed_su=evaluate("SU",GTEST,s0)[2]
    fixed_is=evaluate("IS",GTEST,s0)[2]

    # The actual pre-registered g=0.05 test FAILS on the fixed-design
    # C consent condition. Report this; do not change its pass condition.
    prereg_results={
      "endogenous SU member below SW": bool(ws[0]<w0[0]),
      "endogenous C refuses IS":bool(wi[0]<ws[2]),
      "endogenous IS Pareto superior to SW":bool(wi[0]>w0[0]),
      "FROZEN C accepts IS at preregistered g=0.05":bool(fixed_is[0]>fixed_su[2]),
      "frozen IS above SW at g=0.05":bool(fixed_is[0]>w0[0])
    }
    print("Stage 7.5 nonlinear design diagnostic X_ij=(x_i^2+x_j^2)/2")
    print("SW Nash x:",s0,"SW W:",w0[0])
    print("SU Nash x:",xs,"SU W:",ws)
    print("IS Nash x:",xi,"IS W:",wi[0])
    for n,ok in prereg_results.items():print(("PASS" if ok else "FAIL")+" "+n)
    assert not prereg_results["FROZEN C accepts IS at preregistered g=0.05"]

    # Registered whole-g diagnostic scan: not a universal bound or proof.
    points=np.linspace(0,1,201)
    endo_su=[];endo_C=[];frozen_C=[]
    for g in points:
        _,su=solve("SU",float(g),s0)
        _,intl=solve("IS",float(g),s0)
        endo_su.append(su[0]-w0[0])
        endo_C.append(intl[0]-su[2])
        frozen_C.append(evaluate("IS",g,s0)[2][0]-evaluate("SU",g,s0)[2][2])
    print("201-point g-scan endogenous max SU-SW (excluding zero)",max(endo_su[1:]))
    print("201-point g-scan endogenous max IS-C-outside (excluding zero)",max(endo_C[1:]))
    print("201-point g-scan frozen C admission max",max(frozen_C[1:]))
    assert max(endo_su[1:])<0 and max(endo_C[1:])<0

    # Secondary observation from the PRE-REGISTERED g scan, not a new
    # confirmatory threshold or an author-selected substitute g.
    gsmall=.005
    FSU=evaluate("SU",gsmall,s0)[2]
    FIS=evaluate("IS",gsmall,s0)[2]
    print("Exploratory g=.005 frozen C gain",FIS[0]-FSU[2],
          "frozen IS-SW",FIS[0]-w0[0])
    print("Interpretation: original fixed-g=.05 portability condition FAILS;"
          " an existential smaller-g continuation is only NUMERICALLY SUGGESTED.")
    for regime in ("SU","IS"):
        for g in (0,.5,1):
            x,w=solve(regime,g,s0)
            unilateral_check(regime,g,x)
    print("COMPLETED diagnostic. Non-success is preserved; no alternative parameters tuned.")
    print("NOT PROVED: unique firm Nash over all g/strategies nor continuous-g government SPNE.")

if __name__=="__main__":main()
