def main():
    graph = insertGraph()
    colors = graph[len(graph)-1]
    graph.remove(graph[len(graph)-1])
    graph.remove(graph[len(graph)-1])
    if(colorfulGraph(graph, colors)):
        print("Graf jest kolorowalny")
    else:
        print("Graf nie jest kolorowalny")

def colorfulGraph(graph, colors):
    for next in graph:
        checking = next.pop(0)
        for next2 in next:
            if(colors[checking-1] != colors[next2-1]):
                continue
            return False
    return True

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