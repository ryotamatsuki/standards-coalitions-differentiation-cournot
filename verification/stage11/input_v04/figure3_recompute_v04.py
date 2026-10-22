"""Reproduce descriptive Figure 3 numeric data from primitives; NOT an interval/theorem certificate.
Requires numpy and scipy. Runs 41x41 parameter grid and depth grids with adaptive refinement.
Use from directory containing phase_model_functions.py.
"""
import json
from pathlib import Path
import numpy as np
from scipy.ndimage import binary_dilation
from phase_model_functions import classify, codes

ROOT=Path(__file__).resolve().parent
K=np.linspace(0.70,1.05,41)
E=np.linspace(0.742,0.772,41)
F=np.full((len(E),len(K)),3,dtype=np.uint8)
N=F.copy()

for j,eta in enumerate(E):
    for i,k in enumerate(K):
        frozen,endogenous,_=classify(float(eta),float(k),np.linspace(0,1,81))
        F[j,i]=codes[frozen];N[j,i]=codes[endogenous]
    print('initial-grid eta row',j,'/',len(E),flush=True)
oldF,oldN=F.copy(),N.copy()

flip=np.zeros_like(F,dtype=bool)
for arr in (F,N):
    flip[1:,:]|=arr[1:,:]!=arr[:-1,:]
    flip[:-1,:]|=arr[:-1,:]!=arr[1:,:]
    flip[:,1:]|=arr[:,1:]!=arr[:,:-1]
    flip[:,:-1]|=arr[:,:-1]!=arr[:,1:]
flip|=(F==1)|(N==1)
mask=binary_dilation(flip,iterations=1)
print('near-boundary cells to refine:',int(mask.sum()),flush=True)
for j,i in np.argwhere(mask):
    frozen,endogenous,_=classify(float(E[j]),float(K[i]),np.linspace(0,1,321))
    F[j,i]=codes[frozen];N[j,i]=codes[endogenous]

rechecks=[]
for j,i in np.argwhere((F!=oldF)|(N!=oldN)):
    frozen,endogenous,_=classify(float(E[j]),float(K[i]),np.linspace(0,1,641))
    rechecks.append({'i':int(i),'j':int(j),'kappa':float(K[i]),'eta':float(E[j]),
                     'original81':[int(oldF[j,i]),int(oldN[j,i])],
                     'refined321':[int(F[j,i]),int(N[j,i])],
                     'refined641':[int(codes[frozen]),int(codes[endogenous])],
                     'same_321_641':bool(codes[frozen]==F[j,i] and codes[endogenous]==N[j,i])})

np.savez_compressed(ROOT/'figure3_data_41x41.npz',F=F,N=N,oldF=oldF,oldN=oldN,ks=K,es=E,
                    refine_mask=((F!=oldF)|(N!=oldN)))
(ROOT/'figure3_depth_convergence_641.json').write_text(json.dumps(rechecks,indent=2))
print('final counts frozen',np.unique(F,return_counts=True),'endogenous',np.unique(N,return_counts=True),flush=True)
print('changed',len(rechecks),'stable_641',sum(p['same_321_641'] for p in rechecks),flush=True)
