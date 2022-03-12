



class StackLinkedList:

    class Node: 
        def __init__(self, data):
            self.data = data
            self.next = None
            
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    #O(1)    
    def pop(self):
        retval  = self.head.data
        print("Poped: {}".format(retval))
        self.head = self.head.next
        self.count = self.count -1
        return retval
    
    #O(1)
    def peek(self):
        print("Top: {}".format(self.head.data))
        return self.head.data
    
    #O(1)
    def isEmpty(self):
        print("isEmpty: {}".format(self.count == 0))
        return self.count == 0
    
    #O(1)
    def size(self):
        print("Stack size: {}".format(self.count))
        return self.count
       
    #O(1)    
    def push(self, data):
        if isinstance(data, int):
            print("push", data)
            new_node = self.Node(data)
            new_node.next = self.head
            self.head = new_node
            if self.count == 0:
                self.tail = new_node
            self.count = self.count + 1
        
    def emptyStack(self):
        self.count = 0
        self.head = None
        
    #O(N)   
    def printStack(self):
        if self.count == 0:
            print("empty")
        else:
            printstr = []
            runner = self.head
            while(runner!= None):
                #print(runner.data)
                printstr.append("[ {}|*] -> ".format(str(runner.data)))
                runner = runner.next
            print("".join(printstr))    
            
        