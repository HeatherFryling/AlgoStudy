# These functions insert a value at the bottom of a stack.
# The recursive function illustrates storing values
# in the recursive stack without explicitly storing them.
# Time and space complexity of both functions is O(n).

def insertAtBottomOfStack(theStack, itemToInsert):
    temp = []
    while theStack:
        temp.append(theStack.pop())
    theStack.append(itemToInsert)
    while temp:
        theStack.append(temp.pop())

def recursivelyInsertAtBottomOfStack(theStack, itemToInsert):
    if len(theStack) == 0:
        theStack.append(itemToInsert)
        return

    curr = theStack.pop()
    recursivelyInsertAtBottomOfStack(theStack, itemToInsert)
    theStack.append(curr)