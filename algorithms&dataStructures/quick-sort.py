def quickSort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quickSort(A, p , q-1)
        quickSort(A, q + 1, r)

def partition(A, p, r):
    x = A[r]
    i = p-1 
    for j in range(p, r):
        if(A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    o = A[i + 1]
    A[i + 1] = A[r]
    A[r] = o
    return i + 1

A = []
final = []
C = []
data=input()
A.extend(data.split())

quickSort(A, 0, len(A)-1)

temp=len(A)
for i in A:
    if(temp>0):
        print(i, end=" ")
    else:
        print(i, end="")
    temp-=1