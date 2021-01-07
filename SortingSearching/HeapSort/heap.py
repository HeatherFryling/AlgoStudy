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
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    # PURPOSE
    # Get the index parent index of the given index.
    # If the parent does not exist, return -1.
    # SIGNATURE
    # parent :: Integer => Integer
    def parent(self, arr, index):
        if (index == 0 or index > (len(arr) - 1)):
            return -1
        return (index - 1) // 2

    # PURPOSE
    # Get the index of the left child of the given index.
    # If the child does not exist, return -1.
    # SIGNATURE
    # left_child :: Integer => Integer
    def left_child(self, arr, index):
        child_dex = 2 * (index + 1) - 1
        return child_dex if child_dex < len(arr) else -1

    # PURPOSE
    # Get the index of the right child of the given index.
    # If the child does not exist, return -1.
    # SIGNATURE
    # right_child :: Integer => Integer
    def right_child(self, arr, index):
        child_dex = 2 * (index + 1)
        return child_dex if child_dex < len(arr) else -1

    # PURPOSE
    # Insert a new value in the correct position in the heap.
    # SIGNATURE
    # insert :: Integer => None
    # TIME AND SPACE COMPLEXITY:
    # Time: O(logn), Space: O(1)
    def insert(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1
        while(self.heap[self.parent(self.heap, index)] > self.heap[index] and self.parent(self.heap, index) >= 0):
            self.swap(self.heap, self.parent(self.heap, index), index)
            index = self.parent(self.heap, index)
        return

    # PURPOSE
    # Determine if a given position has a left child.
    # SIGNATURE
    # has_left_child :: Integer => Boolean
    def has_left_child(self, arr, index):
        return self.left_child(arr, index) < len(arr) and self.left_child(arr, index) != -1

    # PURPOSE
    # Determine if a given position has a right child.
    # SIGNATURE
    # has_right_child :: Integer => Boolean
    def has_right_child(self, arr, index):
        return self.left_child(arr, index) < len(arr) and self.right_child(arr, index) != -1

    # PURPOSE
    # Given the index of a value that violates the heap property,
    # bubble the value at the given index down to its correct position.
    # SIGNATURE
    # heapify :: Integer => None
    def heapify(self, arr, index):
        min = index
        curr_pos = index
        while(self.has_left_child(arr, curr_pos) and self.has_right_child(arr, curr_pos)):
            left_child = self.left_child(arr, curr_pos)
            right_child = self.right_child(arr, curr_pos)
            min = curr_pos
            if arr[curr_pos] > arr[left_child]:
                min = self.left_child(arr, curr_pos)
            if arr[min] > arr[right_child]:
                min = right_child
            if min == curr_pos:
                break
            else:
                self.swap(arr, curr_pos, min)
                curr_pos = min
        if self.has_left_child(arr, curr_pos):
        # Add a test for this branch
            if arr[curr_pos] > arr[self.left_child(arr, curr_pos)]:
                self.swap(arr, curr_pos, self.left_child(arr, curr_pos))
        return

    # PURPOSE
    # Delete and return the item at the top of the heap.
    # SIGNATURE
    # delete :: None => Integer
    # TIME AND SPACE COMPLEXITY
    # time = O(lgn) for one call to heapify
    # space = O(1)
    def delete(self):
        min = self.get_min()
        self.swap(self.heap, 0, len(self.heap) - 1)
        self.heap = self.heap[:len(self.heap) - 1]
        self.heapify(self.heap, 0)
        return min

    # PURPOSE
    # Get the minimum item in the heap.
    # SIGNATURE
    # get_min :: None => Integer
    # TIME AND SPACE COMPLEXITY
    # time = O(1) space = O(1)
    def get_min(self):
        return self.heap[0]

    # PURPOSE
    # Take in a list of numbers and turn it into a valid min-heap.
    # SIGNATURE
    # build_heap :: List => None
    def build_heap(self, arr):
        for i in range((len(arr) - 1) / 2, -1, -1):
            self.heapify(arr, i)
        return