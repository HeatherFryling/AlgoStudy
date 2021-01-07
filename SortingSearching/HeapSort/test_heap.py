from heap import *

def test_parent():
    test_list = list(range(20))
    test_heap = MinHeap(test_list)
    assert(-1 == test_heap.parent(test_heap.heap, 0))
    assert(0 == test_heap.parent(test_heap.heap, 1))
    assert(0 == test_heap.parent(test_heap.heap, 2))
    assert(1 == test_heap.parent(test_heap.heap, 3))
    assert(1 == test_heap.parent(test_heap.heap, 4))
    assert(2 == test_heap.parent(test_heap.heap, 5))
    assert(2 == test_heap.parent(test_heap.heap, 6))
    assert(3 == test_heap.parent(test_heap.heap, 7))
    assert(3 == test_heap.parent(test_heap.heap, 8))
    assert(test_heap.parent(test_heap.heap, 9) == 4)
    assert(test_heap.parent(test_heap.heap, 10) == 4)
    assert(test_heap.parent(test_heap.heap, 11) == 5)
    assert(test_heap.parent(test_heap.heap, 12) == 5)
    assert(test_heap.parent(test_heap.heap, 13) == 6)
    assert(test_heap.parent(test_heap.heap, 14) == 6)
    assert(test_heap.parent(test_heap.heap, 15) == 7)
    assert(test_heap.parent(test_heap.heap, 16) == 7)
    assert(test_heap.parent(test_heap.heap, 17) == 8)
    assert(test_heap.parent(test_heap.heap, 18) == 8)
    assert(test_heap.parent(test_heap.heap, 19) == 9)
    assert(test_heap.parent(test_heap.heap, 20) == -1)

def test_left_child():
    test_list = list(range(20))
    test_heap = MinHeap(test_list)
    assert(test_heap.left_child(test_heap.heap, 0) == 1)
    assert(test_heap.left_child(test_heap.heap, 1) == 3)
    assert(test_heap.left_child(test_heap.heap, 2) == 5)
    assert(test_heap.left_child(test_heap.heap, 3) == 7)
    assert(test_heap.left_child(test_heap.heap, 4) == 9)
    assert(test_heap.left_child(test_heap.heap, 5) == 11)
    assert(test_heap.left_child(test_heap.heap, 6) == 13)
    assert(test_heap.left_child(test_heap.heap, 7) == 15)
    assert(test_heap.left_child(test_heap.heap, 8) == 17)
    assert(test_heap.left_child(test_heap.heap, 9) == 19)


def test_right_child():
    test_list = list(range(20))
    test_heap = MinHeap(test_list)
    assert(test_heap.right_child(test_heap.heap, 0) == 2)
    assert(test_heap.right_child(test_heap.heap, 1) == 4)
    assert(test_heap.right_child(test_heap.heap, 2) == 6)
    assert(test_heap.right_child(test_heap.heap, 3) == 8)
    assert(test_heap.right_child(test_heap.heap, 4) == 10)
    assert(test_heap.right_child(test_heap.heap, 5) == 12)
    assert(test_heap.right_child(test_heap.heap, 6) == 14)
    assert(test_heap.right_child(test_heap.heap, 7) == 16)
    assert(test_heap.right_child(test_heap.heap, 8) == 18)
    assert(test_heap.right_child(test_heap.heap, 9) == -1)

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
    assert([1, 3, 2, 7, 4, 5, 6, 15, 8, 9, 10, 11, 12, 13, 14, 20, 16, 17, 18, 19] == test_heap.heap)

    min = test_heap.delete()
    assert(1 == min)
    assert(1 not in test_heap.heap)
    assert([2, 3, 5, 7, 4, 11, 6, 15, 8, 9, 10, 19, 12, 13, 14, 20, 16, 17, 18] == test_heap.heap)

    min = test_heap.delete()
    assert(2 == min)
    assert(2 not in test_heap.heap)
    assert([3, 4, 5, 7, 9, 11, 6, 15, 8, 18, 10, 19, 12, 13, 14, 20, 16, 17] == test_heap.heap)

def test_delete2():
    test_list = [-4, 70, 12, 75, 83, 14, 16, 77, 78, 84, 900, 15, 16, 17, 22]
    test_heap = MinHeap(test_list)
    assert(-4 == test_heap.delete())
    assert([12, 70, 14, 75, 83, 15, 16, 77, 78, 84, 900, 22, 16, 17] == test_heap.heap)
