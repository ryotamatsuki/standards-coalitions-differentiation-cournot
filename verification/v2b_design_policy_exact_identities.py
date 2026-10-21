"""V2b conditional comparative-static algebra verification (SymPy).
Reconstruct at the symmetric SW point BEFORE imposing symmetry of deviations.
Does not prove global uniqueness outside the canonical certified witness.
"""
import sympy as S
A, b, s, d, delta, k, rho = S.symbols('A b s d delta k rho', real=True)
P=A-s; L=A+2*s
I=S.eye(3); J=S.ones(3); q=S.Matrix([d/L]*3)
Minv=(I-s*J/L)/P
E=[]
for i in range(3):
    M=S.zeros(3)
    for j in range(3):
        if j!=i: M[i,j]=b/2; M[j,i]=b/2
    E.append(M)
Eg=S.zeros(3);Eg[0,1]=delta;Eg[1,0]=delta
qx=[-Minv*e*q for e in E]
qg=-Minv*Eg*q
qxx=lambda i,j: Minv*E[j]*Minv*E[i]*q + Minv*E[i]*Minv*E[j]*q
qxg=lambda i: Minv*Eg*Minv*E[i]*q+Minv*E[i]*Minv*Eg*q
ell=-k+6*b**2*d**2*(A-2*s)*(2*A+s)/(P**2*L**4)
h=3*b**2*d**2*(3*A-2*s)/(P*L**4)
p=6*delta*b*d**2*(A-2*s)*(2*A+s)/(P**2*L**4)
r=6*delta*b*d**2*(A**2-2*A*s+4*s**2)/(P**2*L**4)
check={
 'pseudo_gradient_diagonal':(6*(qx[0][0]**2+q[0]*qxx(0,0)[0])-k,ell),
 'pseudo_gradient_off_diagonal':(6*(qx[1][0]*qx[0][0]+q[0]*qxx(0,1)[0]),h),
 'member_policy_Fg':(6*(qg[0]*qx[0][0]+q[0]*qxg(0)[0]),p),
 'outsider_policy_Fg':(6*(qg[2]*qx[2][2]+q[2]*qxg(2)[2]),r),
 'member_outsider_gap':(p-r,6*delta*b*d**2*(A-3*s)/(P**2*L**3)),
 'sym_jacobian_eigen':(ell+2*h,-k+6*b**2*A*d**2*(5*A-8*s)/(P**2*L**4)),
}
B0=(1-s)*I+s*J
Bg=S.zeros(3);Bg[0,1]=rho;Bg[1,0]=rho
cs_g=(q.T*B0*qg)[0]+(q.T*Bg*q)[0]/2
cs_x=(q.T*B0*qx[0])[0]+(q.T*E[0]*q)[0]/2
pi_cross=6*q[0]*qx[1][0]
check.update({
 'direct_member_policy':(cs_g+6*q[0]*qg[0],d**2*(rho/L**2-2*delta*(1+2*s)/L**3-6*delta*A/(P*L**3))),
 'consumer_design':(cs_x,-b*d**2*(2-A+2*s)/L**3),
 'rival_profit_design':(pi_cross,-3*b*d**2*(A-2*s)/(P*L**3)),
})
y,g=S.symbols('y g',real=True)
t=delta*g+b*y
F=k*(1-y)-6*b*A*d**2/((A-t)*(A+2*t)**3)
G=6*b*A*d**2*(5*A-8*t)/((A-t)**2*(A+2*t)**4)
check.update({
 'IS_Fg':(S.diff(F,g),delta*G),
 'IS_Fy':(S.diff(F,y),-k+b*G),
 'IS_Fk':(S.diff(F,k),1-y),
 'IS_Fd':(S.diff(F,d),-12*b*A*d/((A-t)*(A+2*t)**3)),
})
for label,(lhs,rhs) in check.items():
    assert S.cancel(lhs-rhs)==0,label
    print('PASS',label)
print('PASS all exact symbolic identities; inequality signs require stated positivity assumptions.')
