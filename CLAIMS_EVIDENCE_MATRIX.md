# Claims and evidence

| Claim | Evidence |
| --- | --- |
| Every-subgradient dominance for the fixed-cost state-rectangular model | [Theorem 1 and §4](paper/manuscript.pdf) |
| A single feasible convexified kernel realizes any chosen subgradient | [§§2–3](paper/manuscript.pdf) |
| Exact occupancy and gradient identities for worked cases | [Replay](verification/results/replay.txt) |
| Meaning of the rotating bars and row weights | [Worked example](proof/worked-occupancies.md) |
| Original conjecture and prior theorem scope | [Primary sources](audits/public_safe_reports/LITERATURE.md) |

## Partial Lean verification

For arbitrary finite state and model lists, rational weights and nonzero state normalizers, summing the occupancy-reweighted kernel row against state mass and policy equals the mixture of the incoming model flows, for a fixed action and destination. [Scope, source and replay](formalization/README.md)
