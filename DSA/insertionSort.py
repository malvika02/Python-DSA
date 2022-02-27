import random
def insertionSort(arr):
    for i in range(1, len(arr)):
            key = arr[i]
            
            for j in range(i-1, 0, -1):
                if arr[i] < arr[j]:
                    key = arr[i]
                    arr[i] = arr[j]
                    arr[j] = key
                    
                else:
                    key = arr[i]
                    
    return arr

array = [83, 45, 4, 12, 32, 69]
# array = [random.randint(-2,100) for i in range(10)]
print(insertionSort(array))

            