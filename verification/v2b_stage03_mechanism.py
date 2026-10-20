#!/usr/bin/env python3
"""Stage 3: primitive-first decomposition of government standards incentive.
This is an independently constructed comparative-static diagnostic, NOT Stage 4A.
Run: python verification/v2b_stage03_mechanism.py
"""
import numpy as np
import sympy as sp
from scipy.optimize import brentq

u, v, g, eta, rho, kappa=sp.symbols("u v g eta rho kappa",real=True)
beta=1-rho
A=2-eta
m=(rho-eta)*g+beta*u
n=beta*(u+v)/2
D=A*(A+m)-2*n**2
qM=(A-n)/D
qO=(A+m-2*n)/D

# Distinct own-firm partial derivatives: one member moves alone; NOT joint u.
inv11=(1/(A-m)+A/D)/2
inv12=(-1/(A-m)+A/D)/2
inv13=-n/D
qM_own_derivative=-beta/2*(inv11*(qM+qO)+qM*(inv12+inv13))
qO_own_derivative=-beta*((A+m)*qM-n*qO)/D
F_M=kappa*(1-u)+6*qM*qM_own_derivative
F_O=kappa*(1-v)+6*qO*qO_own_derivative

# Each country's consumer surplus is identical; AB member welfare:
CS=(1+rho*g+beta*u)*qM**2+qO**2/2+beta*(u+v)*qM*qO
W_M=CS+3*qM**2-kappa*(1-u)**2/2
W_O=CS+3*qO**2-kappa*(1-v)**2/2
obj=[F_M,F_O]
diffs=[sp.diff(f,z) for f in [F_M,F_O,W_M,W_O] for z in (u,v,g)]
func=sp.lambdify((u,v,g,eta,rho,kappa),obj+diffs, "numpy", cse=True)

def direct_outcomes(S,gg,x,ee,rr,kk):
    H=np.eye(3)
    if S=="SU": H[0,1]=H[1,0]=gg
    if S=="IS": H=H+gg*(np.ones((3,3))-np.eye(3))
    X=np.eye(3)+.5*(x[:,None]+x[None,:])*(np.ones((3,3))-np.eye(3))
    B=rr*H+(1-rr)*X
    q=np.linalg.solve(np.eye(3)+B-ee*H,np.ones(3))
    w=.5*q@B@q + 3*q*q-kk*(1-x)**2/2
    return q,w

def main():
    E,R,K=.758,.9,.8505
    swx=brentq(lambda z:func(z,z,0,E,R,K)[0], .1,.99,xtol=1e-14)
    val=np.array(func(swx,swx,0,E,R,K),dtype=float)
    # First 2 outputs: F_M, F_O; then row-major 4x3 derivative array
    assert np.max(np.abs(val[:2])) < 1e-10
    deriv=val[2:].reshape(4,3)
    J=deriv[:2,:2]
    shift=np.linalg.solve(J,-deriv[:2,2])
    wgrad=deriv[2,:]
    direct=wgrad[2]
    feedback=np.dot(wgrad[:2],shift)
    total=direct+feedback

    q0,w0=direct_outcomes("SW",0,np.repeat(swx,3),E,R,K)
    assert abs(q0[0]-q0[1])<1e-12
    for i in range(3):
        h=1e-6
        # Check independent one-firm payoff FOC numerically.
        xx=np.repeat(swx,3)
        xx[i]+=h;qp=direct_outcomes("SW",0,xx,E,R,K)[0]
        xx[i]-=2*h;qm=direct_outcomes("SW",0,xx,E,R,K)[0]
        derivative=(3*qp[i]**2-K*(1-(swx+h))**2/2-
                    (3*qm[i]**2-K*(1-(swx-h))**2/2))/(2*h)
        assert abs(derivative)<2e-8

    # Independent direct-policy partial derivative with designs fixed:
    h=1e-6
    xm=np.repeat(swx,3)
    fixed_su=(direct_outcomes("SU",h,xm,E,R,K)[1][0]-
              direct_outcomes("SU",-h,xm,E,R,K)[1][0])/(2*h)
    assert abs(direct-fixed_su)<2e-7

    print(f"SW x = {swx:.12f}; SW welfare = {w0[0]:.12f}")
    print(f"SU member design response u'(0) = {shift[0]:+.12f}")
    print(f"SU outsider design response v'(0) = {shift[1]:+.12f}")
    print(f"SU member partial W/partial u = {wgrad[0]:+.12f}")
    print(f"SU member partial W/partial v = {wgrad[1]:+.12f}")
    print(f"SU member direct policy effect = {direct:+.12f}")
    print(f"SU member private-design feedback = {feedback:+.12f}")
    print(f"SU member total policy effect = {total:+.12f}")
    assert abs(direct-.006767924128844666)<2e-8
    assert abs(feedback+.015069744125257679)<2e-8
    assert abs(total+.008301819996413013)<2e-8
    print("PASS: candidate local sign reversal from the same primitives.")
    print("LIMIT: No independent Stage 4A; no global SPNE or prior-art certification in this script.")

if __name__=="__main__":
    main()
