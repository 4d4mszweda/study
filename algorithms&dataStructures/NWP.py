def main():
    data1 = input().lower()
    data2 = input().lower()
    data1 = split(data1)
    data2 = split(data2)
    nwp_matrix, nwp = NWP(data1, data2)
    # print2D(nwp_matrix)

    result = []
    for x in range(len(data2), 0, -1):
        temp = []
        if(nwp_matrix[-1][x][0] == nwp):
            #szukanie ostatniego od końca wystąpienia
            printNWP(nwp_matrix, data1, len(data1), x, temp)        
            if(temp not in result and len(temp) == nwp): result.append(split(temp))

    #szukanie pierwszego od końca wystąpienia
    temp = printNWPsecond(data1, data2, len(data1), len(data2), nwp_matrix)
    temp = split(temp)
    if(temp not in result): result.append(temp)

    result = sorted(result)

    for next in result:
        for next2 in next:
            print(next2, end="")
        if(next != result[-1]): print(" ", end="")

def NWP(data1, data2):
    m = len(data1) 
    n = len(data2) 

    matrix = [[(0,0)] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if(data1[i - 1] == data2[j - 1]):
                matrix[i][j] = (matrix[i - 1][j - 1][0] + 1, '\\')
            elif(matrix[i - 1][j][0] >= matrix[i][j - 1][0]):
                matrix[i][j] = (matrix[i - 1][j][0], '|')
            else:
                matrix[i][j] = (matrix[i][j - 1][0], '--')
    return matrix, matrix[-1][-1][0]

def printNWP(matrix, data, m, n, result):
    if(m == 0 or n == 0): return
    if(matrix[m][n][1] == '\\'):
        printNWP(matrix, data, m - 1, n - 1, result)
        result.append(data[m - 1])
    elif(matrix[m][n][1] == '|'):
        printNWP(matrix, data, m - 1, n, result)
    else:
        printNWP(matrix, data, m, n - 1, result)

def printNWPsecond(data1, data2, m, n, matrix):
	if(m == 0 or n == 0): return str()
	if(data1[m - 1] == data2[n - 1]):
		return printNWPsecond(data1, data2, m - 1, n - 1, matrix) + data1[m - 1]
	if matrix[m - 1][n][0] > matrix[m][n - 1][0]:
		return printNWPsecond(data1, data2, m - 1, n, matrix)
	else:
		return printNWPsecond(data1, data2, m, n - 1, matrix)

def split(word):
    return list(word)

def print2D(m):
    for x in m:
        print(x)

if __name__ == "__main__":
    main()
"""
abcbdab
bdcaba

a c b a
a b b a

acba
abba

abcbdab
bdcaba

sfkpdcnmej
akfdcmejf

xmjyauz
mzjawxu

BACDB
BCDB

BDndnddbdBDbd
bdbddndbDb
"""