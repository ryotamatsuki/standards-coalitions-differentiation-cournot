#!/usr/bin/env python3
"""Stage24 reduced-form novelty kill test only. NOT a proof of the V2b structural model.
Symmetric policy-edge game with private Nash x_i=z+b*sum(incident edges).
Shows sign A/B local pattern also follows generic calculus and graph incidence.
Stage22/23 V2b exact/numerical calculations are reused, NOT rerun."""
import sympy as s
D,A,b,nu,g=s.symbols('D A b nu g', real=True)
mu=D-A*b
m=mu*g; o=nu*g; i=(2*mu+nu)*g
checks={
 'frozen_member': D,
 'endogenous_member':s.diff(m,g),
 'endogenous_outsider_accession':s.diff(i-o,g),
 'endogenous_grand':s.diff(i,g),
 'endogenous_incumbent_accession':s.diff(i-m,g)
}
assert s.simplify(checks['endogenous_outsider_accession']-2*mu)==0
assert s.simplify(checks['endogenous_grand']-(2*mu+nu))==0
toy={D:s.Integer(1),A:s.Integer(2),b:s.Integer(1),nu:s.Integer(3)}
expect={'frozen_member':1,'endogenous_member':-1,'endogenous_outsider_accession':-2,'endogenous_grand':1,'endogenous_incumbent_accession':2}
for k,v in checks.items():
    assert v.subs(toy)==expect[k],(k,v.subs(toy),expect[k])
print('PASS: generic LOCAL sign reversal, outsider veto and Pareto grand, with no network/Cournot.')
print({k: str(s.simplify(v)) for k,v in checks.items()})
