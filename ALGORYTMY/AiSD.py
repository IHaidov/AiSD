import random

###########################
# Heap Sort
###########################
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


###########################
# Quick Sort Random Pivot
###########################


def quicksort_rand(arr, start, stop):
    if start < stop:
        pivot_i = partitionrand(arr, start, stop)
        quicksort_rand(arr, start, pivot_i - 1)
        quicksort_rand(arr, pivot_i + 1, stop)


def partitionrand(arr, start, stop):
    randompivot = random.randrange(start, stop)
    arr[start], arr[randompivot] = arr[randompivot], arr[start]
    return partition_r(arr, start, stop)


def partition_r(arr, start, stop):
    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot


def quicksort_r(arr):
    start = 0
    stop = len(arr) - 1
    quicksort_rand(arr, start, stop)
    return arr


###########################
# Quick Sort Right Pivot
###########################


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_right(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        partition_index = partition(arr, low, high)
        quicksort_right(arr, low, partition_index - 1)
        quicksort_right(arr, partition_index + 1, high)


def quicksort(arr):
    low = 0
    high = len(arr) - 1
    quicksort_right(arr, low, high)
    return arr


