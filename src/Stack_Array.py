



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
       
    #O(1) h
    def size(self):
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
    










