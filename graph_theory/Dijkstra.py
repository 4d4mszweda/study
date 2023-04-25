"""
Peryferium grafu G = (V,E) nazywamy wierzchołki dla których najdłuższa osiągalna 
odległość do innego wierzchołka równa się średnicy grafu diam(G).

Napisz program, który dla danej ważonej macierzy sąsiedztwa wyświetli jego peryferium 
(posortowane po labelach wierzchołków rosnąco).

Dla prostoty zakładamy, że grafy są spójne i jego wagi są dodatnie.

Exemple input:
0 0 0 10
0 0 5 5
0 5 0 7
10 5 7 0

Output:
1 3
"""
from stepik import insertGraph

def main():
    graph = insertGraph()
    # vertex = graph[len(graph)-1][0]
    # graph.remove(graph[len(graph)-1])
    # shortest_path = dijkstra(graph, vertex)
    # for num in range(len(graph)):
    #     print(num + 1, end=" = ")
    #     print(shortest_path[num])
    # print(max(diameter(graph)))
    pphy = peryferium(graph)
    for num in range(len(pphy)):
        if(num < len(pphy)-1):
            print(pphy[num], end=" ")
        else:
            print(pphy[num], end="")
    
def peryferium(graph):
    dia_list = diameter(graph) 
    dia = max(dia_list)
    pphy_list = []
    for num in range(len(dia_list)):
        if(dia_list[num] == dia):
            pphy_list.append(num+1)
    return pphy_list

def diameter(graph):
    dia = []
    for num in range(len(graph)):
        dia.append(max(dijkstra(graph, num+1)))
    return dia

def dijkstra(graph, vertex):
    vertex -= 1                     #może być błąd póżniej z -1
    D = []
    Vg = []
    for num in range(len(graph)):
        D.append(0)
        if(num != vertex):
            Vg.append(num)
    for num in Vg:
        if(graph[vertex][num] == 0):
            D[num] = float('inf')
        else:
            D[num] = graph[vertex][num]
    while(Vg):
        u = Vg[0]
        for num in Vg:
            if(D[u] > D[num]):
                u = num
        Vg.remove(u)
        for num in Vg:
            w = float('inf')
            if(graph[u][num] != 0):
                w = graph[u][num]
            D[num] = min(D[num], D[u]+w)
    return D

if __name__ == "__main__":
    main()