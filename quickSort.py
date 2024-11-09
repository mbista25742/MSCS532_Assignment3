import random

arrayList = [
    [],
    [2,7,1, 4,4,8,90,23,3],
    [1,2,3,4,5,6,7,8],
    [9,8,7,6,5,4,3]
]
    
def quickSort(arr):
    if len(arr) <=1:
        return arr
    randomizedQuickSort(arr,0,len(arr)-1)
    return arr

def randomizedQuickSort(arr, low, high):
    if low < high:
        pivotIndex = partitionArray(arr, low, high)

        randomizedQuickSort(arr, low, pivotIndex-1)
        randomizedQuickSort(arr, pivotIndex+1, high)

def partitionArray(arr, low, high):
    #choose random pivot point
    #pivot = arr[high]
    pid = random.randint(low, high)
    arr[pid], arr[high] = arr[high], arr[pid]
    pivot = arr[high]
    i = low -1

    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    #placing pivot to correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

for a in arrayList:
    print(f"Unsorted:  {a}")
    sortedArray = quickSort(a.copy())
    print(f"Sorted:   {sortedArray}\n")
