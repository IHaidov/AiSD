###########################
# Shell sort
###########################

def shell_sort(sequence: list):
    n = len(sequence)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = sequence[i]
            j = i
            while j >= gap and sequence[j - gap] > temp:
                sequence[j] = sequence[j - gap]
                j -= gap

            sequence[j] = temp
        gap //= 2
    return sequence
