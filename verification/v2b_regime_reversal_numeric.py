#!/usr/bin/env python3
"""V2b coalition-regime reversal witness.
Numerical diagnostics only: not a certificate over continuous g nor proof of SPNE.
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from v2b_policy_numeric import continuation, frozen_welfare

ETA, RHO, KAPPA = 0.758, 0.900, 0.8505
T = 1 - RHO

def outcome(regime, g, x):
    H = np.eye(3)
    if regime == "SU":
        H[0, 1] = H[1, 0] = g
    if regime == "IS":
        H += g * (np.ones((3, 3)) - np.eye(3))
    X = np.eye(3) + 0.5 * (x[:, None] + x[None, :]) * (np.ones((3, 3)) - np.eye(3))
    B = RHO * H + T * X
    q = np.linalg.solve(np.eye(3) + B - ETA * H, np.ones(3))
    W = .5 * q @ B @ q + 3 * q * q - KAPPA / 2 * (1-x)**2
    return q, W

def welfare(g, frozen, x0):
    if frozen:
        su = frozen_welfare(ETA, RHO, KAPPA, "SU", g, x0)
        is_ = frozen_welfare(ETA, RHO, KAPPA, "IS", g, x0)
    else:
        su = continuation(ETA, RHO, KAPPA, "SU", g)[2]
        is_ = continuation(ETA, RHO, KAPPA, "IS", g)[2]
    return su[0], su[2], is_[0]

def verify_br(regime, g):
    x, q, w = continuation(ETA, RHO, KAPPA, regime, g)
    for i in range(3):
        def payoff(z):
            y = x.copy()
            y[i] = z
            qnew = outcome(regime, g, y)[0]
            return 3 * qnew[i]**2 - KAPPA/2 * (1-z)**2
        grid = np.linspace(0, 1, 101)
        results = [(payoff(z), z) for z in grid]
        for j in range(1, 100):
            if results[j][0] >= results[j-1][0] and results[j][0] >= results[j+1][0]:
                r = minimize_scalar(lambda z: -payoff(z),
                                    bounds=(grid[j-1],grid[j+1]),method="bounded")
                results.append((-r.fun, r.x))
        gain = max(v for v, z in results) - payoff(x[i])
        assert gain < 1e-7, (regime, g, i, gain)

def main():
    threshold = 81 * (1-RHO)**2
    assert KAPPA > threshold and ETA < min(1, 4*RHO/3)
    sw_x, sw_q, sw_w = continuation(ETA, RHO, KAPPA, "SW", 0)
    sw = sw_w[0]
    grid = np.linspace(.001, 1, 1001)
    e = np.array([welfare(g, False, sw_x) for g in grid])
    c_gain = e[:,2] - e[:,1]
    su_gain = e[:,0] - sw
    assert np.max(c_gain) < 0 and np.max(su_gain) < 0

    f = lambda g: welfare(g, True, sw_x)
    cap = brentq(lambda g: f(g)[2] - f(g)[1], .05, .1, xtol=1e-13)
    m, o, international = f(cap)
    assert international > max(m,sw)
    for S in ("SW","SU","IS"):
        for g in ([0] if S=="SW" else [0,cap,.5,1]):
            verify_br(S,g)

    # First-order permutation symmetry: derivative of C admission gain = 2*SU member slope.
    for frozen in (False,True):
        h = 1e-6
        member, outsider, is_ = welfare(h,frozen,sw_x)
        dm = (member-sw)/h
        dc = (is_-outsider)/h
        assert abs(dc-2*dm)<3e-6
        if frozen:
            assert dm > 0 and dc > 0
        else:
            assert dm < 0 and dc < 0

    print("Stage-4 uniqueness sufficient bound:",threshold,"<",KAPPA)
    print("SW x=",sw_x[0],"SW W=",sw)
    print("Endogenous max C admission advantage (1001 g)=",max(c_gain))
    print("Endogenous max member SU advantage (1001 g)=",max(su_gain))
    print("Frozen maximum C-compatible depth=",cap,"international welfare=",international)
    print("PASS: numerical regime-reversal witness, unilateral BR and local sign identity")
    print("NOT PROVED: continuous-g policy global inequalities or complete SPNE.")

if __name__ == "__main__":
    main()
