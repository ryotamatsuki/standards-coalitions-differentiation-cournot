from fractions import Fraction as R
from itertools import product
import sympy as s
alpha=R(621,500); beta=R(1,10);D=R(379,500);k=R(1701,2000)
q1=beta/(D*alpha);q2=2*beta**2/(D**2*alpha)
h=6*(q1*q1+q2/alpha)
print('CURVATURE',dict(q1=str(q1),q1_float=float(q1),q2_float=float(q2),h=str(h),h_float=float(h),margin_float=float(k-3*h)))
# B affine in x and g; PSD cone convex, so exact vertex checks certify full domain.
for regime in ['SW','SU','IS']:
 dets=[]; minors=[]
 for bits in product([0,1],repeat=4):
  x=bits[:3];g=bits[3];H=s.eye(3);X=s.eye(3)
  for i in range(3):
   for j in range(i):
    H[i,j]=H[j,i]=g if regime=='IS' or (regime=='SU' and {i,j}=={0,1}) else 0
    X[i,j]=X[j,i]=s.Rational(x[i]+x[j],2)
  B=s.Rational(9,10)*H+s.Rational(1,10)*X
  vals=[B.extract(I,I).det() for I in [(0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2)]]
  dets.append(B.det());minors+=vals
 print('PSD_vertices',regime,'min_det',min(dets),'min_all_principal',min(minors))
x,g=s.symbols('x g');a=s.Rational(621,500);b=s.Rational(1,10);t=s.Rational(71,500)*g+b*x
M=s.ones(3)*t+s.eye(3)*(a-t);q=M.inv()*s.ones(3,1);Mi=s.Matrix([[0,b/2,b/2],[b/2,0,0],[b/2,0,0]])
fi=s.factor(6*q[0]*(-M.inv()*Mi*q)[0]+s.Rational(1701,2000)*(1-x))
expected=s.Rational(1701,2000)*(1-x)-6*b*a/((a-t)*(a+2*t)**3)
print('IS_FOC_difference',s.factor(fi-expected))
