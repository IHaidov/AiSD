from AVL.AVL import *
from BST.dsw import *
user_dec = ''
while user_dec!='3':
    print('Wyberz numer typu drzewa:\n1) AVL Tree\n2) BST Tree\n3) Exit')
    user_dec = input()
    if user_dec == '1':
        AVL_TREE_FUNC()
    elif user_dec == '2':
        BST_TREE_FUNC()
    elif user_dec == '3':
        break
