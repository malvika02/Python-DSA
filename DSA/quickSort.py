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

