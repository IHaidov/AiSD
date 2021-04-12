class BST(object):

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def DSW(self):
        if None != self.root:
            self.createBackbone()  # effectively: createBackbone( self.root)
            self.createPerfectBST()  # effectively: createPerfectBST( self.root)

    # =====================================================================
    # Time complexity: O(n)
    # =====================================================================
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

    # =======================================================================
    #   Before      After
    #    Gr          Gr
    #     \           \
    #     Par         Ch
    #    /  \        /  \
    #   Ch   Z      X   Par
    #  /  \            /  \
    # X    Y          Y    Z
    # =======================================================================
    def rotateRight(self, grandParent, parent, leftChild):
        if None != grandParent:
            grandParent.right = leftChild
        else:
            self.root = leftChild

        parent.left = leftChild.right
        leftChild.right = parent
        return grandParent

    # =======================================================================
    # Time complexity: O(n)
    # =======================================================================
    def createPerfectBST(self):
        n = self.size()

        # m = 2^floor[lg(n+1)]-1, ie the greatest power of 2 less than n: minus 1
        m = self.greatestPowerOf2LessThanN(n + 1) - 1
        self.makeRotations(n - m)

        while m > 1:
            m /= 2
            self.makeRotations(m)

    # =======================================================================
    # Time complexity: log(n)
    # =======================================================================
    def greatestPowerOf2LessThanN(self, n):
        x = self.MSB(n)  # MSB
        return (1 << x)  # 2^x

    # =======================================================================
    # Time complexity: log(n)
    # return the index of most significant set bit: index of
    # least significant bit is 0
    # =======================================================================
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
                    self.rotateLeft(grandParent, parent, child);
                    grandParent = child;
                    parent = grandParent.right;
                    child = parent.right;
                else:
                    break
            except AttributeError:  # TypeError
                break
            bound -= 1

    def rotateLeft(self, grandParent, parent, rightChild):
        if None != grandParent:
            grandParent.right = rightChild
        else:
            self.root = rightChild

        parent.right = rightChild.left
        rightChild.left = parent