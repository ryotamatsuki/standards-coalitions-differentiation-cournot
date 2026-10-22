"""Plot high-resolution illustrative classifications; unlike original v0.3, no unsupported SU stripe is drawn."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch

root=Path(__file__).resolve().parent
m=np.load(root/'figure3_data_41x41.npz')
K=m['ks']; E=m['es']; F=m['F']; N=m['N']
assert F.shape == (41,41) and N.shape == (41,41)
assert not np.any(F==1) and not np.any(N==1), 'SU category requires independent validation'

def edges(v):
    d=np.diff(v)
    return np.r_[v[0]-d[0]/2,(v[:-1]+v[1:])/2,v[-1]+d[-1]/2]

fig,axes=plt.subplots(1,2,figsize=(7.5,3.65))
fig.subplots_adjust(left=0.083,right=0.984,bottom=0.23,top=0.865,wspace=0.21)
# Array has only SW and IS, with no SU detected. Reserved codes preserve reproducibility.
cmap=ListedColormap(['#e3e7eb','#d8b26f','#507fae','#ffffff'])
norm=BoundaryNorm([-0.5,0.5,1.5,2.5,3.5],ncolors=4)
for ix,(ax,Z,ttl) in enumerate(zip(axes,[F,N],['(a) Frozen design','(b) Endogenous design'])):
    ax.imshow(Z, origin='lower', aspect='auto', interpolation='nearest',
              extent=[edges(K)[0],edges(K)[-1],edges(E)[0],edges(E)[-1]],
              cmap=cmap,norm=norm)
    ax.set_xlim(K.min(),K.max())
    ax.set_ylim(E.min(),E.max())
    ax.set_xlabel(r'Design cost $\kappa$',fontsize=9)
    ax.set_title(ttl,fontsize=10,pad=6)
    ax.set_xticks([0.70,0.80,0.90,1.00,1.05])
    ax.set_yticks([0.742,0.750,0.758,0.766,0.772])
    ax.tick_params(labelsize=7.5,length=3)
    if ix == 0: ax.set_ylabel(r'Network effect $\eta$',fontsize=9)
    else: ax.tick_params(labelleft=False)
    # place labels only in actual zones
    if ix == 0:
        ax.text(.875,.7665,'IS',ha='center',va='center',fontsize=12,fontweight='bold',color='#142d42')
        ax.text(.875,.7490,'SW',ha='center',va='center',fontsize=12,fontweight='bold',color='#27313c')
    else:
        ax.text(.875,.7680,'IS',ha='center',va='center',fontsize=12,fontweight='bold',color='#142d42')
        ax.text(.875,.7500,'SW',ha='center',va='center',fontsize=12,fontweight='bold',color='#27313c')
    ax.plot([.8505],[.758],marker='*',markerfacecolor='#111111',markeredgecolor='white',markeredgewidth=.5,markersize=9,zorder=5)
    for spine in ax.spines.values(): spine.set_linewidth(.6)

legend=[Patch(facecolor='#e3e7eb',edgecolor='#4c535b',label='SW: fragmented'),Patch(facecolor='#507fae',edgecolor='#4c535b',label='IS: integrated')]
fig.legend(handles=legend,loc='lower center',bbox_to_anchor=(.5,.058),ncol=2,frameon=False,fontsize=8)
fig.text(.5,.022,r'Black star: $(\kappa,\eta)=(0.8505,\,0.758)$; SU not detected in the refined slice',ha='center',fontsize=7.5,color='#4b5563')
fig.savefig(root/'figure3_v04_kappa_eta_phase.pdf',bbox_inches='tight')
fig.savefig(root/'figure3_v04_kappa_eta_phase.png',dpi=300,bbox_inches='tight')
print('Figure3 plotted from',F.shape,'F and N counts',np.unique(F,return_counts=True),np.unique(N,return_counts=True))
