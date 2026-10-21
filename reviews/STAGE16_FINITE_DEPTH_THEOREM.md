# Stage16 certified positive finite-depth standards agreement

**Only new primitive relative to V2b:** K_i(x_i;lambda)=kappa(1-x_i)^2/2 + lambda(x_i-z)^2/2, where z is a fixed pre-agreement legacy design. All technology/network/quantity government menus unchanged.

## Theorem (finite-depth robust protocol feasibility at theta0)
At (d,eta,rho,kappa)=(1,379/500,9/10,1701/2000), g=1/20 and EVERY lambda ∈ [499/100,501/100], the specified bilateral-first/inherited-g three-country standards accession protocol has a strictly acceptable AB -> ABC path: bilateral members prefer AB to fragmentation, entrant C prefers ABC to remaining outside AB, incumbents prefer ABC to AB, and every country prefers ABC to SW. Both the AB and ABC downstream firm-design Nash equilibria are interior and unique under the inherited sufficient global Rosen diagonal-dominance bound. By continuity, the strict inequalities also persist in a neighborhood of the specified primitive vector, but no explicit radius for that theta neighborhood is provided.

**A stronger distinction at other adjustment costs:** at the same g, lambda=2 yields a strict positive AB member margin but a negative entrant-C accession margin; lambda=4 also has negative entrant-C margin, even while bilateral members strictly favor AB. Therefore crossing a bilateral-vote threshold does not itself ensure outsider accession. Combining strict lambda=4 rejection and lambda=5 acceptance plus continuity establishes existence of a finite-g entrant-vote root in (4,5), but does NOT prove uniqueness, monotonicity across lambda, or a universal equilibrium threshold. Independently computed approximate root = 4.084605682068487 (not a certified interval enclosure).

## Verified strict rational enclosures
All country welfare differences are exact rational intervals enclosing the unique root boxes; decimals are only display summaries:

| lambda | AB-member vs SW | entrant C (IS-SU) | IS vs SW (each country) |
|---:|---:|---:|---:|
| 2 | [6.60320e-5,6.63604e-5] | [-1.77008e-4,-1.76339e-4] | [0.01865455,0.01865489] |
| 4 | [1.52597e-4,1.52927e-4] | [-4.49671e-6,-3.82923e-6] | [0.01893281,0.01893315] |
| 5 | [1.73352e-4,1.73681e-4] | [3.68992e-5,3.75668e-5] | [0.01899962,0.01899997] |
| [4.99,5.01] | [1.57093e-4,1.89939e-4] | [3.85096e-6,7.06149e-5] | [0.01898291,0.01901668] |

Incumbent extension IS-SU is also strictly positive for all certified cases.

## Independent proof method
1. Bracket the pre-agreement SW Nash z with >100 bisection steps under exact Fraction arithmetic and verify F(z_left)>0>F(z_right), yielding width less than 10^-30.
2. Express fulfilled Cournot M matrix with M_ii=2-eta, M_ij=delta*H_ij+beta*(x_i+x_j)/2. Invert with an independent analytic adjugate, derive q_i and each firm's unilateral FOC 6q_i (dq_i/dx_i)+kappa(1-x_i)-lambda(x_i-z), and exact FOC Jacobian via M_x derivatives.
3. Restrict the symmetric AB Nash to x=(u,u,v) and full IS to x=(y,y,y). Use the exact Krawczyk inclusion x0-AF(x0)+(I-AJ(X))(X-x0) in the interior of a rational box of radius 10^-7 for each lambda=2,4,5. For the uniform lambda band, use radius 10^-5 and interval lambda throughout in the same inclusion. Brouwer establishes a root for every lambda in the band.
4. Full THREE-FIRM global Nash uniqueness follows by the inherited strict Rosen sufficient inequality kappa+lambda>54 beta^2/(eta^2(2-eta)^2), stronger than lambda=0. The symmetric roots are therefore the actual three-player Nash equilibria, not restricted candidate best responses.
5. Enclose all quantities, B and CS=q'Bq/2, and once-paid Pi_i=3q_i²-kappa(1-x_i)²/2-lambda(x_i-z)²/2 in exact rational intervals. Check strict margins against interval SW welfare.
6. The direct-stage time ordering and outsider-inherited-g consent are exactly the original PR13 procedure. This theorem is PROTOCOL-FEASIBILITY, not a claim of a particular government global optimum or coalition-proof stability.

**Code:** `verification/stage16_fixed_depth_certificate.py` runs with Python stdlib only, imports NO original V2b verifier and has an independent GitHub Actions test.

## Scope boundaries
The theorem fixes g=0.05; it does not assert this depth is internationally optimal, economically empirically large, a 5% technical standard, or globally stable against alternate menus/transfers. It does NOT certify every lambda in [4,5] or the entire feasible g set. It is a rigorous fixed-depth counterexample of an economically distinct outsider veto margin.
