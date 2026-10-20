/-
 V2b Stage 7.5A | Lean 4 proof-critical EXACT-RATIONAL CORE
 Proof assistant: Lean 4 (toolchain pinned at repo root).
 NO mathlib imported, NO axioms, NO sorry/admit.

 WHAT IS ENCODED:
 Closed-form consumer surplus / national welfare in frozen nonlinear
 residual-similarity model X_ij=(x_i^2+x_j^2)/2.
 At a rational proxy 0.610737479601 for the SW Nash design, the
 (1) frozen C participation at g=.005 is strictly positive;
 (2) the original pre-registered g=.05 C participation is NEGATIVE;
 (3) IS exceeds SW at g=.005;
 (4) an independent proxy for endogenous IS Nash design at g=.05
 yields a Pareto welfare gain over SW.

 IMPORTANT LIMITATION:
 This Lean file does NOT prove that the rational design proxies equal the
 unique best-response Nash roots; the roots are algebraic and lie in
 separately certified rational intervals in the Python Stage 4A files.
 It does NOT prove a quantified sign for every real g, full SPNE,
 market equilibrium, Rosen concavity or economic primitives.
 Accordingly, it is a useful proof-critical payoff SIGN CROSSCHECK, NOT
 "FORMAL VERIFICATION PASS" for the entire headline at this point.
-/
import Init

set_option maxRecDepth 5000
set_option maxHeartbeats 0

namespace V2b.Stage075A

def eta : Rat := 379 / 500
def rho : Rat := 9 / 10
def kappa : Rat := 1701 / 2000
def beta : Rat := 1 - rho
def a : Rat := 2 - eta

def xSWproxy : Rat := 610737479601 / 1000000000000
def xISproxy : Rat := 617707153937 / 1000000000000

/-- International union, all three x equal; national CS + home global profit
    minus ONE-TIME home-firm design investment. -/
def international (g x : Rat) : Rat :=
  let t := (rho-eta)*g + beta*x*x
  let q := 1 / (a + 2*t)
  (9/2 + 3*(rho*g + beta*x*x))*q*q - kappa*(1-x)*(1-x)/2

/-- AB standards union, all x frozen at identical proxy x. 3 goods in 3 markets.
    Returns member and outsider national welfare. -/
def suMember (g x : Rat) : Rat :=
  let m := (rho-eta)*g + beta*x*x
  let n := beta*x*x
  let d := a*(a+m) - 2*n*n
  let qm := (a-n)/d
  let qo := (a+m-2*n)/d
  let cs := (1+rho*g+beta*x*x)*qm*qm + qo*qo/2 + 2*n*qm*qo
  cs + 3*qm*qm - kappa*(1-x)*(1-x)/2

def suOutsider (g x : Rat) : Rat :=
  let m := (rho-eta)*g + beta*x*x
  let n := beta*x*x
  let d := a*(a+m) - 2*n*n
  let qm := (a-n)/d
  let qo := (a+m-2*n)/d
  let cs := (1+rho*g+beta*x*x)*qm*qm + qo*qo/2 + 2*n*qm*qo
  cs + 3*qo*qo - kappa*(1-x)*(1-x)/2

/-- Numerically vulnerable strict fixed-x C accession at g=1/200. -/
theorem frozen_c_participation_small :
  suOutsider (1/200) xSWproxy <
  international (1/200) xSWproxy := by decide +kernel

/-- Keep the PRE-REGISTERED g=.05 failure visible in the FORMAL layer. -/
theorem frozen_c_participation_failed_at_original_depth :
  international (1/20) xSWproxy <
  suOutsider (1/20) xSWproxy := by decide +kernel

/-- Frozen international policy strictly beats complete separation at g=.005. -/
theorem frozen_international_better_than_sw :
  international 0 xSWproxy <
  international (1/200) xSWproxy := by decide +kernel

/-- Nonlinear actual-design rational PROXIES: international g=.05 is Pareto
    better than SW; Nash identity is NOT established inside Lean. -/
theorem endogenous_proxy_pareto_gain :
  international 0 xSWproxy <
  international (1/20) xISproxy := by decide +kernel

#print axioms frozen_c_participation_small
#print axioms frozen_c_participation_failed_at_original_depth
#print axioms frozen_international_better_than_sw
#print axioms endogenous_proxy_pareto_gain

end V2b.Stage075A
