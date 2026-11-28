# Occupancy-weighted incoming flow

For arbitrary finite state and model lists, rational weights and nonzero state normalizers, summing the occupancy-reweighted kernel row against state mass and policy equals the mixture of the incoming model flows, for a fixed action and destination.

This verifies the finite rearrangement in the displayed discounted occupancy equation. The smooth maximum rule, uniqueness from the resolvent, gradient identity as a derivative, and subgradient dominance remain in the manuscript.

[Lean source](Q870Flow.lean) · [Mathematical source](../paper/manuscript.tex) · [Expected axiom report](expected-axioms.txt)

Replay from this directory with Lean 4.30.0 and its standard library.

```sh
lean -DwarningAsError=true Q870Flow.lean > axioms.actual
diff -u expected-axioms.txt axioms.actual
```
