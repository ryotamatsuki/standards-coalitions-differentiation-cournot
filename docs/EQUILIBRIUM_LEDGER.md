# Equilibrium and welfare ledger

**Status convention:** [ALGEBRA] identity checked under displayed candidate continuation; [CANDIDATE] needs complete off-path best-response and SPNE proof; [INTERPRETATION] model-specific.

## 1. Symmetric candidate firm continuations [ALGEBRA, CANDIDATE AS FULL SUBGAME CLAIM]

Define `A=2-eta`, `k=1-eta`, `s=g^2`, normalize `a-c=1`.

| Regime | Chosen `z` | Cournot output per market |
|---|---|---|
| SW | (0,0,0) | (1/A,1/A,1/A) |
| SU(AB,g) | (g,g,0) | (1/(A+ks),1/(A+ks),1/A) |
| IS(g) | (g,g,g) | (1/(A+2ks), repeated 3 times) |

At zero depth there are indifferences in realized `z` and possibly additional strategy profiles. These expressions describe selected continuations; **do not substitute 'unique subgame Nash equilibrium' without a proof.**

## 2. National welfare [ALGEBRA]

```
W_SW = 9 / (2 A^2)
W_SU_member(s) = (4+s)/(A+k*s)^2 + 1/(2 A^2)
W_SU_outsider(s) = (1+s)/(A+k*s)^2 + 7/(2 A^2)
W_IS(s) = 3(3+2s) / [2(A+2k*s)^2]
```
Derivatives:
```
dW_SU_member/ds = [7*eta-6-(1-eta)*s] / (A+k*s)^3
dW_SU_outsider/ds = [eta-(1-eta)*s] / (A+k*s)^3
dW_IS/ds = 3[5*eta-4-2(1-eta)*s] / (A+2k*s)^3
```
The outsider–member advantage is `3[1/A^2 - 1/(A+k*s)^2]` (strictly positive if `s>0`, `eta<1`).

## 3. IS socially/nationally optimal depth without outsider accession restriction [ALGEBRA]
```
s_IS^unrestricted(eta) = 0,                          eta ≤ 4/5
                        (5*eta-4)/[2(1-eta)],      4/5 < eta < 6/7
                        1,                          eta ≥ 6/7

W_IS^unrestricted(eta) =
  9/[2(2-eta)^2]                            for eta ≤ 4/5
  3/[8(1-eta)(2*eta-1)]                     for 4/5 < eta < 6/7
  15/[2(4-3*eta)^2]                         for eta ≥ 6/7
```
This is an **unconstrained IS optimum**, not necessarily a feasible negotiated coalition.

## 4. Fixed-depth accession test [ALGEBRA]

At every proposed `s>0`, C can join only if `W_IS(s) ≥ W_SU_outsider(s)`. A and B require `W_IS(s) ≥ W_SU_member(s)`. Since outsider SU welfare exceeds member SU welfare, C's individual-rationality constraint is **the tighter** one for identical joining terms and no costs.

Define `r=k/A`. Then
```
W_IS(s)-W_SU_outsider(s)
  = -s*P(r,s) / [ A^2*(1+r*s)^2*(1+2*r*s)^2 ]

P(r,s) = 14*r^4*s^3
       + (42*r^3+r^2)*s^2
       + (45*r^2-2*r)*s
       + 16*r-2
```
For `s>0`, C consents iff `P(r,s) ≤ 0`. At `s=0`, C is indifferent.

- `eta ≤ 6/7`: no strictly positive depth meets C's consent constraint.
- `eta > 6/7`: a sufficiently small positive depth meets C's consent constraint; the largest feasible `s` is the root `P(r,s)=0` when below 1.
- Root reaches 1 at `eta_C ≈ 0.884049096671274`, the unique root in `(6/7,1)` of
```
57 eta^4 -312 eta^3 +632 eta^2 -559 eta +181 = 0.
```

## 5. Candidate baseline fixed-depth policy classification [CANDIDATE; NOT A FULL SPNE THEOREM]

Under A-proposes/B-vetoes; C applies; A/B unanimously approve; zero costs; no transfers; at indifference choose admission/acceptance; selected firm continuations:
```
0 ≤ eta ≤ 6/7: economically zero integration (SW-equivalent), g*=0
6/7 < eta < eta_C: IS, g*=sqrt(s_C(eta)) where P(k/A,s_C)=0 in (0,1)
eta_C ≤ eta < 1: IS, g*=1.
```
The `eta=6/7` boundary is weak/tie-sensitive, and `g=0` cannot identify the institutional SW/SU/IS label. Complete off-path verification and tie-sensitive pure-strategy existence are not certified. A–B SU-only unconstrained optimum for comparison:
```
s_SU_member^unrestricted =
  0                                 eta≤6/7
  (7eta-6)/(1-eta)                 6/7<eta<7/8
  1                                 eta≥7/8.
```
The conversation argued that IS dominates the best stable SU on this path when eta>6/7; treat this cross-option inequality as **PROOF REQUIRES INDEPENDENT AUDIT**, even if supporting examples check numerically.

## 6. Contrast: obsolete 'renegotiated IS depth' version [HISTORICAL ONLY]
Earlier model permitted a fresh choice of IS depth after C joined. Its proposed economic threshold was `eta>4/5` (IS begins), with unrestricted IS optimum above; for instance at `eta=0.82`, A–B could set low provisional SU depth and, after C entered, reset IS to `sqrt(5/18)≈0.527046`. **This path is impossible in the fixed-depth model.** It should never be presented as a current equilibrium.

## 7. Illustrative baseline calculations [ALGEBRA]
At `eta=0.82`: `A=1.18`, `k=0.18`, `W_SW≈3.231829934`. For `g=0.2` (`s=.04`):
```
W_SU_member≈3.225471055; W_SU_outsider≈3.251525206; W_IS≈3.238488701.
```
C rejects fixed-depth IS at g=.2. At `g≈.527046`, unconstrained IS welfare is `3.255208333` but C's SU outside option is `≈3.358234`; do not mistake that IS welfare optimum for a feasible fixed-depth accession.

## 8. What is NOT established
- Full best-response correspondence at every differentiation vector and every off-path government history;
- universal positive-quantity interior Cournot solutions (piecewise quantity constraints may matter);
- uniqueness, exhaustive SPNE classification, or robustness to tie rules;
- symmetric positive-cost (`F, kappa`) global analytic regime map;
- empirical calibration or novelty.
