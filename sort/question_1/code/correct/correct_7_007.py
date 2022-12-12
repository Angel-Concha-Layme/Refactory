def bubble_sort(arr):
    while any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        for i in range(len(arr)-1):
            arr[i], arr[i+1] = (arr[i+1], arr[i]) if arr[i] > arr[i+1] else (arr[i], arr[i+1])
    return arr