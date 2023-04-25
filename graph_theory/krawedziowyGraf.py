def main():
    graph = insertGraph()
    new_vertex = newVertexButEdges(graph)
    for num in range(len(graph)): #check skierowanie
        for next2 in graph[num]:
            if(num+1 not in graph[next2-1]):
                # print("skierowany")
                printList(newListSkierowany(graph, new_vertex))
                return 0
    # print("nieskierowany")
    printList(newListNieSkierowany(graph, new_vertex))
    # print(new_vertex)

def newVertexButEdges(graph):
    new_vertex = []
    temp = []
    for next in graph:
        for num in range(1, len(next)):
            new_vertex.append([next[0],next[num]])
    for num in range(len(graph)): #check skierowanie
        for next2 in graph[num]:
            if(num+1 not in graph[next2-1]):
                return new_vertex
    for next in new_vertex:
        if(sorted(next) not in temp):
            temp.append(sorted(next))
    return temp

def newListNieSkierowany(graph, new_v_list):
    new_list = []
    for v in new_v_list:
        temp = []
        temp.append(v)
        for new in new_v_list:
            if(new not in temp and (v[0] in new or v[1] in new)):
                temp.append(new)
        new_list.append(temp)
    return new_list

def newListSkierowany(graph, new_v_list):
    new_list = []
    for v in new_v_list:
        temp = []
        temp.append(v)
        for new in new_v_list:
            if((new not in temp) and v[1] == new[0]):
                temp.append(new)
        new_list.append(temp)
    return new_list
            
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
    for x in list:
        for y in x:
            print(tuple(y), end="")
            if(y == x[-1]):
                print("")
            else:
                print("", end=" ")

if __name__ == "__main__":
    main()