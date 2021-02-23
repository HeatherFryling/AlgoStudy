from lis import *

def test_iterative():
    test1 = [5, 1, 3, 2, 7, 9]
    assert(4 == longest_increasing_subsequence(test1))

    test2 = [0, 0, 0, 0, 0]
    assert(1 == longest_increasing_subsequence(test2))

    test3 = [0, 1, 2, 3, 4, 5]
    assert(6 == longest_increasing_subsequence(test3))

    test4 = [5, 4, 3, 2, 1, 0]
    assert(1 == longest_increasing_subsequence(test4))

def test_recursive():
    test1 = [5, 1, 3, 2, 7, 9]
    assert(4 == lis_top_down(test1))

    test2 = [0, 0, 0, 0, 0]
    assert(1 == lis_top_down(test2))

    test3 = [0, 1, 2, 3, 4, 5]
    assert(6 == lis_top_down(test3))

    test4 = [5, 4, 3, 2, 1, 0]
    assert(1 == lis_top_down(test4))