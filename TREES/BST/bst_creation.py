#!/usr/bin/python
import math

#from BST.dsw import BST

class BST_Tree(object):
    def __init__(self, val=None):
        self.root = Tree()

    def getRoot(self):
        return self.root

    def DSW(self):
        if None != self.root:
            self.createBackbone()
            self.createPerfectBST()

    def createBackbone(self):
        grandParent = None
        parent = self.root
        leftChild = None

        while None != parent:
            leftChild = parent.left
            if None != leftChild:
                grandParent = self.rotateRight(grandParent, parent, leftChild)
                parent = leftChild
            else:
                grandParent = parent
                parent = parent.right



    def rotateRight(self, grandParent, parent, leftChild):
        if None != grandParent:
            grandParent.right = leftChild
        else:
            self.root = leftChild

        parent.left = leftChild.right
        leftChild.right = parent
        return grandParent

    def createPerfectBST(self):
        n = self.root.size()

        # m = 2^floor[lg(n+1)]-1, ie the greatest power of 2 less than n: minus 1
        m = self.greatestPowerOf2LessThanN(n + 1) - 1
        self.makeRotations(n - m)

        while m > 1:
            m //= 2
            self.makeRotations(m)

    def greatestPowerOf2LessThanN(self, n):
        x = self.MSB(n)  # MSB
        return (1 << x)  # 2^x


        #-------------------------------------------------------
        # return the index of most significant set bit: index of
        # least significant bit is 0
        #-------------------------------------------------------

    def MSB(self, n):
        ndx = 0
        while 1 < n:
            n = (n >> 1)
            ndx += 1
        return ndx

    def makeRotations(self, bound):
        grandParent = None
        parent = self.root
        child = self.root.right
        while bound > 0:
            try:
                if None != child:
                    self.rotateLeft(grandParent, parent, child)
                    grandParent = child
                    parent = grandParent.right
                    child = parent.right
                else:
                    break
            except AttributeError:
                break
            bound -= 1

    def rotateLeft(self, grandParent, parent, rightChild):
        if None != grandParent:
            grandParent.right = rightChild
        else:
            self.root = rightChild

        parent.right = rightChild.left
        rightChild.left = parent

class Tree:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        self.tallness = 1

    def size(self):

        size = 0
        if self != None:
            size += 1
            if self.left != None:
                size += self.left.size()
            if self.right != None:
                size += self.right.size()
        return size
    def add(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.add(val)
                return
            self.left = Tree(val)
            return

        if self.right:
            self.right.add(val)
            return
        self.right = Tree(val)

    def find(self, val):
        if self is not None:
            return self._find(val, self)
        else:
            return None

    def _find(self, val, node):
        if val == node.val:
            return node
        elif (val < node.val and node.left is not None):
            return self._find(val, node.left)
        elif (val > node.val and node.right is not None):
            return self._find(val, node.right)

    def delete_postorder(self):
        if self.left is not None:
            self.left.delete_postorder()
        if self.right is not None:
            self.right.delete_postorder()
        if self.val is not None:
            self.val = None
            self.right = self.right = None
        return self

    def delete(self, val):
        if self == None or self.val == None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

    def repr(self):

        if not self:
            return 'Dzewo puste. Proszę dodać elementy.'
        the_tree = '\n'
        nodes = [self]
        cur_tallness = self.tallness
        space = ' ' * (40 - int(len(str(self.val))) // 2)
        buffer = ' ' * (60 - int(len(str(self.val))) // 2)
        while True:
            if all(n is None for n in nodes):
                break
            cur_tallness -= 1
            this_row = ' '
            next_row = ' '
            next_nodes = []
            for cur_node in nodes:
                if not cur_node:
                    this_row += '           ' + space
                    next_nodes.extend([None, None])
                if cur_node and cur_node.val is not Tree:
                    this_row += f'{buffer}{str(cur_node.val)}{buffer}'
                if cur_node and cur_node.left:
                    next_nodes.append(cur_node.left)
                    next_row += space + '/' + space
                else:
                    next_nodes.append(None)
                    next_row += '       ' + space
                if cur_node and cur_node.right:
                    next_nodes.append(cur_node.right)
                    next_row += '\\' + space
                else:
                    next_nodes.append(None)
                    next_row += '       ' + space
            the_tree += (cur_tallness * '   ' + this_row + '\n' + cur_tallness * '   ' + next_row + '\n')
            space = ' ' * int(len(space) // 2)
            buffer = ' ' * int(len(buffer) // 2)
            nodes = next_nodes
        return the_tree






def height(node):
    # Base Case : Tree is empty
    if node is None:
        return 0
    leftHeight = height(node.left)
    rightHeight = height(node.right)
    if leftHeight > rightHeight:
        return leftHeight + 1
    else:

        return rightHeight + 1


def minValue(node):
    current = node
    print("Śćieżka do minimalnej wartości:")
    # loop down to find the lefmost leaf
    while (current.left is not None):
        print(current.val)
        current = current.left

    print("Minimalna wartość: ")
    return current.val


def maxValue(node):
    current = node
    print("Śćieżka do maksymalnej wartości:")
    # loop down to find the lefmost leaf
    while (current.right is not None):
        print(current.val)
        current = current.right
    print("Maksymalna wartość: ")
    return current.val


def isBalanced(root):
    # Base condition
    if root is None:
        return True

    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)

    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and isBalanced(
            root.left) is True and isBalanced(root.right) is True:
        return True
    return False




