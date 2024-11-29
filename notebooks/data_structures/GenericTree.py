class GenericTree:
    def __init__(self, value):
        self.__data = value
        self.__parent = None
        self.__child = None
        self.__sibling = None

    def getValue(self):
        return self.__data
    def setValue(self,newvalue):
        self.__data = newvalue

    def getParent(self):
        return self.__parent
    def setParent(self, parent):
        self.__parent = parent

    def getLeftmostChild(self):
        return self.__child

    def getSibling(self):
        return self.__sibling
    def setSibling(self,sib):
        self.__sibling = sib

    def insertSibling(self,sib):
        if type(sib) != GenericTree:
            raise TypeError("parameter sib is not a GenericTree")
        else:
            nextS = None
            if self.__sibling != None:
                nextS = self.__sibling
            self.__sibling = sib
            sib.setParent(self.getParent())
            sib.setSibling(nextS)

    def insertChild(self,child):
        if type(child) != GenericTree:
            raise TypeError("parameter child is not a GenericTree")
        else:
            nextC = None
            print("from {} adding child --> {}".format(self.getValue(),
                                                       child.getValue()))
            if self.__child != None:
                nextC = self.__child
            child.setParent(self)
            child.setSibling(nextC)
            self.__child = child

    def deleteChild(self):
        if self.__child != None:
            #moves along the sibling structure of child
            self.__child = self.__child.getSibling()

    def deleteSibling(self):
        if self.__sibling != None:
            #moves along the sibling structure of the sibling
            self.__sibling = self.__sibling.getSibling()

if __name__ == "__main__":
    g = GenericTree("Root")
    g1 = GenericTree("First")
    g2 = GenericTree("Second")
    g3 = GenericTree("Third")
    g4 = GenericTree("Fourth")
    g5 = GenericTree("Fifth")
    g6 = GenericTree("Sixth")
    g7 = GenericTree("Seventh")
    g8 = GenericTree("Eighth")
    g9 = GenericTree("Ninth")
    g10 = GenericTree("Tenth")
    g11 = GenericTree("Eleventh")

    #root
    g.insertChild(g4)
    g.insertChild(g3)
    g.insertChild(g2)
    g.insertChild(g1)
    #second
    g2.insertChild(g6)
    g2.insertChild(g5)
    #fourth
    g4.insertChild(g7)
    g7.insertSibling(g11)
    #sixth
    g6.insertChild(g10)
    g6.insertChild(g9)
    g6.insertChild(g8)

    #let's print some stuff
    nodes = [g,g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11]
    for n in nodes:
        print("Node {}:".format(n.getValue()))
        par = n.getParent()
        if par != None:
            par = par.getValue()
        print("\t has parent: {}".format(par))
        c = n.getLeftmostChild()
        children = []
        if c != None:
            children.append(c.getValue())
            nc = c.getSibling()
            while nc != None:
                children.append(nc.getValue())
                nc = nc.getSibling()
        print("\t has children: {}".format(",".join(children)))
        s = n.getSibling()
        sibs = []
        if s != None:
            sibs.append(s.getValue())
            ns = s.getSibling()
            while ns != None:
                sibs.append(ns.getValue())
                ns = ns.getSibling()
        print("\t has next siblings: {}".format(",".join(sibs)))