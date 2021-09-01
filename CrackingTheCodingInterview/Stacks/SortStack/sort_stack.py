import random

class SortStack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            raise IndexError('Cannot pop from empty stack.')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Cannot peek at empty stack.')
        return self.stack[-1]

    def push(self, item):
        self.stack.append(item)

    # O(n^2) time | O(n) space
    def sort_stack(self):
        if self.is_empty():
            return
        temp_stack = []
        # Will need to pop every item off to examine it.
        while len(self.stack) > 0:
            temp_stack.append(self.stack.pop())
        # Put things back in sorted order.
        while(len(temp_stack) > 0):
            # Safe to push.
            if self.is_empty():
                self.push(temp_stack.pop())
                if len(temp_stack) == 0:
                    return
            while (temp_stack[-1] <= self.peek()):
                self.push(temp_stack.pop())
                # Got to end.
                if len(temp_stack) == 0:
                    return
            # Found something larger than what's on top.
            curr = temp_stack.pop()
            # Pop things off until curr can be in its correct location.
            while (not self.is_empty() and curr > self.peek()):
                temp_stack.append(self.pop())
            # Made it down to where curr should be. Put it on top and continue.
            self.push(curr)

    def is_empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return str(self.stack)

# Informal testing.
for i in range(100):
    rand_order = [x for x in range(10)]
    random.shuffle(rand_order)
    my_stack = SortStack()
    for item in rand_order:
        my_stack.push(item)
    my_stack.sort_stack()
    assert(my_stack.stack == [x for x in range(9, -1, -1)])