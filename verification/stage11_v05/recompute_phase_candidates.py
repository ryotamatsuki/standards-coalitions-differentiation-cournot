#!/usr/bin/env python3
"""Stage11 v0.5: reproducible numerical candidate phase map, not a certified theorem.

Run in repository root with numpy scipy:
 python verification/stage11_v05/recompute_phase_candidates.py

The geometry is the existing inherited-depth bilateral-first V2b model.
Uses the archived *unchanged* original three-firm Nash and welfare evaluator.
Relative to the flawed v0.4 mesh, probes logarithmic g near zero and
brackets observed vote-margin sign changes. Continuous exact root-exclusion
over every parameter/depth cell is NOT proved; label SW as 'no offer found'.
"""
from __future__ import annotations
import sys, json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq, minimize_scalar
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"verification"/"stage11"/"input_v04"))
from phase_model_functions import solve_sw,solve_is,solve_su,welfare

def evaluate_factory(eta,kappa):
    z,valid=solve_sw(eta,kappa)
    if not valid: return None,None
    s=float(welfare(np.array([z,z,z]),0,"SW",eta,kappa)[0])
    cache={}
    def ev(g,panel):
        g=float(g);key=(round(g,15),panel)
        if key in cache:return cache[key]
        if panel=="F":
            u=v=y=z;ok=True
        else:
            y,oky=solve_is(g,eta,kappa,z)
            (u,v),okv=solve_su(g,eta,kappa,(z,z))
            ok=oky and okv
        if not ok:
            cache[key]={"ok":False};return cache[key]
        ws=welfare(np.array([u,u,v]),g,"SU",eta,kappa)
        wi=welfare(np.array([y,y,y]),g,"IS",eta,kappa)
        m,o,i=map(float,(ws[0],ws[2],wi[0]))
        cache[key]={"ok":True,"g":g,"ms":m-s,"io":i-o,
                    "im":i-m,"is":i-s}
        return cache[key]
    return ev,s

def classify(eta,kappa,panel):
    ev,s=evaluate_factory(eta,kappa)
    if ev is None:return "UN",None
    G=sorted(set(np.r_[0.,np.geomspace(1e-6,.01,23),np.linspace(.01,1,71)]))
    vals=[ev(g,panel) for g in G]
    if any(not v["ok"] for v in vals):return "UN",None
    t=4e-13*max(1.,abs(s))
    candidates=[]
    def record(g):
        v=ev(g,panel)
        if not v["ok"]:return
        if min(v["is"],v["im"],v["io"])>t and v["is"]>1e-11:
            candidates.append((v["is"],"IS",g,v))
        elif v["ms"]>t and min(v["io"],v["im"]) < -t:
            candidates.append((v["ms"],"SU",g,v))
    for g in G[1:]:record(g)
    # Search for roots of individually binding consent inequalities.
    for key in ("io","im","is","ms"):
        for va,vb in zip(vals[:-1],vals[1:]):
            if va[key]*vb[key]<0:
                try:
                    rt=brentq(lambda g:ev(g,panel)[key],va["g"],vb["g"],xtol=1e-12)
                    for gp in (max(1e-10,rt-1e-6),min(1,rt+1e-6),max(1e-10,rt*.99),min(1,rt*1.01)):
                        record(gp)
                except (ValueError,RuntimeError):
                    return "UN",None
    if candidates:
        candidates.sort(reverse=True)
        best=candidates[0]
        if any(c[1]!=best[1] and best[0]-c[0]<1e-8 for c in candidates):
            return "UN",None
        return best[1],best[2]
    # Never declare SW if the local incident and outsider voting slopes
    # are strictly positive but feasible windows were not resolved.
    vs=[ev(g,panel) for g in (1e-5,1e-4)]
    if min(v["ms"]/v["g"] for v in vs)>1e-9 and min(v["io"]/v["g"] for v in vs)>1e-9:
        return "UN",None
    return "SW",0.

def run():
    from collections import Counter
    K=np.linspace(.70,1.05,41);E=np.linspace(.742,.772,41)
    labels=np.full((2,41,41),3,dtype=np.uint8)
    code={"SW":0,"SU":1,"IS":2,"UN":3}
    ledger=[]
    for j,eta in enumerate(E):
        for i,kappa in enumerate(K):
            for panel,pi in [("F",0),("N",1)]:
                lab,g=classify(float(eta),float(kappa),panel)
                labels[pi,j,i]=code[lab]
                ledger.append({"panel":panel,"eta":float(eta),"kappa":float(kappa),
                               "label":lab,"winning_depth_candidate":g})
        print("row",j+1,"/",len(E),flush=True)
    out=Path(__file__).resolve().parent
    np.savez_compressed(out/"candidate_phase_map.npz",kappas=K,etas=E,F=labels[0],N=labels[1])
    (out/"candidate_phase_ledger.json").write_text(json.dumps(ledger,indent=2))
    print(dict(Counter((x["panel"],x["label"]) for x in ledger)))
    # Eleven permanent counterexamples from PR27.
    old=np.load(ROOT/"verification"/"stage11"/"input_v04"/"figure3_data_41x41.npz")
    dF=np.argwhere(labels[0]!=old["F"]);dN=np.argwhere(labels[1]!=old["N"])
    assert len(dF)==7 and len(dN)==4,(dF,dN)
    assert all(old["F"][j,i]==0 and labels[0,j,i]==2 for j,i in dF)
    assert all(old["N"][j,i]==0 and labels[1,j,i]==2 for j,i in dN)
    # independent center is not a grid point
    assert classify(.758,.8505,"F")[0]=="IS"
    assert classify(.758,.8505,"N")[0]=="SW"
    print("Stage11 known false-SW regression set: PASS")

if __name__=="__main__":run()
