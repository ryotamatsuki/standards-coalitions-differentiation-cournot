#!/usr/bin/env python3
"""Stage23 independent finite-depth check; NEVER an all-g interval certificate."""
import json, sys
import numpy as np
import sympy as sp
from scipy.optimize import root
D, ETA, RHO, KAPPA = 1., .758, .9, .8505
def system(x,g,regime):
    H=np.eye(3)
    if regime=="SU": H[0,1]=H[1,0]=g
    if regime=="IS":
        H=np.full((3,3),g)
        np.fill_diagonal(H,1.)
    X=np.eye(3)
    for a in range(3):
        for b in range(a+1,3):X[a,b]=X[b,a]=(x[a]+x[b])/2
    B=RHO*H+(1-RHO)*X
    M=np.eye(3)+B-ETA*H
    q=np.linalg.solve(M,np.ones(3)*D)
    return B,M,q
def firm_foc(x,g,regime):
    _,M,q=system(x,g,regime)
    out=np.empty(3)
    for a in range(3):
        E=np.zeros((3,3))
        for b in range(3):
            if b!=a:E[a,b]=E[b,a]=(1-RHO)/2
        dq=np.linalg.solve(M,-E@q)
        out[a]=6*q[a]*dq[a]+KAPPA*(1-x[a])
    return out
swroot=root(lambda x:firm_foc(x,0,"SW"),[.72]*3,tol=1e-12)
assert max(abs(firm_foc(swroot.x,0,"SW")))<1e-10
z=float(np.mean(swroot.x))
def calc(g,regime,frozen):
    if frozen:x=np.array([z]*3)
    else:
        sol=root(lambda x:firm_foc(x,g,regime),[z]*3,tol=1e-11)
        x=sol.x
        assert max(abs(firm_foc(x,g,regime)))<1e-8 and np.all(x>0) and np.all(x<1)
    B,M,q=system(x,g,regime)
    return float(q@B@q/2)+3*q*q-KAPPA*(1-x)**2/2
s=calc(0,"SW",False)[0]
cases={}
for fixed in [True,False]:
    SU=calc(.05,"SU",fixed)
    IS=calc(.05,"IS",fixed)
    cases["frozen" if fixed else "endogenous"]={"m_minus_s":float(SU[0]-s),"i_minus_o":float(IS[0]-SU[2]),"i_minus_s":float(IS[0]-s)}
assert cases["frozen"]["m_minus_s"]>0>cases["endogenous"]["m_minus_s"]
assert cases["frozen"]["i_minus_o"]>0>cases["endogenous"]["i_minus_o"]
alpha=2-ETA;beta=1-RHO;delta=RHO-ETA
t=beta*z;P=alpha-t;L=alpha+2*t
direct=RHO/L**2-delta*(2*(1+2*t)/L**3+6*alpha/(P*L**3))
C=beta*(ETA+2*t)/L**3
V=3*beta*(alpha-2*t)/(P*L**3)
ell=-KAPPA+6*beta**2*(alpha-2*t)*(2*alpha+t)/(P**2*L**4)
chi=3*beta**2*(3*alpha-2*t)/(P*L**4)
p=6*delta*beta*(alpha-2*t)*(2*alpha+t)/(P**2*L**4)
r=6*delta*beta*(alpha**2-2*alpha*t+4*t*t)/(P**2*L**4)
u,v=np.linalg.solve([[-ell-chi,-chi],[-2*chi,-ell]],[p,r])
loss=C*(2*u+v)+V*(u+v)
assert 0<direct<loss and u>v>0 and -ell>2*chi
g,T=sp.symbols("g T")
m=(4+g)/(1+T*g)**2+sp.Rational(1,2)
o=(1+g)/(1+T*g)**2+sp.Rational(7,2)
i=(sp.Rational(9,2)+3*g)/(1+2*T*g)**2
poly=14*T**4*g**3+(42*T**3+T**2)*g**2+T*(45*T-2)*g+16*T-2
assert sp.factor(m-sp.Rational(9,2)-g*(1-8*T-4*T*T*g)/(1+T*g)**2)==0
assert sp.factor(i-o+g*poly/((1+T*g)**2*(1+2*T*g)**2))==0
eta,beta_=sp.symbols("eta beta_")
a=2-eta;t0=beta_;de=1-beta_-eta;Ll=a+2*t0
expr=(1-beta_)/Ll**2-de*(2*(1+2*t0)/Ll**3+6*a/((a-t0)*Ll**3))
me=sp.factor(sp.diff(expr,eta).subs({eta:sp.Rational(6,7),beta_:0}))
mb=sp.factor(sp.diff(expr,beta_).subs({eta:sp.Rational(6,7),beta_:0}))
assert me==sp.Rational(2401,512) and mb==sp.Rational(10339,2048)
print(json.dumps({"scope":"local numerical and rho=1 symbolic only; no all-depth interval replay","python":sys.version.split()[0],"numpy":np.__version__,"sympy":sp.__version__,"sw_design":z,"cases":cases,"local":{"D":direct,"loss":loss,"mu":direct-loss,"uprime":float(u),"vprime":float(v)},"exact_face":"PASS, eta critical 6/7 and cutoff slope -211/196"},indent=2))
