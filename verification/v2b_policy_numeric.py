#!/usr/bin/env python3
"""Reproduce provisional V2b policy calculations. NOT an exhaustive SPNE audit."""
import numpy as np
from scipy.optimize import brentq, root, minimize_scalar


def continuation(eta, rho, kappa, regime, g):
    t = 1 - rho
    H = np.eye(3)
    if regime == "IS":
        H += g * (np.ones((3, 3)) - np.eye(3))
    elif regime == "SU":
        H[0, 1] = H[1, 0] = g
    else:
        assert regime == "SW"

    def evaluate(x):
        X = np.eye(3) + .5*(x[:, None]+x[None, :])*(np.ones((3, 3))-np.eye(3))
        B = rho*H + t*X
        M = np.eye(3) + B - eta*H
        q = np.linalg.solve(M, np.ones(3))
        inv = np.linalg.inv(M)
        grad = np.zeros(3)
        for i in range(3):
            v = np.full(3, .5*t*q[i])
            v[i] = .5*t*(sum(q)-q[i])
            dq = -inv @ v
            grad[i] = 6*q[i]*dq[i] + kappa*(1-x[i])
        CS = .5*q@B@q
        return q, CS+3*q*q-.5*kappa*(1-x)**2, grad

    if regime != "SU":
        f = lambda z: evaluate(np.array([z]*3))[2][0]
        assert f(0)>0 and f(1)<0
        y = brentq(f, 0, 1, xtol=1e-13)
        x = np.array([y]*3)
    else:
        def f(y):
            a = evaluate(np.array([y[0],y[0],y[1]]))[2]
            return [a[0],a[2]]
        rt = root(f, [.95,.95], tol=1e-12)
        assert np.max(np.abs(f(rt.x)))<1e-9
        x = np.array([rt.x[0],rt.x[0],rt.x[1]])
    q,w,grad = evaluate(x)
    assert min(q)>0 and min(x)>0 and max(x)<1 and np.max(np.abs(grad))<1e-9
    return x,q,w


def frozen_welfare(eta,rho,kappa,regime,g,x):
    H=np.eye(3)
    if regime=="SU": H[0,1]=H[1,0]=g
    elif regime=="IS": H+=g*(np.ones((3,3))-np.eye(3))
    X=np.eye(3)+.5*(x[:,None]+x[None,:])*(np.ones((3,3))-np.eye(3))
    B=rho*H+(1-rho)*X
    q=np.linalg.solve(np.eye(3)+B-eta*H,np.ones(3))
    return .5*q@B@q+3*q*q-.5*kappa*(1-x)**2


def main():
    # Exact knife-edge formula tested numerically:
    eta=rho=.85; kappa=20.
    SW=continuation(eta,rho,kappa,"SW",0)
    SU=continuation(eta,rho,kappa,"SU",1)
    IS=continuation(eta,rho,kappa,"IS",1)
    assert np.max(abs(SW[0]-SU[0]))<1e-10
    assert np.max(abs(SW[0]-IS[0]))<1e-10
    assert abs(SU[2][0]-SW[2][0]-rho*SW[1][0]**2)<1e-10
    assert abs(IS[2][0]-SW[2][0]-3*rho*SW[1][0]**2)<1e-10
    print("PASS: eta=rho knife-edge welfare identities")

    eta,rho,kappa=.64,.77,5.
    SW=continuation(eta,rho,kappa,"SW",0)
    print("SW: x=%.9f W=%.9f"%(SW[0][0],SW[2][0]))
    assert kappa>81*(1-rho)**2

    for endogenous in (True,False):
        def values(g):
            if endogenous:
                ws=continuation(eta,rho,kappa,"SU",g)[2]
                wi=continuation(eta,rho,kappa,"IS",g)[2]
            else:
                ws=frozen_welfare(eta,rho,kappa,"SU",g,SW[0])
                wi=frozen_welfare(eta,rho,kappa,"IS",g,SW[0])
            return ws[0],ws[2],wi[0]

        def c_diff(g):
            M,O,I=values(g)
            return I-O
        cap=brentq(c_diff,.2,.6,xtol=1e-12)
        M,O,I=values(cap)
        suopt=minimize_scalar(lambda g:-values(g)[0],
                              bounds=(cap,1),method="bounded")
        print(("endogenous" if endogenous else "frozen")+
              " g_C=%.9f W_IS=%.9f maxSUbeyondC=%.9f"%(cap,I,-suopt.fun))
        assert I>max(SW[2][0],M,-suopt.fun)
        reference=.38276541746182835 if endogenous else .45113725990523507
        assert abs(cap-reference)<1e-7

    print("PASS: illustrative policy-depth comparison (numerical only)")


if __name__=="__main__":
    main()
