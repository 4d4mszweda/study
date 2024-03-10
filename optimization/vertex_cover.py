import networkx as nx
import matplotlib.pyplot as plt
import random

def vertex_cover_approximation(graph):
    cover = set()

    while graph.edges():
        u, v = random.choice(list(graph.edges()))
        cover.update([(u, v)])
        graph.remove_node(u)
        graph.remove_node(v)

    return cover

G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5)])

Ed = nx.Graph()
Ed.add_edges_from([(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5)])

cover = vertex_cover_approximation(Ed)
node_colors = []

unique_vertex_list = set([item for sublist in cover for item in sublist])
print(unique_vertex_list)

for node in G.nodes():
    if node in unique_vertex_list:
        node_colors.append('r')
    else:
        node_colors.append('b')


nx.draw(G, with_labels=True, node_color=node_colors)
plt.show()

print(cover)