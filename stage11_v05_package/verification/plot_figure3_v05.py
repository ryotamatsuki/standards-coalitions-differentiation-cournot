from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap,BoundaryNorm
ROOT=Path(__file__).resolve().parent
D=np.load(ROOT/'rerun_outputs/figure3_boundary_aware_map.npz')
ks,es,F,N=D['kappas'],D['etas'],D['F'],D['N']
cmap=ListedColormap(['#dcdcdc','#eec378','#598bbb','#fafafa'])
norm=BoundaryNorm([-.5,.5,1.5,2.5,3.5],4)
fig,axs=plt.subplots(1,2,figsize=(7.2,3.6),layout='constrained')
for ax,arr,title in zip(axs,[F,N],['(a) Frozen design','(b) Endogenous design']):
 ax.imshow(arr,origin='lower',aspect='auto',interpolation='nearest',extent=[.70,1.05,.742,.772],cmap=cmap,norm=norm)
 ax.plot(.8505,.758,'k*',markersize=7)
 ax.text(.85,.763,'IS',ha='center',weight='bold',fontsize=10)
 ax.text(.85,.75,'SW',ha='center',weight='bold',fontsize=10)
 ax.set_title(title,fontsize=9)
 ax.set_xlabel(r'Design cost $\kappa$',fontsize=9)
 ax.set_xticks([.70,.80,.90,1.00])
 ax.set_yticks([.742,.750,.758,.766,.772])
 ax.tick_params(labelsize=8)
axs[0].set_ylabel(r'Network effect $\eta$',fontsize=9)
fig.savefig(ROOT/'rerun_outputs/figure3_v05_corrected.png',dpi=350,bbox_inches='tight')
fig.savefig(ROOT/'rerun_outputs/figure3_v05_corrected.pdf',bbox_inches='tight')
