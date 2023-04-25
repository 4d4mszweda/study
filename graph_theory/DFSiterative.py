def main():
    graph = insertGraph()
    vertex = graph[len(graph)-1][0]
    graph.pop()

    if(vertex<=0 or vertex>len(graph)):
        print("BŁĄD")
        return 0
    for num in range(len(graph)-1):
        if graph[num][0]>=graph[num+1][0]:
            print("BŁĄD")
            return 0
    
    dfs = iterativeDFS(graph, vertex)
    if(len(dfs)==len(graph)):
        print("Porządek DFS:", end=" ")
        printList(dfs)
        print("Graf jest spójny")
    else:
        print("Graf jest niespójny")

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