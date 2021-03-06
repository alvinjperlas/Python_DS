from BinaryTree import BinaryTree   # The code to test
import unittest   # The test framework


class Test_Queue_Array(unittest.TestCase):
    def setUp(self):
        self.myBtvar = BinaryTree()
  
    def configureBaseBT(self):
        myBst = BinaryTree()
        myBst.insert(50)
        myBst.insert(30)
        myBst.insert(20)
        myBst.insert(40)
        myBst.insert(70)
        myBst.insert(60)
        myBst.insert(80)
        return myBst
        
    def testSize(self):
        self.myBtvar.insert(9)
        self.assertEqual(self.myBtvar.size(), 1)

    def testInsertNode(self):
        myBst = self.configureBaseBT()
        myInOrderTraversal = myBst.inOrderTraversal(myBst.root)
        self.assertEqual(myInOrderTraversal,[20, 30, 40, 50, 60, 70, 80])
        myBst.insert(10)
        myInOrderTraversal = myBst.inOrderTraversal(myBst.root)
        self.assertEqual(myInOrderTraversal,[10, 20, 30, 40, 50, 60, 70, 80])
        
    def testRemoveNode(self):
        myBst = self.configureBaseBT()
        inOrderTraversal = myBst.inOrderTraversal(myBst.root)
        self.assertEqual(inOrderTraversal,[20, 30, 40, 50, 60, 70, 80])
        myBst.remove(50)
        inOrderTraversal = myBst.inOrderTraversal(myBst.root)
        self.assertEqual(inOrderTraversal,[20, 30, 40, 60, 70, 80])
        
    
    def testIsLeaf(self):
        myBst = self.configureBaseBT()
        leafNode = myBst._search(20, myBst.root)
        self.assertEqual(myBst.isLeaf(leafNode), True)
        branchNode = myBst._search(30, myBst.root)
        self.assertEqual(myBst.isLeaf(branchNode), False)

    def testGetLargestNode(self):
        myBst = self.configureBaseBT()
        maxNode = myBst.maxValueNode(myBst.root)
        self.assertEqual(maxNode.data, 80)
        myBst.remove(80)
        maxNode = myBst.maxValueNode(myBst.root)
        self.assertEqual(maxNode.data, 70)
        myBst.remove(50)
        maxNode = myBst.maxValueNode(myBst.root)
        self.assertEqual(maxNode.data, 70)
         
    def testGetParent(self):
        myBst = self.configureBaseBT()
        parentNode = myBst.getParent(20)
        self.assertEqual(parentNode.data, 30)
        parentNode = myBst.getParent(30)
        self.assertEqual(parentNode.data, 50)
        parentNode = myBst.getParent(80)
        self.assertEqual(parentNode.data, 70)     

    def testContains(self):
        myBst = self.configureBaseBT()
        self.assertEqual(myBst.contains(50), True)
        self.assertEqual(myBst.contains(20), True)
        self.assertEqual(myBst.contains(30), True)
        self.assertEqual(myBst.contains(40), True)
        self.assertEqual(myBst.contains(80), True)
        self.assertEqual(myBst.contains(1), False)
        self.assertEqual(myBst.contains(2), False)

    def testTreeDepth(self):
        myBst = self.configureBaseBT()
        treeDepth = myBst.getTreeDepth(myBst.root)
        self.assertEqual(treeDepth, 3)

  
    def testPreOrderTraversal(self):
        myBst = self.configureBaseBT()
        PreOrderTraversal = myBst.PreOrderTraversal(myBst.root)
        self.assertEqual(PreOrderTraversal,[50, 30, 20, 40, 70, 60, 80])

    def testInOrderTraversal(self):
        myBst = self.configureBaseBT()
        inOrderTraversal = myBst.inOrderTraversal(myBst.root)
        self.assertEqual(inOrderTraversal,[20, 30, 40, 50, 60, 70, 80])

    def testPostOrderTraversal(self):
        myBst = self.configureBaseBT()
        inOrderTraversal = myBst.PostOrderTraversal(myBst.root)
        self.assertEqual(inOrderTraversal,[20, 40, 30, 60, 80, 70, 50])
    
    def testIsBalancedBinaryTree(self):
        myBst = self.configureBaseBT()
        self.assertEqual(myBst.isBalancedBinaryTree(myBst.root), True)
        myBst.insert(19)
        myBst.insert(18)
        myBst.insert(17)
        self.assertEqual(myBst.isBalancedBinaryTree(myBst.root), False)
        
    def testIsFullBinaryTree(self):
        myBst = self.configureBaseBT()
        self.assertEqual(myBst.isFullBinaryTree(myBst.root), True)
        myBst.insert(19)
        self.assertEqual(myBst.isFullBinaryTree(myBst.root), False)
        
        
    def testIsCompletetBinaryTree(self):
        myBst = self.configureBaseBT()
        self.assertEqual(myBst.isCompleteBinaryTree(myBst.root), True)
        myBst.insert(19)
        self.assertEqual(myBst.isCompleteBinaryTree(myBst.root), True)
        myBst.insert(41)
        self.assertEqual(myBst.isCompleteBinaryTree(myBst.root), False)
    
    
    def testIsPerfectBinaryTree(self):
        myBst = self.configureBaseBT()
        self.assertEqual(myBst.isPerfectBinaryTree(myBst.root), True)
        myBst.insert(19)
        myBst.insert(21)
        self.assertEqual(myBst.isPerfectBinaryTree(myBst.root), False)
        myBst.insert(39)
        myBst.insert(41)
        myBst.insert(59)
        myBst.insert(61)
        myBst.insert(79)
        myBst.insert(81)
        self.assertEqual(myBst.isPerfectBinaryTree(myBst.root), True)

if __name__ == '__main__':
    unittest.main()



# ========================================== #
# Binary Tree Properties
# 
# 1. The maximum number of nodes at level 'x' of a binary tree is 2^x
# 2. The maximum number of nodes in a binary tree of height 'h' is (2^h -1)
# 3. In a binary Tree with N Nodes, minimum possible height or the minimum 
#    number of levels is Log2 (N+1)
# 4. A binary Tree with L Leaves has at least (|log2 L| + 1) levels
# 5. In Binary Tree where every node has 0 or 2 children, the number of 
#    leaf nodes is always one more than nodes with two children.

# ========================================== #