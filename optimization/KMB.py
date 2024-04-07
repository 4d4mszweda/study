import networkx as nx
import matplotlib.pyplot as plt

#Kou, Markowsky, and Berman (KMB) algorithm

def main():
    graph = nx.Graph()
    graph.add_edges_from([('A', 'C'), ('C', 'D'), ('C', 'F'), ('D', 'B'), ('D', 'E'), ('B', 'E'), ('E', 'G'), ('G', 'F')])

    terminals = ['A', 'F', 'B', 'G']

    #DISPALY GRAPH
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    pos = nx.shell_layout(graph)
    colors = get_colors_for_nodes(graph, terminals)
    nx.draw(graph, pos, with_labels=True, node_color=colors, ax=axs[0])
    axs[0].set_title('Original Graph')

    #DISPALY FULL GRAPH STAGE 1
    full_graph = full_graph_with_terminals(graph, terminals)
    pos = nx.spring_layout(full_graph)
    colors = get_colors_for_nodes(full_graph, terminals)
    nx.draw(full_graph, pos, with_labels=True, node_color=colors, ax=axs[1])
    edge_labels = nx.get_edge_attributes(full_graph, 'weight')
    nx.draw_networkx_edge_labels(full_graph, pos, edge_labels=edge_labels, ax=axs[1])
    axs[1].set_title('Stage one: Full graph')

    #DISPALY MIN SPANNIG TREE STAGE 2
    min_spannig_tree = min_spanning_tree(full_graph)
    pos = nx.spring_layout(min_spannig_tree)
    colors = get_colors_for_nodes(min_spannig_tree, terminals)
    nx.draw(min_spannig_tree, pos, with_labels=True, node_color=colors, ax=axs[2])
    edge_labels = nx.get_edge_attributes(min_spannig_tree, 'weight')
    nx.draw_networkx_edge_labels(min_spannig_tree, pos, edge_labels=edge_labels, ax=axs[2])
    axs[2].set_title('Stage two: Min Spanning Tree')

    #DISPALY KMB FINAL STAGE
    kmb_graph = kmb(graph, terminals)
    pos = nx.shell_layout(kmb_graph)
    colors = get_colors_for_nodes(kmb_graph, terminals)
    nx.draw(kmb_graph, pos, with_labels=True, node_color=colors, ax=axs[3])
    axs[3].set_title('Stage three: KMB Graph')

    plt.show()
    return

def kmb(G, terminals):
    H = full_graph_with_terminals(G, terminals)
    T_H = min_spanning_tree(H)
    T_G = nx.Graph()
    for u, v in T_H.edges():
        # additional dikstra path search is bad for performance, better is rember all paths and use them here
        path = nx.dijkstra_path(G, u, v)
        for i in range(len(path) - 1):
            T_G.add_edge(path[i], path[i + 1])
    return T_G

def full_graph_with_terminals(graph, terminals):
    H = nx.Graph()
    for u in terminals:
        for v in terminals:
            if u != v:
                H.add_edge(u, v, weight=nx.dijkstra_path_length(graph, u, v))
    return H

def min_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph)

def get_colors_for_nodes(graph, terminals):
    return ['red' if node in terminals else 'blue' for node in graph.nodes]

if __name__ == '__main__':
    main()