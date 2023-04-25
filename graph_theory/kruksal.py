def main():
    graph = insertGraph()
    num_v=numberOfVertices(graph)
    weight_list, position_list=weightList(graph)
    weight_dict = createDictionary(weight_list, position_list)
    weight_dict=sorted(weight_dict.items(), key=lambda x:x[1])
    weight_dict=dict(weight_dict)
    if(constGraph(graph)):
        if(num_v>2):
            print(minSpanningTree(weight_dict))
        else:
            print(sum(weight_dict.values()))
    else:
        print("Graf nie jest spójny")

def minSpanningTree(weight_dict):
    edges = list(weight_dict.keys())
    weight = list(weight_dict.values())
    sum = 0
    neighbor_list=buildNeighborList(neighbor_list=[], edge=edges[0])
    neighbor_list=buildNeighborList(neighbor_list, edge=edges[1])
    sum+=weight[0]
    sum+=weight[1]
    for num in range(2, len(edges)):
        if(edges[num][1] not in searchingPath(neighbor_list, edges[num][0], visited=[])):
            neighbor_list=buildNeighborList(neighbor_list, edge=edges[num])
            sum+=weight[num]
    return sum
    
def searchingPath(graph, vertex, visited):
    if(vertex not in visited):
        visited.append(vertex)
        for next in graph[vertex-1]:
            searchingPath(graph, next, visited)
    return visited

def buildNeighborList(neighbor_list, edge):
    if(len(neighbor_list)<edge[1]):
        for num in range(len(neighbor_list), edge[1]):
            neighbor_list.append([num+1])
    neighbor_list[edge[0]-1].append(edge[1])
    neighbor_list[edge[1]-1].append(edge[0])
    return neighbor_list

def constGraph(graph):
    num_v=numberOfVertices(graph)
    result=dfs(graph, vertex=1, visited=[])
    for num in range(1, num_v+1):
        if(num not in result):
            return False
    return True

def dfs(graph, vertex, visited):
    if(vertex not in visited):
        visited.append(vertex)
        for num in range(len(graph[vertex-1])):
            if(graph[vertex-1][num]!=0):
                dfs(graph, num+1, visited)
    return visited

def weightList(graph):
    weight=[]
    position=[]
    for num in range(len(graph)):
        for num2 in range(len(graph)):
            if(graph[num][num2]!=0 and [num+1, num2+1] not in position and [num2+1, num+1] not in position):
                weight.append(graph[num][num2])
                position.append([num+1, num2+1])
    return weight, position

def insertGraph():
    G = []
    while True:
        try:
            G.append(( input() ).split())
        except:
            break
    for num in range(len(G)):
        G[num] = list(map(int, G[num]))
    return G

def createDictionary(weight_list, position_list):
    my_dict=dict()
    for num in range(len(weight_list)):
        my_dict[tuple(position_list[num])]=weight_list[num]
    return my_dict

def numberOfVertices(G):
    return len(G)

def numberOfEdges(G):
    edges = 0
    for num in range(len(G)):
        for num2 in range(len(G[num])):
            if(G[num][num2]!= 0):
                edges+=1
    return edges/2

if __name__ == "__main__":
    main()