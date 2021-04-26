visited = []
_WHITE = 0
_GRAY = 1
_BLACK = 2
Asort = []

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

n,m = map(int,input().split())
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
print()

dfs(0)

print()
visited = []
for i in range(n):
    visited.append(False)
for i in range(n):
    if visited[i] ==_WHITE:
        if not sort_dfs(i):
           break
print(Asort[::-1])


