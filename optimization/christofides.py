# Zaimplementuj algorytm Christofidesa wyznaczający rozwiązanie problemu komiwojażera o sumie wag nie większej niż 1.5OPT (alg. 1.5-przyblizony).
# Uwaga: konieczna weryfikacja warunku trójkąta - niezbędnego do faktora przybliżenia 3/2.
import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=2)
    G.add_edge('A', 'C', weight=6)
    G.add_edge('A', 'D', weight=3)
    G.add_edge('A', 'E', weight=7)
    G.add_edge('B', 'C', weight=6)
    G.add_edge('B', 'D', weight=4)
    G.add_edge('B', 'E', weight=8)
    G.add_edge('C', 'D', weight=5)
    G.add_edge('C', 'E', weight=8)
    G.add_edge('D', 'E', weight=9)

    if not check_triangle_inequality(G):
        print("Warunek trójkąta nie jest spełniony")

    fig, axs = plt.subplots(2, 3, figsize=(20, 5))
    # DISPALY INPUT GRAPH
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True, ax=axs[0, 0])
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=axs[0, 0])
    axs[0, 0].set_title('Original Graph')

    # DISPALY MINIMAL SPANNING TREE
    MST = nx.minimum_spanning_tree(G)
    pos = nx.shell_layout(MST)
    nx.draw(MST, pos, with_labels=True, ax=axs[0, 1])
    edge_labels = nx.get_edge_attributes(MST, 'weight')
    nx.draw_networkx_edge_labels(MST, pos, edge_labels=edge_labels, ax=axs[0, 1])
    axs[0, 1].set_title('Minimal Spanning Tree')

    min_maching, H, euler_cycle_graph, hamilton_path_graph = christofides(G)

    # DISPALY MINIMAL MATCHING GRAPH
    pos = nx.shell_layout(min_maching)
    nx.draw(min_maching, pos, with_labels=True, ax=axs[0, 2])
    edge_labels = nx.get_edge_attributes(min_maching, 'weight')
    nx.draw_networkx_edge_labels(min_maching, pos, edge_labels=edge_labels, ax=axs[0, 2])
    axs[0, 2].set_title('Minimal Matching Graph')

    # DISPALY MULTIGRAPH
    H_draw = nx.Graph(H)
    pos = nx.shell_layout(H_draw)
    nx.draw(H_draw, pos, with_labels=True, ax=axs[1, 0])
    edge_labels = nx.get_edge_attributes(H_draw, 'weight')
    nx.draw_networkx_edge_labels(H_draw, pos, edge_labels=edge_labels, ax=axs[1, 0])
    axs[1, 0].set_title('Multigraph')

    # DISPALY EULER CYCLE GRAPH
    pos = nx.shell_layout(euler_cycle_graph)
    nx.draw(euler_cycle_graph, pos, with_labels=True, ax=axs[1, 1])
    edge_labels = nx.get_edge_attributes(euler_cycle_graph, 'weight')
    nx.draw_networkx_edge_labels(euler_cycle_graph, pos, edge_labels=edge_labels, ax=axs[1, 1])
    axs[1, 1].set_title('Euler Cycle Graph')

    # DISPALY HAMILTON PATH GRAPH
    pos = nx.shell_layout(hamilton_path_graph)
    nx.draw(hamilton_path_graph, pos, with_labels=True, ax=axs[1, 2])
    edge_labels = nx.get_edge_attributes(hamilton_path_graph, 'weight')
    nx.draw_networkx_edge_labels(hamilton_path_graph, pos, edge_labels=edge_labels, ax=axs[1, 2])
    axs[1, 2].set_title('Hamilton Path Graph')

    plt.show()

# INPUT -> full graph tree
def christofides(G):
    # Stage 1: Znajdź minimalne drzewo rozpinające (MST) dla danego grafu
    MST = nx.minimum_spanning_tree(G)
    # Stage 2: Znajdź wierzchołki o nieparzystym stopniu w MST
    odd_degree_nodes = [v for v, d in MST.degree() if d % 2 == 1]

    # Stage 3: Znajdź minimalne dopasowanie dla wierzchołków o nieparzystym stopniu
    odd_degree_subgraph = G.subgraph(odd_degree_nodes)
    min_matching = nx.max_weight_matching(odd_degree_subgraph)
    # min_matching = nx.min_weight_matching(odd_degree_subgraph)

    

    # Stage 4: Multigraf z MST i minimalnym dopasowaniem
    H = nx.MultiGraph()
    H.add_weighted_edges_from(MST.edges(data='weight'))
    H.add_weighted_edges_from([(u, v, G[u][v]['weight']) for u, v in min_matching])

    # Stage 5: Znajdź cykl Eulera w H
    if nx.is_eulerian(H):
        eulerian_path_edges = list(nx.eulerian_circuit(H))
        eulerian_path_graph = nx.Graph()
        for u, v in eulerian_path_edges:
            eulerian_path_graph.add_edge(u, v, weight=G[u][v]['weight'])

        # Stage 6: Przekształć cykl Eulera w ścieżkę Hamiltona, usuwając powtarzające się wierzchołki
        hamiltonian_path = list(dict.fromkeys(eulerian_path_edges))

        hamiltonian_path_graph = nx.Graph() 
        for u, v in hamiltonian_path:
            hamiltonian_path_graph.add_edge(u, v, weight=G[u][v]['weight'])

        min_matching_graph = nx.Graph()
        for u, v in min_matching:
            min_matching_graph.add_edge(u, v, weight=G[u][v]['weight'])

        return min_matching_graph, H, eulerian_path_graph, hamiltonian_path_graph
    else:
        print("Graf nie jest eulerowski")
        return False

def check_triangle_inequality(G):
    for u in G.nodes:
        for v in G.nodes:
            if u != v:
                for w in G.nodes:
                    if u != w and v != w:
                        if G[u][v]['weight'] + G[v][w]['weight'] < G[u][w]['weight']:
                            return False
    return True

if __name__ == "__main__":
    main()