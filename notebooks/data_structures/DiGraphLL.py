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
    
    def adjacent(self, node, incoming = True):
        """Your treat! (see exercise 3)"""
        
    def edges(self):
        """Your treat! (see exercise 3). Returns all the edges"""
    
    
if __name__ == "__main__":
    G = DiGraphLL()
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
    print(G)
    
    G.insertNode("Node_7")
    G.insertEdge("Node_1", "Node_7", -1)
    G.insertEdge("Node_2", "Node_7", -2)
    G.insertEdge("Node_5", "Node_7", -5)
    G.insertEdge("Node_7", "Node_2", -2)
    G.insertEdge("Node_7", "Node_3", -3)
    
    print("Size is: {}".format(len(G)))
    print("Nodes: {}".format(G.nodes()))
    print("Graph:")
    print(G)
    G.deleteNode("Node_7")
    G.deleteEdge("Node_6", "Node_2")
    #nodes do not exist! Therefore nothing happens!
    G.insertEdge("72", "25",3)
    print(G)
    print("Nodes: {}".format(G.nodes()))
    G.deleteEdge("72","25")
    print("Nodes: {}".format(G.nodes()))
    print(G)