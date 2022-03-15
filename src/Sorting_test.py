from Sorting import SortingAlgos   # The code to test
import unittest   # The test framework


class Test_SortingAlgos(unittest.TestCase):
    def setUp(self):
        self.mySorter = SortingAlgos()
        self.toSortLists = [1,6,4,2,1,7,8,10,105,32,55,21,0]
        self.sortedLists = sorted(self.toSortLists)

    def testQuickSort(self):
        sortedLists = self.mySorter.doQuickSort(self.toSortLists)
        self.assertEqual(sortedLists, self.sortedLists)

    def testMergeSort(self):
        sortedLists = self.mySorter.doMergeSort(self.toSortLists)
        self.assertEqual(sortedLists, self.sortedLists)
    
    def testRadixSort(self):
        sortedLists = self.mySorter.doRadixSort(self.toSortLists)
        self.assertEqual(sortedLists, self.sortedLists)
        
    def testBubbleSort(self):
        sortedLists = self.mySorter.doBubbleSort(self.toSortLists)
        self.assertEqual(sortedLists, self.sortedLists)
    
    
    def testInsertionSort(self):
        sortedLists = self.mySorter.doInsertionSort(self.toSortLists)
        self.assertEqual(sortedLists, self.sortedLists)
    
    
if __name__ == '__main__':
    unittest.main()
