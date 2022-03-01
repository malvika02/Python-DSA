import random
def selection_sort(arr):
    
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min]> arr[j]:
                temp = arr[min]
                arr[min] = arr[j]
                arr[j] = temp
            
            else:
                min = i
                
    return arr
# array = [34, 45, 4, 12, 32, 69 ]
array = [random.randint(-4,100) for i in range(10)]
print(array)
print(selection_sort(array))



