class BinarySearchTree:
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
        
    def inOrderDFS(self):
        ret = []
        if self != None:
            r = self.getRight()
            l = self.getLeft()
            if l != None:
                ret.extend(l.inOrderDFS())
                
            ret.append(self.getValue())
            
            if r != None:
                ret.extend(r.inOrderDFS())
        return ret

def createBST(intList):
    BST = None
    if len(intList) > 0:
        BST = BinarySearchTree(intList[0])
        for el in intList[1:]:
            cur_el = BST
            alreadyPresent = False
            prev_el = None
            while cur_el != None:
                prev_el = cur_el
                cv = cur_el.getValue()
                if  cv > el:
                    cur_el = cur_el.getLeft()
                elif cv < el:
                    cur_el = cur_el.getRight()
                else:
                    # cv == el (el is already present)
                    # not allowed by rule c, so skip it
                    alreadyPresent = True
                    #print("El {} already present".format(el))
                    break
                
            if not alreadyPresent:
                node = BinarySearchTree(el)
                node.setParent(prev_el)
                if prev_el.getValue() > el:
                    prev_el.insertLeft(node)
                else:
                    prev_el.insertRight(node)
                
    return BST
    
def searchBST(BST, element):
    if BST == None or element == None:
        return False
    else:
        cur_el = BST
        while cur_el != None:
            if cur_el.getValue() == element:
                return True
            else:
                if cur_el.getValue()> element:
                    cur_el = cur_el.getLeft()
                else:
                    cur_el = cur_el.getRight()
        
        return False


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

def plotGraph(tree):    
    #uses pygraphviz 
    G=pgv.AGraph(directed=True)
    
    levels = [tree]
    while len(levels) > 0:
        cur_n = levels.pop()
        if cur_n != None:
            G.add_node(cur_n.getValue(), color = 'black')
            r = cur_n.getRight()
            l = cur_n.getLeft()
            if l != None:
                G.add_node(l.getValue(), color = 'black')
                G.add_edge(cur_n.getValue(), l.getValue())
                levels.append(l)
            if r != None:
                G.add_node(r.getValue(), color = 'black')
                G.add_edge(cur_n.getValue(), r.getValue())
                levels.append(r)
    G.layout(prog='dot') # use dot
    #In the following, the path of the graph. Change
    #it to your liking
    G.draw('images/BST_test.png')
    
if __name__ == "__main__":
    import random
    #import pygraphviz as pgv
    #import time 
    inList = []
    for i in range(1000):
        inList.append(random.randint(0,10000))
        
    BST = createBST(inList)
    
    #printTree(BST)
    #plotGraph(BST)
    for i in range(100):
        v = random.randint(0,100)
        #s_t = time.time()
        ok = searchBST(BST, v)
        #e_t = time.time()
        okL = v in inList
        #e_t2 = time.time()
        print("el {} : present? {}".format(v, ok))
        #print("Time BST:{:.6f} list:{:.6f}".format(e_t - s_t,
        #                                           e_t2 - e_t
        #                                            ))
        assert(ok == okL)
    sorted = BST.inOrderDFS()
    print("\nIn order DFS (first 100 elements):")
    print(sorted[0:100])