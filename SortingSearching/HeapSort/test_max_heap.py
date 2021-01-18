# These tests are less extensive than on the min heap, because this
# is the same as min heap except the direction of the comparison in 
# heapify.

from max_heap import *

def test_build_heap():
    test_list1 = list(range(11))
    test_heap1 = MaxHeap(test_list1)
    assert([10, 9, 6, 8, 4, 5, 2, 7, 3, 1, 0] == test_heap1.heap)

    test_list2 = [99, 7, 12, 4, 8, 9, -1, 6, -900]
    test_heap2 = MaxHeap(test_list2)
    assert([99, 8, 12, 6, 7, 9, -1, 4, -900] == test_heap2.heap)

    test_list_3 = [99, 7, 12, 4, 8, 9, -1, 6]
    test_heap3 = MaxHeap(test_list_3)
    assert([99, 8, 12, 6, 7, 9, -1, 4] == test_heap3.heap)

def test_insert():
    test_list1 = list(range(11))
    test_heap1 = MaxHeap(test_list1)
    test_heap1.insert_to_heap(500)
    assert([500, 9, 10, 8, 4, 6, 2, 7, 3, 1, 0, 5] == test_heap1.heap)