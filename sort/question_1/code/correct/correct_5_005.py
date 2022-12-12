def bubble_sort(arr):
    cambios = True
    while cambios:
        cambios = False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cambios = True
    return arr