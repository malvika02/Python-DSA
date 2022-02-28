import random
def insertionSort(arr):
    for i in range(1, len(arr)):
            key = arr[i]
            
            for j in range(i-1, -1, -1):
                if arr[j] > key:
                    arr[j+1] = arr[j]
                    arr[j+1] = key
                else:
                    break
                    
    return arr

array = [83, 45, 4, 12, 32, 69]
#array = [random.randint(-2,100) for i in range(10)]
print(insertionSort(array))

            