# Q870: Subgradient dominance for state-rectangular transition uncertainty

## Source and exact scope

Toshinori Kitamura, Arnob Ghosh, Alex Ayoub, Thang D. Chu and Csaba Szepesvári, *Revisiting Subgradient Dominance in Robust MDPs: Counterexamples, Hardness, and Sufficient Conditions*, [arXiv:2604.21177v2, §5 Open questions, printed/PDF p. 10](https://arxiv.org/pdf/2604.21177v2#page=10):

> We conjecture that s-rectangular RMDPs satisfy the subgradient dominance property

The [author's publication list](https://syuntoku14.github.io/publication/) lists NeurIPS 2026 and links to arXiv. The [conference index](https://neurips.cc/Downloads/2026) lists poster 153998, but no separate proceedings full text was verified as publicly available before the December meeting. The latest verified full text is the authors' October 8 v2; the pagination here is that edition.

Let S and A be finite, c(s,a) fixed, γ∈[0,1), and μ a full-support initial distribution. Let K=∏_s K_s be compact and nonempty, where each K_s consists of entire action-indexed rows of probability distributions over S; each K_s may couple the actions and need not be convex. For stationary randomized π write J_P(π)=μᵀv_P^π and J(π)=max_{P∈K}J_P(π). Take the direct-policy Fréchet subdifferential in the source's ambient extension. We prove the pinned fixed-cost conjecture with D=1/[(1−γ)min_s μ(s)], for **every** subgradient, not just a selected active gradient.

## Proof

**1. All active models have the same vector value.** At fixed π the state-rectangular Bellman operator sends v to the vector with component
    T(v)(s)=Σ_a π(a|s)c(s,a) + γ max_{p∈K_s} Σ_a π(a|s) p_a·v.
It is monotone and a γ-contraction. At its fixed point V choose a maximizing whole row at every state. Rectangularity places their product in K, and this kernel has value vector V. Each other P∈K has v_P^π≤V: its ordinary operator is bounded above by T, so iteration from V under that operator can only decrease to v_P^π. Thus J(π)=μᵀV. If P is active for J at π, full support of μ implies v_P^π=V componentwise. Also enlarge K to K'=∏_s conv(K_s). Every fixed-policy robust Bellman operator is unchanged, because the optimized expression is linear in the *whole* state row. Hence J is unchanged on the policy set.

**2. Realize any subgradient by a single active model in K'.** The source's Lemma 2.1 (or the smooth maximum rule and Carathéodory) writes each g∈∂J(π) as a finite convex combination Σ_i λ_i∇J_{P_i}(π) of active gradients from K. All these models have the common vector value V by Step 1. Define the normalized state occupancy d_i(s)=(1−γ)Σ_(t≥0) γ^t Pr_{π,P_i}(S_t=s). Put d(s)=Σ_i λ_i d_i(s)>0 and form the entire row
    Pbar(·|s,a)=Σ_i [λ_i d_i(s)/d(s)] P_i(·|s,a),  simultaneously for all a.
The weights depend on the state but not on the action; thus Pbar∈K'. Averaging the active models' statewise Bellman equations with these weights gives v_Pbar^π=V. Averaging their occupancy flow identities gives
    d(t)=(1−γ)μ(t)+γ Σ_s d(s) Σ_a π(a|s) Pbar(t|s,a).
The solution is unique, so d is precisely the discounted occupancy of π under Pbar.

For fixed P, the derivative at π in the direct ambient extension is
    ∇J_P(π)(s,a)=d_P^π(s)/(1−γ) [c(s,a)+γ P(·|s,a)·v_P^π].
This follows by differentiating the equations v_P=c_π+γ P_π v_P, or by the policy-gradient identity. Since V is common, the bracket is affine in each full state row. Substituting the occupancy-weighted row above proves ∇J_Pbar(π)=g entry by entry. We use the original subdifferential representation and never assume that convexification preserves extensions or gradients away from feasible policies.

**3. One fixed-model performance difference controls robust suboptimality.** Let π* minimize J over the compact policy set. Because Pbar is active at π and belongs to K', we have J(π)−J(π*)≤J_Pbar(π)−J_Pbar(π*). Write Q(s,a)=c(s,a)+γ Pbar(·|s,a)·V and b(s)=V(s)−min_a Q(s,a)≥0. The fixed-model performance-difference identity gives
    J_Pbar(π)−J_Pbar(π*)=(1/(1−γ)) Σ_s d_Pbar^π*(s) [V(s)−Σ_a π*(a|s)Q(s,a)]
                         ≤(1/(1−γ)) Σ_s d_Pbar^π*(s) b(s).
The identity follows by applying the resolvent of Pbar under π* to the difference of the two value vectors. On the other hand,
    max_(π'∈Π) ⟨π−π',g⟩=(1/(1−γ)) Σ_s d(s)b(s)
since the maximum over each policy row chooses a minimizing action for Q. The occupancy d(s) is at least (1−γ)μ(s), and d_Pbar^π*(s)≤1. Comparing the two nonnegative sums proves the bound for this g. Since g was arbitrary, taking the minimum over all subgradients proves the conjectured inequality. If one uses the constrained subdifferential by adding feasible-set outward normals to the ambient subdifferential, they contribute ⟨π−π',normal⟩≥0 for every feasible π', so the same inequality holds in that convention.
