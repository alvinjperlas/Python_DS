





    
# Nodes    
class Vertex:
    def __init__(self,key):
        self.id = key           # Each node has to have an ID
        self.connectedTo = {}   # Dictionary of Nodes connected to self.
        self.visited = False

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight  # Append to dictionary (Node, weight)

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()  # Returns list of Keys that are contained in Dictionary. (All Nodes connected to it on first degree)

    def getID(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]    
    
    def setVisited(self, value):
        self.visited = value
        
    def getVisited(self):
        return self.visited
    
    


class Graph:
    def __init__(self):
        pass
    
    
