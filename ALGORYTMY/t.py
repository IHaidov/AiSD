from algorithms.algo_insertion_sort import insertion_sort
from algorithms.algo_selection_sort import selection_sort
from algorithms.algo_shell_sort import shell_sort
from algorithms.algo_heap_sort import heapSort
from algorithms.algo_quick_sort_rand import quicksort_r
from algorithms.algo_quick_sort_right import quicksort
from random_generator import random_sequence
import random
import time
n = 1000

test = ([])
for i in range(10):
    sequence = random_sequence.random_seq(n,n)

    start_time = time.time()
    quicksort_r(sequence)
    #print("Quick sort rand")
    #print("Random")

    print("%s \n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

test = ([])
for i in range(10):
    sequence = random_sequence.static(n,n)

    start_time = time.time()
    quicksort_r(sequence)
    #print("Quick sort rand")
    #print("Random")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000