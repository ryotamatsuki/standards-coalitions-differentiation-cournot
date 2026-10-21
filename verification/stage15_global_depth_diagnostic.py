#!/usr/bin/env python3
"""Independent finite-depth diagnostic for V2b lambda extension.
FLOATING POINT TEST ONLY. Not a global interval certificate.
Standard library only; no imports from prior V2b math scripts.
"""
import json
ETA=379/500;RHO=9/10;KAPPA=1701/2000
BETA=1-RHO;DELTA=RHO-ETA
def solve3(a,b):
    m=[list(map(float,row))+[float(v)] for row,v in zip(a,b)]
    for j in range(3):
        k=max(range(j,3),key=lambda i:abs(m[i][j]))
        m[j],m[k]=m[k],m[j]
        assert abs(m[j][j])>1e-13
        z=m[j][j]
        for h in range(j,4):m[j][h]/=z
        for i in range(3):
            if i!=j:
                fac=m[i][j]
                for h in range(j,4):m[i][h]-=fac*m[j][h]
    return [m[i][3] for i in range(3)]
def link(i,j,policy,g):
    if i==j:return 1.
    return g if policy=='IS' or (policy=='SU' and {i,j}=={0,1}) else 0.
def qty(x,policy,g):
    h=[[link(i,j,policy,g) for j in range(3)] for i in range(3)]
    b=[[1. if i==j else RHO*h[i][j]+BETA*(x[i]+x[j])/2 for j in range(3)] for i in range(3)]
    m=[[(1. if i==j else 0.)+b[i][j]-ETA*h[i][j] for j in range(3)] for i in range(3)]
    return solve3(m,[1,1,1]),b,m
def foc(x,policy,g,lam,z):
    q,b,m=qty(x,policy,g)
    out=[]
    for i in range(3):
        eq=[BETA*q[i]/2 if j!=i else BETA*sum(q[k] for k in range(3) if k!=i)/2 for j in range(3)]
        qi=solve3(m,[-v for v in eq])[i]
        out.append(6*q[i]*qi+KAPPA*(1-x[i])-lam*(x[i]-z))
    return out
def design(policy,g,lam,z):
    x=[z]*3
    for _ in range(35):
        f=foc(x,policy,g,lam,z);err=max(abs(v) for v in f)
        if err<1e-11:
            assert all(0<v<1 for v in x)
            return x
        step=1e-6;jac=[[] for _ in range(3)]
        for j in range(3):
            xp=x[:];xm=x[:];xp[j]+=step;xm[j]-=step
            fp=foc(xp,policy,g,lam,z);fm=foc(xm,policy,g,lam,z)
            for i in range(3):jac[i].append((fp[i]-fm[i])/(2*step))
        dx=solve3(jac,[-v for v in f]);rate=1.
        while rate>1e-8:
            trial=[x[i]+rate*dx[i] for i in range(3)]
            if all(0<t<1 for t in trial) and max(abs(v) for v in foc(trial,policy,g,lam,z))<err:
                x=trial;break
            rate/=2
        else:raise RuntimeError((policy,g,lam,x,err))
    raise RuntimeError('no equilibrium convergence')
def welfare(policy,g,lam,z):
    x=design(policy,g,lam,z);q,b,m=qty(x,policy,g)
    cs=sum(q[i]*b[i][j]*q[j] for i in range(3) for j in range(3))/2
    return [cs+3*q[i]**2-KAPPA*(1-x[i])**2/2-lam*(x[i]-z)**2/2 for i in range(3)]
def margins(g,lam,z,s):
    su=welfare('SU',g,lam,z);ii=welfare('IS',g,lam,z)
    return {'member_vs_SW':su[0]-s,'outsider_join':ii[2]-su[2],'incumbent_join':ii[0]-su[0],'grand_vs_SW':ii[0]-s}
def ceiling(lam,z,s):
    low=1e-5;hi=1.
    if margins(low,lam,z,s)['outsider_join']<=0:return None
    if margins(hi,lam,z,s)['outsider_join']>=0:return None
    for _ in range(37):
        mid=(low+hi)/2
        if margins(mid,lam,z,s)['outsider_join']>0:low=mid
        else:hi=mid
    m=margins(.95*low,lam,z,s)
    assert m['outsider_join']>0 and m['incumbent_join']>0 and m['grand_vs_SW']>0 and m['member_vs_SW']>0
    return {'first_outsider_vote_root':low,'strict_offer_depth':.95*low,'grand_gain_at_strict_offer':m['grand_vs_SW']}
def main():
    lo,hi=.71,.73
    for _ in range(55):
        mid=(lo+hi)/2
        if foc([mid]*3,'SW',0,0,mid)[0]>0:lo=mid
        else:hi=mid
    z=(lo+hi)/2
    assert .71859270<z<.71859272
    s=welfare('SW',0,0,z)[0]
    res={'scope':'floating point, first-crossing diagnostic; no proof of absence of disconnected feasibility regions','z':z,'SW_national_welfare':s,'cases':{}}
    for lam in (.94,1.,1.5,2.,5.,10.):
        v=ceiling(lam,z,s)
        assert v is not None,lam
        res['cases'][str(lam)]=v
        print('lambda',lam,v)
    assert abs(res['cases']['1.0']['first_outsider_vote_root']-.00279541)<2e-6
    assert abs(res['cases']['2.0']['first_outsider_vote_root']-.02953296)<2e-6
    assert abs(res['cases']['5.0']['first_outsider_vote_root']-.05433321)<2e-6
    print('PASS independent finite-depth equilibrium and voting diagnostic (NOT rigorous all-depth certification)')
    print(json.dumps(res,indent=2))
if __name__=='__main__':main()
