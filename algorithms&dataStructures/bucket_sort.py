def main(): 
    x = input()
    y = list(x.split(" "))
    array = bucketSort(y)
    printList(array)

def bucketSort(A):
    B = []
    for i in range(124):
        B.append([])
    for j in A:
        B[ord(j[0])].append(j)
    for i in range(len(B)):
        B[i] = insertionSort(B[i]) 
    k = 0
    for i in range(124):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1
    return A

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        key2 = key.lower()
        j = step - 1        
        while j >= 0 and key2 < array[j].lower():
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array

# def radixSort(A, d):
#     for num in range(d-1, -1, -1):
#         A = countingSort(A, B = [], k = 124, element=num)
#     return A

# def countingSort(A, B, k, element):
#     for i in range(len(A)):
#         B.append(0)
#     C = []
#     for i in range(k):
#         C.append(0)
#     for j in range(len(A)):
#         C[ord(A[j][element])] = C[ord(A[j][element])] + 1
#     for i in range(1, len(C)):
#         C[i] = C[i] + C[i-1]
#     for j in range(len(A)-1, -1, -1):
#         B[C[ord(A[j][element])] - 1] = A[j]
#         C[ord(A[j][element])] = C[ord(A[j][element])] - 1
#     return B

def printList(list):
    for next in list:
        if(next != list[len(list)-1]): print(next, end=" ")
        else: print(next, end="")

if __name__ == "__main__":
    main()