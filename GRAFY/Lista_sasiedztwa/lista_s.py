visited = []
_WHITE = 0
_GRAY = 1
_BLACK = 2
Asort = []
A = []
class lista_s:
    def __init__(self, v):
        self.v = v
        self.next = None


def dfs(v):
    p = lista_s(None)
    visited[v] = True
    print(v,end=' ')
    p = A[v]
    while p:
        if not visited[p.v]:
            dfs(p.v)
        p = p.next

def sort_dfs(v):

    if visited[v] == _GRAY:
        print("NOT a DAG")
        return False
    if visited[v] == _WHITE:
        visited[v] = _GRAY
        p = A[v]
        while p != None:
            if not sort_dfs(p.v):
                return False
            p = p.next
        visited[v] = _BLACK
        Asort.append(v)
    return True


def lista(n,m):
    A = [lista_s(None)]*n
    for i in range(n):
        temp = []
        A[i] = None
        visited.append(False)

    for i in range(m):
        v1,v2 = map(int,input().split())
        p = lista_s(v2)
        p.next = A[v1]
        A[v1] = p

    for i in range(n):
        print(f"A [ {i} ] = ",end=' ')
        p = A[i]
        while p:
            print(p.v,end=' ')
            p = p.next
        print()

def mac_to_lista(array,n,m):
    A = [lista_s(None)] * n
    for i in range(n):
        temp = []
        A[i] = None
        visited.append(False)

    tabela = []
    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                tabela.append([i, j])

    for i in range(m):
        p = lista_s(tabela[i][1])
        p.next = A[tabela[i][0]]
        A[tabela[i][0]] = p

    for i in range(n):
        print(f"A [ {i} ] = ",end=' ')
        p = A[i]
        while p:
            print(p.v,end=' ')
            p = p.next
        print()
a = [[0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
#mac_to_lista(a,len(a),len(a[0]))

n,m = map(int,input().split())
lista(n,m)
#print()

#dfs(0)

#print()
visited = []
for i in range(len(A)):
    visited.append(False)
for i in range(len(A)):
    if visited[i] ==_WHITE:
        if not sort_dfs(i):
           break
print(Asort[::-1])


