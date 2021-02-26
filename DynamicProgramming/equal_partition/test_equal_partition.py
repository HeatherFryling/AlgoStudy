from equal_partition import *

def test_brute_force():
    test1 = [1, 0, 3, 4]
    ans1 = True
    assert(ans1 == equal_brute_force(test1))
    test2 = [1, 1, 3, 1, 2]
    ans2 = True
    assert(ans2 == equal_brute_force(test2))
    test3 = [0, 2, 0, 0, 1, 5]
    ans3 = False
    assert(ans3 == equal_brute_force(test3))

def test_memo():
    test1 = [1, 0, 3, 4]
    ans1 = True
    assert(ans1 == memo_2_partition(test1))
    test2 = [1, 1, 3, 1, 2]
    ans2 = True
    assert(ans2 == memo_2_partition(test2))
    test3 = [0, 2, 0, 0, 1, 5]
    ans3 = False
    assert(ans3 == memo_2_partition(test3))

def test_iterative():
    test1 = [1, 0, 3, 4]
    ans1 = True
    assert(ans1 == equal_partition_it(test1))
    test2 = [1, 1, 3, 1, 2]
    ans2 = True
    assert(ans2 == equal_partition_it(test2))
    test3 = [0, 2, 0, 0, 1, 5]
    ans3 = False
    assert(ans3 == equal_partition_it(test3))