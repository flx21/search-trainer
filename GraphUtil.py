import networkx as nx
import matplotlib.pyplot as plt
import os

def generate_graph_svg(graph_problem, heuristic, name, initial_color = 'red', standard_color = 'blue', goal_color = 'green', figx = 13, figy = 13, background = 'white', override = False, font_color="whitesmoke"):
    path = "svg_cache/" + name + ".svg"
    #File Already exists and we don't want to override
    if(os.path.exists(path) and not override):
        return path
    graph = graph_problem.graph
    G = nx.Graph()
    G.add_nodes_from(graph.nodes())
    node_labels = {k: str(k) for k in G}
    if(heuristic):
        node_labels = {k: str(k) + "\n" +heuristic[k] for k,v in heuristic.items()}
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
    pos = nx.spring_layout(G, iterations = 800)
    nx.draw(G, pos, node_color=color_map, ax=ax, node_size = 1000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, font_color=font_color, labels=node_labels)
    fig.set_facecolor(background)
    plt.savefig(path, facecolor=fig.get_facecolor(), transparent = False)
    return path