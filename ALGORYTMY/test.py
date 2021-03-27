from algorithms.algo_insertion_sort import insertion_sort
from algorithms.algo_selection_sort import selection_sort
from algorithms.algo_shell_sort import shell_sort
from random_generator import random_sequence
import random
import time
import xlsxwriter

workbook = xlsxwriter.Workbook('Testy.xlsx')
worksheet = workbook.add_worksheet("Insertion sort")
worksheet1 = workbook.add_worksheet("Shell sort")
worksheet2 = workbook.add_worksheet("Selection sort")

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
worksheet.write('B1', "Insertion sort", cell_format)
worksheet.write('A2', "Iłość elementów", cell_format)
worksheet.write('B2', "Czas wykonania testów", cell_format)
worksheet.write('C2', "Typ ciągu", cell_format)

worksheet1.set_column(0, 0, 25)
worksheet1.set_column(1, 0, 25)
worksheet1.set_column(2, 0, 25)
worksheet1.write('B1', "Shell sort", cell_format)
worksheet1.write('A2', "Iłość elementów", cell_format)
worksheet1.write('B2', "Czas wykonania testów", cell_format)
worksheet1.write('C2', "Typ ciągu", cell_format)

#______________________insertion_sort_________________________

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.increasing(n,n)

    start_time = time.time()
    insertion_sort(sequence)
    print("Insertion sort")
    print("Increasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, 'rosnący', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.decreasing(n,n)

    start_time = time.time()
    insertion_sort(sequence)
    print("Insertion sort")
    print("Decreasing")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, 'malejący', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.V_type(n,n)

    start_time = time.time()
    insertion_sort(sequence)
    print("Insertion sort")
    print("V type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, 'V type', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.A_type(n,n)

    start_time = time.time()
    insertion_sort(sequence)
    print("Insertion sort")
    print("A type")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, 'A type', cell_format1)
    row += 1

n = 1000
test = ([])
for i in range(10):
    sequence = random_sequence.random_seq(n,n)

    start_time = time.time()
    insertion_sort(sequence)
    print("Insertion sort")
    print("Random")
    print(f"|---> {n} elements <---|\n")
    print("|---> %s seconds <---|\n" % (time.time() - start_time))

    t = str(time.time() - start_time).replace('.',',')
    test.append ([n, t])
    n+=1000

for item, cost in (test):
    worksheet.write(row, col, item, cell_format1)
    worksheet.write(row, col+1, cost, cell_format1)
    worksheet.write(row, col + 2, 'randomny', cell_format1)
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

#__________________save_to_excel________________________

headings = ['Number', 'Malejący', 'Rosnący', 'V type', 'A type', 'Randomny']
chart = workbook.add_chart({'type': 'line'})

chart.add_series({
    'name':       ['Insertion sort', 2, 2],
    'categories': ['Insertion sort', 2, 0, 11, 0],
    'values':     ['Insertion sort', 2, 1, 11, 1],
})
chart.add_series({
    'name':       ['Insertion sort', 12, 2],
    'categories': ['Insertion sort', 12, 0, 21, 0],
    'values':     ['Insertion sort', 12, 1, 21, 1],
})
chart.add_series({
    'name':       ['Insertion sort', 22, 2],
    'categories': ['Insertion sort', 22, 0, 31, 0],
    'values':     ['Insertion sort', 22, 1, 31, 1],
})
chart.add_series({
    'name':       ['Insertion sort', 32, 2],
    'categories': ['Insertion sort', 32, 0, 41, 0],
    'values':     ['Insertion sort', 32, 1, 41, 1],
})
chart.add_series({
    'name':       ['Insertion sort', 42, 2],
    'categories': ['Insertion sort', 42, 0, 51, 0],
    'values':     ['Insertion sort', 42, 1, 51, 1],
})
chart.set_style(10)
worksheet.insert_chart('D2', chart, {'x_offset': 80, 'y_offset': 40})

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
worksheet1.insert_chart('D2', chart1, {'x_offset': 80, 'y_offset': 40})
workbook.close()

