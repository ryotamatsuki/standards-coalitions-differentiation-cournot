import Mathlib

/-!
Lean calculus gate for the LOCAL JPET theorem. Unlike a sign check on raw
derivative coefficients, this proves that derivatives at the zero policy
boundary imply the claimed strict PAYOFF comparisons for all sufficiently
small positive depths. Differentiability of the *actual economic Nash payoff
functions* and the analytic derivative identities are named assumptions.
The theorem does NOT assert full-game verification or an interval certificate.
-/
namespace V2b.JPET

open Filter SignType

/-- Classical calculus: a strictly positive derivative at a zero payoff gap
implies a strictly positive gap throughout some right neighborhood. -/
theorem positive_right_of_positive_derivative
    (f : ℝ → ℝ) (k : ℝ)
    (hf : HasDerivAt f k 0) (hzero : f 0 = 0) (hk : 0 < k) :
    ∀ᶠ g in 𝓝[>] (0:ℝ), 0 < f g := by
  have hderiv : 0 < deriv f 0 := by simpa [hf.deriv] using hk
  have hsign := eventually_nhdsWithin_sign_eq_of_deriv_pos hderiv hzero
  filter_upwards [hsign.filter_mono (nhdsWithin_le_nhds), self_mem_nhdsWithin] with g hsign hg
  have hpositive : 0 < g := hg
  have heq : sign (f g) = 1 := by simpa [sign_pos hpositive] using hsign
  exact sign_eq_one_iff.mp heq

theorem negative_right_of_negative_derivative
    (f : ℝ → ℝ) (k : ℝ)
    (hf : HasDerivAt f k 0) (hzero : f 0 = 0) (hk : k < 0) :
    ∀ᶠ g in 𝓝[>] (0:ℝ), f g < 0 := by
  have hneg : HasDerivAt (fun x => - f x) (-k) 0 := hf.neg
  have hzero_neg : (fun x => - f x) 0 = 0 := by simp [hzero]
  have hpos := positive_right_of_positive_derivative
    (fun x => - f x) (-k) hneg hzero_neg (by linarith)
  filter_upwards [hpos] with x hx
  exact neg_pos.mp hx

/-- Fully formal LOCAL VOTING consequence of the seven model-specific
payoff derivatives. No policy-depth grid and no external arithmetic used here.
The seven derivative identities (not their implications) are the supplied
mathematical interface to the model's implicit Nash derivatives. -/
theorem local_economic_participation_reversal
    (s D L nuF nuN : ℝ)
    (mF oF iF mN oN iN : ℝ → ℝ)
    (hD : 0 < D) (hLoss : D < L)
    (hNuF : -D < nuF) (hNuN : -2*(D-L) < nuN)
    (hZeroF : mF 0 = s ∧ oF 0 = s ∧ iF 0 = s)
    (hZeroN : mN 0 = s ∧ oN 0 = s ∧ iN 0 = s)
    (hFm : HasDerivAt (fun g => mF g - s) D 0)
    (hFa : HasDerivAt (fun g => iF g - oF g) (2*D) 0)
    (hFb : HasDerivAt (fun g => iF g - mF g) (D+nuF) 0)
    (hFi : HasDerivAt (fun g => iF g - s) (2*D+nuF) 0)
    (hNm : HasDerivAt (fun g => mN g - s) (D-L) 0)
    (hNa : HasDerivAt (fun g => iN g - oN g) (2*(D-L)) 0)
    (hNi : HasDerivAt (fun g => iN g - s) (2*(D-L)+nuN) 0) :
    ∀ᶠ g in 𝓝[>] (0:ℝ),
      (mF g > s ∧ iF g > oF g ∧ iF g > mF g ∧ iF g > s) ∧
      (mN g < s ∧ iN g < oN g ∧ iN g > s) := by
  have hFm0 : (fun g => mF g - s) 0 = 0 := by simp [hZeroF.1]
  have hFa0 : (fun g => iF g - oF g) 0 = 0 := by
    simp [hZeroF.2.1, hZeroF.2.2]
  have hFb0 : (fun g => iF g - mF g) 0 = 0 := by
    simp [hZeroF.1, hZeroF.2.2]
  have hFi0 : (fun g => iF g - s) 0 = 0 := by simp [hZeroF.2.2]
  have hNm0 : (fun g => mN g - s) 0 = 0 := by simp [hZeroN.1]
  have hNa0 : (fun g => iN g - oN g) 0 = 0 := by
    simp [hZeroN.2.1, hZeroN.2.2]
  have hNi0 : (fun g => iN g - s) 0 = 0 := by simp [hZeroN.2.2]
  have pFm := positive_right_of_positive_derivative _ D hFm hFm0 hD
  have pFa := positive_right_of_positive_derivative _ (2*D) hFa hFa0 (by linarith)
  have pFb := positive_right_of_positive_derivative _ (D+nuF) hFb hFb0 (by linarith)
  have pFi := positive_right_of_positive_derivative _ (2*D+nuF) hFi hFi0 (by linarith)
  have pNm := negative_right_of_negative_derivative _ (D-L) hNm hNm0 (by linarith)
  have pNa := negative_right_of_negative_derivative _ (2*(D-L)) hNa hNa0 (by linarith)
  have pNi := positive_right_of_positive_derivative _ (2*(D-L)+nuN) hNi hNi0 (by linarith)
  filter_upwards [pFm,pFa,pFb,pFi,pNm,pNa,pNi] with g a b c d e f h
  constructor
  · constructor
    · linarith
    constructor
    · linarith
    constructor
    · linarith
    · linarith
  · constructor
    · linarith
    constructor
    · linarith
    · linarith

end V2b.JPET
