from stepik import insertGraph, printList

"""
Input: graph adjacency list (like example)
Output: DFS path
"""

def main():
    # graph_list = insertGraph()  #if you want inster in console
    graph_list = [[1, 2],
                  [2, 1, 3],
                  [3, 2]]
    vertex = 1
    print("DFS order: ", dfs(graph_list, vertex, visited = []))
    print("iterative DFS order: ", iterativeDFS(graph_list, vertex))

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