#!/usr/bin/env python3
"""Stage19 network-externality comparative statics, exact Fraction witnesses.
No numeric finite differences; strictly sign-check analytic derivatives.
This is NOT a globally certified government policy optimum over eta.
"""
from fractions import Fraction as Q
rho=Q(9,10);beta=1-rho;kappa=Q(1701,2000);d=Q(1)
g=Q(1,20)

def constants(eta,y,g):
    alpha=2-eta
    delta=rho-eta
    t=delta*g+beta*y
    P=alpha-t
    L=alpha+2*t
    assert P>0 and L>0 and alpha>0
    return alpha,delta,t,P,L

def A(eta,y,g):
    alpha,delta,t,P,L=constants(eta,y,g)
    return 6*beta*alpha*d*d/(P*L**3)

def G(eta,y,g):
    alpha,delta,t,P,L=constants(eta,y,g)
    return 6*beta*alpha*d*d*(5*alpha-8*t)/(P**2*L**4)

def A_eta(eta,y,g):
    alpha,delta,t,P,L=constants(eta,y,g)
    return A(eta,y,g)*(-1/alpha+(1-g)/P+3*(1+2*g)/L)

def bracket(fun,low=Q(0),high=Q(1),steps=105):
    l,h=low,high
    assert fun(l)>0>fun(h)
    for _ in range(steps):
        m=(l+h)/2
        if fun(m)>0:l=m
        else:h=m
    assert fun(l)>0 and fun(h)<0
    return l,h

def row(eta,lam):
    zlo,zhi=bracket(lambda z: kappa*(1-z)-A(eta,z,Q(0)))
    z=(zlo+zhi)/2
    zeta=-A_eta(eta,z,Q(0))/(kappa-beta*G(eta,z,Q(0)))
    assert zeta<0
    ylo,yhi=bracket(lambda y:kappa*(1-y)-lam*(y-z)-A(eta,y,g))
    y=(ylo+yhi)/2
    aa,delta,t,P,L=constants(eta,y,g)
    h=A_eta(eta,y,g)
    curv=kappa+lam-beta*G(eta,y,g)
    assert h>0 and curv>0
    dyeta=(lam*zeta-h)/curv
    dyeta_legacy_fixed=-h/curv
    dydg=delta*G(eta,y,g)/curv
    assert dyeta<0 and dyeta_legacy_fixed<0
    # For the three displayed rho/eta regimes under G>0, sign(dy/dg)=sign(rho-eta).
    assert 5*aa-8*t>0 and G(eta,y,g)>0
    assert (dydg>0)==(delta>0) if delta!=0 else dydg==0
    print('eta',float(eta),'lambda',float(lam),
          'z',float(z),'y(g=.05)',float(y),
          'network marginal A_eta',float(h),
          'dz_deta(recenter)',float(zeta),
          'dy_deta(recenter)',float(dyeta),
          'dy_deta(fixed legacy)',float(dyeta_legacy_fixed),
          'dy_dg',float(dydg))
    if eta==rho:assert dydg==0
    if eta<rho:assert dydg>0
    if eta>rho:assert dydg<0

for eta in (Q(379,500),Q(9,10),Q(23,25)):
    for lam in (Q(0),Q(5)):
        row(eta,lam)
print('PASS: rational analytical network-externality comparative statics and rho-eta response sign switch')
print('SCOPE: private symmetric IS branches at g=.05; government g*(eta) requires outsider SU equilibrium too.')
