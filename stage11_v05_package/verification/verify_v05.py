import json,hashlib,pathlib,sys,subprocess
from collections import Counter
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parent
DATA=ROOT
z=np.load(DATA/'figure3_boundary_aware_map.npz')
old=np.load(ROOT/'input_v04'/'figure3_data_41x41.npz')
F,N=z['F'],z['N']
assert F.shape==N.shape==(41,41)
difF=np.argwhere(F!=old['F']);difN=np.argwhere(N!=old['N'])
assert len(difF)==7,(len(difF),difF)
assert len(difN)==4,(len(difN),difN)
assert all(int(old['F'][j,i])==0 and int(F[j,i])==2 for j,i in difF)
assert all(int(old['N'][j,i])==0 and int(N[j,i])==2 for j,i in difN)
assert set(np.unique(F)).issubset({0,2}) and set(np.unique(N)).issubset({0,2})
reg=json.loads((DATA/'regression_cases.json').read_text())
assert len(reg)==4 and all(r['label']=='IS' and r['i-s']>0 and r['i-o']>0 and r['i-m']>0 for r in reg)
checks=json.loads((DATA/'dominance_check.json').read_text())['summary']
assert checks['not_confirmed']==0 and checks['checked']==int((F==2).sum()+(N==2).sum())
assert checks['min_domination_margin']>0
# Factual center check independent from gridded point (not itself a mesh cell)
sys.path.insert(0,str(ROOT))
from stage11_fix_classifier import Cell,classify,strict_agreement
c=Cell(.8505,.758)
f=classify(c,'F');n=classify(c,'N')
assert f['result']=='IS' and n['result']=='SW',(f,n)
expected={'frozen_SW':765,'frozen_IS':916,'endogenous_SW':1047,'endogenous_IS':634}
actual={'frozen_SW':int((F==0).sum()),'frozen_IS':int((F==2).sum()),'endogenous_SW':int((N==0).sum()),'endogenous_IS':int((N==2).sum())}
assert actual==expected,(actual,expected)
# Validate at least 2 exact reference numerical witness signs
assert abs(reg[0]['i-o']-3.94704111296e-10)<1e-14
assert abs(reg[1]['i-o']-1.39497667385e-10)<1e-14
# PDF & LaTeX
pdf=ROOT.parent/'manuscript/stage25_jpet_v05.pdf';tex=ROOT.parent/'manuscript/stage25_jpet_v05.tex';sup=ROOT.parent/'manuscript/stage11_proof_supplement.tex';fig=ROOT.parent/'manuscript/figure3_v05_tikz.tex'
assert all(x.exists() and x.stat().st_size>2000 for x in [pdf,tex,sup,fig])
text=tex.read_text()
for phrase in ['\\input{figure3_v05_tikz.tex}','\\input{stage11_proof_supplement.tex}','\\label{fig:phase}',r'\ref{app:interval}',r'\label{app:networkfull}',r'\label{app:regularity}']:
 if phrase not in text and phrase not in sup.read_text():raise AssertionError(phrase)
log=(ROOT/'build_log.txt').read_text()
assert not any(s in log for s in ['LaTeX Warning','Overfull \\hbox','Undefined control sequence','Fatal error','! LaTeX Error'])
info=subprocess.check_output(['pdfinfo',str(pdf)],text=True)
assert 'Pages:           20' in info
sha={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [pdf,tex,sup,fig,DATA/'figure3_boundary_aware_map.npz',DATA/'dominance_check.json']}
report={'final_status':'PASS for explicitly bounded Stage11 major repairs M1-M3; paper remains working draft, Stage12 not authorized','figure3':{'source_misclassified_SW_fixed':11,'panel_changes':{'F':len(difF),'N':len(difN)},'class_counts':actual,'numeric_IS_dominance_checks':checks,'center':{'frozen':f['result'],'endogenous':n['result']},'continuous_global_phase_certified':False,'residual_limitation':'Numerical search brackets observed roots and samples g near zero, but does not certify absence of every unobserved acceptance window in all 1681 cells.'},'proof':{'model_welfare_bridge':'integrated','full_cube_Nash':'Rosen sufficient inequality and existence/uniqueness explicitly written','all_depth':'Krawczyk definitions, 1000 interval scope, derivative bounds and government existence in supplement','C2':'exact face and local restricted strip quadratic proof integrated','stage11_replay_source':'immutable PR27 log and code, not rerun by current script'},'exposition':{'private_differentiation':'explicit x similarity and 1-x costly differentiation','votes':'sequenced approval and off-path ties','related_literature':'specific nonpriority and narrow result'},'latex':{'page_count':20,'compile_warnings':0,'sha256':sha},'remaining_nonblocking': ['Literature supplemental source access gaps explicitly not certified','Figure3 outside center is exploratory and not an exact all-parameter theorem','author must conduct final journal/AI disclosure checks at Stage14']}
(ROOT/'rerun_outputs').mkdir(exist_ok=True)
(ROOT/'rerun_outputs/STAGE11_V05_QA_recheck.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps(report,indent=2,ensure_ascii=False))
