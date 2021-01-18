from d_ary_heap import *

# Starting off with the same tests as for binary heap with a d-ary heap
# where d = 2.
def test_parent():
    test_list = list(range(20))
    test_heap = DAryMinHeap(2, test_list)
    assert(-1 == test_heap.parent(test_heap.heap, 0))
    assert(0 == test_heap.parent(test_heap.heap, 1))
    assert(0 == test_heap.parent(test_heap.heap, 2))
    assert(1 == test_heap.parent(test_heap.heap, 3))
    assert(1 == test_heap.parent(test_heap.heap, 4))
    assert(2 == test_heap.parent(test_heap.heap, 5))
    assert(2 == test_heap.parent(test_heap.heap, 6))
    assert(3 == test_heap.parent(test_heap.heap, 7))
    assert(3 == test_heap.parent(test_heap.heap, 8))
    assert(4 == test_heap.parent(test_heap.heap, 9))
    assert(4 == test_heap.parent(test_heap.heap, 10))
    assert(5 == test_heap.parent(test_heap.heap, 11))
    assert(5 == test_heap.parent(test_heap.heap, 12))
    assert(6 == test_heap.parent(test_heap.heap, 13))
    assert(6 == test_heap.parent(test_heap.heap, 14))
    assert(7 == test_heap.parent(test_heap.heap, 15))
    assert(7 == test_heap.parent(test_heap.heap, 16))
    assert(8 == test_heap.parent(test_heap.heap, 17))
    assert(8 == test_heap.parent(test_heap.heap, 18))
    assert(9 == test_heap.parent(test_heap.heap, 19))
    assert(-1 == test_heap.parent(test_heap.heap, 20))

def test_kth_child():
    test_list = list(range(20))
    test_heap = DAryMinHeap(2, test_list)
    assert(1 == test_heap.kth_child(test_heap.heap, 1, 0))
    assert(2 == test_heap.kth_child(test_heap.heap, 2, 0))
    assert(3 == test_heap.kth_child(test_heap.heap, 1, 1))
    assert(4 == test_heap.kth_child(test_heap.heap, 2, 1))
    assert(5 == test_heap.kth_child(test_heap.heap, 1, 2))
    assert(6 == test_heap.kth_child(test_heap.heap, 2, 2))
    assert(7 == test_heap.kth_child(test_heap.heap, 1, 3))
    assert(8 == test_heap.kth_child(test_heap.heap, 2, 3))
    assert(9 == test_heap.kth_child(test_heap.heap, 1, 4))
    assert(10 == test_heap.kth_child(test_heap.heap, 2, 4))
    assert(11 == test_heap.kth_child(test_heap.heap, 1, 5))
    assert(12 == test_heap.kth_child(test_heap.heap, 2, 5))
    assert(13 == test_heap.kth_child(test_heap.heap, 1, 6))
    assert(14 == test_heap.kth_child(test_heap.heap, 2, 6))
    assert(15 == test_heap.kth_child(test_heap.heap, 1, 7))
    assert(16 == test_heap.kth_child(test_heap.heap, 2, 7))
    assert(17 == test_heap.kth_child(test_heap.heap, 1, 8))
    assert(18 == test_heap.kth_child(test_heap.heap, 2, 8))
    assert(19 == test_heap.kth_child(test_heap.heap, 1, 9))
    assert(-1 == test_heap.kth_child(test_heap.heap, 2, 9))

def test_insert():
    test_list = list(range(20))
    test_heap = DAryMinHeap(2, test_list)

    # Adding a value on the end.
    test_heap.insert_to_heap(test_heap.heap, 20)
    assert(list(range(21)) == test_heap.heap)

    # Adding a value at the root.
    test_heap.insert_to_heap(test_heap.heap, -1)
    assert([-1, 0, 2, 3, 1, 5, 6, 7, 8, 9, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10] == test_heap.heap)

    # Adding a value in the middle
    test_heap.insert_to_heap(test_heap.heap, 3)
    assert([-1, 0, 2, 3, 1, 5, 6, 7, 8, 9, 3, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 4] == test_heap.heap)

def test_delete():
    test_list = list(range(21))
    test_heap = DAryMinHeap(2, test_list)

    assert(0 in test_heap.heap)
    min = test_heap.delete()
    assert(0 == min)
    assert([1, 3, 2, 7, 4, 5, 6, 15, 8, 9, 10, 11, 12, 13, 14, 20, 16, 17, 18, 19] == test_heap.heap)

    min = test_heap.delete()
    assert(1 == min)
    assert([2, 3, 5, 7, 4, 11, 6, 15, 8, 9, 10, 19, 12, 13, 14, 20, 16, 17, 18] == test_heap.heap)

    min = test_heap.delete()
    assert(2 == min)
    assert([3, 4, 5, 7, 9, 11, 6, 15, 8, 18, 10, 19, 12, 13, 14, 20, 16, 17] == test_heap.heap)

def test_delete2():
    # Testing an initial list that is not sorted.
    test_list = [-4, 70, 12, 75, 83, 14, 16, 77, 78, 84, 900, 15, 16, 17, 22]
    test_heap = DAryMinHeap(2, test_list)
    assert(-4 == test_heap.delete())
    assert([12, 70, 14, 75, 83, 15, 16, 77, 78, 84, 900, 22, 16, 17] == test_heap.heap)

def test_delete3():
    test_list = list(range(7))
    test_heap = DAryMinHeap(2, test_list)
    assert(test_heap.delete() == 0)
    assert([1, 3, 2, 6, 4, 5] == test_heap.heap)

def test_build_heap():
    test_list1 = list(range(11))
    test_heap1 = DAryMinHeap(2, test_list1)
    assert(test_list1 == test_heap1.heap)

    test_list2 = [99, 7, 12, 4, 8, 9, -1, 6, -900]
    test_heap2 = DAryMinHeap(2, test_list2)
    assert([-900, 4, -1, 6, 8, 9, 12, 99, 7] == test_heap2.heap)

# Trying out some different sizes
def test_build_heap_different_d():
    test_list = [99, 7, 12, 4, 8, 9, -1, 6, -900, 17, 19, 22, 27, 24, 300]
    ans_3_ary = [-900, -1, 6, 4, 8, 9, 7, 99, 12, 17, 19, 22, 27, 24, 300]
    test_heap_3_ary = DAryMinHeap(3, test_list)
    assert(ans_3_ary == test_heap_3_ary.heap)
    test_list = [99, 7, 12, 4, 8, 9, -1, 6, -900, 17, 19, 22, 27, 24, 300]
    ans_4_ary = [-900, -1, 12, 4, 8, 9, 99, 6, 7, 17, 19, 22, 27, 24, 300]
    test_heap_4_ary = DAryMinHeap(4, test_list)
    assert(ans_4_ary == test_heap_4_ary.heap)
    test_list = [99, 7, 12, 4, 8, 9, -1, 6, -900, 17, 19, 22, 27, 24, 300]
    ans_5_ary = [-900, -1, 12, 4, 8, 9, 99, 6, 7, 17, 19, 22, 27, 24, 300]
    test_heap_5_ary = DAryMinHeap(4, test_list)
    assert(ans_5_ary == test_heap_5_ary.heap)

def test_parent_3_ary():
    test_list = list(range(30))
    test_heap = DAryMinHeap(3, test_list)
    assert(-1 == test_heap.parent(test_heap.heap, 0))
    assert(0 == test_heap.parent(test_heap.heap, 1))
    assert(0 == test_heap.parent(test_heap.heap, 2))
    assert(0 == test_heap.parent(test_heap.heap, 3))
    assert(1 == test_heap.parent(test_heap.heap, 4))
    assert(1 == test_heap.parent(test_heap.heap, 5))
    assert(1 == test_heap.parent(test_heap.heap, 6))
    assert(2 == test_heap.parent(test_heap.heap, 7))
    assert(2 == test_heap.parent(test_heap.heap, 8))
    assert(2 == test_heap.parent(test_heap.heap, 9))
    assert(3 == test_heap.parent(test_heap.heap, 10))
    assert(3 == test_heap.parent(test_heap.heap, 11))
    assert(3 == test_heap.parent(test_heap.heap, 12))
    assert(4 == test_heap.parent(test_heap.heap, 13))
    assert(4 == test_heap.parent(test_heap.heap, 14))
    assert(4 == test_heap.parent(test_heap.heap, 15))
    assert(5 == test_heap.parent(test_heap.heap, 16))
    assert(5 == test_heap.parent(test_heap.heap, 17))
    assert(5 == test_heap.parent(test_heap.heap, 18))
    assert(6 == test_heap.parent(test_heap.heap, 19))
    assert(6 == test_heap.parent(test_heap.heap, 20))
    assert(6 == test_heap.parent(test_heap.heap, 21))
    assert(7 == test_heap.parent(test_heap.heap, 22))
    assert(7 == test_heap.parent(test_heap.heap, 23))
    assert(7 == test_heap.parent(test_heap.heap, 24))
    assert(8 == test_heap.parent(test_heap.heap, 25))
    assert(8 == test_heap.parent(test_heap.heap, 26))
    assert(8 == test_heap.parent(test_heap.heap, 27))
    assert(9 == test_heap.parent(test_heap.heap, 28))
    assert(9 == test_heap.parent(test_heap.heap, 29))
    assert(-1 == test_heap.parent(test_heap.heap, 30))

def test_parent_4_ary():
    test_list = list(range(30))
    test_heap = DAryMinHeap(4, test_list)
    assert(-1 == test_heap.parent(test_heap.heap, 0))
    assert(0 == test_heap.parent(test_heap.heap, 1))
    assert(0 == test_heap.parent(test_heap.heap, 2))
    assert(0 == test_heap.parent(test_heap.heap, 3))
    assert(0 == test_heap.parent(test_heap.heap, 4))
    assert(1 == test_heap.parent(test_heap.heap, 5))
    assert(1 == test_heap.parent(test_heap.heap, 6))
    assert(1 == test_heap.parent(test_heap.heap, 7))
    assert(1 == test_heap.parent(test_heap.heap, 8))
    assert(2 == test_heap.parent(test_heap.heap, 9))
    assert(2 == test_heap.parent(test_heap.heap, 10))
    assert(2 == test_heap.parent(test_heap.heap, 11))
    assert(2 == test_heap.parent(test_heap.heap, 12))
    assert(3 == test_heap.parent(test_heap.heap, 13))
    assert(3 == test_heap.parent(test_heap.heap, 14))
    assert(3 == test_heap.parent(test_heap.heap, 15))
    assert(3 == test_heap.parent(test_heap.heap, 16))
    assert(4 == test_heap.parent(test_heap.heap, 17))
    assert(4 == test_heap.parent(test_heap.heap, 18))
    assert(4 == test_heap.parent(test_heap.heap, 19))
    assert(4 == test_heap.parent(test_heap.heap, 20))
    assert(5 == test_heap.parent(test_heap.heap, 21))
    assert(5 == test_heap.parent(test_heap.heap, 22))
    assert(5 == test_heap.parent(test_heap.heap, 23))
    assert(5 == test_heap.parent(test_heap.heap, 24))
    assert(6 == test_heap.parent(test_heap.heap, 25))
    assert(6 == test_heap.parent(test_heap.heap, 26))
    assert(6 == test_heap.parent(test_heap.heap, 27))
    assert(6 == test_heap.parent(test_heap.heap, 28))
    assert(7 == test_heap.parent(test_heap.heap, 29))
    assert(-1 == test_heap.parent(test_heap.heap, 30))

def test_kth_child_3_ary():
    test_list = list(range(20))
    test_heap = DAryMinHeap(3, test_list)
    assert(1 == test_heap.kth_child(test_heap.heap, 1, 0))
    assert(2 == test_heap.kth_child(test_heap.heap, 2, 0))
    assert(3 == test_heap.kth_child(test_heap.heap, 3, 0))
    assert(4 == test_heap.kth_child(test_heap.heap, 1, 1))
    assert(5 == test_heap.kth_child(test_heap.heap, 2, 1))
    assert(6 == test_heap.kth_child(test_heap.heap, 3, 1))
    assert(7 == test_heap.kth_child(test_heap.heap, 1, 2))
    assert(8 == test_heap.kth_child(test_heap.heap, 2, 2))
    assert(9 == test_heap.kth_child(test_heap.heap, 3, 2))
    assert(10 == test_heap.kth_child(test_heap.heap, 1, 3))
    assert(11 == test_heap.kth_child(test_heap.heap, 2, 3))
    assert(12 == test_heap.kth_child(test_heap.heap, 3, 3))
    assert(13 == test_heap.kth_child(test_heap.heap, 1, 4))
    assert(14 == test_heap.kth_child(test_heap.heap, 2, 4))
    assert(15 == test_heap.kth_child(test_heap.heap, 3, 4))
    assert(16 == test_heap.kth_child(test_heap.heap, 1, 5))
    assert(17 == test_heap.kth_child(test_heap.heap, 2, 5))
    assert(18 == test_heap.kth_child(test_heap.heap, 3, 5))
    assert(19 == test_heap.kth_child(test_heap.heap, 1, 6))
    assert(-1 == test_heap.kth_child(test_heap.heap, 2, 6))

def test_kth_child_4_ary():
    test_list = list(range(20))
    test_heap = DAryMinHeap(4, test_list)
    assert(1 == test_heap.kth_child(test_heap.heap, 1, 0))
    assert(2 == test_heap.kth_child(test_heap.heap, 2, 0))
    assert(3 == test_heap.kth_child(test_heap.heap, 3, 0))
    assert(4 == test_heap.kth_child(test_heap.heap, 4, 0))
    assert(5 == test_heap.kth_child(test_heap.heap, 1, 1))
    assert(6 == test_heap.kth_child(test_heap.heap, 2, 1))
    assert(7 == test_heap.kth_child(test_heap.heap, 3, 1))
    assert(8 == test_heap.kth_child(test_heap.heap, 4, 1))
    assert(9 == test_heap.kth_child(test_heap.heap, 1, 2))
    assert(10 == test_heap.kth_child(test_heap.heap, 2, 2))
    assert(11 == test_heap.kth_child(test_heap.heap, 3, 2))
    assert(12 == test_heap.kth_child(test_heap.heap, 4, 2))
    assert(13 == test_heap.kth_child(test_heap.heap, 1, 3))
    assert(14 == test_heap.kth_child(test_heap.heap, 2, 3))
    assert(15 == test_heap.kth_child(test_heap.heap, 3, 3))
    assert(16 == test_heap.kth_child(test_heap.heap, 4, 3))
    assert(17 == test_heap.kth_child(test_heap.heap, 1, 4))
    assert(18 == test_heap.kth_child(test_heap.heap, 2, 4))
    assert(19 == test_heap.kth_child(test_heap.heap, 3, 4))
    assert(-1 == test_heap.kth_child(test_heap.heap, 4, 4))

def test_insert_3_ary():
    test_list = [99, 7, 12, 4, 8, 9, -1, 6, -900, 17, 19, 22, 27, 24, 300]
    test_heap = DAryMinHeap(3, test_list)
    test_heap.insert_to_heap(test_heap.heap, -1000)
    assert([-1000, -900, 6, 4, -1, 9, 7, 99, 12, 17, 19, 22, 27, 24, 300, 8] == test_heap.heap)
    test_heap.insert_to_heap(test_heap.heap, 5)
    assert([-1000, -900, 6, 4, -1, 5, 7, 99, 12, 17, 19, 22, 27, 24, 300, 8, 9] == test_heap.heap)
    test_heap.insert_to_heap(test_heap.heap, 5001)
    assert([-1000, -900, 6, 4, -1, 5, 7, 99, 12, 17, 19, 22, 27, 24, 300, 8, 9, 5001] == test_heap.heap)

def test_insert_4_ary():
    test_list = [99, 7, 12, 4, 8, 9, -1, 6, -900, 17, 19, 22, 27, 24, 300]
    test_heap = DAryMinHeap(4, test_list)
    test_heap.insert_to_heap(test_heap.heap, -1000)
    assert([-1000, -1, 12, -900, 8, 9, 99, 6, 7, 17, 19, 22, 27, 24, 300, 4] == test_heap.heap)
    test_heap.insert_to_heap(test_heap.heap, 5)
    assert([-1000, -1, 12, -900, 8, 9, 99, 6, 7, 17, 19, 22, 27, 24, 300, 4, 5] == test_heap.heap)
    test_heap.insert_to_heap(test_heap.heap, 5001)
    assert([-1000, -1, 12, -900, 8, 9, 99, 6, 7, 17, 19, 22, 27, 24, 300, 4, 5, 5001] == test_heap.heap)

def test_delete_3_ary():
    # Testing an initial list that is not sorted.
    test_list = [-4, 70, 12, 75, 83, 14, 16, 77, 78, 84, 900, 15, 16, 17, 22]
    test_heap = DAryMinHeap(3, test_list)
    assert(-4 == test_heap.delete())
    assert([12, 14, 22, 15, 17, 70, 16, 77, 78, 84, 900, 75, 16, 83] == test_heap.heap)

def test_delete_4_ary():
    # Testing an initial list that is not sorted.
    test_list = [-4, 70, 12, 75, 83, 14, 16, 77, 78, 84, 900, 15, 16, 17, 22]
    test_heap = DAryMinHeap(4, test_list)
    assert(-4 == test_heap.delete())
    assert([12, 14, 15, 17, 83, 70, 16, 77, 78, 84, 900, 22, 16, 75] == test_heap.heap)