def selection_sort(sequence: list):
    n = len(sequence)
    temp=0
    for i in range(n):
        min_el = i
        for j in range(i+1,n):
            if sequence[j]<sequence[min_el]:
                min_el = j
        sequence[i],sequence[min_el] = sequence[min_el],sequence[i]
    return sequence




