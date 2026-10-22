"""Stage23 clean-room restricted-face algebra and threshold check.
SymPy proof regression only; NOT an all-depth interval certificate.
"""
import sympy as S
g,eta,beta,z,d,A,th=S.symbols("g eta beta z d A th",positive=True)
s=S.Rational(9,2)*A
m=A*((4+g)/(1+th*g)**2+S.Rational(1,2))
o=A*((1+g)/(1+th*g)**2+S.Rational(7,2))
i=A*(S.Rational(9,2)+3*g)/(1+2*th*g)**2
assert S.simplify(m-s-A*g*(1-8*th-4*th**2*g)/(1+th*g)**2)==0
poly=14*th**4*g**3+(42*th**3+th**2)*g**2+th*(45*th-2)*g+(16*th-2)
assert S.simplify(i-o+A*g*poly/((1+th*g)**2*(1+2*th*g)**2))==0
assert S.solve(S.diff(m,g).subs(g,0).subs(th,(1-eta)/(2-eta)),eta)==[S.Rational(6,7)]
a=2-eta;t=beta*z;P=a-t;L=a+2*t;delta=1-beta-eta
D=(1-beta)*d*d/L**2-delta*d*d*(2*(1+2*t)/L**3+6*a/(P*L**3))
center={beta:0,z:1,eta:S.Rational(6,7)}
et=S.factor(S.diff(D,eta).subs(center));be=S.factor(S.diff(D,beta).subs(center))
assert S.simplify(et-S.Rational(2401,512)*d*d)==0
assert S.simplify(be-S.Rational(10339,2048)*d*d)==0
assert S.simplify(-be/et+S.Rational(211,196))==0
print("Stage23 restricted-face symbolic PASS. No all-depth re-certification.")
