import random

def increasing(el_number: int, rand_range: int):
    sequence = [rand_range//el_number]
    for i in range(1,el_number):
        sequence.append(sequence[i-1]+rand_range//el_number)
    return sequence

def decreasing(el_number: int, rand_range: int):
    sequence = [rand_range]
    for i in range(1, el_number):
        sequence.append(sequence[i - 1] - rand_range // el_number)
    return sequence

def static(el_number: int, rand_range: int):
    sequence = []
    rand = random.randint(0,rand_range)
    for i in range(el_number):
        sequence.append(rand)
    return sequence

def A_type(el_number: int, rand_range: int):
    sequence = []
    for i in range(1, el_number,2):
        sequence.append(i)
    for i in range(el_number, 0,-2):
        sequence.append(i)
    return sequence
def V_type(el_number: int, rand_range: int):
    sequence = []
    for i in range(el_number, 0,-2):
        sequence.append(i)
    for i in range(1, el_number,2):
        sequence.append(i)
    return sequence
def user_input():
    sequence = [int(i) for i in input().split()]
    return sequence

def random_seq(el_number: int, rand_range: int):
    sequence = []
    for i in range(1,el_number):
        sequence.append(random.randint(0,rand_range))
    return sequence
