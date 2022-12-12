def bubble_sort(arr):
    while True:
        cambios = False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cambios = True
        if not cambios:
            break
    return arr