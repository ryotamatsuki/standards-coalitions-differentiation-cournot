#!/usr/bin/env python3
"""Stage13A independent scalar-cofactor derivation and exact Fraction intervals.

No imports from existing V2b programs. Never converts proof coefficients/endpoints
to binary64. Floating point appears only in explicitly labelled diagnostics.
Run from repository root; optional --json writes machine-readable evidence.
"""
import argparse
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction as R
from pathlib import Path
import platform
import sympy as S
import numpy as np
from scipy.optimize import root


@dataclass(frozen=True)
class Interval:
    lo: R
    hi: R

    def __post_init__(self):
        if not isinstance(self.lo, R) or not isinstance(self.hi, R):
            raise TypeError('Proof endpoints must be Fraction')
        assert self.lo <= self.hi

    @staticmethod
    def cast(x):
        if isinstance(x, Interval): return x
        if isinstance(x, float): raise TypeError('No floats in proof arithmetic')
        q = R(x)
        return Interval(q, q)

    def __add__(self, other):
        o = self.cast(other)
        return Interval(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__

    def __neg__(self): return Interval(-self.hi, -self.lo)
    def __sub__(self, other): return self + -self.cast(other)
    def __rsub__(self, other): return self.cast(other) + -self

    def __mul__(self, other):
        o = self.cast(other)
        p = [a*b for a in (self.lo, self.hi) for b in (o.lo, o.hi)]
        return Interval(min(p), max(p))
    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self.cast(other)
        if o.lo <= 0 <= o.hi: raise ZeroDivisionError('Interval includes zero')
        return self * Interval(1/o.hi, 1/o.lo)
    def __rtruediv__(self, other): return self.cast(other) / self

    def __pow__(self, n):
        assert isinstance(n, int)
        if n < 0: return 1/(self**(-n))
        if n == 0: return self.cast(1)
        if n % 2 == 0 and self.lo <= 0 <= self.hi:
            return Interval(R(0), max(self.lo**n, self.hi**n))
        v = [self.lo**n, self.hi**n]
        return Interval(min(v), max(v))

    def positive(self): return self.lo > 0
    def record(self):
        return {'lower_exact': str(self.lo), 'upper_exact': str(self.hi),
                'display_only': [float(self.lo), float(self.hi)]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json')
    args = parser.parse_args()
    evidence = {'environment': {'python': platform.python_version(),
                               'sympy': S.__version__, 'numpy': np.__version__},
                'identities': [], 'scope': 'Canonical phi=x; new local region only'}

    def check(label, lhs, rhs):
        assert S.cancel(lhs-rhs) == 0, label
        evidence['identities'].append(label)
        print('EXACT IDENTITY PASS:', label, flush=True)

    # Cramer's rule using three independent edge coefficients: distinct path from
    # PR9's inverse-matrix derivative identity and symmetric projector inverse.
    A,b,d,k,delta,rho,t = S.symbols('A b d k delta rho t', real=True)
    e,f,h = S.symbols('e f h', real=True)
    edges = [e,f,h]
    det = A**3 - A*(e**2+f**2+h**2) + 2*e*f*h
    q = [d*(A**2-A*(e+f)+h*(e+f)-h**2)/det,
         d*(A**2-A*(e+h)+f*(e+h)-f**2)/det,
         d*(A**2-A*(f+h)+e*(f+h)-e**2)/det]
    M = S.Matrix([[A,e,f],[e,A,h],[f,h,A]])
    for j in range(3): check('Cramer_market_row_'+str(j), (M*S.Matrix(q))[j], d)
    incident = [(e,f),(e,h),(f,h)]
    dx = lambda expr,j: b*sum(S.diff(expr,edge) for edge in incident[j])/2
    dg = lambda expr: delta*S.diff(expr,e)
    at = lambda expr: S.factor(expr.subs({e:t,f:t,h:t}))
    F = [6*q[i]*dx(q[i],i) for i in range(3)]
    # Off-symmetry SU identities: compute unilateral derivatives first.
    u,v,g0=S.symbols('u v g0',real=True)
    cc=delta*g0+b*u; nn=b*(u+v)/2; DD=A*(A+cc)-2*nn**2
    su_sub={e:cc,f:nn,h:nn}
    QM=d*(A-nn)/DD; QO=d*(A+cc-2*nn)/DD
    check('SU_member_quantity',q[0].subs(su_sub),QM)
    check('SU_outsider_quantity',q[2].subs(su_sub),QO)
    check('SU_unilateral_member_FOC',F[0].subs(su_sub),
          -3*b*QM*((A/(2*DD)+1/(2*(A-cc)))*QO+(A-nn)*QM/DD))
    check('SU_unilateral_outsider_FOC',F[2].subs(su_sub),
          -6*b*QO*((A+cc)*QM-nn*QO)/DD)
    P=A-t; L=A+2*t
    ell=-k+6*b*b*d*d*(A-2*t)*(2*A+t)/(P**2*L**4)
    hh=3*b*b*d*d*(3*A-2*t)/(P*L**4)
    p=6*delta*b*d*d*(A-2*t)*(2*A+t)/(P**2*L**4)
    r=6*delta*b*d*d*(A*A-2*A*t+4*t*t)/(P**2*L**4)
    check('unilateral_symmetric_FOC',at(F[0]),-6*b*A*d*d/(P*L**3))
    check('own_Jacobian',at(dx(F[0],0))-k,ell)
    check('rival_Jacobian',at(dx(F[0],1)),hh)
    check('member_policy_forcing',at(dg(F[0])),p)
    check('outsider_policy_forcing',at(dg(F[2])),r)
    check('forcing_gap',p-r,6*delta*b*d*d*(A-3*t)/(P**2*L**3))
    up=S.factor((-ell*p+hh*r)/((ell-hh)*(ell+2*hh)))
    vp=S.factor((2*hh*p-(ell+hh)*r)/((ell-hh)*(ell+2*hh)))
    check('member_IFT_equation',(ell+hh)*up+hh*vp,-p)
    check('outsider_IFT_equation',2*hh*up+ell*vp,-r)
    check('response_rank',up-vp,(p-r)/(hh-ell))

    # Consumer B has off-diagonal e+eta H12 etc; at SW it differs from
    # the Cournot M by (1-eta)I. For policy derivative add rho*qA*qB.
    cs=sum(qi**2 for qi in q)/2 + e*q[0]*q[1]+f*q[0]*q[2]+h*q[1]*q[2]
    # When taking design derivatives A is constant and diag B=1, as above.
    csx=at(dx(cs,0))
    csg=at(dg(cs)+(rho-delta)*q[0]*q[1])
    pig=at(dg(3*q[0]**2))
    pix=at(dx(3*q[0]**2,1))
    D=d*d*(rho/L**2-2*delta*(1+2*t)/L**3-6*delta*A/(P*L**3))
    C=b*d*d*(2-A+2*t)/L**3
    V=3*b*d*d*(A-2*t)/(P*L**3)
    check('consumer_design_derivative',csx,-C)
    check('rival_export_profit_derivative',pix,-V)
    check('direct_government_derivative',csg+pig,D)
    loss=C*(2*up+vp)+V*(up+vp)
    total=D+csx*(2*up+vp)+pix*(up+vp)
    check('assembled_corrected_loss',total,D-loss)
    # Literal PR9 Eq9 is intentionally a failing claim, kept as evidence.
    literal_loss=C*(2*up+vp)-V*(up+vp)
    check('PR9_equation9_error_residual',(D-literal_loss)-total,2*V*(up+vp))
    # A sees 2 incident edges + 1 nonincident under IS; SU outsider sees 1
    # nonincident. Both firms' redesign already incorporated by symmetry.
    member=total
    outsider_direct=csg+at(dg(3*q[2]**2))
    outsider=outsider_direct+csx*(2*up+vp)+pix*(2*up)
    # Independently differentiate IS: all three edges change, and all firms'
    # designs move by the scalar IS IFT derivative at SW.
    yyprime=6*delta*b*A*d*d*(5*A-8*t)/(P**2*L**4) / (
        k-6*b*b*A*d*d*(5*A-8*t)/(P**2*L**4))
    international=3*csg-12*delta*d*d/L**3+csx*3*yyprime+pix*2*yyprime
    check('edge_symmetry_accession_identity',international-outsider,2*member)

    y,g=S.symbols('y g',real=True)
    tt=delta*g+b*y
    sf=k*(1-y)-6*b*A*d*d/((A-tt)*(A+2*tt)**3)
    G=6*b*A*d*d*(5*A-8*tt)/((A-tt)**2*(A+2*tt)**4)
    for label, lhs, rhs in [('IS_Fy',S.diff(sf,y),-k+b*G),
                            ('IS_Fg',S.diff(sf,g),delta*G),
                            ('IS_Fk',S.diff(sf,k),1-y),
                            ('IS_Fd',S.diff(sf,d),-12*b*A*d/((A-tt)*(A+2*tt)**3))]:
        check(label,lhs,rhs)

    # Universal PSD of X on design cube by exact eight-vertex principal minors.
    all_minors=[]
    for vertex in itertools.product([0,1],repeat=3):
        X=S.eye(3)
        for i in range(3):
            for j in range(i): X[i,j]=X[j,i]=S.Rational(vertex[i]+vertex[j],2)
        for n in [1,2,3]:
            for inds in itertools.combinations(range(3),n):
                minor=X.extract(inds,inds).det()
                assert minor>=0
                all_minors.append(str(minor))
    evidence['PSD_X']={'vertices':8,'principal_minors':len(all_minors),
                       'argument':'X affine in x; convexity of PSD cone; H SU/IS PSD for 0<=g<=1'}
    print('EXACT PSD PASS: 8 vertices, 56 principal minors',flush=True)

    # Four-dimensional certified open region, parameterized by (z,eta,rho,d).
    # k is NOT freely tuned: solved from the original SW FOC. Strict positive
    # k_z makes this an open region in the original (k,eta,rho,d) coordinates.
    z=Interval(R('0.7185'),R('0.7187'))
    eta=Interval(R('0.75795'),R('0.75805'))
    rr=Interval(R('0.89995'),R('0.90005'))
    dd=Interval(R('0.999'),R('1.001'))
    aa=2-eta;bb=1-rr;de=rr-eta;ss=bb*z;pp=aa-ss;ll=aa+2*ss
    kk=6*bb*aa*dd**2/(pp*ll**3*(1-z))
    jdiag=-kk+6*bb**2*dd**2*(aa-2*ss)*(2*aa+ss)/(pp**2*ll**4)
    joff=3*bb**2*dd**2*(3*aa-2*ss)/(pp*ll**4)
    ff=6*de*bb*dd**2*(aa-2*ss)*(2*aa+ss)/(pp**2*ll**4)
    oo=6*de*bb*dd**2*(aa**2-2*aa*ss+4*ss**2)/(pp**2*ll**4)
    denom=(jdiag-joff)*(jdiag+2*joff)
    uu=(-jdiag*ff+joff*oo)/denom
    vv=(2*joff*ff-(jdiag+joff)*oo)/denom
    direct=dd**2*(rr/ll**2-2*de*(1+2*ss)/ll**3-6*de*aa/(pp*ll**3))
    ccoef=bb*dd**2*(eta+2*ss)/ll**3
    vcoef=3*bb*dd**2*(aa-2*ss)/(pp*ll**3)
    lost=ccoef*(2*uu+vv)+vcoef*(uu+vv)
    # Global asymmetric uniqueness via the norm Hessian bound for delta>=0.
    # max offdiag=1-eta; alpha-2max=eta; each profit Hessian entry <=18b²d²/(eta²alpha²).
    rosen=kk-54*bb**2*dd**2/(eta**2*aa**2)
    kz=kk*(1/(1-z)+bb/pp-6*bb/ll)
    positive={'delta':de,'alpha_minus_3s':aa-3*ss,
              'negative_diagonal_dominance':-jdiag-2*joff,
              'u_prime':uu,'v_prime':vv,'u_minus_v':uu-vv,
              'D':direct,'loss_minus_D':lost-direct,
              'full_cube_Rosen_margin':rosen,'coordinate_Jacobian_kz':kz}
    for name,value in positive.items():
        assert value.positive(),(name,value.record())
        print('FRACTION REGION PASS:',name,value.record()['display_only'],flush=True)
    evidence['certified_region']={'coordinates':{'z':z.record(),'eta':eta.record(),
        'rho':rr.record(),'d':dd.record()},'kappa_enclosure_only':kk.record(),
        'strict_conditions':{n:v.record() for n,v in positive.items()},
        'warning':'kappa enclosure is NOT an independent rectangular kappa range; local g result only'}

    # rho=eta exact nonvacuity example, with full-cube bounds.
    balanced_r=R(9,10); balanced_a=2-balanced_r;balanced_b=1-balanced_r
    ub=54*balanced_b**2/(balanced_r**2*balanced_a**2)
    interior_bound=6*balanced_b/(balanced_a**3)
    assert ub<1 and interior_bound<1
    evidence['balanced_example']={'rho_eta':'9/10','d':'1','kappa':'1',
                                 'Rosen_bound':str(ub),'interior_bound':str(interior_bound)}
    Q,rho0,gB=S.symbols('Q rho0 gB',positive=True)
    # Direct surplus evaluation at fixed privately optimized q=Q*1.
    for links in [1,3]:
        HH=S.eye(3)
        for i,j in ([(0,1)] if links==1 else [(0,1),(0,2),(1,2)]):
            HH[i,j]=HH[j,i]=gB
        gain=(S.ones(1,3)*(rho0*(HH-S.eye(3)))*S.ones(3,1))[0]*Q**2/2
        check('balanced_CS_gain_'+str(links)+'_edges',gain,links*rho0*gB*Q**2)
    # Unrestricted admissible eta/rho need not yield nonnegative quantities.
    highM=S.Matrix([[S.Rational(101,100) if i==j else -S.Rational(98,100)
                     for j in range(3)] for i in range(3)])
    highq=highM.inv()*S.ones(3,1)
    assert list(highq)==[-S.Rational(20,19)]*3
    evidence['quantity_counterexample']={'rho':'1/100','eta':'99/100','g':'1',
        'regime':'IS','x':[0,0,0],'d':'1','linear_quantity_each':'-20/19',
        'argument':'Negative off-diagonals force all quantities active in any LCP solution; unique linear solution negative, so no nonnegative equilibrium.'}
    # Rigorous positive-kappa boundary counterexample, with rivals at zero.
    # q_i(x)=d(alpha-beta*x)/(alpha²-beta²*x²/2). Its derivative magnitude
    # is >= beta*d*(alpha-beta)/alpha³ and q_i>=d*(alpha-beta)/alpha².
    # Hence F_i<=kappa-6beta*d²*(alpha-beta)²/alpha^5<0 for every x in [0,1].
    boundary_k=R(1,10)
    boundary_loss_bound=6*balanced_b*(balanced_a-balanced_b)**2/balanced_a**5
    assert boundary_k<boundary_loss_bound
    evidence['boundary_counterexample']={'rho_eta':'9/10','d':'1','kappa':'1/10',
        'all_x_F_upper_exact':str(boundary_k-boundary_loss_bound),
        'result':'x=(0,0,0) strict boundary Nash; strict interior derivative conclusions do not apply'}

    # Numeric cross-check using literal asymmetric scalar cofactors, not symbolic
    # derivatives; solve FOCs using finite differences of actual firm profits.
    def numeric_q(x,g0,regime):
        H=np.eye(3)
        for i,j in [(0,1)] if regime=='SU' else ([(0,1),(0,2),(1,2)] if regime=='IS' else []):
            H[i,j]=H[j,i]=g0
        X=np.eye(3)
        for i in range(3):
            for j in range(i):X[i,j]=X[j,i]=(x[i]+x[j])/2
        return np.linalg.solve(np.eye(3)+(.9-.758)*H+.1*X,np.ones(3))
    def profit(x,g0,regime,i):
        return 3*numeric_q(x,g0,regime)[i]**2-.8505*(1-x[i])**2/2
    def num_F(x,g0,regime):
        step=R(1,100000) # diagnostic conversion only
        step=float(step);out=[]
        for i in range(3):
            a1=np.array(x);a2=np.array(x);a1[i]+=step;a2[i]-=step
            out.append((profit(a1,g0,regime,i)-profit(a2,g0,regime,i))/(2*step))
        return np.array(out)
    sol=root(lambda x:num_F(x,0,'SW'),[.7186]*3,tol=1e-8)
    assert max(abs(num_F(sol.x,0,'SW')))<1e-8
    base=sol.x
    epsilon=1e-4
    su=root(lambda x:num_F(x,epsilon,'SU'),base,tol=1e-8)
    assert max(abs(num_F(su.x,epsilon,'SU')))<1e-8
    subs={A:S.Rational(621,500),b:S.Rational(1,10),d:1,k:S.Rational(1701,2000),
          delta:S.Rational(71,500),rho:S.Rational(9,10),t:S.Rational(str(.1*base[0]))}
    approx=lambda expr:float(expr.subs(subs).evalf(20))
    analytic=np.array([approx(up),approx(up),approx(vp)])
    fd=(su.x-base)/epsilon
    assert max(abs(fd-analytic))<2e-5
    evidence['numeric_only']={'z':base.tolist(),'analytic_design_slopes':analytic.tolist(),
        'finite_difference_slopes':fd.tolist(),'D':approx(D),'corrected_loss':approx(loss),
        'literal_PR9_loss':approx(literal_loss),'corrected_member_slope':approx(total),
        'literal_PR9_implied_slope':approx(D-literal_loss)}
    print('NUMERIC DIAGNOSTIC PASS:',evidence['numeric_only'],flush=True)
    evidence['overall']='PASS corrected identities and certified local region; literal PR9 Eq9 FAIL retained'
    if args.json:
        Path(args.json).write_text(json.dumps(evidence,indent=2)+'\n')
    print(evidence['overall'],flush=True)


if __name__=='__main__': main()
