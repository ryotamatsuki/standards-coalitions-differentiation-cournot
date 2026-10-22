# Stage19 — General private/social design distortion and policy-feedback theorem

## Primitive assumptions
The ORIGINAL V2b IS continuation has 3 symmetric firms, scalar residual similarity y in [0,1], technical depth g in [0,1], q=d/(alpha+2t), with
alpha=2-eta, beta=1-rho>0, delta=rho-eta, t=delta g+beta y, b=rho g+beta y, L=alpha+2t, N=9/2+3b. Assume d>0, kappa>0, lambda>=0 (lambda=0 is the frozen original cost model), eta in (2/5,1), eta<=rho<1. The legacy z is only used if lambda>0.

Define once-paid cost K(y)=kappa(1-y)^2/2+lambda(y-z)^2/2 and each national welfare (global Cournot profits of its home firm counted once)
W(g,y)=N d²/L²-K(y).

**Important planner definition:** the *symmetric design planner* chooses one common y for all firms at a FIXED g to maximize 3W(g,y). It does NOT choose independent asymmetric (x1,x2,x3), g, transfers or coalition membership. We do not conflate this restricted planner with unrestricted globally optimal design.

## Proposition 1 (excess private similarity; all policy depths)
Assume the genuine full asymmetric firm-design Nash is unique, interior and symmetric for all IS g in [0,1], e.g. via inherited global Rosen sufficient conditions, and
kappa+lambda > 180 beta² d²/alpha^4.
Then for every such g, the unique maximizer yP(g) of the symmetric planner's welfare function satisfies yP(g)<yN(g).

**Proof identities:** each firm's unilateral Nash FOC is
kappa(1-yN)-lambda(yN-z)= 6 beta alpha d² /[(alpha-t)L³].
The simultaneous all-firm derivative of national welfare is
W_y= beta d²(3/L²-4N/L³)+kappa(1-y)-lambda(y-z).
At PRIVATE Nash, substitute the private FOC:
W_y(g,yN)=beta d²/L³ [3L-18-12b+6alpha/(alpha-t)].
Because eta<=rho<1, 0<=t<=1-eta, 0<=b<=1, L<=4-3eta and alpha-t>=1. Thus
3L-18-12b+6alpha/(alpha-t)
<= 3(4-3eta)-18+6(2-eta) = 6-15eta < 0.
The symmetric planner's W_yy is
24 beta²d²(N-L)/L^4-(kappa+lambda).
Since N-L<=N<=15/2 and L>=alpha, W_yy<180 beta² d²/alpha^4-(kappa+lambda)<0 globally. Strict concavity, compactness and negative derivative at yN imply the unique planner maximizer yP lies strictly below interior yN. QED.

The inequality eta>2/5 is sufficient, NOT necessary. Private excess similarity is a known type of distortion in the IO literature. Claim only this explicit V2b parameter class, not generic priority.

## Proposition 2 (strict adverse private-design feedback into sovereign depth)
Under eta<rho and a regular interior unique Nash branch, define
G(t)=6 beta alpha d²(5alpha-8t)/[(alpha-t)² L^4].
Then FOC differentiation gives
yN_g = delta G/(kappa+lambda-beta G).
Since 5alpha-8t >=2+3eta>0 and the regularity denominator is positive, yN_g>0. At private Nash W_y<0 by Proposition 1, therefore
dW(g,yN(g))/dg = W_g(g,yN(g)) + W_y(g,yN(g))*yN_g < W_g(g,yN(g)).
The explicit partial effect is
W_g(g,y)= d²[3rho/L²-4delta N/L³].
The comparison is to the fixed-design partial derivative evaluated at the SAME yN(g); it is NOT a direct comparison between true and frozen-design optimally chosen policy depths.

At eta=rho, delta=0 and yN_g=0, so the strictly negative policy feedback disappears. At rho=1, beta=0, the private/social similarity externality term vanishes; those cases are outside the strict theorem.

## Proposition 3 (rigorously enclosed canonical example, not general theorem about global planner)
At theta0=(d,eta,rho,kappa)=(1,379/500,9/10,1701/2000), lambda=5 and CERTIFIED PR18 government g* in (.05433320681,.05433320682) under acceptance at indifference:
yN in (.71968163,.71968164);
yP_sym in (.66267728,.66267730);
yN-yP_sym in (.05700433,.05700436);
W(g*,yP_sym)-W(g*,yN) in (.00914828659,.00914832655);
W_y(yN,g*)*yN_g in (-.00629609977,-.00629609966).
The enclosing intervals come from an independent Python standard-library Fraction interval evaluator and exact FOC endpoint signs. **Do not** describe this as the social gain of selecting a different treaty depth.

## New versus old
The previous Stage18 root is a fixed-primitive Nash-depth institutional theorem. Propositions 1-2 introduce transparent PRIMITIVE inequalities valid on a parameter class and include the original lambda=0 model. This is an analytic generality advance within the model, but established predecessor literature also studies design social inefficiency and externality feedback. Publication-level novelty: CONDITIONAL/UNRESOLVED.
