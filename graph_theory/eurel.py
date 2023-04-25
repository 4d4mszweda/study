def main():
    graph = insertGraph()
    dfs_graph = dfs(graph, 0, visited=[])
    if(len(dfs_graph) == len(graph)):
        option = degVertex(graph)
        if(option == 3):
            print("Graf nie jest eulerowski", end="")
        else:
            all_edges = everyEdge(graph)
            suma = sumAll(graph)
            if(option == 1):
                edge_list = usuwanko(graph, 0, suma, visited=[])
                for ed in all_edges:
                    if(ed not in edge_list):
                        return
                if(0 in edge_list[-1]):
                    print("Graf jest eulerowski", end="")
                    # printPathCycle(edge_list)
                else:
                    print("Graf jest półeulerowski", end="")
                    # printPath(edge_list)
            elif(option == 2):
                for num in range(len(graph)):
                    if(sum(graph[num]) % 2 != 0):
                        break
                edge_list = usuwanko(graph, num, suma, visited=[])
                for ed in all_edges:
                    if(ed not in edge_list):
                        return
                print("Graf jest półeulerowski", end="")
                # printPath(edge_list)
        
    else:
        print("Graf jest niespójny", end="")

def usuwanko(graph, vertex, suma, visited):
    if(suma == 0):
        return visited
    for next in range(len(graph[vertex])):
        if(graph[vertex][next] != 0):
            if(sum(graph[next]) != 1 or suma == 2):
                visited.append(sorted([vertex, next]))
                graph[vertex][next] = 0
                graph [next][vertex] = 0
                suma = sumAll(graph)
                # for next2 in graph:
                #     if(sum(next2) == 0):
                #         graph.remove(next2)
                return usuwanko(graph, next, suma, visited)

def printPath(list):
    print("")
    print(list[0][0],"->",list[0][1],end="")
    for next in range(1, len(list)):
        print(" ->", list[next][1], end="")

def printPathCycle(list):
    print("")
    print(list[0][0],"->",list[0][1],end="")
    for next in range(1, len(list)):
        if(list[next] != list[-1]):
            print(" ->", list[next][1], end="")
        else:
            print(" ->", list[next][0], end="")

def sumAll(graph):
    suma = 0
    for next in graph:
        for next2 in next:
            suma += next2
    return suma

def everyEdge(graph):
    edges = []
    for next in range(len(graph)):
        for next2 in range(len(graph)):
            if(graph[next][next2] != 0):
                temp = sorted([next, next2])
                if(temp not in edges): 
                    edges.append(temp)
    return edges

#podawać wierzchołek od 0 do n
def dfs(graph, vertex, visited):
    if(vertex not in visited):
        visited.append(vertex)
        for next in range(len(graph[vertex])):
            if(graph[vertex][next] == 0): continue
            dfs(graph, next, visited)
    return visited

def degVertex(G):
    deg_v=[]
    for num in range(len(G)):
        deg_v.append(sum(G[num]))
    i = 0
    for next in deg_v:
        if(next % 2 != 0):
            i += 1
        if(i > 2):
            return 3
    if(i > 0):
        return 2
    return 1

def insertGraph():
    graph = []
    while True:
        try:
            graph.append(( input() ).split())
        except:
            break
    for num in range(len(graph)):
        graph[num] = list(map(int, graph[num]))
    return graph

if __name__ == "__main__":
    main()