import Std
namespace Occupancy
def sum (v : List X) (f : X → Rat) : Rat :=
  match v with
  | [] => 0
  | h::t => f h + sum t f
theorem add (v : List X) (f g : X → Rat) :
    sum v (fun i => f i + g i) = sum v f + sum v g := by
  induction v with | nil => simp only [sum]; grind | cons h t ih => simp only [sum]; grind
theorem scale (c : Rat) (v : List X) (f : X → Rat) :
    sum v (fun i => c*f i) = c*sum v f := by
  induction v with | nil => simp only [sum]; grind | cons h t ih => simp only [sum]; grind
theorem congr (v : List X) (f g : X → Rat) (h : ∀ x ∈ v, f x=g x) : sum v f=sum v g := by
  induction v with
  | nil => rfl
  | cons a v ih =>
    have aa := h a (by simp)
    have bb := ih (fun x hx => h x (by simp [hx]))
    simp only [sum]; grind
theorem swap (v : List X) (w : List Y) (f : X → Y → Rat) :
    sum v (fun x => sum w (f x)) = sum w (fun y => sum v (fun x => f x y)) := by
  induction v with
  | nil =>
    have z : sum w (fun _ => (0:Rat)) = 0 := by
      induction w with | nil => rfl | cons a w ih => simp only [sum,ih]; grind
    simpa only [sum] using z.symm
  | cons x xs ih =>
    simp only [sum]
    rw [add, ih]
/-- Across finitely many states and model indices, occupancy-weighted
kernel rows preserve the incoming flow for each destination and action.
Here d(s) may be any nonzero row normalizer, including the mixed occupancy. -/
theorem incoming (states : List S) (models : List I) (w : I → Rat)
    (occ : I → S → Rat) (row : I → S → Rat) (policy d : S → Rat)
    (pos : ∀ s ∈ states, d s ≠ 0) :
    sum states (fun s => d s * policy s * (sum models (fun i => w i * occ i s * row i s) / d s)) =
    sum models (fun i => w i * sum states (fun s => occ i s * policy s * row i s)) := by
  calc
    _ = sum states (fun s => sum models (fun i => w i * (occ i s * policy s * row i s))) := by
      apply congr; intro s hs
      calc
        _ = policy s * sum models (fun i => w i * occ i s * row i s) := by
          have hn := pos s hs
          have hx := Rat.div_mul_cancel (a := sum models (fun i => w i * occ i s * row i s)) hn
          grind
        _ = sum models (fun i => policy s * (w i * occ i s * row i s)) := (scale _ _ _).symm
        _ = _ := by apply congr; intro i _; grind
    _ = _ := by
      rw [swap]
      apply congr; intro i _; apply scale
#print axioms incoming
end Occupancy
