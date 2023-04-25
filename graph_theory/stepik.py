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