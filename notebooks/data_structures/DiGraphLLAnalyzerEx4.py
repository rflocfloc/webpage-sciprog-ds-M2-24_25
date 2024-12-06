from collections import deque

class DiGraphLL:
    def __init__(self):
        """Every node is an element in the dictionary. 
        The key is the node id and the value is a dictionary
        with second node as key and the weight as value
        """
        self.__nodes = dict()
        
    def insertNode(self, node):
        test = self.__nodes.get(node, None)
        
        if test == None:
            self.__nodes[node] = {}
            #print("Node {} added".format(node))
    
    def insertEdge(self, node1, node2, weight):
        test = self.__nodes.get(node1, None)
        test1 = self.__nodes.get(node2, None)
        if test != None and test1 != None:
            #if both nodes exist othewise don't do anything
            test = self.__nodes[node1].get(node2, None)
            if test != None:
                exStr = "Edge {} --> {} already existing.".format(node1,node2)
                raise Exception(exStr)
            else:    
                #print("Inserted {}-->{} ({})".format(node1,node2,weight))
                self.__nodes[node1][node2] = weight
        
    
    def deleteNode(self, node):
        test = self.__nodes.get(node, None)
        if test != None:
            self.__nodes.pop(node)
        # need to loop through all the nodes!!!
        for n in self.__nodes:
            test = self.__nodes[n].get(node, None)
            if test != None:
                self.__nodes[n].pop(node)
    
    def deleteEdge(self, node1,node2):
        test = self.__nodes.get(node1, None)
        if test != None:
            test = self.__nodes[node1].get(node2, None)
            if test != None:
                self.__nodes[node1].pop(node2)
                
    def __len__(self):
        return len(self.__nodes)
    
    def nodes(self):
        return list(self.__nodes.keys())
    
    def graph(self):
        return self.__nodes
    
    def __str__(self):
        ret = ""
        for n in self.__nodes:
            for edge in self.__nodes[n]:           
                ret += "{} -- {} --> {}\n".format(str(n),
                                                  str(self.__nodes[n][edge]),
                                                  str(edge))
        return ret
    
    def adjacent(self, node):
        """returns a list of nodes connected to node"""
        ret = []
        test = self.__nodes.get(node, None)
        if test != None:
            for n in self.__nodes:
                if n == node:
                    #all outgoing edges
                    for edge in self.__nodes[node]:
                        ret.append(edge)
                else:
                    #all incoming edges
                    for edge in self.__nodes[n]:
                        if edge == node:
                            ret.append(n)
            
        return ret

    def adjacentEdge(self, node, incoming = True):
        """
        If incoming == False
        we look at the edges of the node
        else we need to loop through all the nodes. 
        An edge is present if there is a 
        corresponding entry in the dictionary.
        If no such nodes exist returns None
        """
        ret = []
        if incoming == False:
            edges = self.__nodes.get(node,None)
            if edges != None:
                for e in edges:
                    w = self.__nodes[node][e]
                    ret.append((node, e, w))
                return ret
        else:
            for n in self.__nodes:
                edge = self.__nodes[n].get(node,None)
                if edge != None:
                    ret.append((n,node, edge))
            return ret
         
    def edges(self):
        """Returns all the edges in a list of triplets"""
        ret = []
        for node in self.__nodes:
            for edge in self.__nodes[node]:
                w = self.__nodes[node][edge]
                ret.append((node,edge, w))
        return ret
 
    def edgeIn(self,node1,node2):
        """Checks if edge node1 --> node2 is present"""
        n1 = self.__nodes.get(node1, None)
        if n1 != None:
            n2 = self.__nodes[node1].get(node2, None)
            if n2 != None:
                return True
            else:
                return False
        else: 
            return False 

class DiGraphLLAnalyzer(DiGraphLL):
    """Every node is an element in the dictionary. 
        The key is the node id and the value is a dictionary
        with key second node and value the weight
        """

    def getTopConnected_incoming(self):
        
        topN = ""
        #accumulator to count connections
        conn = [0]*len(self.nodes())
        for node in self.nodes():
            for el in self.graph()[node]:
                elInd = self.nodes().index(el)
                conn[elInd] +=1
        M = max(conn)
        ind = [x for x in range(len(conn)) if conn[x] == M]
        return [self.nodes()[x] for x in ind]
    
    def getTopConnected_outgoing(self):
        """Returns the node(s)"""
        topN = []
        conn = -1

        for node in self.nodes():
            n = len(self.graph()[node])
            if n > conn:
                topN = [node]
                conn = n
            else:
                if n == conn:
                    topN.append(node) 
                
        return topN
    
    def hasPathAux(self, node1,node2):
        if node1 not in self.nodes() or node2 not in self.nodes():
            return False
        else:
            Q = deque()
            Q.append(node1)
            visited = set()
            while len(Q) > 0:
                curN = Q.popleft()
                #do not travel on already visited nodes
                if curN not in visited:
                    visited.add(curN)
                    #get all outgoing nodes of Q
                    for edge in self.graph()[curN]:
                        if edge == node2:
                            return True
                        else:
                            Q.append(edge)
            
            return False
        
    def hasPath(self, node1, node2):
        #checks both paths and returns True or false
        res = self.hasPathAux(node1,node2)
        if res:
            return True
        else:
            return self.hasPathAux(node2,node1)
                        
    def BFSvisit(self, root, target):
        len_path = 0
        
        if root in self.graph():
            Q = deque()
            Q.append(root)
            #visited is a set of visited nodes
            visited = set()
            if root == target:
                return len_path
            visited.add(root)
            while len(Q) > 0:
                curNode = Q.popleft()
                len_path = len_path + 1
                outGoingEdges = self.adjacentEdge(curNode, incoming = False)
                nextNodes = []
                if outGoingEdges != None:
                    #remember that self.adjacentEdge returns:
                    #[('node1','node2', weight1), ...('node1', 'nodeX', weightX)]
                    nextNodes = [x[1] for x in outGoingEdges]
                    if target in nextNodes:
                        return len_path + 1
                print("From {}:".format(curNode))
                for nextNode in nextNodes:
                    if nextNode not in visited:
                        Q.append(nextNode)
                        visited.add(nextNode)
                        print("\t --> {}".format(nextNode ))
            return None 
    
    def BFS(self, root):
        print("Starting from {}".format(root))
        visited = set()
        visited.add(root)
        self.BFSvisit(root,visited)
        for node in self.nodes():
            if node not in visited:
                print("Starting from {}".format(node)) 
                self.BFSvisit(node,visited)
   
    def findShortestPath(self, node1, node2):
        Q = deque()
        Q.append(node1)
        visited = set()
        #visited is a set of visited nodes
        visited.add(node1)
        #for each node (apart from node1)
        #this will store the node that led to it
        #eg. if path is node1--> node3-->node2
        # previous[node2] = node3
        # previous[node3] = node1
        previous = dict()
        found = False
        while len(Q) > 0 and not found:
            curNode = Q.popleft()
            
            outGoingEdges = self.adjacentEdge(curNode, incoming = False)
            nextNodes = []
            if outGoingEdges != None:
                #remember that self.adjacentEdge returns:
                #[('node1','node2', weight1), ...('node1', 'nodeX', weightX)]
                nextNodes = [x[1] for x in outGoingEdges]
            
            for nextNode in nextNodes:
                if nextNode not in visited:
                    if nextNode == node2:
                        previous[node2] = curNode
                        found = True
                    else:
                        Q.append(nextNode)
                        visited.add(nextNode)
                        previous[nextNode] = curNode
                        

        #if node2 is in the previous dictionary:
        ret = [node2]
        p = previous.get(node2, None)
        
        while p != None:
            ret.append(p)
            p = previous.get(p,None)
    
        #note that ret has the reverseof the path
        #[node2, node3, node1]
        #or just [node2] if not path exists
        return ret
    
    def printPath(self,path):
        L = len(path)
        print("Shortest path between: {} and {}".format(path[-1],
                                                            path[0])
                 )
        for i in range(len(path) -1,0,-1):
            print("{}{} --> {}".format("\t"*(L-i-1),
                                       path[i],
                                       path[i-1]))
    
    def shortestPath(self, node1, node2):
        nodes = self.nodes()
        if node1 not in nodes or node2 not in nodes:
            """one of the two is not in the graph"""
            return None 
        else:
            if node1 == node2:
                """the path is just the node"""
                return node1
            else:
                
                path = self.findShortestPath(node1,node2)
                path1 = self.findShortestPath(node2,node1)
                if path == [node2] and path1 == [node1]:
                    print("No paths exist between {} and {}".format(node1,
                                                                    node2))
                else:
                    L = len(nodes)
                    L1 = L
                    if path != [node2]:
                        L = len(path)
                    if path1 != [node1]:
                        L1 = len(path1)

                    if L < L1:
                        """print first path"""
                        self.printPath(path)

                    else:
                        """print second path"""
                        self.printPath(path1)
        
    def testCyclic(self, root, visited, recStack = set()):
        visited.add(root)
        recStack.add(root)
        ## Uncomment print lines to see what is going on
        print("CURRENT: {}".format(root))
        print("\tStack:{}".format(recStack))
        outGoingEdges = self.adjacentEdge(root, incoming = False)
        nextNodes = []
        if len(outGoingEdges) > 0:
            nextNodes = [x[1] for x in outGoingEdges]
            print("\tNEXTnodes:{}".format(nextNodes))
            for nextN in nextNodes:
                if nextN not in visited:
                    print("\tNext:{}".format(nextN))
                    if self.testCyclic(nextN,visited,recStack) == True:
                        return True
                else:
                    if nextN in recStack:
                        print("\t{} --> {} closes cycle".format(root,nextN))
                        return True
                    
        #when the recursion ends
        #we remove the element from the stack
        recStack.pop()
        return False
    
    def isCyclic(self):
        visited = set()
        ret = False
        stack = set()
        for node in self.nodes():
            if node not in visited:
                ret = ret or self.testCyclic(node, visited, stack)
        return ret
                
if __name__ == "__main__":
    G = DiGraphLLAnalyzer()
    G1 = DiGraphLLAnalyzer()
    G2 = DiGraphLLAnalyzer()
    for i in range(1,10):
        G.insertNode("Node_" + str(i))
        G1.insertNode("Node_" + str(i))
        if i<9:
            G2.insertNode("Node_" + str(i))
        
    G.insertEdge("Node_1", "Node_2",1)
    G.insertEdge("Node_2", "Node_1",1)
    G.insertEdge("Node_1", "Node_3",1)
    G.insertEdge("Node_1", "Node_5",1)
    G.insertEdge("Node_2", "Node_3",1)
    G.insertEdge("Node_2", "Node_5",1)
    G.insertEdge("Node_3", "Node_4",1)
    G.insertEdge("Node_3", "Node_6",1)
    G.insertEdge("Node_5", "Node_3",1)
    G.insertEdge("Node_5", "Node_5",1)
    G.insertEdge("Node_6", "Node_4",1)
    G.insertEdge("Node_6", "Node_6",1)
    G.insertEdge("Node_7", "Node_5",1)
    G.insertEdge("Node_5", "Node_8",1)
    G.insertEdge("Node_8", "Node_7",1)
    G.insertEdge("Node_9", "Node_2",1)
    
    #Graph G1
    G1.insertEdge("Node_1" ,"Node_2", 1)
    G1.insertEdge("Node_1" ,"Node_4", 1)
    G1.insertEdge("Node_1" ,"Node_6", 1)
    G1.insertEdge("Node_1" ,"Node_7", 1)
    G1.insertEdge("Node_2" ,"Node_7", 1)
    G1.insertEdge("Node_3" ,"Node_4", 1)
    G1.insertEdge("Node_5" ,"Node_4", 1)
    G1.insertEdge("Node_6" ,"Node_5", 1)
    G1.insertEdge("Node_6" ,"Node_8", 1)
    G1.insertEdge("Node_7" ,"Node_9", 1)
    G1.insertEdge("Node_8" ,"Node_9", 1)
    
    #Graph G2
    G2.insertEdge("Node_1" ,"Node_2", 1)
    G2.insertEdge("Node_2" ,"Node_3", 1)
    G2.insertEdge("Node_2" ,"Node_4", 1)
    G2.insertEdge("Node_2" ,"Node_5", 1)
    G2.insertEdge("Node_6" ,"Node_2", 1)
    G2.insertEdge("Node_6" ,"Node_7",1)
    G2.insertEdge("Node_8" ,"Node_7", 1)
    G2.insertEdge("Node_8" ,"Node_4", 1)
    G2.insertEdge("Node_7" ,"Node_5", 1)
      
    print("Is G cyclic? {}".format(G.isCyclic()))
    print("\nG1:")
    print("Is G1 cyclic? {}".format(G1.isCyclic()))
    print("\nG2:")
    print("Is G2 cyclic? {}".format(G2.isCyclic()))