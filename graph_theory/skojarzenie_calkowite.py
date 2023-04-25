def main():
    graph = insertGraph()
    if(matchmaker(graph, True) == True):
        print("Istnieje skojarzenie doskonałe", end="")
    else:
        print("Nie istnieje skojarzenie doskonałe", end="")

    
def matchmaker(graph, switch = False):
    graph_colors, chromatic_num = picassoGraph(graph)
    if(chromatic_num != 2): return False
    husbands = []
    wife = []

    if(graph_colors.count(1) > graph_colors.count(2)):
        men = 1
    else:
        men = 2
    for index in range(len(graph_colors)):
        if(graph_colors[index] == men): husbands.append(index)
        else: wife.append(index)
        
    temp = []
    for zero in wife:
        temp.append(0)

    for vertex in husbands:
        for num in graph[vertex]:
            if(num == vertex + 1): continue
            for wife_temp in range(len(wife)):        #poznajemy index żony w tablicy temp
                if(wife[wife_temp] == num - 1): break
            if(temp.count(temp[wife_temp]) > 1 or temp[wife_temp] == 0): temp[wife_temp] = vertex + 1
    
    for check_count in temp:
        if(temp.count(check_count) > 1 or check_count == 0):
            return False

    if(switch == True):
        for num in range(len(temp)):
            print("(",wife[num] + 1,",",temp[num],") ")
    return True

    
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
abBdbn
bdndm
"""