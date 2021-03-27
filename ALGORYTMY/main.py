#________import part________
from algorithms.algo_insertion_sort import insertion_sort
from algorithms.algo_selection_sort import selection_sort
from algorithms.algo_shell_sort import shell_sort
from random_generator import random_sequence
import random
import time

#________initalization_part___________
sequence = []
algorithms = {'1':'insertion_sort','2':'heap_sort','3':'selection_sort','4':'shell_sort','5':'quick_sort_right','6':'quick_sort_random'}
algo_choice = ""
el_number = 10
rand_range = 10
sequence_type = 0
flag = True

#________input_part_________
print("|---> Hello! <---|\n|---> Please, input the next information to get the results of algorithms' work. <---|")
while(flag):
    print("|---> Here You can see a list of the implemented algorithms of sorting:\n"
          "|---> 1.Insertion sort\n"
          "|---> 2.Heap sort\n"
          "|---> 3.Selection sort\n"
          "|---> 4.Shell sort\n"
          "|---> 5.Quick sort(piwot right)\n"
          "|---> 6.Quick sort(piwot random)\n"
          "|---> Please, type a number of algorithm:\n|--->",end='')
    #_________algorithm_choice__________
    temp = input()
    if temp in algorithms.keys():
        algo_choice = algorithms[temp]
        flag = False


#_________number_of_the_elements___________
flag = True
while(flag):
    print("|---> Number of the elements:\n|---> ",end='')
    el_number = int(input())
    if el_number>0:
        flag = False

#_________range_of_the_elements__________
flag = True
while(flag):
    print("|---> Range of the numbers:\n|---> ",end='')
    rand_range = int(input())
    if rand_range>0:
        flag = False

#_________type_of_the_sequence___________
flag = True
while(flag):
    print("|---> Type of the sequence:\n"
          "|---> 1.Increasing \n"
          "|---> 2.Decreasing\n"
          "|---> 3.A (up-down)\n"
          "|---> 4.V (down-up)\n"
          "|---> 5.Increasing with repeat after k elements\n"
          "|---> 6.Decreasing with repeat after k elements")
    sequence_type = int(input())
    if sequence_type >= 1 and sequence_type<=6:
        flag = False
print("")

#________loop_part__________
for j in range(10):
    for i in range(el_number):
        if sequence_type == 1:
            sequence = random_sequence.increasing()
        if sequence_type == 2:
            sequence = random_sequence.decreasing()
        if sequence_type == 3:
            sequence = random_sequence.A_type()
        if sequence_type == 4:
            sequence = random_sequence.V_type()
        if sequence_type == 5:
            sequence = random_sequence.increasing()
        if sequence_type == 6:
            sequence = random_sequence.increasing()

    start_time = time.time()
    #________output_part________
    print(f"|---> Array before sorting <---|\n{sequence}")
    if algo_choice == 'insertion_sort':
        print(f"|---> Array after sorting <---|\n{insertion_sort(sequence)}")
    if algo_choice == 'heap_sort':
        print(f"|---> Array after sorting <---|\n{insertion_sort(sequence)}")
    if algo_choice == 'selection_sort':
        print(f"|---> Array after sorting <---|\n{selection_sort(sequence)}")
    if algo_choice == 'shell_sort':
        print(f"|---> Array after sorting <---|\n{shell_sort(sequence)}")
    if algo_choice == 'quick_sort_right':
        print(f"|---> Array after sorting <---|\n{insertion_sort(sequence)}")
    if algo_choice == 'quick_sort_random':
        print(f"|---> Array after sorting <---|\n{insertion_sort(sequence)}")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))
    sequence=[]




