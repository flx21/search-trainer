# Search Algorithm Trainer
The purpose of this program is to train for the execution of the provided Search Algorithms by hand in order to be well prepared for the Exam of IN2062 (Grundlagen der Künstlichen Intelligenz).

## Seach Algorithms taken from [this repository](https://github.com/aimacode/aima-python): 
| Algorithm | Function name | Notes |
|-----------|---------------|-------|
|**Breadth First Search** | `breadth_first_graph_search`|[unused] also **without** explored set: `breadth_first_tree_search`
|**Depth First Search**|`depth_first_tree_search`|[unused] also **with** explored set: `depth_first_graph_search`|
|**Uniform Cost Search aka Dijkstra**|`uniform_cost_search`||
|**Depth Limited Search**|`depth_limited_search`||
|**Iterative Deepening Search**|`iterative_deepening_search`||
|**Greedy Best First Search**|`greedy_best_first_graph_search`||
|**$A^*$ Search**|`astar_search`||

Additionally, some util functions for these algorithms and the romania example were taken from the same repository.

## **Useful overview of properties of these Search Algorithms:**
- Branching factor (max number of successors of any node) $b$
- Maximum length of any path (in state space) $m$ 
- Depth of shallowest goal node $d$
- Depth of shallowest goal node $d$
- Cost of optimal solution $C^*$
- Minimum Step cost $\epsilon$
- Depth limit $l$ (For depth limited search)
- Estimated and cost from the root to the goal $h$
- Actual cost from the root to the goal $h^*$
- Relative error $\epsilon^* = \frac{(h^* − h)}{h^*}$

| Algorithm | Informed/Uninformed |Complete | Optimal | Time complexity| Space Complexity |
----|------|-----|----|----|-
| BFS | Uninformed |Yes (for finite $b$ and $d$) | No (but Yes if equal cost per stel) |  $O(b^d)$ | Nodes in frontier: $O(b^d)$; Explored nodes:  $O(b^{d-1})$|
| DFS| Uninformed | No (but Yes when checking for cycles in finite state spaces) | No | $O(b^m)$ | $O(bm)$ |
|Uniform Cost Search (Dijkstra) - Best First Search mit $f(n) = g(n)$| Uninformed| Yes (if all costs are $> 0$) | Yes (If cost $\geq \epsilon$ for positive $\epsilon$) | $O(b^{1+\lfloor{\frac{C^*}{\epsilon}}\rfloor})$ | $O(b^{1+\lfloor{\frac{C^*}{\epsilon}}\rfloor})$ (since all nodes are stored) | 
|Depth Limited Search| Uninformed |No (if $l < d$ ) | No (if $l > d$) |  $O(b^l)$ | $O(bl)$ |
|Iterative Deepening| Uninformed| Yes (if $b$ is finite) | Yes, if all step costs are the same |  $O(b^d)$ | $O(bd)$ |
| Greedy Best First Search| Informed | Yes (if graph search is used) | No |  $O(bm)$ (Worst case: heuristic is misleading the search such that the solution is found last) | $O(bm)$ (Worst case: heuristic is misleading the search such that the solution is found last) (since all nodes are stored) |
| $A^*$-Search | Informed | Yes (if all costs are $> 0$) | Yes (if costs are positive and heuristic is admissible) | $O(b^{\epsilon^* d})$ (If the state space has a single goal and all actions are reversible) | $O(b^{\epsilon^* d})$ (If the state space has a single goal and all actions are reversible) (since all nodes are stored) |

Note: 
DFS and BFS conduct a goal check on nodes that are added to the frontier, while the other algorithms do so when nodes are taken out of the frontier
| $A^*$-Search | Informed | Yes (if all costs are $> 0$) | Yes (if costs are positive and heuristic is admissible) | $O(b^{\epsilon^* d})$ (If the state space has a single goal and all actions are reversible) | $O(b^{\epsilon^* d})$ (If the state space has a single goal and all actions are reversible) (since all nodes are stored) |

Note: 
DFS and BFS conduct a goal check on nodes that are added to the frontier, while the other algorithms do so when nodes are taken out of the frontier

Explanations:
- Optimal: Does the strategy find the optimal solution (minimum costs)?
- Complete: Is it guaranteed that the algorithm finds a solution if one exists?
## Properties of heuristics $h(n)$: 
- **Consistency**: $h(n)$ is consistent, iff $h(n) \leq c(n, a, n') + h(n')$ for all nodes $n$, action $a$ and all direct successors $n'$ gilt.
- **Admissible**: An admissible heuristic is an
underestimation, i.e., it has to be less than or equal to the actual cost.
- $h_2$ dominates $h_1$ iff $\forall n:  h_2(n) \geq h_1(n)$
- Every consistent heuristic is also admissible
- In $A^*$: 
    -  If the heuristic is consistent, any node is only expanded if it is located on an optimal path to its state.
    - A dominating heuristic will never expand more nodes than the heuristic it dominates 

## Required libraries
- matplotlib
- networkX
