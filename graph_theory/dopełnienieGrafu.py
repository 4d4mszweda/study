def main():
    graph = insertGraph()
    rest = restGraph(graph)
    for next in rest:
        for num in range(len(next)):
            print(next[num], end="")
            if(num != len(next)-1):
                print("", end=" ")
        if(rest[len(rest)-1] != next):
            print("", end="\n")

def restGraph(graph):
    restG = []
    for next in graph:
        temp = []
        temp.append(next[0])
        for num in range(len(graph)):
            if(num+1 not in next):
                temp.append(num+1)
        restG.append(temp)
    return restG

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