# Stage19 network externalities — essential theoretical mechanism, not an afterthought
2026-10-22 JST. Supplement to PR#19, stacked on PR#18. No new variables/actors. Model source: Stage14 MODEL_SEMANTICS; network externalities are ALREADY included in the original payoff mapping.

## 1. Two fundamentally distinct primitives
Conditional consumer substitutability is **B=rho H+(1-rho)X**, whereas the fulfilled-expectations Cournot system is **M=I+B-eta H**. Here H_ii=1, H_ij is technical compatibility depth within the chosen government union; X_ij=(x_i+x_j)/2 is residual similarity. The network-benefit coefficient eta comes from utility eta q'Hn, with expected n held fixed in the quantity deviations and imposed equal to q only in equilibrium. Do not place eta again in CS: CS=q'Bq/2. rho weights TECHNICAL SUBSTITUTION; eta governs NETWORK WILLINGNESS TO PAY. They are economically and mathematically NOT interchangeable.

Define alpha=2-eta, beta=1-rho, delta=rho-eta. In symmetric IS with common residual y and depth g, t=delta*g+beta*y, L=alpha+2*t, q=d/L. Technical depth has two opposing Cournot channels: rho*g increases gross substitutability and eta*g increases the network benefit, so the NET Cournot off-diagonal change is delta*g. A positive technical link is not synonymous with a positive net substitutability increase.

## 2. Structural network-versus-substitution trichotomy (new transparent sign statement WITHIN V2b)
Write the firm's private unilateral interior FOC as F=kappa(1-y)-lambda(y-z)-A(alpha,t)=0, where
A=6 beta alpha d^2/[(alpha-t)L^3].
Let G(t)=-A_t=6 beta alpha d²(5alpha-8t)/[(alpha-t)^2 L^4] and D=kappa+lambda-beta*G(t).
At a locally regular symmetric IS design equilibrium satisfying alpha-t>0, L>0, **G>0 and D>0**, implicit differentiation gives

dyN/dg=delta*G/D.

Thus:
- rho>eta (substitution channel stronger): dyN/dg>0, private residual similarity increases with deeper public standards.
- rho=eta: dyN/dg=0 although the direct consumer-surplus and network terms can still affect governmental welfare.
- rho<eta (network channel stronger): dyN/dg<0; deeper public technical standardization induces private residual DIFFERENTIATION.

The third case is **conditional**. Original full-cube global positivity is not automatically assured when eta>rho; Stage14 source records eta=.99,rho=.01 yielding negative fulfilled-expectations quantity for certain histories. Restrict claims to positive-quantity, unique interior, regular equilibrium continuations. A local verified witness at rho=.9, eta=.92, g=.05, lambda=0 or 5 satisfies G>0,D>0 and dyN/dg<0. No claim about entire high-eta strategy cube or empirical magnitudes.

Note the maintained Stage19 'private over-similarity' global theorem assumes eta<=rho and cannot automatically be extended to eta>rho. The trichotomy and the private-social wedge are distinct lemmas with different domains.

## 3. How increasing network intensity eta changes equilibrium product choice
Hold rho, kappa, lambda, g and d fixed. Let P=alpha-t and L=alpha+2t. At fixed product index y,
alpha_eta=-1, t_eta=-g, P_eta=-(1-g), L_eta=-(1+2g). Hence

A_eta = A [-1/alpha +(1-g)/P +3(1+2g)/L] > 0

whenever alpha>0, P>0, L>0, g in [0,1], and t<alpha: because L=alpha+2t<3alpha implies 3/L>1/alpha and the (1-g)/P term is nonnegative.

**A. Physically fixed historical legacy design z** (appropriate for a within-economy change in eta):
dyN/deta = -A_eta / D < 0.
Thus increasing network intensity makes the representative firm select MORE differentiation of remaining nonstandard product attributes at a fixed g. It is not equivalent to increasing government technical compatibility g.

**B. Across-economy re-centered benchmark z=zSW(eta)** (the controlled parameter family used by earlier lambda comparisons):
z_eta = -A_eta(z, g=0) /[kappa-beta*G(beta*z)] < 0,
dyN/deta = [lambda*z_eta-A_eta(y,g)]/D <0.
Because the initial architecture moves with eta in this experiment, numerical derivative magnitudes differ from a historically fixed architecture. Do not describe these distinct comparative statics as a single estimated causal effect.

Assumes positive interior Nash, regular denominators. These are partial structural derivatives holding rho fixed; rho comparative statics are DIFFERENT because changing rho simultaneously changes beta=1-rho and delta=rho-eta.

## 4. Consumer benefit and induced product differentiation: welfare decomposition
At a common design and depth, national welfare is W=N d²/L²-K(y), with N=9/2+3(rho*g+beta*y). With a FIXED historical z,
W_eta|g,y = 2N d²(1+2g)/L³ > 0,
dW(g,yN(eta))/deta = W_eta|g,y + W_y*yN_eta.

In the Stage19 strict excess-similarity parameter class, W_y(g,yN)<0 and yN_eta<0. Thus the induced strategic-design feedback is ALSO positive. Stronger network externalities confer direct benefits AND stimulate differentiation which reduces the previously certified excessive similarity. Hence the private design response **amplifies the positive national-welfare effect of eta** for a fixed g and legacy z. This is a useful economically interpretable counterpoint to the STRICTLY NEGATIVE policy-depth design feedback W_y*yN_g for rho>eta.

Under z=zSW(eta), however,
W_eta|g,y = 2N d²(1+2g)/L³ + lambda*(y-z)*z_eta.
The last term can have negative sign and is NOT safely ignored; a net global eta->welfare sign requires additional bounds. This explains why benchmarking choice matters.

## 5. Governments' consent and endogenous optimum
Country C's third-country accession margin is Phi(g,eta)=W_C^IS(g,eta)-W_C^SU(g,eta), each term evaluated at its own full three-firm Nash design, and both include eta in the Cournot demand/network channel. Hence eta affects:
1. consumer and network values of the broader interoperable network;
2. firm design in both the bilateral and grand continuations, via DIFFERENT SU vs IS Nash feedback;
3. the outside option of the third country and incumbent rent shifting;
4. the accepted government depth g* (when an optimal IS branch exists).

On a regular binding outsider-vote branch with Phi_g!=0,
dg*/deta = -Phi_eta/Phi_g,
and, for optimal symmetric grand residual similarity y*(eta)=yN(g*(eta),eta),
dy*/deta = yN_eta+yN_g*dg*/deta.

Neither sign is determined GENERALLY by eta>rho or rho>eta alone: the difference of two endogenized countries' payoffs, and the policy response, can offset the otherwise positive direct network component. Do not claim unconditional 'higher eta gives deeper standards' or 'higher eta always raises welfare' for full endogenous government policy.

**Numerical LOCAL witness** at rho=.9, eta=.758, kappa=.8505, lambda=5, g*~.054333206814, original benchmark z~.718592707322, using independent SciPy 3x3 Cournot + actual firm unilateral Nash FOCs:
- Phi_g ~ -0.00931917;
- moving legacy re-center zSW(eta): Phi_eta ~ +0.312445, dg*/deta ~ +33.5271, yN_eta|fixed-g ~ -0.694592;
- fixing the PREINSTALLED z at its theta0 physical value: Phi_eta ~ +0.313612, dg*/deta ~ +33.6524, yN_eta|fixed-g ~ -0.096155.
These are **finite-difference numerical diagnostic sensitivities**, not Fraction-certified policy parametric theorems. They support only a local sign in a sufficiently small parameter neighborhood if equilibrium/vote regularity persists. The derivatives are in UNCALIBRATED parameter units and very large because the outsider's Phi_g is shallow. Do not linearly extrapolate over wide eta changes.

## 6. Paper design and priority safeguards
Put eta front and center in: Introduction (competing network vs substitution channels), model (B vs M), main design proposition (sign of rho-eta), comparative statics (eta and rho, legacy reference), optimal accession depth (Phi_eta decomposition) and welfare/interpretation. The graphical 'network externality' should be distinct from a standard-compliance cost or rho.

**Very close prior art:** Klimenko (2009, Journal of International Economics) specifically finds noncooperative compatibility policies too high OR too low depending on network-effect strength, and discusses international agreements (publisher Introduction accessible; full final numbered theorem NOT inspected). Gandal & Shy (2001), Barrett–Yang (2001), Baake & Boom (2001), Grossman–McCalman–Staiger (2021) also overlap materially. A new eta sign alone is not sufficient journal novelty; the narrow candidate is eta's interaction with endogenously chosen residual design, THIRD-country accession and optimal standards depth under the same protocol.

Verdict: structural comparative sign math PASS under stated regularity; broad government eta comparative and literature priority CONDITIONAL. No new primitives. Draft PR19 review only, no main/freeze/manuscript production file edits.
