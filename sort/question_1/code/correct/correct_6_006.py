def bubble_sort(arr):
    cambios = True
    while cambios:
        cambios = False
        for j in range(len(arr)-1):
            arr[j], arr[j+1] = (arr[j+1], arr[j]) if arr[j] > arr[j+1] else (arr[j], arr[j+1])
            cambios = True if arr[j] > arr[j+1] else cambios
    return arr