import sys 
from SearchUtil import *

def depth_first_tree_search(problem, max_expansions = sys.maxsize):
    """
    [Figure 3.7]
    Search the deepest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Repeats infinitely in case of loops.
    """

    frontier = [Node(problem.initial)]  # Stack
    expanded = []
    while frontier and len(expanded) < max_expansions:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node, expanded
        #Extending------
        frontier.extend(node.expand(problem))
        expanded.append(node)
        #---------------
    return None, expanded


def depth_first_graph_search(problem):
    """
    [Figure 3.7]
    Search the deepest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Does not get trapped by loops.
    If two paths reach a state, only use the first one.
    """
    frontier = [(Node(problem.initial))]  # Stack

    explored = set()
    expanded = []
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node, expanded
        explored.add(node.state)
        #Extending------
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
        expanded.append(node)
        #---------------
    return None, expanded