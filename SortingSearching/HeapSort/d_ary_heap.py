# Heather Fryling
# 1/11/2021
# As an exercise, I am implementing a d-ary heap instead of a
# binary heap.

class DAryMinHeap:
    heap = []
    # d is the max number of children per node in the heap
    d = 0

    # PURPOSE
    # Initialize the MinHeap
    # SIGNATURE
    # MinHeap() :: self, List => None
    def __init__(self, d, heap):
        self.d = d
        print("from init", self.build_heap(heap))
        self.heap = self.build_heap(heap)

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
    def parent(self, index):
        if (index == 0 or index > len(self.heap) - 1):
            return -1
        return (index - 1) // self.d

    # PURPOSE
    # Get the index of the kth child of the given index.
    # If the child does not exist, return -1.
    # SIGNATURE
    # kth_child :: Integer, Integer => Integer
    def kth_child(self, arr, k, index):
        child_dex = (self.d * index) + k
        return child_dex if child_dex < len(arr) else -1

    # PURPOSE
    # Insert a new value in the correct position in the heap.
    # SIGNATURE
    # insert :: Integer => None
    # TIME AND SPACE COMPLEXITY:
    # Time: O(logn), Space: O(1)
    def insert_to_heap(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1
        while(self.heap[self.parent(index)] > self.heap[index] and self.parent(index) >= 0):
            self.swap(self.heap, self.parent(index), index)
            index = self.parent(index)
        return

    # PURPOSE
    # Determine if a given position has a left child.
    # SIGNATURE
    # has_kth_child :: Integer, Integer => Boolean
    def has_kth_child(self, arr, k, index):
        child_dex = self.kth_child(arr, k, index)
        return True if child_dex > 0 and child_dex < len(arr) else False

    # PURPOSE
    # Return the index of the minimum element considering the node at index
    # and its children. If the minimum at the index, return the index.
    # Otherwise, return the index of the smallest child value.
    # SIGNATURE
    # min_parent_child :: List, Integer => Integer
    def min_parent_child(self, arr, index):
        min_val = arr[index]
        min_index = index
        for i in range(1, self.d + 1):
            if self.has_kth_child(arr, i, index):
                if arr[self.kth_child(arr, i, index)] < min_val:
                    min_val = arr[self.kth_child(arr, i, index)]
                    min_index = self.kth_child(arr, i, index)
        return min_index


    # PURPOSE
    # Given the index of a value that violates the heap property,
    # bubble the value at the given index down to its correct position.
    # SIGNATURE
    # heapify :: Integer => None
    def heapify(self, arr, index):
        min_index = index
        curr_pos = index
        last_parent = (len(self.heap) - 2) // self.d
        while(curr_pos <= last_parent):
            min_index = self.min_parent_child(arr, curr_pos)
            if min_index == curr_pos:
                break
            else:
                self.swap(arr, curr_pos, min_index)
                curr_pos = min_index
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
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.heapify(self.heap, 0)
        return min

    # PURPOSE
    # Get the minimum item in the heap.
    # SIGNATURE
    # get_min :: None => Integer
    # TIME AND SPACE COMPLEXITY
    # time = O(1) space = O(1)
    def get_min(self):
        if len(self.heap)> 0:
            return self.heap[0]
        return None

    # PURPOSE
    # Take in a list of numbers and turn it into a valid min-heap.
    # SIGNATURE
    # build_heap :: List => None
    def build_heap(self, arr):
        for i in range((len(arr) - 1) // self.d, -1, -1):
            self.heapify(arr, i)
        return arr

test_list1 = list(range(11))
test_heap1 = DAryMinHeap(2, test_list1)
print(test_list1)
print(test_heap1.heap)
print(test_heap1.build_heap(test_list1))
print()


test_list2 = [99, 7, 12, 4, 8, 9, -1, 6, -900]
answer = [-900, 4, -1, 6, 8, 9, 12, 99, 7]
test_heap2 = DAryMinHeap(2, test_list2)
print(test_heap2.heap)
print("from outside", test_heap2.build_heap(test_list2))
print(answer)