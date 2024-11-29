class BinaryTree:
    def __init__(self, value):
        self.__data = value
        self.__right = None
        self.__left = None
        self.__parent = None
        self.__depth = 0 #new param

    # new method
    def getDepth(self):
        return self.__depth
    # new method
    def setDepth(self, newdepth):
        self.__depth = newdepth

    def getValue(self):
        return self.__data
    def setValue(self, newValue):
        self.__data = newValue

    def getParent(self):
        return self.__parent
    def setParent(self, tree):
        self.__parent = tree

    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left

    def insertRight(self, tree):
        if self.__right == None:
            self.__right = tree
            tree.setParent(self)
            tree.setDepth(self.getDepth() + 1)
    def insertLeft(self, tree):
        if self.__left == None:
            self.__left = tree
            tree.setDepth(self.getDepth() + 1)
            tree.setParent(self)

    def deleteRight(self):
        self.__right = None
    def deleteLeft(self):
        self.__left = None

def getWidth(tree):
    """gets the width of the tree"""
    if tree == None:
        return 0

    level = [tree]
    res = 1
    while len(level) > 0:
        tmp = []
        for t in level:
            r = t.getRight()
            l = t.getLeft()
            if r != None:
                tmp.append(r)
            if l != None:
                tmp.append(l)
        res = max(res,len(tmp))
        level = tmp

    return res

def getMinHeight(tree):
    """gets the minimum height of the tree in nodes"""
    if tree == None:
        return 0

    level = [tree]
    res = 1
    while len(level) > 0:
        tmp = []
        for t in level:
            r = t.getRight()
            l = t.getLeft()
            if r == None and l == None:
                return res
            else:
                if r != None:
                    tmp.append(r)
                if l != None:
                    tmp.append(l)
        level = tmp
        res += 1
    return res

def nodesAtLevel(tree,k):
    """returns the nodes at level k"""
    if tree == None:
        return 0

    level = [tree]
    cnt = 0
    while cnt != k and len(level) > 0:
        tmp = []
        for t in level:
            r = t.getRight()
            l = t.getLeft()
            if l != None:
                tmp.append(l)
            if r != None:
                tmp.append(r)

        level = tmp
        cnt += 1
    if len(level) == 0:
        return None
    else:
        vals = [x.getValue() for x in level if x != None]
        return vals

if __name__ == "__main__":
    BT = BinaryTree("Root")
    bt1 = BinaryTree(1)
    bt2 = BinaryTree(2)
    bt3 = BinaryTree(3)
    bt4 = BinaryTree(4)
    bt5 = BinaryTree(5)
    bt6 = BinaryTree(6)
    bt5a = BinaryTree("5a")
    bt5b = BinaryTree("5b")
    bt5c = BinaryTree("5c")
    bt7 = BinaryTree(7)
    bt8 = BinaryTree(8)
    bt9 = BinaryTree(9)
    bt10 = BinaryTree(10)
    BT.insertLeft(bt1)
    BT.insertRight(bt2)
    bt2.insertLeft(bt3)
    bt3.insertLeft(bt4)
    bt3.insertRight(bt5)
    bt2.insertRight(bt6)
    bt1.insertRight(bt5b)
    bt1.insertLeft(bt5a)
    bt5b.insertRight(bt5c)
    bt4.insertRight(bt7)
    bt4.insertLeft(bt8)
    bt6.insertRight(bt10)
    bt6.insertLeft(bt9)

    print("The width of BT is {}".format(getWidth(BT)))
    print("The minimum height of BT is {}".format(getMinHeight(BT)))
    for i in range(0,6):
        print("Nodes at level {}: {}".format(i,nodesAtLevel(BT,i)))
    print("The minimum height of BT is {}".format(getMinHeight(BT)))
    bt1.deleteLeft()
    print("Deleting 5ca")
    print("The minimum height of BT is {}".format(getMinHeight(BT)))
    bt5d = BinaryTree("5d")
    bt5c.insertLeft(bt5d)
    print("Adding 5d as left child of 5c")
    print("The minimum height of BT is {}".format(getMinHeight(BT)))