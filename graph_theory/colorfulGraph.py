from stepik import insertGraph

def main():
    graph = insertGraph()
    colors = graph[len(graph)-1]
    graph.remove(graph[len(graph)-1])
    graph.remove(graph[len(graph)-1])
    if(colorfulGraph(graph, colors)):
        print("Graph is colorful")
    else:
        print("Graph is not colorful")

def colorfulGraph(graph, colors):
    for next in graph:
        checking = next.pop(0)
        for next2 in next:
            if(colors[checking-1] != colors[next2-1]):
                continue
            return False
    return True

if __name__ == "__main__":
    main()