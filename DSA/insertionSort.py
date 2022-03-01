import random
def insertionSort(arr):
    j = 0
    for i in range(1, len(arr)):
            temp = arr[i]
            flag = i
            for j in range(i-1, -1, -1):
                if arr[j] > temp:
                    arr[j+1] = arr[j]
                    flag = j
                else:
                    break
            arr[flag] = temp
                    
    return arr

# array = [83, 45, 4, 12, 32, 69]
array = [random.randint(-2,100) for i in range(10)]
print(array)
print(insertionSort(array))

            