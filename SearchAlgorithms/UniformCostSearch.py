from SearchAlgorithms.BestFirstSearch import *

def uniform_cost_search(problem, display=False):
    """[Figure 3.14]"""
    return best_first_graph_search(problem, lambda node: node.path_cost)
