def main():
    graph = insertGraph()
    vertex = graph[len(graph)-1][0]
    graph.remove(graph[len(graph)-1])
    visited = []
    visited2 = []
    print(dfs(graph, vertex, visited))


def dfs(graph, vertex, visited):
    if(vertex not in visited):
        visited.append(vertex)
        for next in graph[vertex-1]:
            dfs(graph, next, visited)
    return visited

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

def printList(list):
    for num in range(len(list)):
        if(len(list)-1>num):
            print(list[num], end=" ") 
        else:
            print(list[num], end="\n")

if __name__ == "__main__":
    main()