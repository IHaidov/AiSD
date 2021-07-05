import random
from Lista_sasiedztwa import lista_s
from Macierz_sasiedztwa import macierz_s
from Tabela_krawedzi import  tabela_k

A = []
def generacja_DAG(n):
    for i  in range(n):
        temp = []
        for j in range(n):
            if i>=j:
                temp.append(0)
            else:
                temp.append(1)
        A.append(temp)
    return A
print(generacja_DAG(5))


k = 0

while k !=4:
    print("Wprowadz n i m:")

    n, m = map(int, input().split())
    if k ==1:
        macierz_s.macierz_sasiedztwa(n,m)
    if k ==2:
        lista_s.lista(n,m)
    if k ==3:
        tabela_k(n,m)
