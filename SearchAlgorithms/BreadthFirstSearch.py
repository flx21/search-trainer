from SearchAlgorithms.utils import *

def breadth_first_tree_search(problem):
    """
    [Figure 3.7]
    Search the shallowest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Repeats infinitely in case of loops.
    """

    frontier = deque([Node(problem.initial)])  # FIFO queue
    expanded = []
    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node, expanded
        #Extending------
        frontier.extend(node.expand(problem))
        expanded.append(node)
        #---------------
    return None, expanded



def breadth_first_graph_search(problem):
    """[Figure 3.11]
    Note that this function can be implemented in a single line as below:
    return graph_search(problem, FIFOQueue())
    """
    expanded = []
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node, expanded
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        #Extending------
        expanded.append(node)
        for child in node.expand(problem):
        #---------------
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child, expanded
                frontier.append(child)
    return None, expanded