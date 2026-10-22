"""Fresh Stage 11 local matrix audit; no production imports; numeric results are not intervals."""
import json,itertools
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np
import sympy as sy
from scipy.optimize import root,brentq
D,E,R,K=1.,.758,.9,.8505

def state(x,g,r):
 H=np.eye(3)
 if r=='SU':H[0,1]=H[1,0]=g
 if r=='IS':H[:]=g;np.fill_diagonal(H,1)
 X=(x[:,None]+x[None,:])/2;np.fill_diagonal(X,1)
 B=R*H+(1-R)*X;M=np.eye(3)+B-E*H
 q=np.linalg.solve(M,np.full(3,D));Ri=np.linalg.inv(M);EE=[]
 for j in range(3):
  A=np.zeros((3,3));A[j,:]=(1-R)/2;A[:,j]=(1-R)/2;A[j,j]=0;EE.append(A)
 qx=np.column_stack([-Ri@A@q for A in EE]);F=6*q*np.diag(qx)+K*(1-x);J=np.empty((3,3))
 for a in range(3):
  for b in range(3):
   qab=Ri@EE[a]@Ri@EE[b]@q+Ri@EE[b]@Ri@EE[a]@q
   J[a,b]=6*(qx[a,a]*qx[a,b]+q[a]*qab[a])-(K if a==b else 0)
 W=q@B@q/2+3*q*q-K*(1-x)**2/2
 return F,J,W,q,B,M,EE,qx

z=root(lambda x:state(x,0,'SW')[0],[.7]*3,tol=1e-12).x
F,J,W,q,B,M,EE,qx=state(z,0,'SW');assert max(abs(F))<1e-11
Eg=np.array([[0,R-E,0],[R-E,0,0],[0,0,0.]])
Bg=np.array([[0,R,0],[R,0,0],[0,0,0.]])
Ri=np.linalg.inv(M);qg=-Ri@Eg@q;Fg=[]
for a in range(3):
 qag=Ri@Eg@Ri@EE[a]@q+Ri@EE[a]@Ri@Eg@q
 Fg.append(6*(qg[a]*qx[a,a]+q[a]*qag[a]))
response=np.linalg.solve(J,-np.array(Fg))
csx=np.array([q@B@qx[:,a]+q@EE[a]@q/2 for a in range(3)])
WG=csx+6*q[0]*qx[0,:];WG[0]+=K*(1-z[0])
cs_g=q@B@qg+q@Bg@q/2
fixed=cs_g+6*q[0]*qg[0];endo=fixed+WG@response
alpha=2-E;beta=1-R;t=beta*z[0];P=alpha-t;L=alpha+2*t
C=beta*(E+2*t)/L**3;V=3*beta*(alpha-2*t)/(P*L**3)
assert np.max(abs(WG-np.array([-C,-C-V,-C-V])))<1e-12
loss=-WG@response;assert 0<fixed<loss
fd={}
for h in [1e-4,1e-5,1e-6]:
 def welfare(g,r):
  xx=root(lambda x:state(x,g,r)[0],z,tol=1e-12).x
  ff,j,w,*_=state(xx,g,r);assert max(abs(ff))<1e-10
  return w
 su=(welfare(h,'SU')-welfare(-h,'SU'))/(2*h)
 ii=(welfare(h,'IS')[0]-welfare(-h,'IS')[0])/(2*h)
 assert abs(ii-(2*su[0]+su[2]))<1e-7 and abs(su[0]-endo)<1e-7
 fd[str(h)]={'mu':su[0],'nu':su[2],'integrated':ii,'edge_identity_error':ii-2*su[0]-su[2]}
def ll(lam):return -WG@np.linalg.solve(-J+lam*np.eye(3),np.array(Fg))
lam=brentq(lambda x:ll(x)-fixed,0,5,xtol=1e-14);assert .93538<lam<.93539
assert all(ll(a)>ll(b)>0 for a,b in zip([0,.1,1,10],[.1,1,10,100]))
verts=[]
for bits in itertools.product([0,1],repeat=3):
 A=sy.eye(3)
 for i in range(3):
  for j in range(i):A[i,j]=A[j,i]=sy.Rational(bits[i]+bits[j],2)
 minors=[]
 for n in [1,2,3]:
  for inds in itertools.combinations(range(3),n):minors.append(A.extract(inds,inds).det())
 assert all(v>=0 for v in minors)
 verts.append({'x':bits,'principal_minors':[str(v) for v in minors]})
ea,rr,kk=Fr(379,500),Fr(9,10),Fr(1701,2000);aa=2-ea;bb=1-rr
rosen=kk-54*bb**2/(ea**2*aa**2);assert rosen>0
g,T=sy.symbols('g T')
m=(4+g)/(1+T*g)**2+sy.Rational(1,2);o=(1+g)/(1+T*g)**2+sy.Rational(7,2)
i=(sy.Rational(9,2)+3*g)/(1+2*T*g)**2
poly=14*T**4*g**3+(42*T**3+T**2)*g**2+T*(45*T-2)*g+16*T-2
assert sy.factor(i-o+g*poly/((1+T*g)**2*(1+2*T*g)**2))==0
assert sy.factor(m-sy.Rational(9,2)-g*(1-8*T-4*T*T*g)/(1+T*g)**2)==0
out={'scope':'Fresh local matrix differentiation and exact domain checks; not an all-depth interval certificate','sw_x':z.tolist(),'q':q.tolist(),'FOC_residual':max(abs(F)),'J':J.tolist(),'forcing':Fg,'response':response.tolist(),'national_gradient':WG.tolist(),'D':fixed,'loss':loss,'mu':endo,'lambda_cutoff_numeric':lam,'finite_difference_edge_identity':fd,'X_vertex_exact_psd':verts,'full_cube_Rosen_margin_exact':str(rosen),'full_cube_Rosen_margin_display':float(rosen),'network_face_polynomials':'exact PASS'}
Path('verification/stage11/independent_matrix_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
