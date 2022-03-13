from Queue_LL import QueueLinkedList   # The code to test
import unittest   # The test framework


class Test_Queue_Array(unittest.TestCase):
    def setUp(self):
        self.myQueueLinkedListVariable = QueueLinkedList()
  
    def testSize(self):
        self.myQueueLinkedListVariable.push(9)
        self.assertEqual(self.myQueueLinkedListVariable.size(), 1)

    def testPush(self):
        myQueueLinkedList = QueueLinkedList()
        myQueueLinkedList.push(9)
        self.assertEqual(myQueueLinkedList.size(), 1)

    def testIsEmpty(self):
        myQueueLinkedList = QueueLinkedList()
        self.assertTrue(myQueueLinkedList.isEmpty())
        myQueueLinkedList.push(1)
        self.assertFalse(myQueueLinkedList.isEmpty())

    def testFillAndEmptyQueue(self):
        myQueueLinkedList = QueueLinkedList()
        myQueueLinkedList.push(1)
        self.assertFalse(myQueueLinkedList.isEmpty())
        myQueueLinkedList.empty()
        self.assertTrue(myQueueLinkedList.isEmpty())
    
    def testIsEmptyByAdding1000Items(self):
        myQueueLinkedList = QueueLinkedList()
        for i in range(0,1000):
            myQueueLinkedList.push(i)
        self.assertEqual(myQueueLinkedList.size(), 1000)
        self.assertFalse(myQueueLinkedList.isEmpty(), 
        "Adding multiple entries invalidated the isEmpty function")

    #@unittest.skip("Pretending component fails")
    def testPop(self):
        myQueueLinkedList = QueueLinkedList()
        myQueueLinkedList.push(1)
        self.assertEqual(myQueueLinkedList.size(), 1)
        myQueueLinkedList.pop()
        self.assertTrue(myQueueLinkedList.isEmpty())

    def testPeek(self):
        myQueueLinkedList = QueueLinkedList()
        myQueueLinkedList.push(9)
        self.assertEqual(myQueueLinkedList.peek(), 9)
        myQueueLinkedList.push(4)
        self.assertEqual(myQueueLinkedList.peek(), 9)
        myQueueLinkedList.push(1)
        self.assertEqual(myQueueLinkedList.peek(), 9)


if __name__ == '__main__':
    unittest.main()
