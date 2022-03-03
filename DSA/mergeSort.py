import random
def merge(A, B):
    #arr[A] & arr[B] are of length m,n respectively
    (m,n) = (len(A),len(B)) 
    (C,i,j,k) = ([], 0, 0, 0)
    while k < m+n:
        if i == m: #A is empty
            C.extend(B[j:])
            k = k + (n-j)
        elif j == n:
            C.extend(A[i:])
            k = k + (n-i)
        elif A[i] < B[j]:
            C.append(A[i])
            (i,k) = (i+1,k+1)
        else:
            C.append(B[j])
            (j,k) = (j+1, k+1)
        return(C)
def mergeSort(A):
    n = len(A)
    if n <= 1:
        return(A)
    L = mergeSort(A[:n//2])
    R = mergeSort(A[n//2:])

    B = merge(L,R)
    return(B)
array = [random.randint(0,100) for i in range(10)]
print(array)
print(mergeSort(array))































# def MergeSort(arr):
#     for i in range(len(arr)):
#         m = len(arr)/2
#         L = arr[:m]
#         R = arr[m+1:]

#     return m
# m = [12,32,43,41,33,1,9]
# print(m)


            