#!/usr/bin/env python3
"""Stage17 global SU-envelope dominance. Exact Fraction arithmetic, no NumPy.
Certifies EVERY g in [0,1], all SU firm Nash strategies at lambda=5,
then compares an inherited exactly accepted IS(g=1/20) witness.
"""
from fractions import Fraction as Q
import heapq
class I:
    __slots__=("l","h")
    def __init__(self,l,h=None):
        if isinstance(l,I):self.l,self.h=l.l,l.h
        else:self.l,self.h=Q(l),Q(l if h is None else h)
        assert self.l<=self.h
    def cv(self,x):return x if isinstance(x,I) else I(x)
    def __add__(self,x):
        x=self.cv(x);return I(self.l+x.l,self.h+x.h)
    __radd__=__add__
    def __neg__(self):return I(-self.h,-self.l)
    def __sub__(self,x):return self+-self.cv(x)
    def __rsub__(self,x):return self.cv(x)+-self
    def __mul__(self,x):
        x=self.cv(x);v=(self.l*x.l,self.l*x.h,self.h*x.l,self.h*x.h)
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.cv(x);assert x.l*x.h>0
        return self*I(1/x.h,1/x.l)
    def __rtruediv__(self,x):return self.cv(x)/self
    def __pow__(self,n):
        assert n==2
        if self.l>=0:return I(self.l*self.l,self.h*self.h)
        if self.h<=0:return I(self.h*self.h,self.l*self.l)
        return I(0,max(self.l*self.l,self.h*self.h))
alpha=I(Q(621,500));eta=Q(379,500);beta=Q(1,10)
rho=Q(9,10);delta=Q(71,500);k=Q(1701,2000)
z=I(Q('0.71859270732'),Q('0.71859270733'))
lam=Q(5);CEILING=Q('2.4405')
# For ALL primitive g,x: 0<=M_ij<=beta+delta=.242,
# M_ii=alpha=1.242; row slack alpha-2*(beta+delta)=eta=.758.
# Positive q has qi<=1/alpha, ||M^-1||inf<=1/eta,
# ||M_xi*q||inf<=beta/alpha. Hence
# |6 qi qi_xi|<=6*beta/(alpha^2*eta) for EVERY unilateral firm.
# FOC: (k+lam)*xi=k+lam*z+6qi*qi_xi; endpoint FOC signs ensure
# each design Nash root is interior; strict Rosen sufficiency inherited.
PRIVATE=6*beta/(alpha.l**2*eta)
x_lo=(k+lam*z.l-PRIVATE)/(k+lam)
x_hi=(k+lam*z.h+PRIVATE)/(k+lam)
assert Q('0.67')<x_lo and x_hi<Q('0.85')
assert k+lam*z.l>PRIVATE and lam*(1-z.h)>PRIVATE
print('PASS: all-regime global Nash design enclosure',float(x_lo),float(x_hi))
def national_member_upper(box):
    # AB symmetric Nash is x_A=x_B=u, x_C=v.
    # Enclose a deliberately larger rectangle of all such designs,
    # requiring no root-finding and no assumption on policy monotonicity.
    u,v,g=[I(*b) for b in box]
    t=delta*g+beta*u
    h=beta*(u+v)/2
    det=alpha*(alpha+t)-2*h*h
    assert det.l>0
    qm=(alpha-h)/det
    qo=(alpha+t-2*h)/det
    gross_member_subst=rho*g+beta*u
    # CS=(1+B_AB)*qm^2 + qo^2/2 +2*B_AC*qm*qo;
    # W_A=CS+3qm^2 -k(1-u)^2/2 -lam(u-z)^2/2.
    cs=(1+gross_member_subst)*qm**2+qo**2/2+2*h*qm*qo
    w=cs+3*qm**2-k*(1-u)**2/2-lam*(u-z)**2/2
    return w.h
def main():
    initial=[(Q('.67'),Q('.85')),(Q('.67'),Q('.85')),(Q(0),Q(1))]
    first=national_member_upper(initial)
    heap=[(-float(first),0,initial)]
    iterations=0
    while heap:
        _,_,box=heapq.heappop(heap)
        # Partition exact rational policy/design boxes, retain only
        # descendants whose exact interval upper bound exceeds CEILING.
        widths=[float(hi-lo)*w for (lo,hi),w in zip(box,(1.4,.4,.5))]
        axis=max(range(3),key=widths.__getitem__)
        lo,hi=box[axis];mid=(lo+hi)/2
        for side in ((lo,mid),(mid,hi)):
            sub=list(box);sub[axis]=side
            upper=national_member_upper(sub)
            iterations+=1
            if upper>=CEILING:heapq.heappush(heap,(-float(upper),iterations,sub))
        if iterations>100000:
            raise AssertionError('INCOMPLETE: exact global subdivision limit exceeded')
    print('PASS: SU member welfare <',float(CEILING),
          'for all g in [0,1] and all Nash x, boxes',iterations)
    # Imported fixed-depth exact Krawczyk certificate is an independent
    # checked predecessor, not a new proof of an all-g optimum.
    import stage16_fixed_depth_certificate as prev
    assert z.l<=prev.Z.l<=prev.Z.h<=z.h
    is_value=prev.welfare(prev.rootbox('IS',Q(5)),'IS',Q(5))[0]
    assert is_value.l>CEILING
    sw=prev.SW
    assert sw.h<CEILING
    print('PASS: strict accepted IS(g=.05) proposer welfare lower',
          float(is_value.l),'> entire SU envelope',float(CEILING))
    print('THEOREM: any payoff-maximizing substantive SPNE outcome, if attained')
    print('and under original acceptance rules, must end with a three-country IS.')
    print('NOT PROVED: exact optimal depth, acceptance-tie SPNE existence, priority.')
if __name__=='__main__':main()
