from Stack_Array import StackArray   # The code to test
import unittest   # The test framework


class Test_Stack_Array(unittest.TestCase):
    def setUp(self):
        self.myArrayListVariable = StackArray()
  
    def testSize(self):
        self.myArrayListVariable.push(9)
        self.assertEqual(self.myArrayListVariable.getStackCount(), 1)

    def testPush(self):
        myArrayListStack = StackArray()
        myArrayListStack.push(9)
        self.assertEqual(myArrayListStack.getStackCount(), 1)

    def testIsEmpty(self):
        myArrayListStack = StackArray()
        self.assertTrue(myArrayListStack.isEmpty())
        myArrayListStack.push(1)
        self.assertFalse(myArrayListStack.isEmpty())

    def testFillAndEmptyStack(self):
        myArrayListStack = StackArray()
        myArrayListStack.push(1)
        self.assertFalse(myArrayListStack.isEmpty())
        myArrayListStack.emptyStack()
        self.assertTrue(myArrayListStack.isEmpty())
    
    def testIsEmptyByAddingInvalidCharacter(self):
        myArrayListStack = StackArray()
        myArrayListStack.push('a')
        self.assertTrue(myArrayListStack.isEmpty(), "Invalid character was inserted.")

    def testIsEmptyByAdding1000Items(self):
        myArrayListStack = StackArray()
        for i in range(0,1000):
            myArrayListStack.push(i)
        self.assertEqual(myArrayListStack.getStackCount(), 1000)
        self.assertFalse(myArrayListStack.isEmpty(), 
        "Adding multiple entries invalidated the isEmpty function")

    #@unittest.skip("Pretending component fails")
    def testPop(self):
        myArrayListStack = StackArray()
        myArrayListStack.push(1)
        self.assertEqual(myArrayListStack.getStackCount(), 1)
        myArrayListStack.pop()
        self.assertTrue(myArrayListStack.isEmpty())

    def testPeek(self):
        myArrayListStack = StackArray()
        myArrayListStack.push(9)
        self.assertEqual(myArrayListStack.peek(), 9)
        myArrayListStack.push(4)
        self.assertEqual(myArrayListStack.peek(), 4)
        myArrayListStack.push(1)
        self.assertEqual(myArrayListStack.peek(), 1)


if __name__ == '__main__':
    unittest.main()
