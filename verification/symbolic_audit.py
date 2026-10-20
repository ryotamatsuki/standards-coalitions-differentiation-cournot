#!/usr/bin/env python3
"""SymPy audit of archived algebra. Does NOT certify full SPNE or novelty."""
import sympy as sp

eta, s, r = sp.symbols("eta s r", real=True)
A, k = 2-eta, 1-eta
Qsw, Qsu, Qis = 1/A, 1/(A+k*s), 1/(A+2*k*s)

# Linear Cournot FOCs for the selected continuation candidates.
M_sw = sp.diag(A, A, A)
M_su = sp.Matrix([[A, k*s, 0], [k*s, A, 0], [0, 0, A]])
M_is = sp.Matrix([[A,k*s,k*s], [k*s,A,k*s], [k*s,k*s,A]])
for M, q in [(M_sw,[Qsw]*3), (M_su,[Qsu,Qsu,Qsw]), (M_is,[Qis]*3)]:
    assert all(sp.simplify(v-1)==0 for v in M*sp.Matrix(q))

# Consumer surplus at fulfilled expectations: q'Bq/2.
cs_sw = sp.Rational(3,2)*Qsw**2
cs_su = (1+s)*Qsu**2 + sp.Rational(1,2)*Qsw**2
cs_is = sp.Rational(3,2)*(1+2*s)*Qis**2
Wsw = sp.factor(cs_sw+3*Qsw**2)
Wab = sp.factor(cs_su+3*Qsu**2)
Wc = sp.factor(cs_su+3*Qsw**2)
Wi = sp.factor(cs_is+3*Qis**2)
assert sp.simplify(Wsw-sp.Rational(9,2)/A**2)==0
assert sp.simplify(Wab-((4+s)/(A+k*s)**2+sp.Rational(1,2)/A**2))==0
assert sp.simplify(Wc-((1+s)/(A+k*s)**2+sp.Rational(7,2)/A**2))==0
assert sp.simplify(Wi-3*(3+2*s)/(2*(A+2*k*s)**2))==0

# Derivatives.
assert sp.simplify(sp.diff(Wab,s)-(7*eta-6-k*s)/(A+k*s)**3)==0
assert sp.simplify(sp.diff(Wc,s)-(eta-k*s)/(A+k*s)**3)==0
assert sp.simplify(sp.diff(Wi,s)-3*(5*eta-4-2*k*s)/(A+2*k*s)**3)==0

# C's participation constraint with NO renegotiation of g.
P = 14*r**4*s**3+(42*r**3+r**2)*s**2+(45*r**2-2*r)*s+16*r-2
Delta = Wi-Wc
assert sp.simplify(Delta+s*P.subs(r,k/A)/(A**2*(1+k*s/A)**2*(1+2*k*s/A)**2))==0
quartic = 57*eta**4-312*eta**3+632*eta**2-559*eta+181
assert sp.simplify(P.subs({r:k/A,s:1})-2*quartic/(eta-2)**4)==0
roots = [float(sp.re(rt)) for rt in sp.nroots(quartic)
         if abs(float(sp.im(rt)))<1e-12 and 6/7<float(sp.re(rt))<1]
assert len(roots)==1
assert abs(roots[0]-0.884049096671274)<1e-12

# Interior unconstrained IS welfare optimum.
sstar = (5*eta-4)/(2*k)
assert sp.simplify(sp.diff(Wi,s).subs(s,sstar))==0
assert sp.simplify(Wi.subs(s,sstar)-3/(8*(1-eta)*(2*eta-1)))==0

# Example eta=0.82: C vetoes IS at both the low initial depth and
# the unconstrained (but not participation-feasible) IS optimal depth.
e82=sp.Rational(41,50)
assert (Wi-Wc).subs({eta:e82,s:sp.Rational(1,25)})<0
assert (Wi-Wc).subs({eta:e82,s:sp.Rational(5,18)})<0
assert Wi.subs({eta:e82,s:sp.Rational(5,18)})>Wsw.subs(eta,e82)

# Symmetric adoption-cost witness: eta=0.9, F=0.163.
e90=sp.Rational(9,10)
F=sp.Rational(163,1000)
assert Wab.subs({eta:e90,s:1})-F>Wsw.subs(eta,e90)
assert Wi.subs({eta:e90,s:1})-F<Wc.subs({eta:e90,s:1})
assert sp.diff(Wab,s).subs({eta:e90,s:0})>0
assert sp.diff(Wab,s).subs({eta:e90,s:1})>0
delta_s=sp.cancel(Delta.subs(eta,e90))
deriv_num=sp.together(sp.diff(delta_s,s)).as_numer_denom()[0]
critical=[0.,1.]
for rt in sp.nroots(deriv_num):
    if abs(float(sp.im(rt)))<1e-10 and 0<float(sp.re(rt))<1:
        critical.append(float(sp.re(rt)))
max_gain=max(float(delta_s.subs(s,v)) for v in critical)
assert max_gain<float(F)

print("PASS: quantity, welfare, derivatives, C participation polynomial")
print(f"eta_C = {roots[0]:.15f}")
print(f"eta=.9, maximal gross C entry gain = {max_gain:.12f} < 0.163")
print("WARNING: complete off-path firm Nash and SPNE NOT certified.")
