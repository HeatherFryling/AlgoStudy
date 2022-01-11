from insert_at_bottom_of_stack import insertAtBottomOfStack, recursivelyInsertAtBottomOfStack

def testInsertAtBottomOfStack():
    myStack = [1,2,3,4]
    itemToInsert = 5
    insertAtBottomOfStack(myStack, itemToInsert)
    assert([5,1,2,3,4] == myStack)

def testRecursivelyInsertAtBottomOfStack():
    myStack = [1,2,3,4]
    itemToInsert = 5
    recursivelyInsertAtBottomOfStack(myStack, itemToInsert)
    assert([5,1,2,3,4] == myStack)