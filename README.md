Uses the implementation from [this repository](https://github.com/aimacode/aima-python) for the following seach algorithms:

1. **Breadth First Search** aka `breadth_first_graph_search` ([unused] also without explored set: `breadth_first_tree_search`)
2. **Depth First Search** aka  `depth_first_tree_search` ([unused] also with explored set: `depth_first_graph_search`)
3. **Uniform Cost Search aka Dijkstra** aka `uniform_cost_search`
4. **Depth Limited Search** aka `depth_limited_search`
5. **Iterative Deepening Search** aka `iterative_deepening_search`
6. **Greedy Best First Search** aka `greedy_best_first_graph_search`
7. **$A^*$ Search** aka `astar_search`

The romania example and the util and SearchUtil functions were also taken from said repository.

The Algorithms were adjusted to return the nodes in order of their expansion.
The purpose of this program is to train for the execution of these Search Algorithms by hand in order to be well prepared for the Exam of IN2062 (Grundlagen der Künstlichen Intelligenz).

Useful overview of properties of these Search Algorithms:

- Branching factor aka as max number of successors of any node $b$
- Maximum length of any path (in state space) $m$ 
- Depth of shallowed goal node $d$
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
| A*| Informed | Yes (if all costs are $> 0$) | Yes (if costs are positive and heuristic is admissible) | $O(b^{\epsilon^* d})$ (If the state space has a single goal and all actions are reversible) | $O(b^{\epsilon^* d})$ (If the state space has a single goal and all actions are reversible) (since all nodes are stored) |

Erläuterungen:
- Optimal: Does the strategy find the optimal solution (minimum costs)?
- Complete: Is it guaranteed that the algorithm finds a solution if one exists?

Eigenschaften von Heuristiken $h(n)$: 
- Consistency: $h(n)$ ist consistent, wenn $h(n) \leq c(n, a, n') + h(n')$ für alle nodes $n$, action $a$ und alle direkten Nachfolger $n'$ gilt.
- Admissible: An admissible heuristic is an
underestimation, i.e., it has to be less than or equal to the actual cost.
- Every consistent heuristic is also admissible
- 