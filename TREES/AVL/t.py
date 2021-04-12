import unittest
from AVL.avl_creation import BST
#from cStringIO import StringIO
import sys


class Test(unittest.TestCase):

    def testDswBalanceEmptyBST(self):
        emptyTree = BST()

        self.assertEquals(0, emptyTree.height())
        emptyTree.DSW()
        self.assertEquals(0, emptyTree.height())

    def testDswBalanceForwardSlashTree(self):
        leftChildren = BST()

        self.assertEquals(0, leftChildren.height())
        tape = [87, 75, 62, 50, 37, 25, 12]
        for i in tape:
            leftChildren.add(i)

        self.assertEquals(len(tape), leftChildren.size())
        self.assertEquals(len(tape), leftChildren.height())
        leftChildren.DSW()
        self.assertEquals(3, leftChildren.height())
        self.assertEquals(len(tape), leftChildren.size())

    def testDswBalanceBackslashTree(self):
        rightChildren = BST()

        self.assertEquals(0, rightChildren.height())
        tape = [12, 25, 37, 50, 62, 75, 87]
        for i in tape:
            rightChildren.add(i)

        self.assertEquals(len(tape), rightChildren.size())
        self.assertEquals(len(tape), rightChildren.height())
        rightChildren.DSW()
        self.assertEquals(3, rightChildren.height())
        self.assertEquals(len(tape), rightChildren.size())

    def testDswBalancePerfectTree(self):
        perfectBST = BST()

        self.assertEquals(0, perfectBST.height())
        tape = [50, 25, 75, 12, 40, 62, 87]
        for i in tape:
            perfectBST.add(i)

        self.assertEquals(len(tape), perfectBST.size())
        self.assertEquals(3, perfectBST.height())
        perfectBST.DSW()
        self.assertEquals(3, perfectBST.height())
        self.assertEquals(len(tape), perfectBST.size())

    def testDswBalanceWeirdTree(self):
        weirdBST = BST()

        self.assertEquals(0, weirdBST.height())
        tape = [87, 75, 62, 50, 37, 25, 12, 6, 15, 40]
        for i in tape:
            weirdBST.add(i)

        self.assertEquals(len(tape), weirdBST.size())
        self.assertEquals(8, weirdBST.height())
        weirdBST.DSW()
        self.assertEquals(4, weirdBST.height())
        self.assertEquals(len(tape), weirdBST.size())
