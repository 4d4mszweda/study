def main(): 
    x = input()
    y = list(x.split(" "))
    array = radixSort (y, len(y[0]))
    printList(array)

def radixSort(A, d):
    for num in range(d-1, -1, -1):
        A = countingSort(A, B = [], k = 123, element=num)
    return A

def countingSort(A, B, k, element):
    for i in range(len(A)):
        B.append(0)
    C = []
    for i in range(k):
        C.append(0)
    for j in range(len(A)):
        C[ord(A[j][element])] = C[ord(A[j][element])] + 1
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[ord(A[j][element])] - 1] = A[j]
        C[ord(A[j][element])] = C[ord(A[j][element])] - 1
    return B

def printList(list):
    for next in list:
        if(next != list[len(list)-1]): print(next, end=" ")
        else: print(next, end="")

if __name__ == "__main__":
    main()