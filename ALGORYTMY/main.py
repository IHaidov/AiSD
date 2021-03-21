#________import part________
from algorithms.algo_insertion_sort import insertion_sort
import random
import time

#________initalization_part___________
sequence = []

#________input_part_________
print("|---> Hello!<---|\n|---> Please, input information to get results of algorithms' work.<---|\n|---> Number of the elements:\n|---> ",end='')
el_number = int(input())
print("|---> Range of the numbers:\n|---> ",end='')
rand_range = int(input())
print("")
for j in range(10):
    for i in range(el_number):
        sequence.append(random.randint(0,1000))

    start_time = time.time()
    #________output_part________
    print(sequence)
    print(insertion_sort(sequence))
    print("|---> %s seconds <---|" % (time.time() - start_time))
    sequence=[]




