def insertion_sort(sequence: list):
    operation_count = 0
    seq_len = len(sequence)
    for i in range(1,seq_len):

        key = sequence[i]
        j = i-1
        while(j>=0 and sequence[j]>key):
            sequence[j+1] = sequence[j]
            j-=1
            operation_count+=1
        sequence[j+1] = key
    return (sequence, operation_count)