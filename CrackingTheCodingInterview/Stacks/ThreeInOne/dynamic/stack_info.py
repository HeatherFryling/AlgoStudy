class StackInfo:

    def __init__(self, start, size, capacity, total_capacity):
        self.start = start
        self.size = size
        self.capacity = capacity
        self.total_capacity = total_capacity

    def is_within_stack_capacity(self, idx):
        if idx < 0 or idx > (self.total_capacity - 1):
            return False

        contiguous_idx = idx + self.total_capacity if idx < self.start else idx
        end = self.start + self.capacity

        return self.start <= contiguous_idx and contiguous_idx < end

    def end_of_stack(self):
        return (self.start + self.capacity - 1) % self.total_capacity

    def top_idx(self):
        return (self.start + self.size - 1) % self.total_capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def __repr__(self):
        return "StackInfo[{start}, {size}, {capacity}, {total_capacity}]".format(start = self.start, size = self.size, capacity = self.capacity, total_capacity = self.total_capacity)

        