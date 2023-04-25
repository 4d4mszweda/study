def main():
    graph = insertGraph()
    final = kwadrat(graph)
    for num in range(len(final)):
        final[num] = sortExcept(final[num], 0, len(final[num]))
    for next in final:
        for num in range(len(next)):
            print(next[num], end="")
            if(num != len(next)-1):
                print("", end=" ")
        if(final[len(final)-1] != next):
            print("", end="\n")

def kwadrat(graph):
    order = []
    for next in graph:
        temp = []
        temp.extend(next)
        for next2 in next:
            for next3 in graph[next2-1]:
                if(next3 not in temp):
                    temp.append(next3)
        order.append(temp)
    return order

def sortExcept(arr, k, n):
    arr[k], arr[-1] = arr[-1], arr[k]
    arr = sorted(arr, key = lambda i: (i is arr[-1], i))
    last = arr[-1]
    i = n - 1
    while i > k:
        arr[i] = arr[i - 1]
        i -= 1
    arr[k] = last
    return arr

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