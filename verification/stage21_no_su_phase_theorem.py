#!/usr/bin/env python3
"""Stage21 exact Fraction proof regression: NO optimum SU when rho=1,
and exact quadratic margins for perturbation to rho<1.
The derivative-compactness proof is mathematical, in the review note.
"""
from fractions import Fraction as Q
def payoff(theta,g):
    return (Q(9,2),(4+g)/(1+theta*g)**2+Q(1,2),
            (1+g)/(1+theta*g)**2+Q(7,2),
            (Q(9,2)+3*g)/(1+2*theta*g)**2)
# theta=(1-eta)/(2-eta). For eta<=6/7 (theta>=1/8)
# SU member-minus-SW = -g*(4*theta**2*g+8*theta-1)/(1+theta*g)**2.
# Grand outsider accession difference is -g*P/positive, with
# P=14*g^3*theta^4 +g^2*(42theta^3+theta^2)
#  +g*theta*(45theta-2)+(16theta-2) >0.
assert 45*Q(1,8)-2>0 and 16*Q(1,8)-2==0
# For eta>6/7, v=1-8theta and SU proposer gain <= v.
# Offer h=min(1,2v) is strictly acceptable grand, dominates all SU.
# If theta<=1/16, h=1, member/outsider SU <=11/2 while IS>=160/27.
assert Q(160,27)>Q(11,2)
assert Q(160,27)-Q(9,2)>1
# If 1/16<theta<1/8, let 0<v<1/2 and h=2v.
# Multiplying by positive denominators, each claimed payoff difference
# becomes the displayed polynomial in v. Check IDENTITIES with exact
# rationals at 10 distinct points; both cleared sides have degree <=8,
# so exact equality at 10 points implies polynomial identity.
for n in range(1,11):
    v=Q(n,20)
    theta=(1-v)/8;h=2*v
    s,m,o,i=payoff(theta,h)
    A=2*(v-2)**2*(v+1)**2
    B=A*(v*v-v-4)**2
    assert A*(i-s-v)==v*(4+19*v+24*v*v-5*v**3-2*v**4)
    assert B*(i-o)==v*v*(280+492*v-83*v*v-240*v**3+42*v**4+28*v**5-7*v**6)
    assert B*(i-m)==v*(192+304*v+132*v*v-77*v**3-48*v**4+6*v**5+4*v**6-v**7)
u=Q(1,2)
assert 5*u**3+2*u**4 <= Q(3,4) < 4
assert 83*u*u+240*u**3+7*u**6 < 51 < 280
assert 77*u**3+48*u**4+u**7 < 13 < 192
# Critical eta=6/7 => theta=1/8, second-order strictly negative.
t=Q(1,8)
for g in (Q(1,10),Q(1,2),Q(1)):
    s,m,o,i=payoff(t,g)
    assert m-s == -g*g/(16*(1+g/8)**2)
    assert i-o == -g*g*(Q(29,64)+Q(25,256)*g+Q(7,2048)*g*g)/((1+g/8)**2*(1+g/4)**2)
    assert m<s and i<o
eta0=Q(6,7);alpha=2-eta0
assert (1-eta0)/alpha==t
assert 8/alpha**4==Q(2401,512)
assert 3-18*t==2-10*t==Q(3,4)
print('PASS: global rho=1 selection eta<=6/7 -> SW, eta>6/7 -> IS; SU never optimal')
print('PASS: explicit accepted grand depth min(1,2*(1-8theta)) defeats every SU offer')
print('PASS: strict quadratic gap at threshold and nonzero network-strength transversality')
print('SCOPE: original rho<1 endogenous-design no-SU region follows by smooth/compact proof in reviews; not a universal theorem')
