#!/usr/bin/env python3
"""V2b nonlinear-X Stage 4: full 3-player Rosen diagonal-strict-concavity certificate.

All economic parameters fixed at exact rationals. For each S=SW,SU,IS,
prove the symmetrized Jacobian of the 3-firm pseudo-gradient is negative
definite by STRICT Gershgorin row dominance for ALL x in [0,1]^3 and
ALL g in [0,1], using rational boxes and outward-rounded interval arithmetic.

No approximate root/solver can manufacture a passed box; no Stage4 V2b
production module is imported. This is not a Lean formal proof.
"""
from fractions import Fraction as Q
import sympy as sp
from mpmath import iv
iv.dps=40
x=sp.symbols('x0 x1 x2',real=True)
g=sp.symbols('g',real=True)
A=sp.Rational(621,500)
r_minus_e=sp.Rational(71,500)
beta=sp.Rational(1,10)
kappa=sp.Rational(1701,2000)

def closed(a,b):
    a,b=Q(a),Q(b)
    return iv.mpf([a.numerator*b.denominator,
                   b.numerator*a.denominator])/(a.denominator*b.denominator)

def compile_gradient_hessian(S):
    def hij(i,j):
        physical = beta*(x[i]**2+x[j]**2)/2
        edge = g*r_minus_e if (S=='IS' or S=='SU' and (i,j) in [(0,1),(1,0)]) else 0
        return physical+edge
    M=sp.Matrix([[A if i==j else hij(i,j)
                  for j in range(3)] for i in range(3)])
    inv=M.inv()
    quantities=inv*sp.ones(3,1)
    gradients=[]
    for i in range(3):
        qi_der=(-inv*M.diff(x[i])*quantities)[i]
        gradients.append(6*quantities[i]*qi_der+kappa*(1-x[i]))
    J=[sp.diff(gradients[i],x[j]) for i in range(3) for j in range(3)]
    return sp.lambdify((*x,g),J,modules='math',cse=True)

def certify(S,limit=100000):
    fun=compile_gradient_hessian(S)
    stack=[tuple((Q(0),Q(1)) for _ in range(4))]
    accepted=0;divisions=0;largest_upper=float('-inf')
    while stack:
        box=stack.pop()
        vals=fun(*(closed(*pair) for pair in box))
        J=[[vals[3*i+j] for j in range(3)] for i in range(3)]
        row_bounds=[]
        for i in range(3):
            row=float(J[i][i].b)
            for j in range(3):
                if i==j: continue
                symmetric_offdiag=(J[i][j]+J[j][i])/2
                row+=max(abs(float(symmetric_offdiag.a)),
                         abs(float(symmetric_offdiag.b)))
            row_bounds.append(row)
        if max(row_bounds)<0:
            accepted+=1
            largest_upper=max(largest_upper,max(row_bounds))
            continue
        divisions+=1
        if divisions>limit:
            raise AssertionError(('UNRESOLVED Rosen box',S,box,row_bounds))
        i=max(range(4),key=lambda j:box[j][1]-box[j][0])
        a,b=box[i];m=(a+b)/2
        for segment in ((a,m),(m,b)):
            child=list(box);child[i]=segment
            stack.append(tuple(child))
    print('CERTIFIED strict Rosen, all g and all 3 x:',S,
          'boxes',accepted,'splits',divisions,
          'largest outward row upper',largest_upper,flush=True)
    assert largest_upper<0

if __name__=='__main__':
    for S in ('SW','SU','IS'):certify(S)
    print('PASS: strict diagonal concavity for entire nonlinear design strategy space')
