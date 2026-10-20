#!/usr/bin/env python3
"""V2b Stage-6: strict rational-interval Pareto gain despite coalition holdout.

Proof: at the EXACT rational witness and g=1/20, a globally unique
endogenous Stage-4 IS design produces higher welfare in ALL countries
than the globally unique SW outcome. Unreachability is separately
certified for ALL g by the Stage-4A Krawczyk interval proof.

Run with mpmath only: python verification/v2b_stage06_pareto_holdout.py.
"""
from fractions import Fraction as Q
from mpmath import iv
iv.dps=40

def interval(a,b=None):
    if b is None:b=a
    a,b=Q(a),Q(b)
    return iv.mpf([a.numerator*b.denominator,b.numerator*a.denominator])/(a.denominator*b.denominator)

E=interval(Q(379,500))
R=interval(Q(9,10))
K=interval(Q(1701,2000))
A=2-E
beta=1-R

def firm_foc(x,g):
    t=(R-E)*g+beta*x
    return K*(1-x)-6*beta*A/((A-t)*(A+2*t)**3)

def national_welfare_is(x,g):
    t=(R-E)*g+beta*x
    q=1/(A+2*t)
    return (iv.mpf(9)/2+3*(R*g+beta*x))*q*q-K*(1-x)**2/2

def bracketed_payoff(a,b,g):
    lower,upper=interval(a),interval(b)
    assert firm_foc(lower,g).a>0, (a,g,firm_foc(lower,g))
    assert firm_foc(upper,g).b<0, (b,g,firm_foc(upper,g))
    # Opposite signs + Stage-4A Rosen global Nash uniqueness certify identity.
    return national_welfare_is(interval(Q(a),Q(b)),g)

def main():
    assert Q(1701,2000)>81*Q(1,10)**2
    sw=bracketed_payoff('0.71859270731','0.71859270734',interval(Q(0)))
    is05=bracketed_payoff('0.72610900359','0.72610900362',interval(Q(1,20)))
    improvement=is05-sw
    assert improvement.a>0
    print('SW welfare interval',sw)
    print('IS(g=1/20) welfare interval',is05)
    print('strict per-country Pareto gain interval',improvement)
    print('PASS: Pareto-improving IS possible even with endogenous firm design')
    print('Global game unreachability requires separately passed Stage-4A all-g proofs.')

if __name__=='__main__':main()
