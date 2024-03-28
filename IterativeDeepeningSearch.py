from DepthLimitedSearch import * 

def iterative_deepening_search(problem):
    """[Figure 3.18]"""
    expanded = []
    for depth in range(sys.maxsize):
        result, expanded_at_depth = depth_limited_search(problem, depth)
        expanded.extend(expanded_at_depth)
        if result != 'cutoff':
            return result, expanded