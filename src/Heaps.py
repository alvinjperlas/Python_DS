# Helpful facts:
# Left child: 2n +1
# Right child 2n+2
# parent = floor((n-1)/2)


class MinHeaps:
    
    def __init__(self):
        self.heapList = []
        self.size = 0
        
    
    # ======================================== #
    # getMini(): 
    # It returns the root element of Min Heap. 
    # Time Complexity of this operation is O(1).
    # ======================================== #
    def getMin(self):
        return self.heapList[0]
    
    
    # ======================================== #
    # extractMin(): 
    # Removes the minimum element from MinHeap. 
    # Time Complexity of this Operation is O(Logn) 
    # as this operation needs to maintain the 
    # heap property (by calling heapify()) 
    # after removing root.
    # ======================================== #
    def extractMin(self):
        if self.size < 2:
            return
        minVal = self.heapList[0]
        maxVal = self.heapList[self.size]
        self.heapList[0] = maxVal
        self.heapList[self.size] = minVal
        self.heapList.pop()
        self.size -= 1
        self._percolateDown(0)
        return minVal
    
    
    # ======================================== #
    # percolateDown(): 
    # Decreases value of key. The time complexity 
    # of this operation is O(Logn). If the 
    # decreases key value of a node is greater 
    # than the parent of the node, then we don’t 
    # need to do anything. Otherwise, we need to
    # traverse up to fix the violated heap property.
    # ======================================== #
    def _percolateDown(self,dataIdx):
        currentIdx = dataIdx
        while currentIdx < self.size-1:
            swapWith = self._getSmallerChild(currentIdx)
            if self.heapList[swapWith] > self.heapList[currentIdx]:
                swapValue = self.heapList[currentIdx]
                self.heapList[currentIdx] = self.heapList[swapWith]
                self.heapList[swapWith] = swapValue
            currentIdx = swapWith
        
    
    # ======================================== #
    # percolateDown(): 
    # Increase value of key. The time complexity 
    # of this operation is O(Logn). If the 
    # Increase key value of a node is less 
    # than the left child of the node, then we don’t 
    # need to do anything. Otherwise, we need to
    # traverse down to fix the violated heap property.
    # ======================================== #
    def _percolateUp(self, dataIdx):
        currentIdx = dataIdx
        # Bounds: current Index cannot be 0, as the parent will be -1//2
        while currentIdx > 0:   
            parentId = self._getParentId(currentIdx)
            # If parent is greater than current Node, swap them
            if self.heapList[parentId] > self.heapList[currentIdx]:
                parentVal = self.heapList[parentId]
                self.heapList[parentId] = self.heapList[currentIdx]
                self.heapList[currentIdx] = parentVal
            currentIdx = parentId

    # ======================================== #
    # insert(): 
    # Inserting a new key takes O(Logn) time. 
    # We add a new key at the end of the tree. 
    # IF new key is greater than its parent, 
    # then we don’t need to do anything. Otherwise, 
    # we need to traverse up to fix the violated 
    # heap property.
    # ======================================== #
    def insert(self, data):
        self.heapList.append(data)
        self.size += 1
        self.percolateUP(self.size)
    
    
    # ======================================== #
    # delete():
    # Deleting a key also takes O(Logn) time. 
    # We replace the key to be deleted with 
    # minum infinite by calling decreaseKey(). 
    # After decreaseKey(), the minus infinite 
    # value must reach root, so we call 
    # extractMin() to remove the key.
    # ======================================== #
    def delete(self, dataIdx):
        if dataIdx >self.size:
            return
        
        toDeleteVal = self.heapList[dataIdx]
        maxVal = self.heapList[self.size]
        self.heapList[dataIdx] = maxVal
        self.heapList[self.size] = toDeleteVal
        self.heapList.pop()
        self.size -= 1
        self._percolateDown(dataIdx)
        return toDeleteVal
    
    

    def _getParentId(self, idx):
        return (idx-1)//2
    
    def _getLeftChildId(self, idx):
        return 2*idx + 1
    
    def _getRightChildId(self, idx):
        return 2*idx + 2
    
    def _getSmallerChild(self, idx):
        lc = self.heapLists[self._getLeftChildId(idx)]
        rc = self.heapLists[self.getRightCHildId(idx)]
        return min(lc, rc)
        
        
        
        
        
        
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
    
    