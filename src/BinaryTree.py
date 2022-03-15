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

import math
from operator import length_hint

class BinaryTree:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.parent = None
            
            
    def __init__ (self):
        self.root = None
        self.count = 0
      
    # ====================================== #
    # ==========  Insert Operation ========= #
    # ====================================== #
    
    def insert(self, data):
        newNode = self.Node(data)
        if self.count == 0:
            self.root = newNode
            self.count += 1
            
        else:
            if self._insert(newNode, self.root):
                self.count += 1
    
    def _insert(self, node, root):
        
        if node.data > root.data:
            if root.right == None:
                root.right = node
                node.parent = root
            else:
                self._insert(node, root.right)            
        elif node.data < root.data:
            if root.left == None:
                root.left = node
                node.parent = root
            else:
                self._insert(node, root.left)        
        else:
            # Do nothing. same data. 
            print("Node {} already exists.".format(node.data))
            return False
        return True
    
    # ====================================== #
    # ==========  Search Operation ========= #
    # ====================================== #
    

    def _search(self, data, currentNode):
        if currentNode == None:
            return None
        elif currentNode.data == data:
            return currentNode
        elif currentNode.data > data:
            return self._search(data, currentNode.left)
        elif currentNode.data < data:
            return self._search(data, currentNode.right)
        else:
            return None
    
    def contains(self, data):
        return None != self._search(data, self.root)
       
              
    # ====================================== #
    # ==========  Remove Operation ========= #
    # ====================================== #
      
    # 3 cases for node removal  
    # Case 1: Delete a leaf. just dereferrence from parent.
    # Case 2: Node to be deleted only has 1 child.
    # Case 3: Node to be deleted has 2 child. 
    def remove(self, data):
        return self._remove(data, self.root)
        
    
    def _remove(self, data, currentNode):
        
        if currentNode == None:
            return currentNode
        
        # data is more than currentNode
        elif currentNode.data < data:
            currentNode.right = self._remove(data, currentNode.right)
        
        # data is less than currentNode
        elif currentNode.data > data:
            currentNode.left = self._remove(data, currentNode.left)
            
        # data is same as currentNode    
        else:
            # case 2: 1 child only
            if currentNode.left is None:
                temp = currentNode.right
                currentNode = None
                self.count -= 1
                return temp
            elif currentNode.right is None:
                temp = currentNode.left
                currentNode = None
                self.count -= 1
                return temp
            
            # case 3: 2 childs
            # get inorder  {left, root, right} successor
            temp = self.minValueNode(currentNode.right)
            
            # swap data.
            currentNode.data = temp.data
            currentNode.right = self._remove(temp.data, currentNode.right)
            self.count -= 1
        
        return currentNode
 

    # ====================================== #
    # ==========  Node Properties  ========= #
    # ====================================== #

    def isLeaf(self, node):
        return node.left == None and node.right == None
    
    def getParent(self, data):
        searchNode = self._search(data, self.root)
        return self._getParent(searchNode, self.root)

    
    def _getParent(self, node, root):
        if root == None:
            return None
        elif self._checkMatchForChildren(node.data, root):
            return root
        elif root.data > node.data:
            return self._getParent(node, root.left)
        elif root.data < node.data:
            return self._getParent(node, root.right)
        else:
            return None
    
    def _checkMatchForChildren(self, data, root):
        if root== None:
            return False
        elif root.left != None and root.left.data == data:
            return True
        elif root.right != None and root.right.data == data:
            return True    
        return False
    
    
    def minValueNode(self, node):
        current = node
        while current.left != None:
            current = current.left
        return current
    
    def maxValueNode(self, node):
        current = node
        while current.right != None:
            current = current.right
        return current     
    
    # ====================================== #
    # =============  Traversals  =========== #
    # ====================================== #
    
    # InOrder: Left, Root, Right
    def inOrderTraversal(self, root):
        retval = []
        if root != None:
            retval += (self.inOrderTraversal(root.left))
            retval.append(root.data)
            retval+=(self.inOrderTraversal(root.right))
      
        return retval
        
    # PreOrder: Root, Left, Right, 
    def PreOrderTraversal(self, root):
        retval = []
        if root != None:
            retval.append(root.data)
            retval += (self.PreOrderTraversal(root.left))
            retval+=(self.PreOrderTraversal(root.right))
        
        return retval
    
    # PostOrder: Left, Right, Root
    def PostOrderTraversal(self, root):
        retval = []
        if root != None:
            retval += (self.PostOrderTraversal(root.left))
            retval+=(self.PostOrderTraversal(root.right))
            retval.append(root.data)

        return retval
    
    # ====================================== #
    # ======  Binary Tree Properties  ====== #
    # ====================================== #   
    
    
    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0
    
    def getTreeDepth(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.getTreeDepth(root.left), self.getTreeDepth(root.right))




    # A balanced binary tree, also referred to as a height-balanced binary tree, is defined
    # as a binary tree in which the height of the left and right subtree of any node differ 
    # by not more than 1.

    # 1. difference between the left and the right subtree for any node is not more than one
    # 2. the left subtree is balanced
    # 3. the right subtree is balanced
    def isBalancedBinaryTree(self, root):
        if root == None:
            return True
        else:
            leftDepth = self.getTreeDepth(root.left)
            rightDepth = self.getTreeDepth(root.right)
            delta =  abs(leftDepth - rightDepth) <= 1 
            isLeftBalanced = self.isBalancedBinaryTree(root.left)
            isRightBalanced = self.isBalancedBinaryTree(root.right)
            return delta and isLeftBalanced and isRightBalanced
    
    
    # A complete binary tree is a binary tree in which all the levels 
    # are completely filled except possibly the lowest one, which is 
    # filled from the left.

    # A complete binary tree is just like a full binary tree, but with two major differences
    # 1. All the leaf elements must lean towards the left.
    # 2. The last leaf element might not have a right sibling i.e. 
    #    a complete binary tree doesn't have to be a full binary tree.

    def isCompleteBinaryTree(self, root):
        # useful info: property 1, 3
        # Get max depth.
        # recurse and pass depth +1 and have an array that counts the nodes on each level.
        # if we're at max level
        self._nodeCntLists = {}
        if root == None:
            return True
        
        firstAssesment = self._verifyCompleteBT(self.root, 0)
        # Cover only until the height-1 since height h is where the leafs should be located.
        depth = len(self._nodeCntLists.keys()) - 1
        for i in self._nodeCntLists.keys():
            if i == depth:
                break
            maxNodesInLevel = math.pow(2,i)
            if self._nodeCntLists[i] != maxNodesInLevel:
                return False
        return firstAssesment 
            
    
    def _verifyCompleteBT(self, root, level):
        if root == None:
            return True
        
        elif root.left == None and root.right != None:
            return False
        
        # First time recursion enters a new level.
        if level in self._nodeCntLists.keys():
            self._nodeCntLists[level] += 1
        else:
            self._nodeCntLists[level] = 1
            
        return self._verifyCompleteBT(root.left, level+1) and self._verifyCompleteBT(root.right, level+1)
       

    
    # A full Binary tree is a special type of binary tree in which every parent node/internal 
    # node has either two or no children.
    def isFullBinaryTree(self, root):
        if root == None:
            return True
        else:
            hasLeftChild =  root.left != None
            hasRightChild =  root.right != None
            if hasLeftChild and hasRightChild:
                return self.isFullBinaryTree(root.left) and self.isFullBinaryTree(root.right)
            elif hasLeftChild == False and hasRightChild == False:
                return True
            else:
                return False

    # A perfect binary tree is a type of binary tree in which every internal node has exactly
    # two child nodes and all the leaf nodes are at the same level.
    def isPerfectBinaryTree(self, root):
        pass
    
        
        
    
    