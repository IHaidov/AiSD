import random
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
