class StackQueue:

    def __init__(self):
        self.stack = []
        self.queue = []

    # O(1)
    def enqueue(self, item):
        self.stack.append(item)

    # O(1) - amortized.
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty.')
        if len(self.queue) == 0:
            self.load_queue()
        return self.queue.pop()

    # O(n)
    def load_queue(self):
        while len(self.stack) > 0:
            self.queue.append(self.stack.pop())

    def is_empty(self):
        return len(self.stack) == 0 and len(self.queue) == 0

q = StackQueue()
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
assert(q.stack == [3, 2, 1])
q.load_queue()
assert(q.dequeue() == 3)
q.enqueue(4)
assert(q.dequeue() == 2)
assert(q.dequeue() == 1)
assert(q.dequeue() == 4)
assert(q.is_empty())