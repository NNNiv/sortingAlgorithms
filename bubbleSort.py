def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =arr[j+1], arr[j]
    
    return arr

print(bubbleSort([45,677,23,1,10]))