from stepik import insertGraph, printList

def main():
    graph = insertGraph()
    vertex = graph[len(graph)-1][0]
    graph.remove(graph[len(graph)-1])
    visited = []
    print(dfs(graph, vertex, visited))

def dfs(graph, vertex, visited):
    if(vertex not in visited):
        visited.append(vertex)
        for next in graph[vertex-1]:
            dfs(graph, next, visited)
    return visited

if __name__ == "__main__":
    main()