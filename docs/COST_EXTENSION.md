# Symmetric standard-adoption cost: optional extension

**Not part of the canonical zero-cost baseline.** These are proposed primitives and a replicable witness, pending a full global-SPNE audit.

## Symmetry principle
Every country is ex ante symmetric. A member adopting a common design-constraining standard at positive depth `g` incurs a **real resource** cost
```
K(g)=F + (kappa/2)*g^2, g>0
K(0)=0; F>=0, kappa>=0.
```
All adopters have identical `K`. A/B pay on SU formation; C pays only when entering later, because A/B already converted. No A/B extra payment on C's acceptance at unchanged g. The discontinuity at g=0 from F is intentional and needs justification if retained (fixed certification/tooling cost).

## Welfare accounting
```
Wtilde_SW = W_SW
Wtilde_SU_A = Wtilde_SU_B = W_SU_member(s) - K(sqrt(s))
Wtilde_SU_C = W_SU_outsider(s)
Wtilde_IS_A = Wtilde_IS_B = Wtilde_IS_C = W_IS(s) - K(sqrt(s))
```
For A/B comparing IS to SU once payment is sunk, `K` cancels. C's entry compares `W_IS(s)-K(g)` with `W_SU_outsider(s)`. At stage 1 A/B compare actual total welfare net of conversion cost with the SW default. The sunk-payment assumption is a commitment to irreversible investment; if the cost is recurrent or reversible, explicitly change the timing.

## Why C-only costs are rejected
A country-specific C penalty in an otherwise ex ante symmetric model would introduce an arbitrary asymmetry. Symmetric adopter costs and path-dependent timing are the minimal economically interpretable replacement.

## Terminal SU witness under symmetric F
Take `eta=0.9`, `F=0.163`, `kappa=0`, and `s=1`. Approximately:
```
W_SW = 3.719008264
W_SU_member(s=1) = 3.885445363; net of F = 3.722445363
W_SU_outsider(s=1) = 4.281450872
W_IS(s=1) = 4.437869822; C net of F = 4.274869822
```
So A/B strictly prefer SU to SW, while C strictly rejects joining at s=1. In fact the maximal gross C accession gain over s∈[0,1] is approximately
```
max_s (W_IS(s)-W_SU_outsider(s)) = 0.1610558136
attained near s=0.8309872043.
```
Since `F=0.163` exceeds this maximum, C does not join at any positive g. A/B's SU welfare is increasing in s at eta=.9 and hence selects s=1; A/B's gain over SW at s=1 is about 0.1664370983 before cost. The witness exists for the narrow interval
```
0.161055814... < F < 0.166437098...
```
with strict preferences.

**Status:** arithmetic witness of a terminal SU outcome given selected firm continuation and timing. Strict verification of the full off-path firm subgame, cost incidence, mixed strategies / alternative sequential bargaining histories is outstanding. Do not claim this tiny F interval is robust.

## Next analytic task
Determine the full `(eta,F,kappa)` regime map (SW/SU/IS), including acceptance regions, welfare ordering, constraint-binding status, and whether positive-depth SU occupies an open robust region.
