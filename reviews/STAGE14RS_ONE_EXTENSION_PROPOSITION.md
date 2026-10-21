# A unique local adjustment-friction threshold for international-standards consent

## 1. Primitive and timing

Change ONLY the original firm cost to K_i=kappa(1-x_i)^2/2 + lambda(x_i-z)^2/2. z denotes the *pre-existing* symmetric fragmentation Nash at the canonical theta0; it is not a new strategic variable and is held fixed as lambda changes. This models the increasing marginal resource cost of moving a residual product attribute away from an existing architecture. It is paid once and included in firm income and national welfare. This does **not** add a calendar period or a second design dimension.

The initial fragmentation Nash remains x_i=z for all lambda >=0: the new penalty is zero, with zero marginal cost there, and the original strict Rosen uniqueness margin only improves. Government decisions, conditional demand B, fulfilled-expectations M, national W_i, original bilateral-first / inherited-depth procedure, g in [0,1], and the three industrial regimes are unchanged.

## 2. Local theorem

Take theta0=(d,eta,rho,kappa)=(1,379/500,9/10,1701/2000), beta=1-rho, delta=rho-eta, alpha=2-eta and true SW design z in (0.71859270732,0.71859270733). At SW define t=beta*z, P=alpha-t and L=alpha+2t. Define the old Stage13A firm pseudo-gradient Jacobian diagonal ell and off diagonal h, and government-policy forcing b=(p,p,r) on the AB edge, with:

ell = -kappa + 6 beta^2 (alpha-2t)(2alpha+t)/(P^2 L^4)

h = 3 beta^2 (3alpha-2t)/(P L^4)

p = 6 delta beta (alpha-2t)(2alpha+t)/(P^2 L^4)

r = 6 delta beta (alpha^2-2alpha t+4t^2)/(P^2 L^4).

At theta0: ell<0, h>0, p>0, r>0 and -ell>2h. The new adjustment penalty changes the Nash Jacobian from J0 to Jlambda=J0-lambda I without altering b. Write A=lambda-ell and det=(A+h)(A-2h)>0. Then the true unilateral firm Nash response to AB depth at g=0+ is

u'_lambda=(A p+h r)/det,
v'_lambda=(2h p+(A-h)r)/det.

The fixed-design member's welfare derivative is D= rho/L^2 - delta[2(1+2t)/L^3 + 6alpha/(P L^3)]. The correct post-design induced loss uses the **SUM**, not the erroneous PR#9 difference:

C= beta (eta+2t)/L^3,
V= 3 beta(alpha-2t)/(P L^3),
Loss(lambda)=C(2u'_lambda+v'_lambda)+V(u'_lambda+v'_lambda).

Here D>0, C>0, V>0. Hence mu(lambda)=m'_lambda(0)=D-Loss(lambda).

**Theorem (local unique crossing):** There exists a UNIQUE lambda_c>0 at which mu(lambda_c)=0. mu(lambda)<0 for lambda<lambda_c; mu(lambda)>0 for lambda>lambda_c. The existing edge-symmetry identity (i-o)'(0)=2mu(lambda) implies that both bilateral member consent and outsider inherited-depth accession consent switch at that same lambda_c. Because nu(lambda)=o'_lambda(0)>0 and i'_lambda(0)=2mu(lambda)+nu(lambda)>0 for all lambda>=0 at theta0, at each lambda>lambda_c a sufficiently small g>0 is unanimously accepted along the original sequential accession protocol. Thus a substantive positive-depth grand standard is feasible and dominates SW under the given agenda. This is local-in-g, not a unique global-in-lambda SPNE threshold.

**Proof:** The M-matrix A(lambda)=-J0+lambda I has positive diagonal, strictly negative off diagonal, and is strictly diagonally dominant. Thus A(lambda)^{-1} >= 0 and r(lambda)=A(lambda)^{-1} b>0. Differentiating with respect to lambda gives r_lambda=-A(lambda)^{-2}b<0 componentwise. Therefore Loss(lambda) is strictly decreasing and tends to zero as lambda tends to infinity. Exact Stage14 signs give Loss(0)>D>0. The intermediate value theorem and strict monotonicity give a unique lambda_c. The government direct effect at SW is independent of lambda because the adjustment term and its first derivative vanish at x=z. Monotonic outsider positivity follows from its constant direct term minus a positive-weight linear form in the decreasing responses u',v', and its exact positive value at lambda=0; similarly the grand derivative is increasing and positive at lambda=0. By continuity in g, strict vote slopes imply votes at all sufficiently small positive g. The sequence and rejecting branches are *unchanged*, and the proposer can attain strictly more than SW, proving a positive agreement is feasible and optimally preferred to fragmentation.

The original lambda=0 all-g failure is inherited, not re-proved here. By strict uniform original all-depth derivative margins and the strengthened firm Nash regularity, an epsilon>0 exists such that failure persists for all 0<=lambda<epsilon. We do not certify a numeric epsilon and do not infer global single crossing from the local crossing.

## 3. Numerical witness / rigor

z ~ 0.7185927073221111; ell ~ -0.81714003894; h ~ 0.02490822337; p ~ 0.04737114470; r ~ 0.02336820966; D ~ 0.00676792413.

lambda=0: u' ~ 0.06081023, v' ~ 0.03230482, mu ~ -0.0083018200, outsider slope nu ~ 0.367866966, grand slope i' ~ 0.351263326.
lambda=1: u' ~ 0.02662024, v' ~ 0.01358967, mu ~ +0.00024813259, outsider slope nu ~ 0.378054482, grand slope i' ~ 0.378550747.

Independent exact-rational interval checks certify mu(0.93538)<0 and mu(0.93539)>0 at the true SW root, while preserving strict response/outsider/grand signs. Program: verification/stage14rs_adjustment_cost.py.

The threshold is in units of the original design-cost curvature: lambda_c/kappa ~ 1.09981. It is NOT a calibrated real-world transaction-cost estimate.

## 4. Economic significance, limitations and priority

A counterintuitive prediction is that lowering private flexibility costs may discourage national consent to interface harmonization, because cheap **residual** redesign encourages excessive similarity and adverse consumer/rival-export-profit incidence. This differs from the conventional claim that high costs of **standard compliance** hinder harmonization. Those are distinct costs and can coexist.

The special reference value z makes the counterfactual internally controlled and could be criticized as convenient calibration. Separate historical design evidence and robustness to a neighborhood of z need confirmation before claiming external relevance. This is still a highly stylized bilateral-first inherited-g model. Allowing direct grand proposals can bypass the rejection even at lambda=0. Barrett–Yang, Cabral–Salant, Lambertini–Rossini, Cheng–Huang and relevant dynamic/protocol theory MUST be checked proposition by proposition. An M-matrix comparative static or interpolation across two known models is not automatically priority-worthy: the alleged incremental discovery must be the interaction with *national consent constraints*.

Recommended claim scope: "At a certified primitive configuration under a specified sequential accession procedure, higher costs of residual product redesign can restore governmental consent to standards harmonization, with a unique local threshold in design-adjustment curvature."

No general welfare optimum, empirical identification, arbitrary-depth threshold, all-demand-function robustness, or unconditional journal-ready novelty is established.
