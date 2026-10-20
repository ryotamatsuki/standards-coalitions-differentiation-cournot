#!/usr/bin/env python3
"""Stage 7 V2b welfare/agenda accounting. Independent primitive reconstruction.

Numerical finite-point and small parameter-cube diagnostics, NOT a global theorem:
- exact-witness full-g no-agreement result depends on independent Stage4A certificate;
- strict Pareto gain at g=.05 separately interval-certified by Stage6;
- no market-access agreement or transfer scheme is added to canonical game.
"""
from itertools import product
import numpy as np
from scipy.optimize import root

BASE=(.758,.900,.8505)
G=.05

def equilibrium(regime,g,params):
    eta,rho,kappa=params
    H=np.eye(3)
    if regime=="SU":H[0,1]=H[1,0]=g
    elif regime=="IS": H+=g*(np.ones((3,3))-np.eye(3))
    elif regime!="SW":raise ValueError(regime)
    beta=1-rho
    def evaluate(x):
        x=np.array(x,dtype=float)
        X=np.eye(3)
        for i in range(3):
            for j in range(i+1,3):X[i,j]=X[j,i]=(x[i]+x[j])/2
        B=rho*H+beta*X
        M=np.eye(3)+B-eta*H
        q=np.linalg.solve(M,np.ones(3))
        inv=np.linalg.inv(M)
        grad=np.empty(3)
        for i in range(3):
            partial=np.zeros((3,3))
            for j in range(3):
                if i!=j:partial[i,j]=partial[j,i]=beta/2
            dq=-inv@partial@q
            grad[i]=6*q[i]*dq[i]+kappa*(1-x[i])
        CS=q@B@q/2
        gross=3*q*q
        invest=kappa*(1-x)**2/2
        national=CS+gross-invest
        return dict(x=x,q=q,CS=CS,operating=gross,cost=invest,W=national,
                    grad=grad,B=B,M=M)
    sol=root(lambda x:evaluate(x)["grad"],[.72]*3,tol=1e-12)
    assert max(abs(evaluate(sol.x)["grad"]))<1e-10,(regime,g,params)
    assert np.min(sol.x)>0 and np.max(sol.x)<1
    return evaluate(sol.x)

def world(s):
    # Each market's domestic CS is identical; 3 countries each have one CS.
    return 3*s["CS"]+sum(s["operating"])-sum(s["cost"])

def test():
    eta,rho,kappa=BASE
    assert kappa>81*(1-rho)**2
    sw=equilibrium("SW",0,BASE)
    su=equilibrium("SU",G,BASE)
    intl=equilibrium("IS",G,BASE)
    assert max(abs(sw["W"]-2.422078421718))<1e-10
    assert max(abs(intl["W"]-2.439013049624))<1e-10
    for name,a in [("SW",sw),("SU",su),("IS",intl)]:
        assert abs(world(a)-sum(a["W"]))<1e-11
        print(name,
              "x=",np.round(a["x"],9).tolist(),
              "q=",np.round(a["q"],9).tolist(),
              "domestic_CS=",round(a["CS"],9),
              "home_firm_world_gross_profit=",np.round(a["operating"],9).tolist(),
              "once_paid_design_cost=",np.round(a["cost"],9).tolist(),
              "national_W=",np.round(a["W"],9).tolist(),
              "world_W=",round(world(a),9))
    assert all(intl["W"]>sw["W"])
    assert su["W"][0]<sw["W"][0]
    assert intl["W"][0]<su["W"][2]
    assert world(su)>world(sw)
    assert world(intl)>world(su)
    print("IS-SW national Pareto gains",np.round(intl["W"]-sw["W"],12))
    print("World welfare gain IS-SW",world(intl)-world(sw))
    print("World welfare gain SU-SW",world(su)-world(sw))
    print("SU member loss versus SW",su["W"][0]-sw["W"][0])
    print("SU outsider rent versus SW",su["W"][2]-sw["W"][2])
    print("IS member accession gain over SU",intl["W"][0]-su["W"][0])
    print("IS C outsider opportunity loss",intl["W"][2]-su["W"][2])
    print("Aggregate SU-to-IS welfare gain",world(intl)-world(su))
    # Hypothetical different institution, NOT a strategy or SPNE of canonical V2b:
    # All-or-nothing three-country unanimous offered IS(g=.05), rejection -> SW.
    assert min(intl["W"]-sw["W"])>0
    print("Counterfactual all-or-nothing unanimous offer at g=.05: strictly acceptable to A,B,C vs SW")
    print("This does not prove the original AB-first V2b game can implement the offer.")
    # Finite numerical neighborhood diagnostic; whole-policy proof only at BASE.
    worst=np.full(4,float("inf"))
    best=np.full(4,-float("inf"))
    for de,dr,dk in product((-.001,0,.001),repeat=3):
        ps=(eta+de,rho+dr,kappa+dk)
        assert ps[2]>81*(1-ps[1])**2
        SW=equilibrium("SW",0,ps)
        SU=equilibrium("SU",G,ps)
        IS=equilibrium("IS",G,ps)
        measures=np.array([SU["W"][0]-SW["W"][0],
                           IS["W"][2]-SU["W"][2],
                           IS["W"][0]-SW["W"][0],
                           world(IS)-world(SW)])
        worst=np.minimum(worst,measures)
        best=np.maximum(best,measures)
    assert worst[0]<best[0]<0
    assert worst[1]<best[1]<0
    assert 0<worst[2]<best[2]
    assert 0<worst[3]<best[3]
    print("27 point LOCAL diagnostic min",worst,"max",best)
    print("PASS Stage 7: welfare decomposition and finite local scenario checks")
    print("NOT proved: all-g policy SPNE for shifted parameters or any actual treaty implementability.")

if __name__=="__main__":test()
