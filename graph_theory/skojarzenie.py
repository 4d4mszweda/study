def main():
    graph = insertGraph()
    edge_list = []
    for num in reversed(graph):
        if(num == []):
            break
        edge_list.append(num)
    for num in range(len(graph)-1, -1, -1):
        if(graph[num] == []):
            graph.remove(graph[num])
            break
        graph.remove(graph[num])

    new_vertex = newVertexButEdges(graph)

    for num in range(len(graph)): #check skierowanie
        for next2 in graph[num]:
            if(num+1 not in graph[next2-1]):
                new_list = newListSkierowany(graph, new_vertex)
                for x in new_list:
                    if(x[0] in edge_list):
                        i = 0
                        for y in edge_list:
                            if(y in x):
                                i += 1
                            if(i >= 2):
                                print("Nie jest to skojarzenie", end="")
                                return 0
                print("Jest to skojarzenie", end="")
                return 0
    #tutaj nie skierowany
    new_list = newListNieSkierowany(graph, new_vertex)
    for x in new_list:
        if(x[0] in edge_list):
            i = 0
            for y in edge_list:
                if(y in x):
                    i += 1
                if(i >= 2):
                    print("Nie jest to skojarzenie", end="")
                    return 0
    print("Jest to skojarzenie", end="")


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

def printList(list):
    for x in list:
        for y in x:
            print(tuple(y), end="")
            if(y == x[-1]):
                print("")
            else:
                print("", end=" ")

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