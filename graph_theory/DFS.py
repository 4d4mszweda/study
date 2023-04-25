from stepik import insertGraph, printList

def main():
    # graph_matrix = insertGraph()  #if you want inster in console
    graph_matrix = [[1,1,1],
                    [1,1,1],
                    [1,1,1]]
    vertex = 1
    print(dfs(graph_matrix, vertex, visited = []))
    printList(iterativeDFS(graph_matrix, vertex))

def dfs(graph, vertex, visited):
    if(vertex not in visited):
        visited.append(vertex)
        for next in graph[vertex-1]:
            dfs(graph, next, visited)
    return visited

def iterativeDFS(graph, vertex):
    stack = []
    visited = []
    stack.append(vertex)
    visited.append(vertex)
    while(stack):
        vertex = stack[len(stack)-1]
        for next in graph[vertex-1]:
            if(next in visited):
                if(next==graph[vertex-1][len(graph[vertex-1])-1]):
                    stack.pop()
                continue
            stack.append(next)
            visited.append(next)
            break
    return visited

if __name__ == "__main__":
    main()