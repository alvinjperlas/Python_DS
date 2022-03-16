

class MinHeaps:
    
    def __init__(self):
        self.heap = []
        
    
    # ======================================== #
    # getMini(): 
    # It returns the root element of Min Heap. 
    # Time Complexity of this operation is O(1).
    # ======================================== #
    def getMin(self):
        return self.heap[0]
    
    
    # ======================================== #
    # extractMin(): 
    # Removes the minimum element from MinHeap. 
    # Time Complexity of this Operation is O(Logn) 
    # as this operation needs to maintain the 
    # heap property (by calling heapify()) 
    # after removing root.
    # ======================================== #
    def extractMin(self):
        pass
    
    
    # ======================================== #
    # decreaseKey(): 
    # Decreases value of key. The time complexity 
    # of this operation is O(Logn). If the 
    # decreases key value of a node is greater 
    # than the parent of the node, then we don’t 
    # need to do anything. Otherwise, we need to
    # traverse up to fix the violated heap property.
    # ======================================== #
    def decreaseKey(self):
        pass
    
    # ======================================== #
    # insert(): 
    # Inserting a new key takes O(Logn) time. 
    # We add a new key at the end of the tree. 
    # IF new key is greater than its parent, 
    # then we don’t need to do anything. Otherwise, 
    # we need to traverse up to fix the violated 
    # heap property.
    # ======================================== #
    def insert(self):
        pass
    
    
    # ======================================== #
    # delete():
    # Deleting a key also takes O(Logn) time. 
    # We replace the key to be deleted with 
    # minum infinite by calling decreaseKey(). 
    # After decreaseKey(), the minus infinite 
    # value must reach root, so we call 
    # extractMin() to remove the key.
    # ======================================== #
    def delete(self):
        pass
    
  
    
    
    
    
class MaxHeaps:
        
    def __init__(self):
        pass
    
    def getMax(self):
        pass
    
    def extractMax(self):
        pass
    
    def decreaseKey(self):
        pass
    
    def insert(self):
        pass
    
    def delete(self):
        pass
    
    