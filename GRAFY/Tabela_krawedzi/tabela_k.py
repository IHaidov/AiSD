visited = []
A = []
_WHITE = 0
_GRAY = 1
_BLACK = 2
Asort = []

def tabela_kr(n):
    for i in range(n):
        temp = []
        A.append(temp)

    for i in range(n):
        v1, v2 = map(int, input().split())
        A[i].append(v1)
        A[i].append(v2)
        visited.append(False)
    print()
    A.sort()
    for i in range(n):
        print(A[i][0], A[i][1])

def mac_to_tab(array,n):

    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                 A.append([i,j])
    for i in range(n):
        visited.append(False)


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(len(A)):
        if A[i][0] == v and not visited[A[i][1]]:
            dfs(A[i][1])

def sort_dfs(v):

    if visited[v] == _GRAY:
        print("NOT a DAG")
        return False
    if visited[v] == _WHITE:
        visited[v] = _GRAY
        for i in range(len(A)):
            if A[i][0] == v:
                if not sort_dfs(A[i][1]):
                    return False


        visited[v] = _BLACK
        Asort.append(v)

    return True

tabela_kr(10)
print()
print(A)
#dfs(0)
#print(visited)
#for i in range(len(A)):
#    sort_dfs(A[i][0])
#print(Asort[::-1])
#a = [[0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
#A = []
#visited = []
#mac_to_tab(a,5)
#print(A)
#dfs(0)

#for i in range(len(A)):
#    sort_dfs(A[i][0])
#print(Asort[::-1])

