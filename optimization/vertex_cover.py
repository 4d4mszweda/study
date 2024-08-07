import networkx as nx
import matplotlib.pyplot as plt
import random

def vertex_cover_approximation(graph):
    tmp_graph = nx.Graph()
    tmp_graph.add_edges_from(graph.edges())
    cover = set()
    while tmp_graph.edges():
        u, v = random.choice(list(tmp_graph.edges()))
        cover.update([(u, v)])
        tmp_graph.remove_node(u)
        tmp_graph.remove_node(v)
    return cover

def display_graph(graph, cover):
    node_colors = []
    unique_vertex_list = set([item for sublist in cover for item in sublist])
    for node in graph.nodes():
        if node in unique_vertex_list:
            node_colors.append('r')
        else:
            node_colors.append('b')
    nx.draw(G, with_labels=True, node_color=node_colors)
    plt.show()

G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5)])

cover = vertex_cover_approximation(G)

display_graph(G, cover)