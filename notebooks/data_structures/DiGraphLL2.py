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