def bubble_sort_optimized(array):
    for i in range(len(array)):
        swapped = False
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array