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
            #line modified
            tree.setDepth(self.getDepth() + 1)              
    def insertLeft(self, tree):
        if self.__left == None:
            self.__left = tree
            #line modified
            tree.setDepth(self.getDepth() + 1)
            tree.setParent(self)
            
    def deleteRight(self):
        self.__right = None    
    def deleteLeft(self):
        self.__left = None
            
def getCommonAncestor(node1, node2):
    if node1 == node2:
        return node1
    
    if node1 == None or node2 == None:
        return None
    
    n1anc = set()
    n1anc.add(node1)
    
    anc = node1.getParent()
    while anc != None:
        n1anc.add(anc)
        anc = anc.getParent()
    
    anc = node2
    while anc != None:
        if anc in n1anc:
            return anc
        else:
            anc = anc.getParent()
    
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
    
    ca = getCommonAncestor(bt7,bt5)
    if ca != None:
        ca = ca.getValue()
    print("The CA between {} and {} is: {}".format(bt7.getValue(),
                                                  bt5.getValue(),
                                                  ca))
    ca = getCommonAncestor(bt7,bt10)
    if ca != None:
        ca = ca.getValue()
    print("The CA between {} and {} is: {}".format(bt7.getValue(),
                                                  bt10.getValue(),
                                                  ca))
    ca = getCommonAncestor(bt7,bt8)
    if ca != None:
        ca = ca.getValue()
    print("The CA between {} and {} is: {}".format(bt7.getValue(),
                                                  bt8.getValue(),
                                                  ca))
    
    ca = getCommonAncestor(bt5b,bt8)
    if ca != None:
        ca = ca.getValue()
    print("The CA between {} and {} is: {}".format(bt5b.getValue(),
                                                  bt8.getValue(),
                                                  ca))