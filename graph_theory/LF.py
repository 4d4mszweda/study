def main():
    graph = insertGraph()
    # print(colorOrder(graph))
    graph_colors, chromatic_num = picassoGraph(graph)
    print("Pokolorowanie wierzchołków: ", end="")
    for num in range(len(graph_colors)):
        if(num < len(graph_colors)-1):
            print(graph_colors[num], end=" ")
        else:
            print(graph_colors[num], end="\n")
    print("Liczba chromatyczna ==", chromatic_num)

# def colorOrder(graph):
#     degree = []
#     order = []
#     for next in graph:
#         degree.append(len(next)-1)
#     for num in range(len(degree)):
#         first = 0
#         # index = 0                       #to powoduje błąd
#         for next in range(len(degree)):
#             if(degree[next] >= first and next not in order):
#                 first = degree[next]
#                 index = next
#         order.append(index)
#     return order

def colorOrder(graph):
    order = []
    nb = neighbor(graph)
    for iterative in range(len(nb)):
        first = 0
        for num in range(len(nb)):
            if(len(nb[num]) >= first and num not in order):
                first = len(nb[num])
                index = num
        order.append(index)
    return order

def neighbor(graph):
    amount = []
    for next in range(len(graph)):
        temp = []
        for next2 in range(1, len(graph[next])):
            temp.append(graph[next][next2]-1)
        for num in range(len(graph)):
            for num2 in graph[num]:
                if(num2-1 == next and num not in temp):
                    temp.append(num)
        temp.remove(next)
        amount.append(temp)
    return amount

def picassoGraph(graph):
    order = colorOrder(graph)
    amount = neighbor(graph)
    colors = []
    for num in range(len(order)):
        colors.append(0)
    for next in order:
        temp =[]
        if(len(amount[next]) == 0):
            colors[next] += 1
            continue
        for num in amount[next]:
            temp.append(colors[num])
        for num in range(1, max(temp)+2):
            if(num not in temp):
                colors[next] = num
                break
    return colors, max(colors)

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

"""
1 2
2 3
3 4
4 5
5 6
6
"""