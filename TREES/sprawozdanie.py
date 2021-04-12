import random
from AVL.AVL import *
from BST.dsw import *
import time
###########################
# Shell sort
###########################
import sys
sys.setrecursionlimit(max(sys.getrecursionlimit(),100000000))
def shell_sort(sequence: list):
    n = len(sequence)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = sequence[i]
            j = i
            while j >= gap and sequence[j - gap] <= temp:
                sequence[j] = sequence[j - gap]
                j -= gap

            sequence[j] = temp
        gap //= 2
    return sequence

n = 400
bst_creation = []
avl_creation = []
bst_min = []
avl_min = []
bst_in_order = []
avl_in_order = []

bst_balance = []

for i in range(10):
    array = [random.randint(0,n) for j in range(n)]
    n+=400
    array = shell_sort(array)
    start_time = time.time()
    bst_tree = BST_Tree()
    for j in array:
        bst_tree.root.add(j)
    bst_creation.append("%s\n" % (time.time() - start_time))

    start_time = time.time()
    avl_tree = DrzewoAVL()
    korzen = None
    for j in array:
        korzen = avl_tree.dodaj_node(korzen, j)
    avl_creation.append("%s\n" % (time.time() - start_time))

    start_time = time.time()
    bst_tree.DSW()
    bst_balance.append(f'{time.time() - start_time}\n')

    start_time = time.time()
    minValue(bst_tree.root)
    bst_min.append("%s\n" % (time.time() - start_time))

    start_time = time.time()
    avl_tree.najmniejszaWartosc(korzen)
    avl_min.append("%s\n" % (time.time() - start_time))

    start_time = time.time()
    avl_tree.inOrder(korzen)
    avl_in_order.append("%s\n" % (time.time() - start_time))

    start_time = time.time()
    bst_tree.root.inorder([])
    bst_in_order.append("%s\n" % (time.time() - start_time))
print('\n')
print(f'N_min = 400, STEP = 400\n')
print('Tworzenie BST')
print(bst_creation)
print('Tworzenie AVL')
print(avl_creation)
print('Minimum BST')
print(bst_min)
print('Minimum AVL')
print(avl_min)
print('In-order BST')
print(bst_in_order)
print('In-order AVL')
print(avl_in_order)
print('Balance BST')
print(bst_balance)

bst_f_creation = open("ATworzenie BST.txt","a")
bst_f_creation.writelines(bst_creation)
bst_f_creation.close()

avl_f_creation = open("ATworzenie AVL.txt","a")
avl_f_creation.writelines(bst_creation)
avl_f_creation.close()

bst_f_min = open("BMinimum BST.txt","a")
bst_f_min.writelines(bst_min)
bst_f_min.close()

avl_f_min = open("BMinimum AVL.txt","a")
avl_f_min.writelines(avl_min)
avl_f_min.close()

bst_f_in_order = open("CIn-order BST.txt","a")
bst_f_in_order.writelines(bst_in_order)
bst_f_in_order.close()

avl_f_in_order = open("CIn-order AVL.txt","a")
avl_f_in_order.writelines(avl_min)
avl_f_in_order.close()

bst_f_balance = open("DSW BST.txt","a")
bst_f_balance.writelines(bst_balance)
bst_f_balance.close()
