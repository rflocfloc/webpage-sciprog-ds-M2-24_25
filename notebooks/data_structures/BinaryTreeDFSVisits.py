class BinaryTree:
    def __init__(self, value):
        self.__data = value
        self.__right = None
        self.__left = None
        self.__parent = None

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
    def insertLeft(self, tree):
        if self.__left == None:
            self.__left = tree
            tree.setParent(self)

    def deleteRight(self):
        self.__right = None
    def deleteLeft(self):
        self.__left = None

    def preOrderDFS(self):
        if self != None:
            r = self.getRight()
            l = self.getLeft()
            print(self.getValue()) # print before recursive calls!
            if l != None:
                l.preOrderDFS()
            if r != None:
                r.preOrderDFS()

    def inOrderDFS(self):
        if self != None:
            r = self.getRight()
            l = self.getLeft()
            if l != None:
                l.inOrderDFS()
            print(self.getValue()) # print in the between the recursive calls!
            if r != None:
                r.inOrderDFS()

    def postOrderDFS(self):
        if self != None:
            r = self.getRight()
            l = self.getLeft()
            if l != None:
                l.postOrderDFS()
            if r != None:
                r.postOrderDFS()
            print(self.getValue()) # print after the recursive calls!

def printTree(root):
    cur = root
    #each element is a node and a depth
    #depth is used to format prints (with tabs)
    nodes = [(cur,0)]
    tabs = ""
    lev = 0
    while len(nodes) >0:
        cur, lev = nodes.pop(-1)
        #print("{}{}".format("\t"*lev, cur.getValue()))
        if cur.getRight() != None:
            print ("{}{} (r)-> {}".format("\t"*lev,
                                          cur.getValue(),
                                          cur.getRight().getValue()))
            nodes.append((cur.getRight(), lev+1))
        if cur.getLeft() != None:
            print ("{}{} (l)-> {}".format("\t"*lev,
                                          cur.getValue(),
                                          cur.getLeft().getValue()))
            nodes.append((cur.getLeft(), lev+1))

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

    BT.insertLeft(bt1)
    BT.insertRight(bt2)
    
    bt2.insertLeft(bt3)
    
    bt3.insertLeft(bt4)
    bt3.insertRight(bt5)
    bt2.insertRight(bt6)
    bt1.insertRight(bt5b)
    bt1.insertLeft(bt5a)
    bt5b.insertRight(bt5c)

    printTree(BT)
    
    print("Pre-order DFS:")
    BT.preOrderDFS()
    print("\nIn-order DFS:")
    BT.inOrderDFS()
    print("\nPost-order DFS:")
    BT.postOrderDFS()