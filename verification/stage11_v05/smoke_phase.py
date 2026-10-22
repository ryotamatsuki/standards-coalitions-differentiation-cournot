#!/usr/bin/env python3
"""Smoke regression on eleven documented false SW cells and the exact center."""
from recompute_phase_candidates import classify,evaluate_factory
import math
frozen=[.93625,.945,.95375,.9625,.97125,.98,.98875]
endogenous=[(.945,.760),(.95375,.760),(.86625,.76075),(.79625,.7615)]
for k in frozen:
    lab,g=classify(.7555,k,"F")
    assert lab=="IS" and g is not None and g>0, ("frozen",k,lab,g)
for k,e in endogenous:
    lab,g=classify(e,k,"N")
    assert lab=="IS" and g is not None and g>0, ("N",k,e,lab,g)
assert classify(.758,.8505,"F")[0]=="IS"
assert classify(.758,.8505,"N")[0]=="SW"
# audit-specific 80-digit counterexample re-evaluated at its published positive depth
for tr,k,e in [("F",.93625,.7555),("N",.945,.760)]:
    ev,s=evaluate_factory(e,k)
    v=ev(.0001,tr)
    assert v["is"]>1e-5 and v["io"]>1e-11 and v["im"]>0, (tr,k,e,v)
print("PASS: 11 false-SW regressions + center F-IS/N-SW + tiny accepted IS proposals")
