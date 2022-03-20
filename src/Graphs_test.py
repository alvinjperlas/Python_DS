from Graphs import Graph   # The code to test
import unittest   # The test framework


class Test_Graphs(unittest.TestCase):
    def setUp(self):
        pass
      
    def _getTestHeap(self):
        myGraph = Graph()
        myGraph.addVertex('A')
        myGraph.addVertex('B')
        myGraph.addVertex('C')
        myGraph.addVertex('D')
        myGraph.addVertex('E')
        myGraph.addVertex('F')
        myGraph.addVertex('G')
        myGraph.addVertex('H')
        myGraph.addVertex('I')
        myGraph.addVertex('J')
        myGraph.addVertex('K')
        myGraph.addVertex('L')
        myGraph.addVertex('M')
        myGraph.addVertex('N')
        myGraph.addVertex('O')
        myGraph.addVertex('P')
        myGraph.addVertex('Q')
        myGraph.addVertex('R')
        myGraph.addVertex('S')
        myGraph.addVertex('T')
        myGraph.addVertex('U')
        myGraph.addVertex('V')
        myGraph.addVertex('W')
        myGraph.addVertex('X')
        myGraph.addVertex('Y')
        myGraph.addVertex('Z')
        myGraph.addEdge('A', 'B', 1)
        myGraph.addEdge('A', 'D', 1)
        myGraph.addEdge('B', 'F', 1)
        myGraph.addEdge('B', 'M', 1)
        myGraph.addEdge('F', 'G', 1)
        myGraph.addEdge('G', 'C', 1)
        myGraph.addEdge('G', 'I', 1)
        myGraph.addEdge('I', 'H', 1)
        myGraph.addEdge('I', 'J', 1)
        myGraph.addEdge('J', 'K', 1)
        myGraph.addEdge('K', 'L', 1)
        myGraph.addEdge('L', 'M', 1)
        myGraph.addEdge('M', 'N', 1)
        myGraph.addEdge('M', 'B', 1)
        myGraph.addEdge('N', 'O', 1)
        myGraph.addEdge('O', 'D', 1)
        myGraph.addEdge('O', 'P', 1)
        myGraph.addEdge('P', 'Q', 1)
        myGraph.addEdge('Q', 'R', 1)
        myGraph.addEdge('R', 'S', 1)
        myGraph.addEdge('S', 'U', 1)
        myGraph.addEdge('S', 'T', 1)
        myGraph.addEdge('A', 'E', 1)
        myGraph.addEdge('C', 'H', 1)
        myGraph.addEdge('H', 'Q', 1)
        myGraph.addEdge('V', 'X', 1)
        myGraph.addEdge('V', 'W', 1)
        myGraph.addEdge('W', 'Y', 1)
        myGraph.addEdge('V', 'Z', 1)
        return myGraph
        

    def testcase1(self):
        pass
     
    def testcase2(self):
        pass
     
    def testcase3(self):
        pass
     
    def testcase4(self):
        pass
     

if __name__ == '__main__':
    unittest.main()
