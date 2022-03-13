from Queue_Array import QueueArray   # The code to test
import unittest   # The test framework


class Test_Queue_Array(unittest.TestCase):
    def setUp(self):
        self.myQueueArrayVariable = QueueArray()
  
    def testSize(self):
        self.myQueueArrayVariable.push(9)
        self.assertEqual(self.myQueueArrayVariable.size(), 1)

    def testPush(self):
        myQueueArray = QueueArray()
        myQueueArray.push(9)
        self.assertEqual(myQueueArray.size(), 1)

    def testIsEmpty(self):
        myQueueArray = QueueArray()
        self.assertTrue(myQueueArray.isEmpty())
        myQueueArray.push(1)
        self.assertFalse(myQueueArray.isEmpty())

    def testFillAndEmptyQueue(self):
        myQueueArray = QueueArray()
        myQueueArray.push(1)
        self.assertFalse(myQueueArray.isEmpty())
        myQueueArray.empty()
        self.assertTrue(myQueueArray.isEmpty())
    
    def testIsEmptyByAdding1000Items(self):
        myQueueArray = QueueArray()
        for i in range(0,1000):
            myQueueArray.push(i)
        self.assertEqual(myQueueArray.size(), 1000)
        self.assertFalse(myQueueArray.isEmpty(), 
        "Adding multiple entries invalidated the isEmpty function")

    #@unittest.skip("Pretending component fails")
    def testPop(self):
        myQueueArray = QueueArray()
        myQueueArray.push(1)
        self.assertEqual(myQueueArray.size(), 1)
        myQueueArray.pop()
        self.assertTrue(myQueueArray.isEmpty())

    def testPeek(self):
        myQueueArray = QueueArray()
        myQueueArray.push(9)
        self.assertEqual(myQueueArray.peek(), 9)
        myQueueArray.push(4)
        self.assertEqual(myQueueArray.peek(), 9)
        myQueueArray.push(1)
        self.assertEqual(myQueueArray.peek(), 9)


if __name__ == '__main__':
    unittest.main()
