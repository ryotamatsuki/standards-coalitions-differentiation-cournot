#!/usr/bin/env python3
"""Self-contained Stage11 v0.5 test entrance. Execute from ANY working directory.
Smoke validates archived outputs and 11 counterexamples; --mode full reruns all
41x41 candidate cells, 1550 IS envelope tests and 1812 SW micro-depth tests.
Regenerated outputs go in verification/rerun_outputs, never overwrite release data.
These computations do not prove the entire 2D phase-plane partition.
"""
import argparse, subprocess, sys, json, time
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
V=HERE/'verification'
OUT=V/'rerun_outputs'

def run(script):
    start=time.monotonic()
    print('RUN',script,flush=True)
    subprocess.run([sys.executable,str(V/script)],cwd=HERE,check=True)
    print('PASS',script,'seconds',round(time.monotonic()-start,1),flush=True)

def smoke():
    sys.path.insert(0,str(V))
    from stage11_fix_classifier import Cell,classify,strict_agreement
    old=np.load(V/'input_v04/figure3_data_41x41.npz')
    saved=np.load(V/'figure3_boundary_aware_map.npz')
    assert old['F'].shape==saved['F'].shape==(41,41)
    cases=[('F',k,.7555) for k in (.93625,.945,.95375,.9625,.97125,.98,.98875)]
    cases += [('N',k,e) for k,e in ((.945,.760),(.95375,.760),(.86625,.76075),(.79625,.7615))]
    for tr,k,e in cases:
        c=Cell(k,e)
        r=classify(c,tr)
        assert r['result']=='IS' and r['g']>0,(tr,k,e,r)
    assert classify(Cell(.8505,.758),'F')['result']=='IS'
    assert classify(Cell(.8505,.758),'N')['result']=='SW'
    for tr,k,e in [('F',.93625,.7555),('N',.945,.760)]:
        v=Cell(k,e).at(.0001,tr)
        assert strict_agreement(v)=='IS' and min(v['is'],v['im'],v['io'])>0
    print('PASS 11 former false-SW cells, two near-zero witnesses and certified benchmark labels')

def full():
    run('stage11_fix_classifier.py')
    saved=np.load(V/'figure3_boundary_aware_map.npz')
    recreated=np.load(OUT/'figure3_boundary_aware_map.npz')
    for key in ('F','N','kappas','etas'):
        assert np.array_equal(saved[key],recreated[key]),'Mismatch: '+key
    print('PASS 41x41 two-panel labels match original 3362 entries')
    run('stage11_dominance_check.py')
    now=json.loads((OUT/'dominance_check.json').read_text())['summary']
    old=json.loads((V/'dominance_check.json').read_text())['summary']
    assert now['checked']==old['checked']==1550
    assert now['not_confirmed']==old['not_confirmed']==0
    assert abs(now['min_domination_margin']-old['min_domination_margin'])<1e-8
    print('PASS 1550 IS superiority numerical checks')
    run('stress_swcells.py')
    stat=json.loads((OUT/'extra_SW_stress.json').read_text())
    assert stat['checked_SW_cells']==1812 and stat['additional_accepted_IS_found']==0
    print('PASS 1812 SW micro-depth numerical checks')
    run('plot_figure3_v05.py')
    assert (OUT/'figure3_v05_corrected.pdf').stat().st_size>2000

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode',choices=('smoke','full'),default='smoke')
    args=p.parse_args()
    OUT.mkdir(exist_ok=True)
    run('verify_v05.py')
    smoke()
    if args.mode=='full':full()
    print('PASS Stage11 distribution reproducibility',args.mode,flush=True)

if __name__=='__main__':main()
