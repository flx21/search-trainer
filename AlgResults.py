from BreadthFirstSearch import *
from DepthFirstSearch import *
from UniformCostSearch import *
from DepthLimitedSearch import *
from IterativeDeepeningSearch import *
from GreedyBestFirstSearch import *
from AStarSearch import *

def expansion_order(problem, heuristic = None, steps = 6):
    res = {}
    res["BFS"] = breadth_first_graph_search(problem)[1][:steps]
    res["DFS"] = depth_first_tree_search(problem, steps)[1][:steps]
    res["Uniform Cost Search/Dijkstra"] = uniform_cost_search(problem)[1][:steps]
    res["Depth Limited"] = depth_limited_search(problem, steps)[1][:steps]
    res["Iterative Deepening"] = iterative_deepening_search(problem)[1][:steps]
    if(heuristic):
        res["Greedy Best First Search"] = greedy_best_first_graph_search(problem, heuristic)[1][:steps]
        res["A*"] = greedy_best_first_graph_search(problem, heuristic)[1][:steps]
    return res
    