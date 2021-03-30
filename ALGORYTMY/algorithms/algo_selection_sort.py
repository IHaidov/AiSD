def selection_sort(sequence: list):
    n = len(sequence)
    operation_count = 0
    temp=0
    for i in range(n):
        min_el = i
        for j in range(i+1,n):
            if sequence[j]<sequence[min_el]:
                min_el = j
                operation_count += 1
        sequence[i],sequence[min_el] = sequence[min_el],sequence[i]
    return (sequence, operation_count)




