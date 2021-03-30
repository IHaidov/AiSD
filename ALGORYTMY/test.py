from algorithms.algo_insertion_sort import insertion_sort
from algorithms.algo_selection_sort import selection_sort
from algorithms.algo_shell_sort import shell_sort
from algorithms.algo_heap_sort import heapSort
from algorithms.algo_quick_sort_rand import quicksort_r
from algorithms.algo_quick_sort_right import quicksort
from random_generator import random_sequence
import random
import time
import xlsxwriter
import sys
sys.setrecursionlimit(max(sys.getrecursionlimit(),10000000))

workbook = xlsxwriter.Workbook('Testy.xlsx')
worksheet = workbook.add_worksheet("Insertion sort")
worksheet1 = workbook.add_worksheet("Shell sort")
worksheet2 = workbook.add_worksheet("Heap sort")
worksheet3 = workbook.add_worksheet("Selection sort")
worksheet4 = workbook.add_worksheet("Quick sort (right pivot)")
worksheet5 = workbook.add_worksheet("Quick sort (random pivot)")

cell_format = workbook.add_format()
cell_format1 = workbook.add_format()
cell_format.set_align('center')
cell_format1.set_align('center')
cell_format.set_bg_color('yellow')

row = 2
col = 0

worksheet.set_column(0, 0, 25)
worksheet.set_column(1, 0, 25)
worksheet.set_column(2, 0, 25)
worksheet.set_column(3, 0, 25)
worksheet.write('B1', "Insertion sort", cell_format)
worksheet.write('A2', "Ilość elementów", cell_format)
worksheet.write('B2', "Ilość operacji", cell_format)
worksheet.write('C2', "Czas wykonania testów", cell_format)
worksheet.write('D2', "Typ ciągu", cell_format)

worksheet1.set_column(0, 0, 25)
worksheet1.set_column(1, 0, 25)
worksheet1.set_column(2, 0, 25)
worksheet1.write('B1', "Shell sort", cell_format)
worksheet1.write('A2', "Iłość elementów", cell_format)
worksheet1.write('B2', "Czas wykonania testów", cell_format)
worksheet1.write('C2', "Typ ciągu", cell_format)

worksheet2.set_column(0, 0, 25)
worksheet2.set_column(1, 0, 25)
worksheet2.set_column(2, 0, 25)
worksheet2.write('B1', "Heap sort", cell_format)
worksheet2.write('A2', "Iłość elementów", cell_format)
worksheet2.write('B2', "Czas wykonania testów", cell_format)
worksheet2.write('C2', "Typ ciągu", cell_format)

worksheet3.set_column(0, 0, 25)
worksheet3.set_column(1, 0, 25)
worksheet3.set_column(2, 0, 25)
worksheet3.write('B1', "Selection sort", cell_format)
worksheet3.write('A2', "Iłość elementów", cell_format)
worksheet3.write('B2', "Czas wykonania testów", cell_format)
worksheet3.write('C2', "Typ ciągu", cell_format)

worksheet4.set_column(0, 0, 25)
worksheet4.set_column(1, 0, 25)
worksheet4.set_column(2, 0, 25)
worksheet4.write('B1', "Quick sort (right pivot)", cell_format)
worksheet4.write('A2', "Iłość elementów", cell_format)
worksheet4.write('B2', "Czas wykonania testów", cell_format)
worksheet4.write('C2', "Typ ciągu", cell_format)

worksheet5.set_column(0, 0, 25)
worksheet5.set_column(1, 0, 25)
worksheet5.set_column(2, 0, 25)
worksheet5.write('B1', "Quick sort (random pivot)", cell_format)
worksheet5.write('A2', "Iłość elementów", cell_format)
worksheet5.write('B2', "Czas wykonania testów", cell_format)
worksheet5.write('C2', "Typ ciągu", cell_format)

#______________________insertion_sort_________________________

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.increasing(n,n)

    start_time = time.time()
    t = insertion_sort(sequence)
    print("Insertion sort")
    print("Increasing")
    print(f"|---> {n} elements <---|\n")
    print(f"|---> {t[1]} operations <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    tim = str(time.time() - start_time).replace('.',',')
    test.append ([n, t[1], tim])
    n+=1000

for item, cost, op in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, op, cell_format1)
    worksheet.write(row, col + 3, 'rosnący', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.decreasing(n,n)

    start_time = time.time()
    t = insertion_sort(sequence)
    print("Insertion sort")
    print("Decreasing")
    print(f"|---> {n} elements <---|\n")
    print(f"|---> {t[1]} operations <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    tim = str(time.time() - start_time).replace('.',',')
    test.append ([n, t[1], tim])
    n+=1000

for item, cost, op in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, op, cell_format1)
    worksheet.write(row, col + 3, 'malejący', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.V_type(n,n)

    start_time = time.time()
    t = insertion_sort(sequence)
    print("Insertion sort")
    print("V type")
    print(f"|---> {n} elements <---|\n")
    print(f"|---> {t[1]} operations <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    tim = str(time.time() - start_time).replace('.',',')
    test.append ([n, t[1], tim])
    n+=1000

for item, cost, op in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, op, cell_format1)
    worksheet.write(row, col + 3, 'V type', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.A_type(n,n)

    start_time = time.time()
    t = insertion_sort(sequence)
    print("Insertion sort")
    print("A type")
    print(f"|---> {n} elements <---|\n")
    print(f"|---> {t[1]} operations <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    tim = str(time.time() - start_time).replace('.',',')
    test.append ([n, t[1], tim])
    n+=1000

for item, cost, op in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, op, cell_format1)
    worksheet.write(row, col + 3, 'A type', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.random_seq(n,n)

    start_time = time.time()
    t = insertion_sort(sequence)
    print("Insertion sort")
    print("Random")
    print(f"|---> {n} elements <---|\n")
    print(f"|---> {t[1]} operations <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    tim = str(time.time() - start_time).replace('.',',')
    test.append ([n, t[1], tim])
    n+=1000

for item, cost, op in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, op, cell_format1)
    worksheet.write(row, col + 3, 'randomny', cell_format1)
    row += 1

#______________________shell_sort_________________________

n = 1000
row = 2
col = 0
test = ([])
for i in range(10):
    sequence = random_sequence.increasing(n,n)

    start_time = time.time()
    shell_sort(sequence)
    print("Shell sort")
    print("Increasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet1.write(row, col, item, cell_format1)
    worksheet1.write(row, col+1, cost, cell_format1)
    worksheet1.write(row, col + 2, 'Increasing', cell_format1)
    row += 1

n = 1000

test = ([])
for i in range(10):
    sequence = random_sequence.decreasing(n,n)

    start_time = time.time()
    shell_sort(sequence)
    print("Shell sort")
    print("Decreasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet1.write(row, col, item, cell_format1)
    worksheet1.write(row, col+1, cost, cell_format1)
    worksheet1.write(row, col + 2, 'Decreasing', cell_format1)
    row += 1

n = 1000

test = ([])
for i in range(10):
    sequence = random_sequence.A_type(n,n)

    start_time = time.time()
    shell_sort(sequence)
    print("Shell sort")
    print("A_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet1.write(row, col, item, cell_format1)
    worksheet1.write(row, col+1, cost, cell_format1)
    worksheet1.write(row, col + 2, 'A_type', cell_format1)
    row += 1

n = 1000

test = ([])
for i in range(10):
    sequence = random_sequence.V_type(n,n)

    start_time = time.time()
    shell_sort(sequence)
    print("Shell sort")
    print("V_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet1.write(row, col, item, cell_format1)
    worksheet1.write(row, col+1, cost, cell_format1)
    worksheet1.write(row, col + 2, 'V_type', cell_format1)
    row += 1

n = 1000

test = ([])
for i in range(10):
    sequence = random_sequence.random_seq(n,n)

    start_time = time.time()
    shell_sort(sequence)
    print("Shell sort")
    print("Random")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet1.write(row, col, item, cell_format1)
    worksheet1.write(row, col+1, cost, cell_format1)
    worksheet1.write(row, col + 2, 'randomny', cell_format1)
    row += 1

#__________________heap_sort___________________________

n = 1000
row = 2
col = 0
test = ([])
for i in range(10):
    sequence = random_sequence.increasing(n,n)

    start_time = time.time()
    heapSort(sequence)
    print("Heap sort")
    print("Increasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet2.write(row, col, item, cell_format1)
    worksheet2.write(row, col+1, cost, cell_format1)
    worksheet2.write(row, col + 2, 'Increasing', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.decreasing(n,n)

    start_time = time.time()
    heapSort(sequence)
    print("Heap sort")
    print("Decreasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet2.write(row, col, item, cell_format1)
    worksheet2.write(row, col+1, cost, cell_format1)
    worksheet2.write(row, col + 2, 'Decreasing', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.V_type(n,n)

    start_time = time.time()
    heapSort(sequence)
    print("Heap sort")
    print("V_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet2.write(row, col, item, cell_format1)
    worksheet2.write(row, col+1, cost, cell_format1)
    worksheet2.write(row, col + 2, 'V_type', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.A_type(n,n)

    start_time = time.time()
    heapSort(sequence)
    print("Heap sort")
    print("A_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet2.write(row, col, item, cell_format1)
    worksheet2.write(row, col+1, cost, cell_format1)
    worksheet2.write(row, col + 2, 'A_type', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.random_seq(n,n)

    start_time = time.time()
    heapSort(sequence)
    print("Heap sort")
    print("Randomny")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet2.write(row, col, item, cell_format1)
    worksheet2.write(row, col+1, cost, cell_format1)
    worksheet2.write(row, col + 2, 'Randomny', cell_format1)
    row += 1

#_________________selection_sort________________________

n = 1000
row = 2
col = 0
test = ([])
for i in range(10):
    sequence = random_sequence.increasing(n,n)

    start_time = time.time()
    selection_sort(sequence)
    print("Selection sort")
    print("Increasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet3.write(row, col, item, cell_format1)
    worksheet3.write(row, col+1, cost, cell_format1)
    worksheet3.write(row, col + 2, 'Increasing', cell_format1)
    row += 1

n = 1000

test = ([])
for i in range(10):
    sequence = random_sequence.decreasing(n,n)

    start_time = time.time()
    selection_sort(sequence)
    print("Selection sort")
    print("Decreasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet3.write(row, col, item, cell_format1)
    worksheet3.write(row, col+1, cost, cell_format1)
    worksheet3.write(row, col + 2, 'Decreasing', cell_format1)
    row += 1

n = 1000

test = ([])
for i in range(10):
    sequence = random_sequence.A_type(n,n)

    start_time = time.time()
    selection_sort(sequence)
    print("Selection sort")
    print("A_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet3.write(row, col, item, cell_format1)
    worksheet3.write(row, col+1, cost, cell_format1)
    worksheet3.write(row, col + 2, 'A_type', cell_format1)
    row += 1

n = 1000

test = ([])
for i in range(10):
    sequence = random_sequence.V_type(n,n)

    start_time = time.time()
    selection_sort(sequence)
    print("Selection sort")
    print("V_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet3.write(row, col, item, cell_format1)
    worksheet3.write(row, col+1, cost, cell_format1)
    worksheet3.write(row, col + 2, 'V_type', cell_format1)
    row += 1

n = 1000

test = ([])
for i in range(10):
    sequence = random_sequence.random_seq(n,n)

    start_time = time.time()
    selection_sort(sequence)
    print("Selection sort")
    print("Random")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet3.write(row, col, item, cell_format1)
    worksheet3.write(row, col+1, cost, cell_format1)
    worksheet3.write(row, col + 2, 'randomny', cell_format1)
    row += 1

#_________________quick_sort_right_______________________

n = 200
row = 2
col = 0
test = ([])
for i in range(10):
    sequence = random_sequence.increasing(n,n)

    start_time = time.time()
    quicksort(sequence)
    print("Quick sort")
    print("Increasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet4.write(row, col, item, cell_format1)
    worksheet4.write(row, col+1, cost, cell_format1)
    worksheet4.write(row, col + 2, 'Increasing', cell_format1)
    row += 1

n = 200

test = ([])
for i in range(10):
    sequence = random_sequence.decreasing(n,n)

    start_time = time.time()
    quicksort(sequence)
    print("Quick sort")
    print("Decreasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet4.write(row, col, item, cell_format1)
    worksheet4.write(row, col+1, cost, cell_format1)
    worksheet4.write(row, col + 2, 'Decreasing', cell_format1)
    row += 1

n = 200

test = ([])
for i in range(10):
    sequence = random_sequence.A_type(n,n)

    start_time = time.time()
    quicksort(sequence)
    print("Quick sort")
    print("A_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet4.write(row, col, item, cell_format1)
    worksheet4.write(row, col+1, cost, cell_format1)
    worksheet4.write(row, col + 2, 'A_type', cell_format1)
    row += 1

n = 200

test = ([])
for i in range(10):
    sequence = random_sequence.V_type(n,n)

    start_time = time.time()
    quicksort(sequence)
    print("Quick sort")
    print("V_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet4.write(row, col, item, cell_format1)
    worksheet4.write(row, col+1, cost, cell_format1)
    worksheet4.write(row, col + 2, 'V_type', cell_format1)
    row += 1

n = 200

test = ([])
for i in range(10):
    sequence = random_sequence.random_seq(n,n)

    start_time = time.time()
    quicksort(sequence)
    print("Quick sort")
    print("Random")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet4.write(row, col, item, cell_format1)
    worksheet4.write(row, col+1, cost, cell_format1)
    worksheet4.write(row, col + 2, 'randomny', cell_format1)
    row += 1

#_________________quick_sort_rand_______________________

n = 200
row = 2
col = 0
test = ([])
for i in range(10):
    sequence = random_sequence.increasing(n,n)

    start_time = time.time()
    quicksort_r(sequence)
    print("Quick sort rand")
    print("Increasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet5.write(row, col, item, cell_format1)
    worksheet5.write(row, col+1, cost, cell_format1)
    worksheet5.write(row, col + 2, 'Increasing', cell_format1)
    row += 1

n = 200

test = ([])
for i in range(10):
    sequence = random_sequence.decreasing(n,n)

    start_time = time.time()
    quicksort_r(sequence)
    print("Quick sort rand")
    print("Decreasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet5.write(row, col, item, cell_format1)
    worksheet5.write(row, col+1, cost, cell_format1)
    worksheet5.write(row, col + 2, 'Decreasing', cell_format1)
    row += 1

n = 200

test = ([])
for i in range(10):
    sequence = random_sequence.A_type(n,n)

    start_time = time.time()
    quicksort_r(sequence)
    print("Quick sort rand")
    print("A_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet5.write(row, col, item, cell_format1)
    worksheet5.write(row, col+1, cost, cell_format1)
    worksheet5.write(row, col + 2, 'A_type', cell_format1)
    row += 1

n = 200

test = ([])
for i in range(10):
    sequence = random_sequence.V_type(n,n)

    start_time = time.time()
    quicksort_r(sequence)
    print("Quick sort rand")
    print("V_type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet5.write(row, col, item, cell_format1)
    worksheet5.write(row, col+1, cost, cell_format1)
    worksheet5.write(row, col + 2, 'V_type', cell_format1)
    row += 1

n = 200

test = ([])
for i in range(10):
    sequence = random_sequence.random_seq(n,n)

    start_time = time.time()
    quicksort_r(sequence)
    print("Quick sort rand")
    print("Random")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=200

for item, cost in (test):
    worksheet5.write(row, col, item, cell_format1)
    worksheet5.write(row, col+1, cost, cell_format1)
    worksheet5.write(row, col + 2, 'randomny', cell_format1)
    row += 1

#__________________save_to_excel________________________

headings = ['Number', 'Malejący', 'Rosnący', 'V type', 'A type', 'Randomny']
chart = workbook.add_chart({'type': 'line'})

chart.add_series({
    'name':       ['Insertion sort', 2, 3],
    'categories': ['Insertion sort', 2, 0, 11, 0],
    'values':     ['Insertion sort', 2, 2, 11, 2],
})
chart.add_series({
    'name':       ['Insertion sort', 12, 3],
    'categories': ['Insertion sort', 12, 0, 21, 0],
    'values':     ['Insertion sort', 12, 2, 21, 2],
})
chart.add_series({
    'name':       ['Insertion sort', 22, 3],
    'categories': ['Insertion sort', 22, 0, 31, 0],
    'values':     ['Insertion sort', 22, 2, 31, 2],
})
chart.add_series({
    'name':       ['Insertion sort', 32, 3],
    'categories': ['Insertion sort', 32, 0, 41, 0],
    'values':     ['Insertion sort', 32, 2, 41, 2],
})
chart.add_series({
    'name':       ['Insertion sort', 42, 3],
    'categories': ['Insertion sort', 42, 0, 51, 0],
    'values':     ['Insertion sort', 42, 2, 51, 2],
})
chart.set_style(10)
worksheet.insert_chart('F2', chart, {'x_offset': 80, 'y_offset': 40})

chart1 = workbook.add_chart({'type': 'line'})

chart1.add_series({
    'name':       ['Shell sort', 2, 2],
    'categories': ['Shell sort', 2, 0, 11, 0],
    'values':     ['Shell sort', 2, 1, 11, 1],
})
chart1.add_series({
    'name':       ['Shell sort', 12, 2],
    'categories': ['Shell sort', 12, 0, 21, 0],
    'values':     ['Shell sort', 12, 1, 21, 1],
})
chart1.add_series({
    'name':       ['Shell sort', 22, 2],
    'categories': ['Shell sort', 22, 0, 31, 0],
    'values':     ['Shell sort', 22, 1, 31, 1],
})
chart1.add_series({
    'name':       ['Shell sort', 32, 2],
    'categories': ['Shell sort', 32, 0, 41, 0],
    'values':     ['Shell sort', 32, 1, 41, 1],
})
chart1.add_series({
    'name':       ['Shell sort', 42, 2],
    'categories': ['Shell sort', 42, 0, 51, 0],
    'values':     ['Shell sort', 42, 1, 51, 1],
})
chart1.set_style(10)
worksheet1.insert_chart('F2', chart1, {'x_offset': 80, 'y_offset': 40})

chart2 = workbook.add_chart({'type': 'line'})

chart2.add_series({
    'name':       ['Heap sort', 2, 2],
    'categories': ['Heap sort', 2, 0, 11, 0],
    'values':     ['Heap sort', 2, 1, 11, 1],
})
chart2.add_series({
    'name':       ['Heap sort', 12, 2],
    'categories': ['Heap sort', 12, 0, 21, 0],
    'values':     ['Heap sort', 12, 1, 21, 1],
})
chart2.add_series({
    'name':       ['Heap sort', 22, 2],
    'categories': ['Heap sort', 22, 0, 31, 0],
    'values':     ['Heap sort', 22, 1, 31, 1],
})
chart2.add_series({
    'name':       ['Heap sort', 32, 2],
    'categories': ['Heap sort', 32, 0, 41, 0],
    'values':     ['Heap sort', 32, 1, 41, 1],
})
chart2.add_series({
    'name':       ['Heap sort', 42, 2],
    'categories': ['Heap sort', 42, 0, 51, 0],
    'values':     ['Heap sort', 42, 1, 51, 1],
})
chart2.set_style(10)
worksheet2.insert_chart('F2', chart2, {'x_offset': 80, 'y_offset': 40})

chart3 = workbook.add_chart({'type': 'line'})

chart3.add_series({
    'name':       ['Selection sort', 2, 2],
    'categories': ['Selection sort', 2, 0, 11, 0],
    'values':     ['Selection sort', 2, 1, 11, 1],
})
chart3.add_series({
    'name':       ['Selection sort', 12, 2],
    'categories': ['Selection sort', 12, 0, 21, 0],
    'values':     ['Selection sort', 12, 1, 21, 1],
})
chart3.add_series({
    'name':       ['Selection sort', 22, 2],
    'categories': ['Selection sort', 22, 0, 31, 0],
    'values':     ['Selection sort', 22, 1, 31, 1],
})
chart3.add_series({
    'name':       ['Selection sort', 32, 2],
    'categories': ['Selection sort', 32, 0, 41, 0],
    'values':     ['Selection sort', 32, 1, 41, 1],
})
chart3.add_series({
    'name':       ['Selection sort', 42, 2],
    'categories': ['Selection sort', 42, 0, 51, 0],
    'values':     ['Selection sort', 42, 1, 51, 1],
})
chart3.set_style(10)
worksheet3.insert_chart('F2', chart3, {'x_offset': 80, 'y_offset': 40})

chart4 = workbook.add_chart({'type': 'line'})

chart4.add_series({
    'name':       ['Quick sort (right pivot)', 2, 2],
    'categories': ['Quick sort (right pivot)', 2, 0, 11, 0],
    'values':     ['Quick sort (right pivot)', 2, 1, 11, 1],
})
chart4.add_series({
    'name':       ['Quick sort (right pivot)', 12, 2],
    'categories': ['Quick sort (right pivot)', 12, 0, 21, 0],
    'values':     ['Quick sort (right pivot)', 12, 1, 21, 1],
})
chart4.add_series({
    'name':       ['Quick sort (right pivot)', 22, 2],
    'categories': ['Quick sort (right pivot)', 22, 0, 31, 0],
    'values':     ['Quick sort (right pivot)', 22, 1, 31, 1],
})
chart4.add_series({
    'name':       ['Quick sort (right pivot)', 32, 2],
    'categories': ['Quick sort (right pivot)', 32, 0, 41, 0],
    'values':     ['Quick sort (right pivot)', 32, 1, 41, 1],
})
chart4.add_series({
    'name':       ['Quick sort (right pivot)', 42, 2],
    'categories': ['Quick sort (right pivot)', 42, 0, 51, 0],
    'values':     ['Quick sort (right pivot)', 42, 1, 51, 1],
})
chart4.set_style(10)
worksheet4.insert_chart('F2', chart4, {'x_offset': 80, 'y_offset': 40})

chart5 = workbook.add_chart({'type': 'line'})

chart5.add_series({
    'name':       ['Quick sort (random pivot)', 2, 2],
    'categories': ['Quick sort (random pivot)', 2, 0, 11, 0],
    'values':     ['Quick sort (random pivot)', 2, 1, 11, 1],
})
chart5.add_series({
    'name':       ['Quick sort (random pivot)', 12, 2],
    'categories': ['Quick sort (random pivot)', 12, 0, 21, 0],
    'values':     ['Quick sort (random pivot)', 12, 1, 21, 1],
})
chart5.add_series({
    'name':       ['Quick sort (random pivot)', 22, 2],
    'categories': ['Quick sort (random pivot)', 22, 0, 31, 0],
    'values':     ['Quick sort (random pivot)', 22, 1, 31, 1],
})
chart5.add_series({
    'name':       ['Quick sort (random pivot)', 32, 2],
    'categories': ['Quick sort (random pivot)', 32, 0, 41, 0],
    'values':     ['Quick sort (random pivot)', 32, 1, 41, 1],
})
chart5.add_series({
    'name':       ['Quick sort (random pivot)', 42, 2],
    'categories': ['Quick sort (random pivot)', 42, 0, 51, 0],
    'values':     ['Quick sort (random pivot)', 42, 1, 51, 1],
})
chart5.set_style(10)
worksheet5.insert_chart('F2', chart5, {'x_offset': 80, 'y_offset': 40})
workbook.close()
