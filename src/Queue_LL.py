class QueueLinkedList:
    
    class Node: 
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0
      
    #O(1)    
    def pop(self):
        if self._count >0:
            retval = self._head
            self._head = self._head.next
            self._count = self._count - 1
            print(retval)
            return retval
    
    #O(1)
    def peek(self):
        retval = None
        if self._count >0:
            retval = self._head.data
            print("Front: {}".format(retval))
            return retval
        else:
            print("Empty Queue")
            return None
        
    #O(1)
    def isEmpty(self):
        print("isEmpty: {}".format(self._count == 0))
        return self._count == 0
    
    #O(1)
    def size(self):
        print("Size: {}".format(self._count))
        return self._count
     
    #O(1)    
    def push(self, data): 
        print("Push: ", data)
        new_node = self.Node(data)
        if self._count == 0:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._count = self._count + 1    
        
    #O(1)
    def empty(self):
        self._head = None
        self._tail = None
        self._count = 0
        
    #O(N)   
    def printQueue(self):
        
        if self._count == 0:
            print("Empty Queue")
        else:
            printstr = []
            runner = self._head
            while(runner!= None):
                #print(runner.data)
                printstr.append("[ {}|*] -> ".format(str(runner.data)))
                runner = runner.next
            print("".join(printstr))    
            
            
            