#!/usr/bin/env python3
"""Stage14 clean-room local audit. No imports from previous V2b programs.
Symbolic identities plus exact rational interval checks; numeric displays are not proofs.
Alternative mapping is a DIAGNOSTIC, not a change to frozen primitives.
"""
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import sympy as s

class I:
    def __init__(self,lo,hi=None):
        self.lo=Q(lo); self.hi=Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def c(x): return x if isinstance(x,I) else I(x)
    def __add__(self,o):
        o=self.c(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-self.c(o)
    def __rsub__(self,o):return self.c(o)+-self
    def __mul__(self,o):
        o=self.c(o);v=[a*b for a,b in product((self.lo,self.hi),(o.lo,o.hi))];return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.c(o);assert not o.lo<=0<=o.hi;return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return self.c(o)/self
    def __pow__(self,n):
        if n<0:return 1/(self**(-n))
        if n==0:return I(1)
        v=[self.lo**n,self.hi**n]
        if n%2==0 and self.lo<=0<=self.hi:v.append(Q(0))
        return I(min(v),max(v))
    def record(self):return {'lo_exact':str(self.lo),'hi_exact':str(self.hi),'display_only':[float(self.lo),float(self.hi)]}

def calc(z,eps):
    # Exact constants from canonical freeze.
    eta=Q(379,500);rho=Q(9,10);b=1-rho;a=2-eta;k=Q(1701,2000);de=rho-eta
    t=b*z;P=a-t;L=a+2*t
    ell=-k+6*b*b*(a-2*t)*(2*a+t)/(P**2*L**4)
    h=3*b*b*(3*a-2*t)/(P*L**4)
    # Mapping B=(rho-eps)H+b X+eps(H Hadamard X), diagonal one.
    # At SW H_ij=0: unchanged base game; mixed design-policy derivative matters.
    de_e=de+eps*(z-1)
    p=6*de_e*b*(a-2*t)*(2*a+t)/(P**2*L**4)-3*eps*a/(P*L**3)
    r=6*de_e*b*(a*a-2*a*t+4*t*t)/(P**2*L**4)
    den=(ell-h)*(ell+2*h)
    up=(-ell*p+h*r)/den
    vp=(2*h*p-(ell+h)*r)/den
    C=b*(eta+2*t)/L**3
    V=3*b*(a-2*t)/(P*L**3)
    A=1/L**2
    BB=2*(1+2*t)/L**3+6*a/(P*L**3)
    D=(rho+eps*(z-1))*A-de_e*BB
    loss=C*(2*up+vp)+V*(up+vp)
    m=D-loss
    # Nonincident-edge outsider response, including own-profit FOC cancellation.
    csg=(rho+eps*(z-1))/L**2-2*de_e*(1+2*t)/L**3
    outsider=csg+12*de_e*t/(P*L**3)-C*(2*up+vp)-V*(2*up)
    grand=2*m+outsider
    return {'u_prime':up,'v_prime':vp,'D':D,'loss':loss,'member_slope':m,
            'outsider_slope':outsider,'grand_slope':grand,'global_slope':3*grand,
            'CS_direct':csg,'profit_direct':-6*de_e*a/(P*L**3),
            'CS_loss':C*(2*up+vp),'profit_loss':V*(up+vp),
            'threshold_lower':A/(BB+loss/de_e),'threshold_upper':A/BB,
            'effective_net_ratio':de_e/(rho+eps*(z-1)),'global_nash_J_margin':-ell-2*h}

def main():
    ids=[]
    def check(name,a,b):
        assert s.factor(a-b)==0,name;ids.append(name);print('EXACT SYMBOLIC PASS',name)
    a,b,d,k,t,de,rho,eps,z=s.symbols('a b d k t de rho eps z',nonzero=True)
    P=a-t;L=a+2*t
    R=(s.eye(3)-t/L*s.ones(3))/P; q=d/L*s.ones(3,1)
    E=[]
    for i in range(3):
        Ei=s.zeros(3)
        for j in range(3):
            if i!=j:Ei[i,j]=Ei[j,i]=b/2
        E.append(Ei)
    Eg=s.Matrix([[0,de+eps*(z-1),0],[de+eps*(z-1),0,0],[0,0,0]])
    qg=-R*Eg*q
    xx=[-R*Ei*q for Ei in E]
    Fg=[]
    J=s.zeros(3)
    for i in range(3):
        mixed=s.zeros(3)
        if i in (0,1):mixed[0,1]=mixed[1,0]=eps/2
        qxg=R*Eg*R*E[i]*q+R*E[i]*R*Eg*q-R*mixed*q
        Fg.append(s.factor(6*(qg[i]*xx[i][i]+q[i]*qxg[i])))
        for j in range(3):
            qxx=R*E[j]*R*E[i]*q+R*E[i]*R*E[j]*q
            J[i,j]=s.factor(6*(xx[j][i]*xx[i][i]+q[i]*qxx[i])-(k if i==j else 0))
    ell=-k+6*b*b*d*d*(a-2*t)*(2*a+t)/(P**2*L**4)
    h=3*b*b*d*d*(3*a-2*t)/(P*L**4)
    p=6*(de+eps*(z-1))*b*d*d*(a-2*t)*(2*a+t)/(P**2*L**4)-3*eps*a*d*d/(P*L**3)
    r=6*(de+eps*(z-1))*b*d*d*(a*a-2*a*t+4*t*t)/(P**2*L**4)
    check('J_own',J[0,0],ell);check('J_cross',J[0,1],h)
    check('nonlinear_member_forcing',Fg[0],p);check('nonlinear_outsider_forcing',Fg[2],r)
    Bd=(1-t)*s.eye(3)+t*s.ones(3)
    csx=(q.T*Bd*xx[0])[0]+(q.T*E[0]*q)[0]/2
    csg=(q.T*Bd*qg)[0]+(rho+eps*(z-1))*d*d/L**2
    C=b*d*d*(2-a+2*t)/L**3
    V=3*b*d*d*(a-2*t)/(P*L**3)
    check('consumer_design_incidence',csx,-C)
    check('rival_profit_incidence',6*q[0]*xx[1][0],-V)
    check('consumer_direct_nonlinear',csg,(rho+eps*(z-1))*d*d/L**2-2*(de+eps*(z-1))*d*d*(1+2*t)/L**3)
    uu,vv=s.symbols('uu vv')
    literal_loss=C*(2*uu+vv)-V*(uu+vv)
    correct_loss=C*(2*uu+vv)+V*(uu+vv)
    check('PR9_literal_error',correct_loss-literal_loss,2*V*(uu+vv))
    y,g=s.symbols('y g')
    tt=de*g+b*y
    F=k*(1-y)-6*b*a*d*d/((a-tt)*(a+2*tt)**3)
    G=6*b*a*d*d*(5*a-8*tt)/((a-tt)**2*(a+2*tt)**4)
    K=k-b*G
    check('IS_amplification',de+b*(-s.diff(F,g)/s.diff(F,y)),de*k/K)
    A,BB,CC=s.symbols('A BB CC',positive=True)
    check('threshold_D_minus_loss',rho*A-de*BB-de*CC,rho*(A-de/rho*(BB+CC)))
    # Independent actual root bracket, not a substituted symmetric optimum.
    eta0=Q(379,500);rho0=Q(9,10);a0=2-eta0;b0=1-rho0;k0=Q(1701,2000)
    def FF(zz):return k0*(1-zz)-6*b0*a0/((a0-b0*zz)*(a0+2*b0*zz)**3)
    zl=Q('0.7185');zh=Q('0.7187')
    assert FF(zl)>0 and FF(zh)<0
    # Existing full-cube Rosen sufficient bound, re-evaluated exactly.
    margin=k0-54*b0*b0/(eta0**2*a0**2)
    assert margin>0
    base=calc(I(zl,zh),I(0))
    assert base['D'].lo>0 and base['member_slope'].hi<0 and base['grand_slope'].lo>0
    # Not merely eps=0 or a number of sampled eps values: an interval of changed kernels.
    nonlin=calc(I(zl,zh),I('0','0.001'))
    assert nonlin['D'].lo>0 and nonlin['member_slope'].hi<0 and nonlin['grand_slope'].lo>0
    assert nonlin['u_prime'].lo>0 and nonlin['v_prime'].lo>0
    # Economic consistency on ENTIRE policy and strategy cubes:
    # H and X PSD; Schur product PSD; coefficients rho-eps,b,eps nonnegative.
    # M offdiag is nonnegative and no greater than 1-eta for eps<=delta.
    ee=Q(1,1000)
    M_slack=eta0
    design_derivative_norm=b0+ee
    perturbed_rosen=k0-54*design_derivative_norm**2/(M_slack**2*a0**2)
    assert rho0-ee>0 and rho0-eta0-ee>0 and perturbed_rosen>0
    out={'source_sha':'79b1a2a140754699a5a4c6d27aa469608e508bee',
         'symbolic_identity_checks':ids,
         'root_bracket':{'z_lower':str(zl),'z_upper':str(zh),'F_lower':str(FF(zl)),'F_upper':str(FF(zh))},
         'Rosen_margin_exact':str(margin),
         'canonical_local':{n:v.record() for n,v in base.items()},
         'nonlinear_cross_mapping_local':{'epsilon_exact':['0','1/1000'],
                                          'results':{n:v.record() for n,v in nonlin.items()},
                                          'scope':'Globally coherent PSD-preserving mapping; government sign certification LOCAL in depth only; unchanged SW game; no all-depth government-sign or arbitrary-kernel claim',
                                          'economic_domain_certificate':{'B_PSD_argument':'nonnegative sum of PSD H,X and Schur product H Hadamard X','M_row_slack_exact':str(M_slack),'Rosen_slack_exact':str(perturbed_rosen)},
                                          'mapping':'B_eps=(rho-eps)H+(1-rho)X+eps(H Hadamard X); distinct from an invalid unnormalized +eps H X perturbation'},
         'agenda_test':'canonical local grand slope positive while member slope negative; direct grand unanimity gains for sufficiently small g; no transfer theorem or first-best claim'}
    for name,obj in [('canonical',base),('nonlinear',nonlin)]:
        print('FRACTION INTERVAL PASS',name,{n:v.record()['display_only'] for n,v in obj.items()})
    Path('verification/stage14').mkdir(exist_ok=True)
    Path('verification/stage14/math_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS independent local identities, exact root bracket, two diagnostic tests')
if __name__=='__main__':main()
