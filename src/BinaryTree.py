


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
      
      
    
    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0
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
        return None == self._search(data, self.root)
       
              
    # ====================================== #
    # ==========  Remove Operation ========= #
    # ====================================== #
      
    def remove(self, data):
        self._remove(data, self.root)

        
    
    def _remove(self, data):
        self._remove(data, self.root)


      
 

    # ====================================== #

    def isLeaf(self, node):
        return node.left == None and node.right == None
    
    def getLargestNode(self, node):
        pass
    
    def getParent(self, node):
        pass
    

      
    # ====================================== #
    # =============  Traversals  =========== #
    # ====================================== #
    
    
    def printInOrderTraversal(self):
        pass
    
    def printPreOrderTraversal(self):
        pass
    
    def printPostOrderTraversal(self):
        pass
    
    def getTreeDepth(self, node):
        pass
    
    def isBalancedBinaryTree(self, node):
        pass
    
    def isCompleteBInaryTree(self, node):
        pass
    
    def isFullBinaryTree(self, node):
        pass
    
    def isPerfectBinaryTree(self, node):
        pass
    
        
        
    