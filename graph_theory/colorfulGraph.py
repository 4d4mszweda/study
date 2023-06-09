from stepik import insertGraph

"""
Input: graph adjacency list (like example) and number of colors that you want to use
Output: information whether it is possible to color this graph with the given number of colors
"""

def main():
    # graph_list = insertGraph()  #if you want insert in console
    graph_list = [[1, 2],
                  [2, 1, 3],
                  [3, 2]]
    colors = 3
    if(colorfulGraph(graph_list, colors)):
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