# QuickSort [C.A.R Hoare]
import random
def quickSort(arr, left, right):
    if left < right:
        partiton_pos = partition(arr, left, right)
        # elements that are less than the pivot element
        quickSort(arr, left, partiton_pos-1)    
        # elements that are greater than the pivot element
        quickSort(arr, partiton_pos+1, right)

# declare partition function
# returns the index of pivot element after the first step of quick sort.
def partition(arr, left, right):
    i = left
    j = right-1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    if arr[i] > pivot:
        temp = arr[i]
        arr[i] = arr[right]
        arr[right] = temp
    return i

array = [random.randint(-2,100) for i in range(10)]
# array = [23, 43, 3, 56, 22, 11, 46, 98, 9]
quickSort(array, 0, len(array)-1)
print(array)



