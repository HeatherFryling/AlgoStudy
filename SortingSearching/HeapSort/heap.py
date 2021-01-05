# Heather Fryling
# 1/5/2021
# Minheap as explained by Zhifeng Sun
# CS5800 Northeastern University, Seattle

class MinHeap:
    heap = []

    def __init__(self, heap=[]):
        self.size = len(heap)
        self.heap = heap

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def parent(self, index):
        if (index == 0 or index > (len(self.heap) - 1)):
            return -1
        return (index - 1) // 2

    def left_child(self, index):
        child_dex = 2 * (index + 1) - 1
        return child_dex if child_dex < len(self.heap) else -1

    def right_child(self, index):
        child_dex = 2 * (index + 1)
        return child_dex if child_dex < len(self.heap) else -1

    def insert(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1
        while(self.heap[self.parent(index) > self.heap[index]]):
            self.swap(self.parent(index), index)
            index = self.parent(index)
        return

    def delete(self, val):
        return

    def heapify(self, arr):
        return

    def get_min(self):
        return