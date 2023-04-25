import math                                                 
                                                    
def main():
    G = insertGraph()
    num_v=numberOfVertices(G)
    num_edg=numberOfEdges(G)    
    deg_list=degVertex(G)
    deg_avg=averageDeg(deg_list)
    print("Ilość wierzchołków:", num_v)
    print("Ilość krawędzi:", num_edg)
    print("Stopnie wierzchołków:", end=" ")
    printList(deg_list)
    print("Średni stopień:", deg_avg)                  
    graphClass(G, num_v, num_edg, deg_list, deg_avg)   

def numberOfVertices(G):
    return len(G)

def numberOfEdges(G):
    edges = 0
    for num in range(len(G)):
        for num2 in range(1, len(G[num])):
            if(G[num][num2]!= 0):
                edges=edges+1
    return int(edges/2)

def degVertex(G):
    deg_v=[]
    for num in range(len(G)):
        if(len(G[num])-1!=0):
            deg_v.append(len(G[num])-1)
        else:
            deg_v.append(0)
    return deg_v

def averageDeg(deg_list):
    sum_deg = 0 
    for num in deg_list:
        sum_deg+=num
    sum_deg/=len(deg_list)
    if(sum_deg-int(sum_deg)==0):
        return int(sum_deg)
    else:
        return sum_deg

def graphClass(G, num_v, num_edg, deg_list, deg_avg):
    temp = True
    if(graphFull(num_v, deg_avg)):
        print("Jest to graf pełny")
        temp=False
    if(graphCycle(deg_list, num_v, num_edg)):
        print("Jest to cykl")
        temp=False
    if(graphPath(deg_list, num_v)):
        print("Jest to ścieżka")
        temp=False
    if(graphTree(num_v, num_edg, deg_list)):
        print("Jest to drzewo")
        temp=False
    if(graphHipercube(G, num_v, num_edg, deg_avg)):
        print("Jest to hiperkostka")
        temp=False                           
    if(temp):
        print("Graf nie należy do żadnej z podstawowych klas")

def graphFull(num_v, deg_avg):
    if(deg_avg == float(num_v-1)):
        return True
    else:
        return False

def graphCycle(deg_list, num_v, num_edg):  
    if(num_v==num_edg):
        for num in deg_list:
            if(num != 2):
                return False
        return True
    else:
        return False

def graphPath(deg_list, num_v):
    for num in range(1, num_v-1):
        if(deg_list[num]!=2):
            return False
    if(deg_list[0]== 1 and deg_list[num_v-1] == 1):
        return True
    else:
        return False

def graphTree(num_v, num_edg, deg_list):
    for deg in deg_list:
        if(deg==0):
            return False
    if(num_v==num_edg+1):
        return True
    else:
        return False

def graphHipercube(G, num_v, num_edg, deg_avg):
    q = math.log(num_v, 2)
    edg_q = q*2**(q-1)
    if(edg_q == num_edg and q==deg_avg):
        indicator = (deg_avg+1)*q
        for vertex in G:
            if(sum(vertex)==indicator):
                indicator+=q-1
                continue
            else:
                return False

        return True
    else:
        return False

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

def printList(list):
    for num in range(len(list)):
        if(len(list)-1>num):
            print(list[num], end=" ") 
        else:
            print(list[num], end="\n")

if __name__ == "__main__":
    main()