class StackOfStacks:

    def __init__(self, stack_size=10):
        self.stacks = [[]]
        self.stacksize = []

    def push(self, item):
        if self.stack_full(self.stacks[-1]):
            self.stacks.append([item])
        else:
            self.stacks[-1].append(item)

    def pop(self):
        if self.empty_stack_of_stacks():
            raise IndexError('Cannot pop from empty stack.')
        value = self.stacks[-1].pop()
        if self.empty_stack(-1):
            self.stacks.pop()
        return value

    def peek(self):
        if self.empty_stack_of_stacks():
           raise IndexError('Cannot peek at empty stack.')
        return self.stacks[-1][-1]

    def popAtStack(self, stack_num):
        if self.empty_stack_of_stacks():
            raise IndexError('Cannot pop from empty stack.')
        if stack_num < 0 or stack_num >= len(self.stacks):
            raise IndexError('Stack number out of range: {num}'.format(num = stack_num))
        
        value = self.stacks[stack_num].pop()
        if self.empty_stack(stack_num):
            self.stacks.pop()
        return value    
    
    def empty_stack_of_stacks(self):
        return len(self.stacks[0]) == 0

    def empty_stack(self, stack_num):
        return len(self.stacks[stack_num]) == 0

    def stack_full(self, stack_num):
        return len(self.stacks[stack_num]) == 10