# Heather Fryling
# 1/5/2021
# Minheap as explained by Zhifeng Sun
# I altered heapify from recursive to iterative
# to save space on the call stack.
# CS5800 Northeastern University, Seattle

class MinHeap:
    heap = []

    # PURPOSE
    # Initialize the MinHeap
    # SIGNATURE
    # MinHeap() :: self, List => None
    def __init__(self, heap=[]):
        self.size = len(heap)
        self.heap = heap

    # PURPOSE
    # Swap the values at indices i and j in the heap.
    # SIGNATURE
    # swap :: Integer, Integer => None
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # PURPOSE
    # Get the index parent index of the given index.
    # If the parent does not exist, return -1.
    # SIGNATURE
    # parent :: Integer => Integer
    def parent(self, index):
        if (index == 0 or index > (len(self.heap) - 1)):
            return -1
        return (index - 1) // 2

    # PURPOSE
    # Get the index of the left child of the given index.
    # If the child does not exist, return -1.
    # SIGNATURE
    # left_child :: Integer => Integer
    def left_child(self, index):
        child_dex = 2 * (index + 1) - 1
        return child_dex if child_dex < len(self.heap) else -1

    # PURPOSE
    # Get the index of the right child of the given index.
    # If the child does not exist, return -1.
    # SIGNATURE
    # right_child :: Integer => Integer
    def right_child(self, index):
        child_dex = 2 * (index + 1)
        return child_dex if child_dex < len(self.heap) else -1

    # PURPOSE
    # Insert a new value in the correct position in the heap.
    # SIGNATURE
    # insert :: Integer => None
    # TIME AND SPACE COMPLEXITY:
    # Time: O(logn), Space: O(1)
    def insert(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1
        while(self.heap[self.parent(index)] > self.heap[index] and self.parent(index) >= 0):
            self.swap(self.parent(index), index)
            index = self.parent(index)
        return

    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)

    def has_right_child(self, index):
        return self.left_child(index) < len(self.heap)

    def heapify(self, index):
        min = index
        curr_pos = index
        while(self.has_left_child(index) and self.has_right_child(curr_pos)):
            if self.heap[curr_pos] > self.heap[self.left_child(curr_pos)]:
                min = self.left_child(curr_pos)
            if self.heap[curr_pos] > self.heap[self.right_child(curr_pos)]:
                min = self.right_child(curr_pos)
            if min == curr_pos:
                break
            self.swap(min, curr_pos)
            curr_pos = min
        if self.has_left_child(curr_pos):
            if self.heap[curr_pos] > self.heap[self.left_child(curr_pos)]:
                self.swap(curr_pos, self.left_child(curr_pos))
        return

    def delete(self):
        self.swap(0, len(self.heap) - 1)
        self.heap = self.heap[:len(self.heap) - 1]
        self.heapify(0)
        return

    def get_min(self):
        return self.heap(0)

test_list = list(range(21))
test_heap = MinHeap(test_list)
test_heap.insert(-1)
print(test_heap.heap)
test_heap.insert(3)
print(test_heap.heap)