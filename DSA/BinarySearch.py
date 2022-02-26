#def binary_search(sequence, item)
def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    index = -1
    #
    while low <= high:
        mid = (low+high)//2    
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return index
arr = [1,2,3,4,5,6,7,8,9,10]
x=4

value = binary_search(arr, x)
print(value)