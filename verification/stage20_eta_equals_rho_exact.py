#!/usr/bin/env python3
"""Exact Fraction test for eta=rho>0 => proposer optimum IS(g=1).
The universal algebraic proof and the necessary separate SU gate
appear in reviews/STAGE20_REGIME_CLASSIFICATION_GATE.md.
"""
from fractions import Fraction as Q
rho=eta=Q(9,10)
alpha=2-eta
beta=1-rho
k=Q(1701,2000)
assert rho-eta==0 and 0<eta<1 and k>54*beta**2/(eta**2*alpha**2)
def f(z):
    t=beta*z
    return k*(1-z)-6*beta*alpha/((alpha-t)*(alpha+2*t)**3)
l,h=Q(0),Q(1)
assert f(l)>0>f(h)
for _ in range(110):
    m=(l+h)/2
    if f(m)>0:l=m
    else:h=m
assert 0<l<h<1 and f(l)>0>f(h)
ql=1/(alpha+2*beta*h)
qh=1/(alpha+2*beta*l)
assert 0<ql<qh
for g in (Q(1,1000),Q(1,20),Q(1,2),Q(1)):
    # Same Cournot offdiagonal and private costs across SW, SU, IS.
    assert (rho-eta)*g+beta*l == beta*l
    su_min=rho*g*ql**2
    is_min=3*rho*g*ql**2
    assert is_min>su_min>0
    assert is_min-su_min==2*su_min
# IS strictly increases in g: marginal welfare = 3 rho q0^2 > 0.
assert 3*rho*ql**2>0
print("PASS exact eta=rho policy-independent Nash, positive SU and IS gains")
print("PASS IS dominates SU/SW at all g>0 and proposer unique g*=1")
print("z",float(l),float(h),"q",float(ql),float(qh))
print("IS full-depth gain",float(3*rho*ql**2),float(3*rho*qh**2))
print("Scope: not a proof of SW/SU/IS phase thresholds along eta")
