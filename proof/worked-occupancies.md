# Three states and two active kernels

The states are 0, 1 and 2. The law μ is uniform, the discount is 1/2, and each action is chosen with probability 1/2. Both actions cost 3/16 in states 0 and 1, and 7/16 in state 2.

The set of whole rows at every state contains the two deterministic rows below.

| Row | Action a | Action b |
| --- | --- | --- |
| First | Move to 0 | Move to 2 |
| Second | Move to 2 | Move to 1 |

Both rows yield a continuation value of 5/8 against V=(1/2,1/2,3/4). The discounted continuation is 5/16. Adding the stated costs recovers V, so all eight statewise row selections tie. Let P₁ use only first rows and P₂ use only second rows. From time 1 their state distributions are constant at (1/2,0,1/2) and (0,1/2,1/2). Their normalized discounted occupancies are therefore d₁=(5/12,1/6,5/12) and d₂=(1/6,5/12,5/12).

For the average of the two active gradients, the combined occupancy is (7/24,7/24,5/12). The weight of P₁ in state s is d₁(s)/[d₁(s)+d₂(s)]. In states 0, 1 and 2 these weights are 5/7, 2/7 and 1/2. Each weight applies jointly to both actions. The convexified kernel has the same value vector and realizes the average gradient. These identities also hold for every convex gradient weight λ, with local coefficient λd₁(s)/[λd₁(s)+(1−λ)d₂(s)].
