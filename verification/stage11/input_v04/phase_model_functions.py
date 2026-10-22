import numpy as np, json, time, os
from scipy.optimize import root, root_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch

RHO=0.9
DVAL=1.0

def H_matrix(g, regime):
    H=np.eye(3)
    if regime=='SU': H[0,1]=H[1,0]=g
    elif regime=='IS': H=np.full((3,3),g); np.fill_diagonal(H,1.)
    return H

def X_from_vec(x):
    X=np.eye(3)
    for i in range(3):
        for j in range(i+1,3):
            X[i,j]=X[j,i]=(x[i]+x[j])/2
    return X

def welfare(x,g,regime,eta,kappa):
    H=H_matrix(g,regime)
    B=RHO*H+(1-RHO)*X_from_vec(x)
    M=np.eye(3)+B-eta*H
    q=np.linalg.solve(M,np.ones(3)*DVAL)
    CS=0.5*q@B@q
    Pi=3*q*q-kappa*(1-x)**2/2
    return CS+Pi

def foc(x,g,regime,eta,kappa):
    H=H_matrix(g,regime)
    B=RHO*H+(1-RHO)*X_from_vec(x)
    M=np.eye(3)+B-eta*H
    q=np.linalg.solve(M,np.ones(3)*DVAL)
    out=np.empty(3)
    beta=1-RHO
    for a in range(3):
        E=np.zeros((3,3))
        for b in range(3):
            if b!=a: E[a,b]=E[b,a]=beta/2
        dq=np.linalg.solve(M,-E@q)
        out[a]=6*q[a]*dq[a]+kappa*(1-x[a])
    return out

def solve_sw(eta,kappa):
    def f(z): return foc(np.array([z,z,z]),0,'SW',eta,kappa)[0]
    xs=np.linspace(1e-6,1-1e-6,21)
    vals=[f(x) for x in xs]
    for i in range(len(xs)-1):
        if vals[i]*vals[i+1]<0:
            sol=root_scalar(f, bracket=[xs[i],xs[i+1]], method='brentq')
            return float(sol.root), sol.converged
    sol=root(lambda zz: np.array([f(zz[0])]), [0.72])
    z=float(sol.x[0]); return z, sol.success and 0<z<1 and abs(f(z))<1e-7

def solve_is(g,eta,kappa,guess):
    def f(y): return foc(np.array([y,y,y]),g,'IS',eta,kappa)[0]
    sol=root(lambda yy: np.array([f(yy[0])]), [guess])
    y=float(sol.x[0]); return y, sol.success and 0<y<1 and abs(f(y))<1e-6

def solve_su(g,eta,kappa,guess):
    def f(v):
        u,w=v
        ff=foc(np.array([u,u,w]),g,'SU',eta,kappa)
        return np.array([ff[0],ff[2]])
    sol=root(f, guess)
    u,w=map(float,sol.x); res=f(sol.x)
    return (u,w), sol.success and 0<u<1 and 0<w<1 and np.max(np.abs(res))<1e-6

codes={'SW':0,'SU':1,'IS':2,'UN':3}

def classify(eta,kappa,ggrid):
    z,ok=solve_sw(eta,kappa)
    if not ok: return 'UN','UN',None
    s=welfare(np.array([z,z,z]),0,'SW',eta,kappa)[0]
    y_guess=z; uv_guess=(z,z)
    GF=[]; GN=[]; TF=[]; TN=[]; tol=1e-8
    for g in ggrid:
        Wsu=welfare(np.array([z,z,z]),g,'SU',eta,kappa); Wis=welfare(np.array([z,z,z]),g,'IS',eta,kappa)
        mF,oF,iF=Wsu[0],Wsu[2],Wis[0]
        if iF>=max(s,mF,oF)-tol: TF.append('IS'); GF.append(iF)
        elif mF>=s-tol: TF.append('SU'); GF.append(mF)
        else: TF.append('SW'); GF.append(s)
        y,oky=solve_is(g,eta,kappa,y_guess); uv,okuv=solve_su(g,eta,kappa,uv_guess)
        if not (oky and okuv):
            TN.append('UN'); GN.append(np.nan); continue
        y_guess=y; uv_guess=uv
        iN=welfare(np.array([y,y,y]),g,'IS',eta,kappa)[0]
        Wsun=welfare(np.array([uv[0],uv[0],uv[1]]),g,'SU',eta,kappa)
        mN,oN=Wsun[0],Wsun[2]
        if iN>=max(s,mN,oN)-tol: TN.append('IS'); GN.append(iN)
        elif mN>=s-tol: TN.append('SU'); GN.append(mN)
        else: TN.append('SW'); GN.append(s)
    def choose(G,T):
        G=np.asarray(G)
        if np.any(~np.isfinite(G)): return 'UN'
        mx=np.max(G)
        if mx<=s+1e-6: return 'SW'
        idx=np.where(np.abs(G-mx)<=1e-6)[0]
        labs=set(np.asarray(T)[idx])
        return list(labs)[0] if len(labs)==1 else 'UN'
    return choose(GF,TF), choose(GN,TN), z

