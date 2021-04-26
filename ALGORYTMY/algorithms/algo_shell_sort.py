###########################
# Shell sort
###########################

def shell_sort(sequence: list):
    n = len(sequence)
    gap = n // 2
    a = 0
    while gap > 0:
        a+=1
        print(gap)
        for i in range(gap, n):
            temp = sequence[i]
            j = i
            while j >= gap and sequence[j - gap] > temp:
                sequence[j] = sequence[j - gap]
                j -= gap

            sequence[j] = temp
        gap //= 2
    return sequence

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
shell_sort(list)