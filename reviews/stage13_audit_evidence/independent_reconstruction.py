"""Audit implementation from manuscript equations, no project imports.
Floating-point diagnostics are NOT an interval certificate.
"""
import json, itertools
from fractions import Fraction as R
import numpy as np
import scipy
from scipy.optimize import root, minimize_scalar

eta,rho,kappa=379/500,9/10,1701/2000
alpha,beta=2-eta,1-rho
def primitives(x,S,g,p=1):
    H=np.eye(3)
    for i,j in itertools.combinations(range(3),2):
        H[i,j]=H[j,i]=g if S=='IS' or (S=='SU' and (i,j)==(0,1)) else 0
    xp=np.asarray(x)**p
    X=(xp[:,None]+xp[None,:])/2
    np.fill_diagonal(X,1.)
    B=rho*H+beta*X
    M=np.eye(3)+B-eta*H
    q=np.linalg.solve(M,np.ones(3))
    return H,B,M,q
def outcome(x,S,g,p=1):
    H,B,M,q=primitives(x,S,g,p)
    dq=np.empty((3,3)); Ms=[]
    for j in range(3):
        Mj=np.zeros((3,3))
        for t in range(3):
            if t!=j: Mj[j,t]=Mj[t,j]=beta*p*x[j]**(p-1)/2
        Ms.append(Mj)
        dq[:,j]=-np.linalg.solve(M,Mj@q)
    F=6*q*np.diag(dq)+kappa*(1-np.asarray(x))
    cost=kappa*(1-np.asarray(x))**2/2
    CS=q@B@q/2
    profits=3*q*q-cost
    W=CS+profits
    return dict(x=list(x),q=q.tolist(),F=F.tolist(),CS=CS,profits=profits.tolist(),W=W.tolist())
def equilibrium(S,g,p=1,guess=None):
    guess=np.array([.72]*3 if p==1 else [.61]*3) if guess is None else guess
    sol=root(lambda x:outcome(x,S,g,p)['F'],guess,tol=1e-11)
    if np.linalg.norm(sol.fun,np.inf)>1e-10: raise RuntimeError(str(sol))
    return outcome(sol.x,S,g,p)

report={'method':'independent numpy matrix implementation; diagnostic not proof','versions':{'numpy':np.__version__,'scipy':scipy.__version__}}
for p in [1,2]:
    sw=equilibrium('SW',0,p); fixed=np.array(sw['x']); s=sw['W'][0]
    data={'SW':sw,'depths':{}}
    for g in [.05,.005]:
        su=equilibrium('SU',g,p); Is=equilibrium('IS',g,p)
        suf=outcome(fixed,'SU',g,p); Isf=outcome(fixed,'IS',g,p)
        data['depths'][str(g)]={'SU':su,'IS':Is,'frozen_SU':suf,'frozen_IS':Isf,
            'endogenous_margins':[su['W'][0]-s,Is['W'][0]-su['W'][2],Is['W'][0]-s],
            'frozen_margins':[suf['W'][0]-s,Isf['W'][0]-suf['W'][2],Isf['W'][0]-s]}
    # Alternative equilibria search: full asymmetric starting vectors, all regimes/depth endpoints.
    max_root_deviation=0.; attempts=0
    for S in ['SW','SU','IS']:
        for g in [0,.05,.5,1]:
            target=np.array(equilibrium(S,g,p)['x'])
            for guess in itertools.product([.05,.5,.95],repeat=3):
                other=equilibrium(S,g,p,np.array(guess)); attempts+=1
                max_root_deviation=max(max_root_deviation,float(np.max(abs(np.array(other['x'])-target))))
    data['asymmetric_root_search']={'attempts':attempts,'max_deviation':max_root_deviation,'limitation':'root search, not boundary Nash enumeration or global proof'}
    report['linear' if p==1 else 'quadratic']=data

# Reconstruct the local welfare chain; each partial uses primitive outcomes, own FOC independently visible.
eps=1e-5
sw=equilibrium('SW',0); x=np.array(sw['x'])
xprime=(np.array(equilibrium('SU',eps)['x'])-np.array(equilibrium('SU',-eps)['x']))/(2*eps)
direct=(np.array(outcome(x,'SU',eps)['W'])-np.array(outcome(x,'SU',-eps)['W']))/(2*eps)
DW=np.column_stack([(np.array(outcome(x+np.eye(3)[j]*eps,'SU',0)['W'])-np.array(outcome(x-np.eye(3)[j]*eps,'SU',0)['W']))/(2*eps) for j in range(3)])
report['local_SU']={'xprime':xprime.tolist(),'direct_Wprime':direct.tolist(),'W_design_partials':DW.tolist(),'indirect_contributions_A':(DW[0]*xprime).tolist(),'A_total':float(direct[0]+DW[0]@xprime)}

# Exact curvature bound in manuscript.
a,b,D,k=R(621,500),R(1,10),R(379,500),R(1701,2000)
h=6*((b/(D*a))**2+2*b*b/(D*D*a*a))
report['exact_curvature']={'qprime':str(b/(D*a)),'qprime_float':float(b/(D*a)),'qsecond':str(2*b*b/(D*D*a)),'qsecond_float':float(2*b*b/(D*D*a)),'h':str(h),'h_float':float(h),'margin':str(k-3*R(203092,1000000)),'margin_float':float(k-3*R(203092,1000000))}

# PSD of B,H on whole cube: affine in each variable; convex combination of vertices.
def det3(A):
    return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
psd=[]
for S in ['SW','SU','IS']:
    minors=[]
    for g,*x in itertools.product([R(0),R(1)],repeat=4):
        B=[[R(int(i==j)) for j in range(3)] for i in range(3)]
        for i,j in itertools.combinations(range(3),2):
            hij=g if S=='IS' or (S=='SU' and (i,j)==(0,1)) else R(0)
            B[i][j]=B[j][i]=R(9,10)*hij+R(1,10)*(x[i]+x[j])/2
        ms=[B[i][i] for i in range(3)]+[B[i][i]*B[j][j]-B[i][j]**2 for i,j in itertools.combinations(range(3),2)]+[det3(B)]
        assert min(ms)>=0
        minors.extend(ms)
    psd.append({'regime':S,'vertices':16,'minimum_principal_minor':str(min(minors))})
report['PSD_vertex_proof']=psd
print(json.dumps(report,indent=2))
