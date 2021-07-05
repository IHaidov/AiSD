import random
import copy
import time

koniec = False
Graf = []
test = False
Ham_path = []
visited = []
p = []

S = []
import sys

limit = sys.getrecursionlimit()
sys.setrecursionlimit(1000000)

limit = sys.getrecursionlimit()



def CyklEulera(A_E):
    counter = 0
    f = True
    for i in range(len(A_E)):
        for j in range(len(A_E)):
            if A_E[i][j] == 1:
                counter += 1
        if counter != 0 and counter % 2 == 0:
            counter = 0
        else:
            # print("Nie jest spełniony warunek: stopień każdego wierzchołka jest parzysty")
            f = False
            break
    if f:
        Euler(A_E, 0)
        # print(p)


def Euler(A, v):
    """
        ZWRACA CYKL EULERA
    :param A:
    :param v:
    :return:
    """
    for i in range(len(A)):
        while A[v][i]:
            A[v][i] -= 1
            A[i][v] -= 1
            Euler(A, i)
    p.append(v)


def Hamilton(A, v,k):
    if k == 1:
        return 0
    else:
        Ham_path.append(v)
        if len(Ham_path) < len(A):
            visited[v] = True
            for i in range(len(A[0])):
                if A[v][i] == 1:

                    if not visited[i]:
                        Hamilton(A, i,k)
            visited[v] = False
        else:
            test = False

            if A[v][0] == 1:
                test = True
            if test:
                k = 1

                if k == 1:
                    return 0

                return 0
        Ham_path.pop()


def generacja_grafu_ham(n, perc):
    A = [[0 for i in range(n)] for j in range(n)]
    counter = 0
    liczba_wierz = ((n * (n - 1) / 2) * (perc) / 100)
    l = [i for i in range(n)]
    l_copy = copy.deepcopy(l)
    ham = []
    ham.append(0)

    for i in range(n):
        x = random.choice(l)
        if x != 0:
            ham.append(x)
        l.remove(x)
    ham.append(0)
    # print(ham)

    for i in range(len(ham) - 1):
        A[ham[i]][ham[i + 1]] = 1
        A[ham[i + 1]][ham[i]] = 1
    temp_licz_kraw = len(ham)
    if len(ham) < liczba_wierz:

        while True:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            z = random.randint(0, n - 1)
            if x != y and x != z and y != z and A[x][y] == 0 and A[x][z] == 0 and A[y][z] == 0 and A[y][x] == 0 and \
                    A[z][x] == 0 and A[z][y] == 0:
                # print(x, y, z)
                A[x][y] = 1
                A[y][x] = 1
                A[z][x] = 1
                A[z][y] = 1
                A[x][z] = 1
                A[y][z] = 1
                temp_licz_kraw += 3
                if temp_licz_kraw >= liczba_wierz:
                    break

    # for i in range(n):
    #    for j in range(n):
    #        print(A[i][j], end=' ')
    #    print()
    return A


def generacja_grafu_nham(n, perc):
    A = [[0 for i in range(n)] for j in range(n)]
    counter = 0
    liczba_wierz = ((n * (n - 1) / 2) * (perc) / 100)
    l = [i for i in range(n)]
    l_copy = copy.deepcopy(l)
    ham = []
    ham.append(0)

    for i in range(n):
        x = random.choice(l)
        if x != 0:
            ham.append(x)
        l.remove(x)
    ham.append(0)
    #print(ham)

    for i in range(len(ham) - 1):
        A[ham[i]][ham[i + 1]] = 1
        A[ham[i + 1]][ham[i]] = 1
    temp_licz_kraw = len(ham)
    if len(ham) < liczba_wierz:

        while True:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            z = random.randint(0, n - 1)
            if x != y and x != z and y != z and A[x][y] == 0 and A[x][z] == 0 and A[y][z] == 0 and A[y][x] == 0 and \
                    A[z][x] == 0 and A[z][y] == 0:
                #print(x, y, z)
                A[x][y] = 1
                A[y][x] = 1
                A[z][x] = 1
                A[z][y] = 1
                A[x][z] = 1
                A[y][z] = 1
                temp_licz_kraw += 3
                if temp_licz_kraw >= liczba_wierz:
                    break
    x = random.randint(0, n)
    for i in range(n):
        A[x][i] = 0
        A[i][x] = 0
    #for i in range(n):
    #    for j in range(n):
    #        print(A[i][j], end=" ")
     #   print()
    return A


n = 10
n_end = 20

print("GENERACJA HAMILTON 30%")
for i in range(200,2200,200):
    start_time = time.time()
    generacja_grafu_ham(i, 30)
    print(f"{(time.time() - start_time)}")
print()


print("GENERACJA HAMILTON 70%")
for i in range(200,2200,200):
    start_time = time.time()
    generacja_grafu_ham(i, 70)
    print(f"{(time.time() - start_time)}")



print()
print("HAMILTON HAMILTONOWSKI 30%")
for i in range(200,2200,200):
    Graf = generacja_grafu_ham(i, 30)
    start_time = time.time()
    visited = [0 for i in range(len(Graf))]
    Hamilton(Graf, 0,0)
    print(f"{(time.time() - start_time)}")

print()

print("HAMILTON HAMILTONOWSKI 70%")
for i in range(200,2200,200):
    start_time = time.time()
    Graf = generacja_grafu_ham(i, 70)

    visited = [0 for i in range(len(Graf))]
    Hamilton(Graf, 0,0)
    print(f"{(time.time() - start_time)}")

print()
print("EULER HAMILTONOWSKI 30%")
for i in range(n, n_end):
    Graf = generacja_grafu_ham(i, 30)
    start_time = time.time()
    CyklEulera(Graf)
    print(f"{(time.time() - start_time)}")

print()
print("EULER HAMILTONOWSKI 70%")
for i in range(n, n_end):
    Graf = generacja_grafu_ham(i, 70)
    start_time = time.time()
    CyklEulera(Graf)
    print(f"{(time.time() - start_time)}")

print()
print("GENERACJA NIE-HAMILTON 50%")
for i in range(n, n_end):
    start_time = time.time()
    generacja_grafu_nham(i, 50)
    print(f"{(time.time() - start_time)}")
