def except_mes_func():
    print()
    print('Something went wrong')
    print()

import random
from BST.bst_creation import *
def BST_TREE_FUNC():
    user_choice = ''
    flag_1_step = False
    flag_2_step = False
    flag_7_step = False
    while(user_choice!='10'):
        print("----BST Tree----\n"
              "1) Create a tree\n"
              "2) Initialize tree\n"
              "3) Add element to the tree\n"
              "4) Print the tree\n"
              "5) Find element in the tree\n"
              "6) Delete element from the tree\n"
              "7) Delete the tree\n"
              "8) Balance the tree using DSW algorithm\n"
              "9) Graphic representaion of the tree\n"
              "10) Exit")
        user_choice = input()
        sub_user_choice = ''

        if user_choice == '1':
            flag_1_step = True
            tree = BST_Tree()
            print("\nTree was created\n")
        elif user_choice == '2':
            if flag_1_step:
                print('1) Initialize tree by yourself\n'
                      '2) Initialize tree by system')
                sub_user_choice = input()
                array = []
                if sub_user_choice =='1':
                    print('Input array in one line, like: 1 2 3 4 5')
                    array = [int(i) for i in input().split()]
                elif sub_user_choice == '2':
                    array = [random.randint(0, 100) for i in range(5)]
                for i in array:
                    tree.root.add(i)
                flag_2_step = True
                print('\nTree was initialized\n')
        elif user_choice == '3':
            if flag_1_step and flag_2_step:
                try:
                    print('Input value to add:')
                    val = int(input())
                    tree.root.add(val)
                    print()
                    print(f'{val} was successfully added to the tree')
                    print()
                except:
                    except_mes_func()
        elif user_choice == '4':
            sub_user_choice = ''
            if flag_1_step and flag_2_step:
                print('1) In-order method\n2) Pre-order method')
                sub_user_choice = input()
                if sub_user_choice == '1':
                    print()
                    print(tree.root.inorder([]))

                    print(f'\nHeight of the tree: {height(tree.root)}\n')

                elif sub_user_choice == '2':
                    print()
                    print(tree.root.preorder([]))

                    print(f'\nHeight of the tree: {height(tree.root)}\n')


        elif user_choice == '5':
            if flag_1_step and flag_2_step:
                try:
                    print()
                    print('1) Find minimum element\n'
                          '2) Find maximum element\n')
                    sub_user_choice = input()
                    if sub_user_choice == '1':
                        print(minValue(tree.root))
                    elif sub_user_choice == '2':
                        print(maxValue(tree.root))
                    print()
                except:
                    except_mes_func()
        elif user_choice == '6':
            if flag_1_step and flag_2_step:
                try:
                    print()
                    print(tree.root.inorder([]))
                    print('Input number to delete:')
                    val = int(input())
                    tree.root.delete(val)
                except:
                    except_mes_func()
        elif user_choice == '7':
            if flag_1_step and flag_2_step:
                try:
                    tree.root.delete_postorder()
                    print()
                    print('Tree was deleted')
                    print()
                except:
                    except_mes_func()
        elif user_choice == '8':
            if flag_1_step and flag_2_step:
                try:
                    tree.DSW()
                    print()
                    print('Tree was rebalanced')
                    print()
                except:
                    except_mes_func()
        elif user_choice == '9':
            if flag_1_step:
                print(tree.root.repr())

        elif user_choice == '10':
            break