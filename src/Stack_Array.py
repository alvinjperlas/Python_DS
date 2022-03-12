



class StackArray:
    def __init__(self):
        self.stackList = []
        self.count = 0
    
    #O(1)     
    def pop(self):
        item =  self.stackList.pop(len(self.stackList)-1)
        self.count = self.count - 1
        return item
    
    #O(1)
    def peek(self):
        return self.stackList[len(self.stackList)-1]
    
    def emptyStack(self):
        self.count = 0
        self.stackList.clear()

    #O(1)
    def isEmpty(self):
        return self.count == 0
       
    #O(1)
    def getStackCount(self):
        return self.count
    
    #O(1)
    def push(self,data):
        if isinstance(data, int):
            self.stackList.append(data)
            self.count = self.count + 1
        
    #O(N)
    def printStack(self):
        retval = "".join(str(self.stackList))
        print(retval)
        return retval
    












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
        print("Poped: {}".format(self.head.data))
        self.head = self.head.next
    
    #O(1)
    def peek(self):
        print("Top: {}".format(self.head.data))
    
    #O(1)
    def isEmpty(self):
        print("isEmpty: {}".format(self.count == 0))
    
    #O(1)
    def size(self):
        print("Stack size: {}".format(self.count))
        return self.count
       
    #O(1)    
    def push(self, data):
        print("push", data)
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.count == 0:
            self.tail = new_node
        self.count = self.count + 1
        
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
            
        