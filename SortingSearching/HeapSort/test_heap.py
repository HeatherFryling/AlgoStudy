from heap import *

def test_parent():
    test_list = list(range(20))
    test_heap = MinHeap(test_list)
    assert(test_heap.parent(0) == -1)
    assert(test_heap.parent(1) == 0)
    assert(test_heap.parent(2) == 0)
    assert(test_heap.parent(3) == 1)
    assert(test_heap.parent(4) == 1)
    assert(test_heap.parent(5) == 2)
    assert(test_heap.parent(6) == 2)
    assert(test_heap.parent(7) == 3)
    assert(test_heap.parent(8) == 3)
    assert(test_heap.parent(9) == 4)
    assert(test_heap.parent(10) == 4)
    assert(test_heap.parent(11) == 5)
    assert(test_heap.parent(12) == 5)
    assert(test_heap.parent(13) == 6)
    assert(test_heap.parent(14) == 6)
    assert(test_heap.parent(15) == 7)
    assert(test_heap.parent(16) == 7)
    assert(test_heap.parent(17) == 8)
    assert(test_heap.parent(18) == 8)
    assert(test_heap.parent(19) == 9)
    assert(test_heap.parent(20) == -1)

def test_left_child():
    test_list = list(range(20))
    test_heap = MinHeap(test_list)
    assert(test_heap.left_child(0) == 1)
    assert(test_heap.left_child(1) == 3)
    assert(test_heap.left_child(2) == 5)
    assert(test_heap.left_child(3) == 7)
    assert(test_heap.left_child(4) == 9)
    assert(test_heap.left_child(5) == 11)
    assert(test_heap.left_child(6) == 13)
    assert(test_heap.left_child(7) == 15)
    assert(test_heap.left_child(8) == 17)
    assert(test_heap.left_child(9) == 19)


def test_right_child():
    test_list = list(range(20))
    test_heap = MinHeap(test_list)
    assert(test_heap.right_child(0) == 2)
    assert(test_heap.right_child(1) == 4)
    assert(test_heap.right_child(2) == 6)
    assert(test_heap.right_child(3) == 8)
    assert(test_heap.right_child(4) == 10)
    assert(test_heap.right_child(5) == 12)
    assert(test_heap.right_child(6) == 14)
    assert(test_heap.right_child(7) == 16)
    assert(test_heap.right_child(8) == 18)
    assert(test_heap.right_child(9) == -1)

def test_insert():
    test_list = list(range(20))
    test_heap = MinHeap(test_list)

    # Adding a value on the end.
    test_heap.insert(20)
    assert(list(range(21)) == test_heap.heap)

    # Adding a value at the root.
    test_heap.insert(-1)
    assert([-1, 0, 2, 3, 1, 5, 6, 7, 8, 9, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10] == test_heap.heap)

    # Adding a value in the middle
    test_heap.insert(3)
    assert([-1, 0, 2, 3, 1, 5, 6, 7, 8, 9, 3, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 4] == test_heap.heap)

def test_delete():
    test_list = list(range(21))
    test_heap = MinHeap(test_list)

    assert(0 in test_heap.heap)
    min = test_heap.delete()
    assert(0 == min)
    assert(0 not in test_heap.heap)
    assert([1, 3, 2, 7, 4, 5, 6, 15, 8, 9, 10, 11, 12, 13, 14, 19, 16, 17, 18, 20] == test_heap.heap)

    min = test_heap.delete()
    assert(1 == min)
    assert(1 not in test_heap.heap)
    assert([2, 3, 5, 7, 4, 11, 6, 15, 8, 9, 10, 18, 12, 13, 14, 19, 16, 17, 20] == test_heap.heap)

    min = test_heap.delete()
    assert(2 == min)
    assert(2 not in test_heap.heap)
    assert([3, 4, 5, 7, 9, 11, 6, 15, 8, 17, 10, 18, 12, 13, 14, 19, 16, 20] == test_heap.heap)

def test_delete2():
    test_list = [-4, 70, 12, 71, 99, 15, 19, 72, 100, 17, 21, 88, 500]
    test_heap = MinHeap(test_list)
    assert(-4 == test_heap.delete())
