from email import header


class LinkedLists:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0
        
    # O(1)
    def add(self, data):
        newNode = self.Node(data)
        if self._head == None:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.next = newNode
            self._tail = newNode
        self._count += 1
            
        
    # O(1)
    def size(self):
        return self._count
    
    # O(N)
    def remove(self, data):
        current = self._head
        previous = self.Node(None)
        previous.next = current
    
        while current != None :
            if current.data == data:
                previous.next = current.next
                self._count -= 1
                return
            previous = current
            current = current.next
            
            
       
    def isEmpty(self):
        return self._count == 0
        
    # O(1) 
    def empty(self):
        self._head = None
        self._tail = None
        self._count = 0
        
    # O(N) - returns pointer to data.
    def find(self, data):
        current = self._head
        while current != None:
            if current.data == data:
                return current
            current = current.next
        return None
        
    # O(N)
    def reverse(self):
        current = self._head
        previous = self.Node(None)
        previous.next = current
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self._head = previous
    
    # O(N)
    def print(self):
        current = self._head
        if self._count ==0:
            print("None")
        else:
            printStr = []
            current = self._head
            while(current  != None):
                printStr.append(" [{}|*]-> ".format(current.data))
                current = current.next
            print(printStr)