from collections import deque

class DiGraphAsAdjacencyMatrix:
    def __init__(self):
        self.__nodes = list()
        self.__matrix = list()
        
    def __len__(self):
        """gets the number of nodes"""
        return len(self.__nodes)
        
    def nodes(self):
        return self.__nodes
    def matrix(self):
        return self.__matrix
    
    def __str__(self):
        header = "\t".join([n for n in self.__nodes])
        data = ""
        for i in range(0,len(self.__matrix)):
            data += str(self.__nodes[i]) +"\t" + "\t".join([str(x) for x in self.__matrix[i]]) + "\n"

        return "\t"+ header +"\n" + data
    
    def insertNode(self, node):
        #add the node if not there.
        if node not in self.__nodes:
            self.__nodes.append(node)
            #add a row and a column of zeros in the matrix
            if len(self.__matrix) == 0:
                #first node
                self.__matrix = [[0]]
            else:
                N = len(self.__nodes)
                for row in self.__matrix:
                    row.append(0)
                self.__matrix.append([0 for x in range(N)])
    
    def insertEdge(self, node1, node2, weight):
        i = -1
        j = -1
        if node1 in self.__nodes:
            i = self.__nodes.index(node1)
        if node2 in self.__nodes:
            j = self.__nodes.index(node2)
        if i != -1 and j != -1:
            self.__matrix[i][j] = weight
    
    def deleteEdge(self, node1,node2):
        """removing an edge means to set its
        corresponding place in the matrix to 0"""
        i = -1
        j = -1
        if node1 in self.__nodes:
            i = self.__nodes.index(node1)
        if node2 in self.__nodes:
            j = self.__nodes.index(node2)
        if i != -1 and j != -1:
            self.__matrix[i][j] = 0
    
    def deleteNode(self, node):
        """removing a node means removing
        its corresponding row and column in the matrix"""
        i = -1

        if node in self.__nodes:
            i = self.__nodes.index(node)
        #print("Removing {} at index {}".format(node, i))
        if node != -1:
            self.__matrix.pop(i)
            for row in self.__matrix:
                row.pop(i)
            self.__nodes.pop(i)
    
    
    def adjacent(self, node):
        """returns a list of nodes connected to node"""
        ret = []
        if node in self.__nodes:
            i = self.__nodes.index(node)
            #get both incoming and outgoing edges to return nodes
            for j in range(len(self.__nodes)):
                nodeJ = self.__nodes[j]
                
                #incoming edges
                if self.__matrix[i][j] != 0:
                    ret.append(nodeJ)

        return ret
        
    def adjacentEdge(self, node, incoming = True):
        """
        If incoming == False we look at the row of the node,
        else at the column. An edge is present if weight
        is different from zero
        """
        ret = []
        i = -1
        if node in self.__nodes:
            i = self.__nodes.index(node)
        if i != -1:
            #if the node is present
            if incoming == False:
                for e in range(len(self.__matrix[i])):
                    node2 = self.__nodes[e]
                    w = self.__matrix[i][e]
                    if w != 0:
                        ret.append((node, node2, self.__matrix[i][e]))           
            else:
                for e in range(len(self.__matrix)):
                    node2 = self.__nodes[e]
                    w = self.__matrix[e][i]
                    if w != 0:
                        ret.append((node2, node, self.__matrix[e][i]))
            return ret
    
    def edges(self):
        """Returns all the edges in the graph as triplets"""
        ret = []
        for i in range(len(self.__nodes)):
            start = self.__nodes[i]
            for j in range(len(self.__nodes)):
                end = self.__nodes[j]
                w = self.__matrix[i][j]
                if w != 0:
                    ret.append((start, end, w))
        return ret
    
    def edgeIn(self,node1,node2):
        """
        Checks if there exist an edge between node1 and node2
        (i.e. weight != 0)
        """
        if node1 in self.__nodes and node2 in self.__nodes:
            n1 = self.__nodes.index(node1)
            n2 = self.__nodes.index(node2)
            w =  self.__matrix[n1][n2]
            
            if w != 0:
                return True
            else:
                return False
        
        else:
            return False

class DiGraphAmAnalyzer(DiGraphAsAdjacencyMatrix):    
    def getTopConnected_incoming(self):
        topN = ""
        #accumulator to count connections
        conn = [0]*len(self.nodes())
        for node in range(len(self.nodes())):
            for el in range(len(self.matrix()[node])):
                w = self.matrix()[node][el]
                if w != 0:
                    conn[el] +=1
        M = max(conn)
        ind = [x for x in range(len(conn)) if conn[x] == M]
        return [self.nodes()[x] for x in ind]
    
    def getTopConnected_outgoing(self):
        """Returns the node(s)"""
        topN = []
        conn = -1

        for node in range(len(self.nodes())):
            n = len([x for x in self.matrix()[node] if x != 0])
            if n > conn:
                topN = [self.nodes()[node]]
                conn = n
            else:
                if n == conn:
                    topN.append(self.nodes()[node]) 
                
        return topN
    
    def __hasPathAux__(self, node1,node2):
        if node1 not in self.nodes() or node2 not in self.nodes():
            return False
        else:
            Q = deque()
            Q.append(node1)
            visited = set()
            i2 = self.nodes().index(node2)
            while len(Q) > 0:
                curN = Q.popleft()
                i1 = self.nodes().index(curN)
                #do not travel on already visited nodes
                if curN not in visited:
                    visited.add(curN)
                    #get all outgoing nodes of Q
                    for edge in range(len(self.matrix()[i1])):
                        w = self.matrix()[i1][edge]
                        if w != 0:
                            if edge == i2:
                                return True
                            else:
                                Q.append(self.nodes()[edge])
            
            return False
        
    def hasPath(self, node1, node2):
        #checks both paths and returns True or false
        res = self.__hasPathAux__(node1,node2)
        if res:
            return True
        else:
            return self.__hasPathAux__(node2,node1)
    

if __name__ == "__main__":    
    G = DiGraphAmAnalyzer()
    for i in range(6):
        n = "Node_{}".format(i+1)
        G.insertNode(n)

    for i in range(0,4):
        n = "Node_" + str(i+1)
        six = "Node_6"
        n_plus = "Node_" + str((i+2) % 6)
        G.insertEdge(n, n_plus,0.5)
        G.insertEdge(n, six,1)
    
    G.insertEdge("Node_5", "Node_1", 0.5)
    G.insertEdge("Node_5", "Node_6", 1)
    G.insertEdge("Node_6", "Node_6", 1)
    print("Top connected (outgoing):")
    print(G.getTopConnected_outgoing())
    print("Top connected (incoming):")
    print(G.getTopConnected_incoming())    
    print("\nAdding edge Node_5 -- 0.5 --> Node_5")
    G.insertEdge("Node_5", "Node_5", 0.5)
    print("Top connected (outgoing):")
    print(G.getTopConnected_outgoing())
    print("\nAre Node_1 and Node_4 connected?")
    print("{}".format(G.hasPath("Node_1","Node_4")))
    print("\nRemoving Node_6")
    G.deleteNode("Node_6")
    print("Top connected (outgoing):")
    print(G.getTopConnected_outgoing())
    print("Top connected (incoming):")
    print(G.getTopConnected_incoming())
    G.insertNode("Node_alone")
    G.insertNode("Node_alone2")
    G.insertEdge("Node_alone", "Node_alone2", 1)
    
    print("\nAre Node_1 and Node_alone2 connected?")
    print(G.hasPath("Node_1", "Node_alone2"))
    print("Are Node_alone2 and Node_alone connected?")
    print(G.hasPath("Node_alone2", "Node_alone"))