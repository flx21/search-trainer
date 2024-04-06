import networkx as nx
import matplotlib.pyplot as plt
import os
import datetime
import numpy as np
import string
import math 
from itertools import product
from SearchAlgorithms.utils import * 

def generate_graph_svg(graph_problem, heuristic, name, initial_color = 'red', standard_color = 'blue', goal_color = 'green', figx = 13, figy = 13, background = 'white', override = False, font_color="whitesmoke"):
    path = 'svg_cache/' 
    if(not os.path.exists(path)):
        os.makedirs(path)
    path += name + '.svg'
    # File Already exists and we don't want to override
    if(os.path.exists(path) and not override):
        return path
    graph = graph_problem.graph
    G = nx.Graph()
    G.add_nodes_from(graph.nodes())
    node_labels = {k: str(k) for k in G}
    if(heuristic):
        node_labels = {k: str(k) + "\n" +str(heuristic[k]) for k,v in heuristic.items()}
    edges, edge_labels = [], {}
    for u, t in graph.graph_dict.items():
        for v, w in t.items():
            G.add_edge(u, v, weight=w)
            edge_labels[(u, v)] = w
    color_map = []
    for node in G:
        if node == graph_problem.initial:
            color_map.append(initial_color)
        elif node == graph_problem.goal:
            color_map.append(goal_color)
        else:
            color_map.append(standard_color)
        
    fig, ax = plt.subplots(figsize=(figx, figy))
    #pos = nx.spring_layout(G, iterations = 800)
    pos = nx.spring_layout(G, iterations = 1)
    nx.draw(G, pos, node_color=color_map, ax=ax, node_size = 1000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, font_color=font_color, labels=node_labels)
    fig.set_facecolor(background)
    plt.savefig(path, facecolor=fig.get_facecolor(), transparent = False)
    plt.close()
    return path

def random_problem(nodes = 10, seed = int(datetime.datetime.now().timestamp()), p = 0.3, min_weight = 0.1, max_weight = 10, min_heuristic = 0.1, max_heuristic = 500, round_digit = 1):
    seed = int(datetime.datetime.now().timestamp()) if not seed else seed
    rng = np.random.default_rng(seed=seed)

    # Generate random Names for the nodes
    n = ''.join(rng.choice(list(string.ascii_uppercase), (math.ceil(nodes/26))))
    g_dict, node_names, edges, prev = dict(), set([n]), list(), n
    g_dict[n] = dict()
    while len(node_names) < nodes:
        n = ''.join(rng.choice(list(string.ascii_uppercase), (math.ceil(nodes/26))))
        g_dict[n] = dict()
        node_names.add(n)
        if(n != prev):
            edges.append((prev, n))
        prev = n
    node_names = sorted(node_names)
    [start, finish] = rng.choice(node_names, 2, replace=False)

    for n1, n2 in product(node_names, node_names):
        if(n1 == n2 or ((n1,n2) in edges) or ((n2, n1) in edges)): 
            continue
        elif rng.uniform() <= p:
            edges.append((n1, n2))

    # Assign weights to all edges
    edges = [(u, v, round(rng.uniform(min_weight, max_weight), round_digit)) for (u, v) in edges]
    G = UndirectedGraph(g_dict)
    for (u, v, w) in edges:
        G.connect(u, v, distance=w)

    # Generate heuristic for the problem
    heuristic = {n : (0 if n == finish else round(rng.uniform(min_heuristic, max_heuristic), round_digit)) for n in node_names}

    return GraphProblem(start, finish, G), heuristic, seed