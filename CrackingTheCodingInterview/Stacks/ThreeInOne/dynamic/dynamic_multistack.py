from stack_info import StackInfo

class MultiStack:
    
    def __init__(self, num_stacks=3, default_capacity=10):
        self.num_stacks = num_stacks
        self.total_capacity = num_stacks * default_capacity
        self.array = [0 for x in range(self.total_capacity)]
        self.stack_infos = [StackInfo(x * default_capacity - 1, 0, default_capacity, self.total_capacity) for x in range(num_stacks)]

    def push(self, stack_num, value):
        if self.all_stacks_full():
            raise IndexError("Cannot add to multistack. All stacks full.")
        if self.stack_infos[stack_num].isFull():
            self.expand(self.stack_infos(stack_num))

        self.stack_infos[stack_num].size += 1
        self.array[self.stack_infos[stack_num].top_idx()] = value

    def pop(self, stack_num):
        if (self.stack_infos[stack_num].isEmpty()):
            raise IndexError("Cannot pop from empty stack.")
        self.stack_infos[stack_num].size -= 1
        return self.array[self.stack_infos[stack_num].top_idx() + 1]

    def peek(self, stack_num):
        stack = self.stack_infos[stack_num]
        if stack.size < 1:
            return None
        return self.array[stack.top_idx()]

    def shift(self, stack_num):
        stack = self.stack_infos[stack_num]
        if stack.size >= stack.capacity:
            next_stack = (stack_num + 1) % self.num_stacks
            self.shift(next_stack)
            stack.capacity += 1

        idx = stack.top_idx()
        while stack.is_within_stack_capacity(idx):
            self.array[idx] = self.array[(idx - 1) % self.total_capacity]
            idx = (idx - 1) % self.total_capacity

        self.array[stack.start] = 0
        stack.start = (stack.start + 1) % self.total_capacity
        stack.capacity -= 1


    def all_stacks_full(self):
        for stack in self.stack_infos:
            if not stack.isFull():
                return True
        return False

    def expand(self, stack_num):
        stack = self.stack_infos[stack_num]
        self.shift((self.stack_num + 1) % self.num_stacks)
        stack.capacity += 1

    def num_elements(self):
        size = 0
        for si in self.stack_infos:
            size += si.size
        return size


    


m = MultiStack()
