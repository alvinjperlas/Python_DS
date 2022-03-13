
        
class QueueArray:
    
    def __init__(self):
        self._queueLists = []
        self._count = 0
        self._frontIndx = 0

    
    # O(1)
    def peek(self): 
        retval = self._queueLists[self._frontIndx]
        print("Top: {}".format(retval))
        return retval
    
    #O(1)
    def isEmpty(self):
        retval = self._count == 0
        print("isEmpty: {}".format(retval))
        return retval
       
    #O(1)   
    def size(self):
        print("Queue size: {}".format(self._count))
        return self._count
    
    #O(1) time, #O(N) Memory          
    def pop(self):
        retval = self._queueLists[self._frontIndx]
        self._frontIndx = self._frontIndx + 1
        self._count = self._count - 1
        return retval
        
    #O(1)    
    def push(self,data):
        if self._count == 0:
            self._frontIndx = 0
        self._queueLists.append(data)
        self._count = self._count + 1
        print("Pushed: {}".format(data))
        
    #O(1)
    def empty(self):
        self._queueLists = []
        self._count = 0
        self._frontIndx = 0
    
    #O(N)
    def printQueue(self):
        print("".join(str(self._queueLists[self._frontIndx:])))
    
    