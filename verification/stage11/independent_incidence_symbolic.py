#!/usr/bin/env python3
"""Exact audit from inverse-matrix derivatives; no historical evaluator imported."""
import json
import sympy as s

a,b,t,d,k,delta,rho=s.symbols('alpha beta t d kappa delta rho')
P=a-t; L=a+2*t
R=(s.eye(3)-t/L*s.ones(3))/P
q=s.ones(3,1)*d/L
B=(1-t)*s.eye(3)+t*s.ones(3)
E=[]
for j in range(3):
    ej=s.zeros(3)
    for v in range(3):
        if v!=j: ej[j,v]=ej[v,j]=b/2
    E.append(ej)
qx=[-R*ej*q for ej in E]
Q=s.zeros(3);Q[0,1]=Q[1,0]=delta
Bg=s.zeros(3);Bg[0,1]=Bg[1,0]=rho
qg=-R*Q*q
tests={}
def check(name,expression):
    tests[name]=s.factor(expression)==0
    assert tests[name],(name,s.factor(expression))
C=b*d**2*(2-a+2*t)/L**3
V=3*b*d**2*(a-2*t)/(P*L**3)
csx=[]
for j in range(3):
    cx=(qx[j].T*B*q)[0]+(q.T*E[j]*q)[0]/2
    csx.append(cx)
    check('CS_x'+str(j),cx+C)
    # The own-profit FOC exactly cancels own operating-profit/cost derivative.
    actual=cx if j==0 else cx+6*q[0]*qx[j][0]
    check('W_A_x'+str(j),actual+(C if j==0 else C+V))
J=s.zeros(3);f=s.zeros(3,1)
for i in range(3):
    for j in range(3):
        qij=R*E[j]*R*E[i]*q+R*E[i]*R*E[j]*q
        J[i,j]=s.factor(6*(qx[j][i]*qx[i][i]+q[i]*qij[i])-(k if i==j else 0))
    qig=R*Q*R*E[i]*q+R*E[i]*R*Q*q
    f[i]=s.factor(6*(qg[i]*qx[i][i]+q[i]*qig[i]))
ell=-k+6*b*b*d*d*(a-2*t)*(2*a+t)/(P*P*L**4)
chi=3*b*b*d*d*(3*a-2*t)/(P*L**4)
p=6*delta*b*d*d*(a-2*t)*(2*a+t)/(P*P*L**4)
r=6*delta*b*d*d*(a*a-2*a*t+4*t*t)/(P*P*L**4)
for i in range(3):
    for j in range(3): check('J_'+str(i)+str(j),J[i,j]-(ell if i==j else chi))
    check('forcing_'+str(i),f[i]-(p if i<2 else r))
D=rho*d*d/L**2-delta*d*d/L**3*(2*(1+2*t)+6*a/P)
actual=(qg.T*B*q)[0]+(q.T*Bg*q)[0]/2+6*q[0]*qg[0]
check('fixed_member_D',actual-D)
u,v=s.symbols('u v')
check('loss_plus_sign',(-C*u-(C+V)*(u+v))+C*(2*u+v)+V*(u+v))
print(json.dumps({'scope':'exact local algebra at symmetric SW, not full-depth Nash existence','sympy':s.__version__,'tests':tests,'all_pass':all(tests.values())},indent=2))
