class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, num):
        self.stack.append(num)
        if self.is_empty():
            self.mins.append(num)
        else:
            self.mins.append(min(num, self.mins[-1]))

    def pop(self):
        if self.is_empty():
            raise IndexError('Cannot pop from empty stack.')
        self.mins.pop()
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Cannot peek in stack.')
        return self.stack[-1]

    def get_min(self):
        if self.is_empty():
            raise IndexError('Cannot get min from empty stack.')
        return self.mins[-1]

    def is_empty(self):
        return self.stack.length == 0