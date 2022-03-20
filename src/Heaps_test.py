from Heaps import MaxHeaps, MinHeaps   # The code to test
import unittest   # The test framework


class Test_Heaps(unittest.TestCase):
    def setUp(self):
        pass
      
    def _getTestHeap(self):
        myHeap = MinHeaps()
        myHeap.insert(10)
        myHeap.insert(8)
        myHeap.insert(6)
        myHeap.insert(5)
        myHeap.insert(4)
        myHeap.insert(1)
        return myHeap

    def testgetMin(self):
        myHeap = MinHeaps()
        myHeap.insert(10)
        self.assertEqual(myHeap.size(), 1)
        self.assertEqual(myHeap.getMin(), 10)
        myHeap.insert(8)
        self.assertEqual(myHeap.getMin(), 8)
        myHeap.insert(6)
        self.assertEqual(myHeap.getMin(), 6)
        myHeap.insert(5)
        self.assertEqual(myHeap.getMin(), 5)
        myHeap.insert(4)
        self.assertEqual(myHeap.getMin(), 4)
        myHeap.insert(1)
        self.assertEqual(myHeap.getMin(), 1)
     
    def testExtractMin(self):
        myheap = self._getTestHeap()
        retval = myheap.extractMin()
        self.assertEqual(retval, 1)
    
    def testDeleteOnMinHeap(self):
        myheap = self._getTestHeap()
        retval = myheap.delete(0)
        self.assertEqual(retval, 1) 
        currHeap = myheap._getHeap()
        self.assertEqual(currHeap, [4,5,8,10,6])
        

if __name__ == '__main__':
    unittest.main()
