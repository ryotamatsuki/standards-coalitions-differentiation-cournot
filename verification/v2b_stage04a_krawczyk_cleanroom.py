#!/usr/bin/env python3
"""Stage 4A adversarial clean rederivation: interval Krawczyk certificates.
No calls to previous V2b computational modules. Exact-rational box endpoints.
Not formal proof-assistant verified; inspect algorithm/third-party arithmetic separately.
"""
from fractions import Fraction as F
from scipy.optimize import root, brentq
from mpmath import iv
import sympy as s
import numpy as np
from time import perf_counter
iv.dps=35
# Independently derive system via bilateral symmetric Cournot linear equations.
u,v,g,eta,rho,kappa=s.symbols('u v g eta rho kappa',real=True)
y=s.symbols('y',real=True)
A=2-eta; b=1-rho
m=(rho-eta)*g+b*u
n=b*(u+v)/2
D=A*(A+m)-2*n*n
qa=(A-n)/D; qc=(A+m-2*n)/D
# 3x3 inverse M in A/B symmetric basis, derived via basis decomposition
r11=(A/D+1/(A-m))/2
r12=(A/D-1/(A-m))/2
r13=-n/D
# unilateral change by firm A (others held fixed), firm C
dqa=-b/2*(r11*(qa+qc)+r12*qa+r13*qa)
dqc=-b*((A+m)*qa-n*qc)/D
fa=kappa*(1-u)+6*qa*dqa
fc=kappa*(1-v)+6*qc*dqc
B12=rho*g+b*u
B13=b*(u+v)/2
cs=(1+B12)*qa**2+qc**2/2+2*B13*qa*qc
wa=cs+3*qa**2-kappa*(1-u)**2/2
wc=cs+3*qc**2-kappa*(1-v)**2/2
S=[fa,fc,wa,wc]+[s.diff(z,t) for z in (fa,fc,wa,wc) for t in (u,v,g)]
SU=s.lambdify((u,v,g,eta,rho,kappa),S,modules='math',cse=True)
SUn=s.lambdify((u,v,g,eta,rho,kappa),(fa,fc),modules='numpy',cse=True)
M=(rho-eta)*g+b*y
QI=1/(A+2*M)
# unilateral deviation: inverse 3x3 equicorrelated at symmetric point
# q own derivative = -b * A / [(A-M)*(A+2*M)**2]; f= 6q dq + k(1-y)
fi=kappa*(1-y)-6*b*A/((A-M)*(A+2*M)**3)
wi=(s.Rational(9,2)+3*(rho*g+b*y))*QI**2-kappa*(1-y)**2/2
I=[fi,wi,s.diff(fi,y),s.diff(fi,g),s.diff(wi,y),s.diff(wi,g)]
IS=s.lambdify((y,g,eta,rho,kappa),I,modules='math',cse=True)
ISn=s.lambdify((y,g,eta,rho,kappa),fi,modules='numpy',cse=True)
E=iv.mpf(379)/500;R=iv.mpf(9)/10;K=iv.mpf(1701)/2000

# Exact rational endpoints in all boxes; denominator arithmetic is exact prior to interval rounding.
def rect(a,b=None):
    if b is None: b=a
    a=F(a);b=F(b)
    return iv.mpf(a.numerator)/a.denominator if a==b else iv.mpf([a.numerator*b.denominator,b.numerator*a.denominator])/(a.denominator*b.denominator)

def su(U,V,G):return SU(U,V,G,E,R,K)
def si(Y,G):return IS(Y,G,E,R,K)
def pos(x):return x.a>0
def neg(x):return x.b<0

def cr(gfloat):
    a=root(lambda z:SUn(z[0],z[1],gfloat,.758,.9,.8505),[.735,.72],tol=1e-12)
    assert np.max(abs(np.array(a.fun)))<2e-11
    yy=brentq(lambda z:ISn(z,gfloat,.758,.9,.8505),.60,.95,xtol=1e-14)
    return a.x[0],a.x[1],yy

# Krawczyk method: for every g in G, existence unique root in X by Krawczyk inclusion
# K=z0-C f(z0,G) + (I-C F'(X,G))(X-z0), with rational C approximate J^-1.
# All inclusion calculations are interval operations. C quality only affects proof cost.
def krawczyk_SU(G,uv,eps):
    mid=np.array(uv[:2])
    cz=[F(str(round(float(z),12))) for z in mid]
    U=rect(cz[0]-eps,cz[0]+eps);V=rect(cz[1]-eps,cz[1]+eps)
    w=su(U,V,G)
    J=[[w[4],w[5]],[w[7],w[8]]]
    det=J[0][0]*J[1][1]-J[0][1]*J[1][0]
    if not(pos(det) or neg(det)):return None
    gc=(float(G.a)+float(G.b))/2
    J0=np.array([[float(si0.a) for si0 in [su(rect(cz[0]),rect(cz[1]),rect(F(str(round(gc,12)))))[k] for k in (4,5)]],
                 [float(si0.a) for si0 in [su(rect(cz[0]),rect(cz[1]),rect(F(str(round(gc,12)))))[k] for k in (7,8)]]])
    inv=np.linalg.inv(J0)
    C=[[rect(F(str(round(float(inv[i,j]),12)))) for j in range(2)] for i in range(2)]
    f0=su(rect(cz[0]),rect(cz[1]),G)[:2]
    Krect=[]
    Xdelta=[U-rect(cz[0]),V-rect(cz[1])]
    for i in range(2):
        z=rect(cz[i])-(C[i][0]*f0[0]+C[i][1]*f0[1])
        for j in range(2):
            t=(iv.mpf(1) if i==j else iv.mpf(0))-sum(C[i][k]*J[k][j] for k in range(2))
            z+=t*Xdelta[j]
        Krect.append(z)
    if not all(Krect[i].a> (U if i==0 else V).a and Krect[i].b<(U if i==0 else V).b for i in range(2)):
        return None
    return (U,V,w,det)

def krawczyk_IS(G,y0,eps):
    cy=F(str(round(float(y0),12)))
    Y=rect(cy-eps,cy+eps)
    w=si(Y,G)
    if not neg(w[2]):return None
    f0=si(rect(cy),G)[0]
    z=rect(cy)-f0/w[2]
    if not(z.a>Y.a and z.b<Y.b):return None
    return (Y,w)

def slopes_SU(w):
    det=w[4]*w[8]-w[5]*w[7]
    uP=(-w[6]*w[8]+w[5]*w[9])/det
    vP=(-w[4]*w[9]+w[6]*w[7])/det
    return w[12]+w[10]*uP+w[11]*vP, w[15]+w[13]*uP+w[14]*vP

def proof():
    max_S=-1e10; max_C=-1e10
    accepted=0;split=0
    stack=[(F(i,1000),F(i+1,1000)) for i in range(1000)]
    tic=perf_counter()
    while stack:
        p,q=stack.pop();G=rect(p,q)
        middle=cr(float((p+q)/2))
        eps=F(1,5000)
        su_cert=krawczyk_SU(G,middle,eps)
        is_cert=krawczyk_IS(G,middle[2],eps)
        if su_cert and is_cert:
            sg,og=slopes_SU(su_cert[2])
            z=is_cert[1]
            ider=z[5]-z[4]*z[3]/z[2]
            cg=ider-og
            if neg(sg) and neg(cg):
                accepted+=1;max_S=max(max_S,float(sg.b));max_C=max(max_C,float(cg.b));continue
        split+=1
        if split>20000: raise AssertionError(f'Split budget exceed at g={p},{q}; {accepted=}')
        mid=(p+q)/2
        stack.append((p,mid));stack.append((mid,q))
    print('KRAWCZYK SIGN CERT SUCCESS', 'accepted=',accepted,'splits=',split,'max upper derivatives=',max_S,max_C,'seconds=',perf_counter()-tic,flush=True)

def certify_frozen():
    yl=F(71859270731,10**11); yh=F(71859270734,10**11)
    g0=rect(F(0))
    assert pos(si(rect(yl),g0)[0]) and neg(si(rect(yh),g0)[0])
    Y=rect(yl,yh)
    frozenSW=su(Y,Y,g0)[2]
    point=rect(F(1,20))
    member,outsider=su(Y,Y,point)[2:4]
    international=si(Y,point)[1]
    assert pos(international-outsider), ('C would reject',international-outsider)
    assert pos(international-member), ('A or B would reject accession')
    assert pos(international-frozenSW), ('A would prefer SW')
    bestSU= -1e9
    for j in range(500):
        G=rect(F(j,500),F(j+1,500))
        memberSU=su(Y,Y,G)[2]
        bestSU=max(bestSU,float(memberSU.b))
        assert international.a>memberSU.b, ('some SU payoff potentially larger',j)
    print('FROZEN CERT SUCCESS',
          'C lower gain=',float((international-outsider).a),
          'IS lower=',float(international.a),
          'SW upper=',float(frozenSW.b),
          'SU upper=',bestSU,flush=True)

def independent_payoff_attack():
    rng=np.random.default_rng(20261021)
    largest=0.
    for _ in range(200):
        gg=float(rng.uniform(0,1));uu=float(rng.uniform(.05,.95));vv=float(rng.uniform(.05,.95))
        x=np.array([uu,uu,vv]);
        def prof(i,z):
            xx=x.copy();xx[i]=z
            H=np.eye(3);H[0,1]=H[1,0]=gg
            X=np.eye(3)
            for aa in range(3):
                for bb in range(aa+1,3):X[aa,bb]=X[bb,aa]=(xx[aa]+xx[bb])/2
            MM=np.eye(3)+(.9-.758)*H+.1*X
            q=np.linalg.solve(MM,np.ones(3))
            return 3*q[i]**2-.8505*(1-z)**2/2
        h=1e-6
        arr=SUn(uu,vv,gg,.758,.9,.8505)
        for i in (0,2):
            fd=(prof(i,x[i]+h)-prof(i,x[i]-h))/(2*h)
            largest=max(largest,abs(fd-arr[0 if i==0 else 1]))
    assert largest<1e-7,largest
    print('INDEPENDENT PROFIT DEVIATION PASS: max FOC error',largest,flush=True)

if __name__=='__main__':
    independent_payoff_attack()
    proof()
    certify_frozen()
    print('PASS: adversarial stage 4A independent method, all g∈[0,1]')
