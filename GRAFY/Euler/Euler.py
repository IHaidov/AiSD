import copy
import random

visited = []
A = []
A_E = []
p = []


def generate_ham(n, perc):
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
    print(ham)


    for i in range(len(ham) - 1):
        A[ham[i]][ham[i + 1]] = 1
        A[ham[i+1]][ham[i]] = 1
    temp_licz_kraw = len(ham)
    if len(ham) < liczba_wierz:

        while True:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            z = random.randint(0, n - 1)
            if x != y and x != z and y != z and A[x][y] == 0 and A[x][z] == 0 and A[y][z] == 0 and A[y][x] == 0 and \
                    A[z][x] == 0 and A[z][y] == 0:
                print(x, y, z)
                A[x][y] = 1
                A[x][z] = 1
                A[y][z] = 1
                temp_licz_kraw += 3
                if temp_licz_kraw >= liczba_wierz:
                    break

    for i in range(n):
        for j in range(n):
            print(A[i][j], end=' ')
        print()
    return A


A = generate_ham(10, 30)
print(A)


def macierz_sasiedztwa(n, m):
    """
                TWORZY MACIERZ SĄSIEDZTWA

    :param n: rozmiar macierzy sąsiedztwa, ilosc wierzchołków
    :param m: ilość krawędzi
    :return:
    """
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        A.append(temp)
    for i in range(m):
        x, y = map(int, input().split())
        A[x][y] = 1
        A[y][x] = 1
        visited.append(False)
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=' ')
        print()


test = False
Ham_path = []
visited = [0 for i in range(len(A))]


def Hamilton(A, v):
    Ham_path.append(v)
    if len(Ham_path) < len(A):
        visited[v] = True
        for i in range(len(A[0])):
            if A[v][i] == 1:

                if not visited[i]:
                    Hamilton(A, i)
        visited[v] = False
    else:
        test = False
        for i in range(len(A[0])):
            if A[v][0] == 1:
                test = True
                break
        if test:
            print("Hamiltonian cycle: ")
        else:
            print("Hamiltonian path: ")
        for i in Ham_path:
            print(i, end=' ')
        if test:
            print(v, end=' ')
        print()
    Ham_path.pop()


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


indeks = 0
# macierz_sasiedztwa(6, 8)

A_E = copy.deepcopy(A)
S = []


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
            print("Nie jest spełniony warunek: stopień każdego wierzchołka jest parzysty")
            f = False
            break
    if f:
        Euler(A_E, 0)
        print(p)
# CyklEulera(A_E)
# Hamilton(A,0)
