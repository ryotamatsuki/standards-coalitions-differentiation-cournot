/-!
JPET final pre-submission formal audit -- CURRENT linear residual-design specification.
NO sorry / admit / axiom. Mathlib pinned to Lean v4.24.0.

Formal trust boundaries:
* Cournot row: derived from the primitive inverse-price expression and a private FOC.
* Welfare: a transparent sum of consumer surplus, worldwide profit, and design cost;
  partial derivative VALUES (-C and -V) are stated as hypotheses -- not yet
  derived from the full matrix demand, firm optimization and Nash equation.
* Incidence: exact abstract permutation-symmetric edge calculus.
* Participation: rational/real arithmetic transfer from explicit primitive sign
  assumptions. Does NOT import externally computed all-depth interval certificates.
No claim of full Nash existence, all-g interval verification or full SPNE inside Lean.
-/
import Mathlib

namespace V2b.JPET

/-- A representative destination market's inverse price, under fulfilled
network expectations. B_AA = H_AA = 1. The FOC is private, not joint profit. -/
def inversePriceA
    (c d eta hAB hAC bAB bAC qA qB qC : ℝ) : ℝ :=
  c + d - qA - bAB*qB - bAC*qC
    + eta * (qA + hAB*qB + hAC*qC)

/-- (I+B-ηH)q=d1: its A row follows from the Cournot FOC and primitive price. -/
theorem cournot_row_from_primitive_price
    (c d eta hAB hAC bAB bAC qA qB qC : ℝ)
    (hFOC : inversePriceA c d eta hAB hAC bAB bAC qA qB qC - c = qA) :
    (2-eta)*qA + (bAB-eta*hAB)*qB + (bAC-eta*hAC)*qC = d := by
  dsimp [inversePriceA] at hFOC
  nlinarith only [hFOC]

/-- At fragmentation with symmetric outputs, the symmetric matrix row
gives the simple closed-form output. The nonzero denominator is explicit. -/
theorem symmetric_quantity_inversion (d eta t q : ℝ)
    (hFOC : (2-eta)*q + t*q + t*q = d)
    (hdenom : 2-eta+2*t ≠ 0) :
    q = d / (2-eta+2*t) := by
  apply (eq_div_iff hdenom).2
  nlinarith only [hFOC]

/-- Primitive decomposition of A's national welfare at the chosen path:
domestic consumer surplus + worldwide resident-firm profit - one-time cost. -/
def nationalWelfare (cs pi designCost : ℝ → ℝ) (g : ℝ) : ℝ :=
  cs g + pi g - designCost g

theorem nationalWelfare_derivative
    (cs pi designCost : ℝ → ℝ) (cc pp kk : ℝ)
    (hCS : HasDerivAt cs cc 0)
    (hPi : HasDerivAt pi pp 0)
    (hCost : HasDerivAt designCost kk 0) :
    HasDerivAt (nationalWelfare cs pi designCost) (cc+pp-kk) 0 := by
  exact (hCS.add hPi).sub hCost

/-- Consumer incidence from three unilateral design changes and rival
world-profit incidence. The own-profit/own-cost envelope is explicit. -/
def inducedLoss (C V u v : ℝ) : ℝ :=
  C * (2*u+v) + V * (u+v)

def welfareSlopeFromPrimitives
    (direct csA csB csC ownProfit ownCost crossProfit u v : ℝ) : ℝ :=
  direct + csA*u + csB*u + csC*v
    + ownProfit*u - ownCost*u + crossProfit*(u+v)

/-- Formal algebraic bridge: specifying the three CS partials, the
own-profit/own-cost FOC and rivals' worldwide profit response yields D-L.
This does NOT assume the desired national welfare formula directly. -/
theorem national_incidence_from_components
    (D C V u v ownProfit ownCost : ℝ)
    (hEnvelope : ownProfit = ownCost) :
    welfareSlopeFromPrimitives D (-C) (-C) (-C)
      ownProfit ownCost (-V) u v
      = D - inducedLoss C V u v := by
  dsimp [welfareSlopeFromPrimitives, inducedLoss]
  rw [hEnvelope]
  ring

/-- First-order effect on country A of independently varied country-pair links,
under the *hypothesized* permutation symmetry of national welfare. -/
def edgeResponseA (mu nu ab ac bc : ℝ) : ℝ :=
  mu*ab + mu*ac + nu*bc

/-- A link AB activates one incident edge; all three links activate two
incident and one nonincident edges for A. -/
theorem edge_incidence (mu nu : ℝ) :
    edgeResponseA mu nu 1 0 0 = mu ∧
    edgeResponseA mu nu 0 0 1 = nu ∧
    edgeResponseA mu nu 1 1 1 = 2*mu+nu ∧
    (edgeResponseA mu nu 1 1 1 -
      edgeResponseA mu nu 0 0 1) = 2*mu ∧
    (edgeResponseA mu nu 1 1 1 -
      edgeResponseA mu nu 1 0 0) = mu+nu := by
  unfold edgeResponseA
  constructor
  · ring
  constructor
  · ring
  constructor
  · ring
  constructor
  · ring
  · ring

/-- Strict controlled local slope reversal, independent of any numerical
search. This is the purely algebraic consequence of two incidence lemmas. -/
theorem local_participation_slope_reversal
    (D L nuN nuF : ℝ)
    (hD : 0 < D) (hLoss : D < L)
    (hGrandN : -(2*(D-L)) < nuN)
    (hIncumbentF : -D < nuF) :
    0 < D ∧ D-L < 0 ∧
    0 < 2*D ∧ 2*(D-L) < 0 ∧
    0 < 2*(D-L)+nuN ∧
    0 < D+nuF ∧
    0 < 2*D+nuF := by
  constructor
  · exact hD
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  · linarith

/-- The protocol's actual enlargement requires ALL three levels:
strictly positive direct-grand welfare i>s by itself is not enough. -/
def inheritedDepthIntegration (s m o i : ℝ) : Prop :=
  i ≥ s ∧ i ≥ m ∧ i ≥ o

def standAloneBilateral (s m : ℝ) : Prop := m ≥ s

/-- Strict all-depth welfare barriers exclude each inherited-depth proposal,
while allowing direct integration to Pareto improve on fragmentation. -/
theorem accession_veto_and_direct_grand
    (s m o i : ℝ)
    (hMember : m < s) (hOutsider : i < o) (hDirect : s < i) :
    ¬ inheritedDepthIntegration s m o i ∧
    ¬ standAloneBilateral s m ∧ s < i := by
  constructor
  · intro h
    exact (not_le.mpr hOutsider) h.2.2
  constructor
  · intro h
    exact (not_le.mpr hMember) h
  · exact hDirect

/-- External computer certification may be imported only as explicitly
stated, strictly uniform *level* enclosures. Here the implication to actual
participation is kernel checked; the source of bounds is NOT Lean-certified. -/
theorem whole_menu_rejection_conditional
    (s : ℝ) (m o i : ℝ → ℝ) (am ao : ℝ)
    (hAm : 0 < am) (hAo : 0 < ao)
    (hMemberBound : ∀ g, 0 < g → g ≤ 1 → m g - s ≤ -am*g)
    (hOutsiderBound : ∀ g, 0 < g → g ≤ 1 → i g - o g ≤ -ao*g) :
    ∀ g, 0 < g → g ≤ 1 →
      ¬ inheritedDepthIntegration s (m g) (o g) (i g) ∧
      ¬ standAloneBilateral s (m g) := by
  intro g hg hle
  have hm := hMemberBound g hg hle
  have ho := hOutsiderBound g hg hle
  have hmstrict : m g < s := by nlinarith [mul_pos hAm hg]
  have hostrict : i g < o g := by nlinarith [mul_pos hAo hg]
  constructor
  · intro h
    exact (not_le.mpr hostrict) h.2.2
  · intro h
    exact (not_le.mpr hmstrict) h

/-- Purely logical frozen-case witness: an approved direct integrated payoff
that exceeds the global bilateral envelope dominates every bilateral fallback. -/
theorem frozen_witness_dominates_all_bilaterals
    (s : ℝ) (m : ℝ → ℝ) (o i gstar : ℝ)
    (hAccepted : i ≥ s ∧ i ≥ m gstar ∧ i ≥ o)
    (hEnvelope : ∀ g, 0 ≤ g → g ≤ 1 → m g < i) :
    inheritedDepthIntegration s (m gstar) o i ∧
    (∀ g, 0 ≤ g → g ≤ 1 → m g < i) := by
  exact ⟨hAccepted, hEnvelope⟩

end V2b.JPET
