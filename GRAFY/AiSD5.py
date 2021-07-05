from copy import deepcopy
import os
import time


def returnBitList(value, n):
    res = []
    i = 1 << n - 1
    while i > 0:
        if i & value:
            res.append(1)
        else:
            res.append(0)
        i = i // 2
    return res


def knapsackBruteForce(items, maxWeight):
    fmax = 0
    bruteForce = []  # rozwiązanie
    result = []  # zmnienna wspomagująca do rozwiązania
    n = len(items)
    for i in range(1, 2 ** n + 1):
        X = returnBitList(i, n)
        Wx = 0  # Wx=suma wag przedmiotów w plecaku
        for i in range(n):
            if X[i]:
                Wx += items[i][1]
        if Wx <= maxWeight:  # jeżeli rozwiązanie dopuszczalne
            Fx = 0  # f(X) = suma wartości przedmiotów w plecaku
            for i in range(n):
                if X[i]: Fx += items[i][2]
            if Fx > fmax:  # jeśli f(X) > fmax => fmax = f(X); rozwiazanie = X
                fmax = Fx
                bruteForce = X
    for i in range(n):
        if bruteForce[i]:
            result.append(i + 1)
    return result


def knapsackDynamic(items, maxWeight):
    n = len(items)
    # BUDOWANIE MACIERZY PROGRAMOWANIA DYNAMICZNEGO
    dynamicMatrix = [[0 for x in range(maxWeight + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(maxWeight + 1):
            if i == 0 or j == 0:
                dynamicMatrix[i][j] = 0
            elif items[i - 1][1] <= j:
                dynamicMatrix[i][j] = max(items[i - 1][2] + dynamicMatrix[i - 1][j - items[i - 1][1]],
                                          dynamicMatrix[i - 1][j])
            else:
                dynamicMatrix[i][j] = dynamicMatrix[i - 1][j]

    # ODCZYTYWANIE ROZWIAZANIA
    path = []  # wynik
    j = maxWeight  # j odpowiada pojemności plecaku
    for i in range(n, 0, -1):
        if dynamicMatrix[i - 1][j] < dynamicMatrix[i][j]:
            path.append(i)
            j -= items[i - 1][1]
    print("Macierz programowania dynamicznego:")
    for i in dynamicMatrix:
        print(i)
    return path


clear = lambda: os.system('cls')
filename = '1.txt'
operating = True
items = []
maxWeight = 0
while operating:
    clear()
    sumWeight = 0
    sumValue = 0
    print("ITEMS:")
    for i in items:
        print("{}: w = {}, v = {}".format(i[0], i[1], i[2]))
    print("maxWeight = {}".format(maxWeight))
    var = input('''\nOPTIONS:
1. Add item 
2. Set maxWeight
3. Read from file
4. Algorytm programowania dynamicznego APD
5. Algorytm wyczerpujący AW
0. Exit
> ''')

    if var == '1':
        items.append([len(items) + 1, int(input("Weight = ")), int(input("Value = "))])
    if var == '2':
        try:
            maxWeight = int(input("maxWeight = "))
            if maxWeight <= 0:
                print("Wprowadź liczbę dodatnią")
        except:
            print("Wprowadź liczbę całkowitą")
    if var == '3':
        items = []
        f = open(filename, "r")
        firstline = f.readline().split()
        maxWeight = int(firstline[0])
        firstline = f.readline().split()
        n = int(firstline[0])
        try:
            for i in range(n):
                line = f.readline().split()
                if int(line[0]) < 0 or int(line[1]) < 0:
                    print("Found negative value in file input, aborting.")
                    items = []
                    maxWeight = 0
                    input()
                    break
                items.append([i + 1, int(line[0]), int(line[1])])
        except:
            print("Wrong n = {} in first line, correcting n = {}!".format(n, len(items)))
            input()
        f.close()
    if var == '4':
        AD = knapsackDynamic(items, maxWeight)
        for i in AD:
            sumWeight += items[i - 1][1]
            sumValue += items[i - 1][2]
        print("Przedmioty: {}, sumValue = {}, sumWeight = {}".format(AD, sumValue, sumWeight))
        input()
    if var == '5':
        start = time.time()
        AW = knapsackBruteForce(items, maxWeight)
        for i in AW:
            sumWeight += items[i - 1][1]
            sumValue += items[i - 1][2]
        print("Przedmioty: {}, sumValue = {}, sumWeight = {}".format(AW, sumValue, sumWeight))
        end = time.time()
        print(end - start)
        input()
    if var == '0':
        operating = False