from BinaryTree import BinaryTree   # The code to test
import unittest   # The test framework


class Test_Queue_Array(unittest.TestCase):
    def setUp(self):
        self.myBt = BinaryTree()
  
    def testSize(self):
        self.myBt.add(9)
        self.assertEqual(self.myBt.size(), 1)

    def testInsertNode(self):
        pass
 
    def testRemoveNode(self):
        pass
    
    def testIsLeaf(self):
        pass
    
    def testIsEmptyByAdding1000Items(self):
        pass

    def testGetLargestNode(self):
        pass
    
    def testGetParent(self):
        pass

    def testContains(self):
        pass

    def testSearch(self):
        pass

    def testTreeDepth(self):
        pass

    def testRebalance(self):
        pass

    def testPreOrderTraversal(self):
        pass

    def testInOrderTraversal(self):
        pass

    def testPostOrderTraversal(self):
        pass
    
    def testIsFullBinaryTree(self):
        pass
    
    def testIsPerfectBinaryTree(self):
        pass

if __name__ == '__main__':
    unittest.main()
