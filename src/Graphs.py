    
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
        self.allVertex = {}
    
    def addVertex(self, key):
        newVertex = Vertex(key)
        self.allVertex[key] = newVertex
        return newVertex
    
    def getVertex(self, key):
        return None if not self.containsVertex(key) else self.vertLallVertexist[key]
    
    def containsVertex(self, key):
        return key in self.allVertex
    
    def addEdge(self, vertex1, vertex2, weight):
        
        if not self.containsVertex(vertex1):  
            self.addVertex(vertex1)                
        if not self.containsVertex(vertex2):            
            self.addVertex(vertex2)                   
            
        # Add (Edges, Weight) here
        self.vertList[vertex1].addNeighbor(self.vertList[vertex2], weight)    
    
    def getVertices(self):
        return self.allVertex.keys()
    
    def printGraph(self):
        for x in self.allVertex:
            print("{} - {}".format(x, self.vertList[x]))
            

class GraphScenarios:
    def __init__(self):
        pass
    
    def dfs(self):
        pass
    
    def bfs(self):
        pass
    
    def unionFind(self):
        pass
    
    def cycleFind(self):
        pass
    
    def biPartition(self):
        pass
    
    def topologicalSort(self):
        pass
    
    def findShortestPath(self):
        pass
    
    
    