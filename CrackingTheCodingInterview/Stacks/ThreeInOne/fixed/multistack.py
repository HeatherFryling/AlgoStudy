class MultiStack:
    num_stacks = 3
    total_size = 30

    def __init__(self):
        self.array = [0 for x in range(self.total_size)]
        self.stack_size = self.total_size // 3
        self.stack_tops = [self.start_idx(x) - 1 for x in range(self.num_stacks)]

    def push(self, value, stack_num):
        if self.is_full(stack_num):
            raise(IndexError("Cannot push. Stack {stack_num} is full.".format(stack_num = stack_num)))
        else:
            self.stack_tops[stack_num] += 1
            self.array[self.stack_tops[stack_num]] = value

    def pop(self, stack_num):
        print(stack_num)
        if self.is_empty(stack_num):
            raise(IndexError("Cannot pop. Stack {stack_num} is empty.".format(stack_num = stack_num)))
        self.stack_tops[stack_num] -= 1
        return self.array[self.stack_tops[stack_num] + 1]

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise(IndexError("Cannot peek. Stack {stack_num} is empty.".format(stack_num = stack_num)))

        else:
            return self.stack_tops[stack_num]

    def is_full(self, stack_num):
        return self.stack_tops[stack_num] >= self.end_idx(stack_num)

    def is_empty(self, stack_num):
        return self.stack_tops[stack_num] < self.start_idx(stack_num)

    def start_idx(self, stack_num):
        return stack_num * self.stack_size

    def end_idx(self, stack_num):
        return (stack_num + 1) * self.stack_size - 1


m = MultiStack()
print(m.stack_tops)

for i in range(10):
    m.push(1, 0)
for i in range(10):
    m.push(2, 1)
for i in range(10):
    m.push(3, 2)

# m.push(1, 0)
# m.push(1, 1)
# m.push(1, 2)
print(m.array)
print(m.stack_tops)

for i in range(10):
    m.pop(0)
for i in range(10):
    m.pop(1)
for i in range(10):
    m.pop(2)

print(m.stack_tops)

# m.pop(0)
# m.pop(1)
# m.pop(2)