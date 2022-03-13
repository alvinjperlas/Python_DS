from LinkedList import LinkedLists   # The code to test
import unittest   # The test framework


class Test_Queue_Array(unittest.TestCase):
    def setUp(self):
        self.myLLVariable = LinkedLists()
  
    def testSize(self):
        self.myLLVariable.add(9)
        self.assertEqual(self.myLLVariable.size(), 1)

    def testAdd(self):
        myLL = LinkedLists()
        myLL.add(9)
        self.assertEqual(myLL.size(), 1)

 
    def testFillAndEmptyQueue(self):
        myLL = LinkedLists()
        myLL.add(1)
        self.assertFalse(myLL.isEmpty())
        myLL.empty()
        self.assertTrue(myLL.isEmpty())
    
    def testIsEmptyByAdding1000Items(self):
        myLL = LinkedLists()
        for i in range(0,1000):
            myLL.add(i)
        self.assertEqual(myLL.size(), 1000)
        self.assertFalse(myLL.isEmpty(), 
        "Adding multiple entries invalidated the isEmpty function")

    #@unittest.skip("Pretending component fails")
    def testRemove(self):
        myLL = LinkedLists()
        for i in range(0,100):
            myLL.add(i)
        myLL.remove(50)
        self.assertTrue(myLL.find(50) == None)

    def testReverse(self):
        myLL = LinkedLists()
        for i in range(0,100):
            myLL.add(i)
        
        myLL.reverse()
        current = myLL._head
        for i in range (99, 0, -1):
            self.assertEqual(current.data, i)
            current = current.next


if __name__ == '__main__':
    unittest.main()
