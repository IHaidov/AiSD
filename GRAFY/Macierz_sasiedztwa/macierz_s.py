visited = []
A = []
_WHITE = 0
_GRAY = 1
_BLACK = 2
Asort = []
def macierz_sasiedztwa(n,m):

    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        A.append(temp)
    for i in range(m):
        x,y = map(int,input().split())
        A[x][y] = 1
        visited.append(False)
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=' ')
        print()

def dfs(v):
    visited[v] = True
    print(v,end=' ')
    for i in range(len(A)):
        if A[v][i]== 1 and not visited[i]:
            dfs(i)

def sort_dfs(v):

    if visited[v] == _GRAY:
        print("NOT a DAG")
        return False
    if visited[v] == _WHITE:
        visited[v] = _GRAY
        f = 0

        for i in range(len(A)):
            if A[v][i] == 1:
                if not sort_dfs(i):
                    return False


        visited[v] = _BLACK
        Asort.append(v)

    return True

n,m = map(int,input().split())
macierz_sasiedztwa(n,m)
print()
dfs(0)

visited = []
for i in range(n):
    visited.append(_WHITE)
print()
for i in range(len(A)):
    sort_dfs(i)
print(Asort[::-1])

