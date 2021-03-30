import random
###########################
# Quick Sort Right Pivot
###########################
import sys
import time
sys.setrecursionlimit(max(sys.getrecursionlimit(), 1000000))
from random_generator import random_sequence
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

