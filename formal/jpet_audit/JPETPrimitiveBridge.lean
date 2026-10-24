import Mathlib

/-!
Stage 1b: symbolic matrix and national-welfare incidence cross-checks.

All equalities are quantified over arbitrary real primitives with explicit
nonzero denominators, NOT just one rational witness. The quantity derivatives
are checked against the Cournot differentiated Mq=d1 linear system. This verifies
the algebra in Appendix A given the primitive private-design coupling X_ij
=(x_i+x_j)/2 and symmetry at fragmentation. Analytic differentiability of the
global Nash selection, Rosen uniqueness and the Python all-depth certificate are
outside this file.
-/

namespace V2b.JPET

noncomputable section

def qSym (d L : ℝ) : ℝ := d / L
def dxOwn (beta alpha d P L : ℝ) : ℝ :=
  -(beta * alpha * (d/L)) / (P*L)
def dxOther (beta alpha t d P L : ℝ) : ℝ :=
  -(beta*(alpha-2*t)*(d/L)) / (2*P*L)

/-- The design sensitivity formulas actually solve the full symmetric
3-firm COURNOT LINEARIZED SYSTEM under a unilateral increase in x_A.
No assumption of coordinated redesign enters. -/
theorem own_design_quantity_matrix_rows
    (beta alpha t d P L : ℝ)
    (hP : P=alpha-t) (hL : L=alpha+2*t)
    (hPnz : P ≠ 0) (hLnz : L ≠ 0) :
    alpha * dxOwn beta alpha d P L
      + 2*t * dxOther beta alpha t d P L = -beta*qSym d L ∧
    t * dxOwn beta alpha d P L
      + (alpha+t)*dxOther beta alpha t d P L = -(beta*qSym d L)/2 := by
  subst P
  subst L
  dsimp [dxOwn, dxOther, qSym]
  have hSquare : t*alpha*4 + t^2*4 + alpha^2 = (alpha+2*t)^2 := by ring
  constructor
  · field_simp [hPnz, hLnz]
    <;> ring
  · have hLnonzero : alpha + t*2 ≠ 0 := by
      have heq : alpha + t*2 = alpha + 2*t := by ring
      rw [heq]
      exact hLnz
    field_simp [hPnz, hLnz, hLnonzero]
    <;> ring

/-- At the symmetric fragmentation reference, the total domestic CS
effect from changing x_A: direct B-link changes plus three q responses. -/
def consumerDesignSlope (beta t q ownDQ otherDQ : ℝ) : ℝ :=
  beta*q*q + (1+2*t)*q*(ownDQ+2*otherDQ)

/-- This is C as defined in the current JPET manuscript. -/
def consumerC (beta d eta t L : ℝ) : ℝ :=
  beta*d*d*(eta+2*t)/(L*L*L)

theorem consumer_incidence_exact
    (beta alpha d eta t P L : ℝ)
    (hP : P=alpha-t) (hL : L=alpha+2*t)
    (hAlpha : alpha=2-eta)
    (hPnz : P ≠ 0) (hLnz : L ≠ 0) :
    consumerDesignSlope beta t (qSym d L)
      (dxOwn beta alpha d P L) (dxOther beta alpha t d P L)
      = -consumerC beta d eta t L := by
  subst P
  subst L
  subst alpha
  dsimp [consumerDesignSlope, consumerC, dxOwn, dxOther, qSym]
  field_simp [hPnz, hLnz]
  <;> ring

/-- This is the incremental rival-firm worldwide-profit incidence V. -/
def rivalV (beta alpha d t P L : ℝ) : ℝ :=
  3*beta*d*d*(alpha-2*t)/(P*L*L*L)

theorem rival_profit_incidence_exact
    (beta alpha d t P L : ℝ)
    (hPnz : P ≠ 0) (hLnz : L ≠ 0) :
    6 * qSym d L * dxOther beta alpha t d P L
      = -rivalV beta alpha d t P L := by
  dsimp [qSym, dxOther, rivalV]
  field_simp [hPnz, hLnz]
  <;> ring

/-- The D formula is verified by adding a direct CS effect and
the three-market resident firm's operating-profit quantity response. -/
def directCS (rho delta d t L : ℝ) : ℝ :=
  rho*d*d/(L*L) - 2*delta*(1+2*t)*d*d/(L*L*L)
def dProfitFixed (delta alpha d P L : ℝ) : ℝ :=
  6*(d/L)*(-(delta*alpha*(d/L))/(P*L))
def fixedD (rho delta alpha d t P L : ℝ) : ℝ :=
  rho*d*d/(L*L) -
    (delta*d*d/(L*L*L))*(2*(1+2*t)+6*alpha/P)

theorem fixed_design_direct_incidence_exact
    (rho delta alpha d t P L : ℝ)
    (hPnz : P ≠ 0) (hLnz : L ≠ 0) :
    directCS rho delta d t L + dProfitFixed delta alpha d P L
      = fixedD rho delta alpha d t P L := by
  dsimp [directCS, dProfitFixed, fixedD]
  field_simp [hPnz, hLnz]
  <;> ring

end

end V2b.JPET
