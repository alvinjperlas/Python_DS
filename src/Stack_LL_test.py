from Stack_LL import StackLinkedList    # The code to test
import unittest   # The test framework

class Test_Stack_LinkedLists(unittest.TestCase):
    def setUp(self):
        self.myLinkedListVariable = StackLinkedList()
  
    def testSize(self):
        self.myLinkedListVariable.push(9)
        self.assertEqual(self.myLinkedListVariable.size(), 1)

    def testPush(self):
        myLinkedListStack = StackLinkedList()
        myLinkedListStack.push(9)
        self.assertEqual(myLinkedListStack.size(), 1)

    def testIsEmpty(self):
        myLinkedListStack = StackLinkedList()
        self.assertTrue(myLinkedListStack.isEmpty())
        myLinkedListStack.push(1)
        self.assertFalse(myLinkedListStack.isEmpty())

    def testFillAndEmptyStack(self):
        myLinkedListStack = StackLinkedList()
        myLinkedListStack.push(1)
        self.assertFalse(myLinkedListStack.isEmpty())
        myLinkedListStack.emptyStack()
        self.assertTrue(myLinkedListStack.isEmpty())
    
    def testIsEmptyByAddingInvalidCharacter(self):
        myLinkedListStack = StackLinkedList()
        myLinkedListStack.push('a')
        self.assertTrue(myLinkedListStack.isEmpty(), "Invalid character was inserted.")

    def testIsEmptyByAdding1000Items(self):
        myLinkedListStack = StackLinkedList()
        for i in range(0,1000):
            myLinkedListStack.push(i)
        self.assertEqual(myLinkedListStack.size(), 1000)
        self.assertFalse(myLinkedListStack.isEmpty(), 
        "Adding multiple entries invalidated the isEmpty function")

    def testPop(self):
        myLinkedListStack = StackLinkedList()
        myLinkedListStack.push(1)
        self.assertEqual(myLinkedListStack.size(), 1)
        myLinkedListStack.pop()
        self.assertTrue(myLinkedListStack.isEmpty())

    def testPeek(self):
        myLinkedListStack = StackLinkedList()
        myLinkedListStack.push(9)
        self.assertEqual(myLinkedListStack.peek(), 9)
        myLinkedListStack.push(4)
        self.assertEqual(myLinkedListStack.peek(), 4)
        myLinkedListStack.push(1)
        self.assertEqual(myLinkedListStack.peek(), 1)

if __name__ == '__main__':
    unittest.main()
