from subset_sum import *

def test_iterative():
    test1 = [1, 2, 3]
    for i in range(7):
        assert(True == subset_sum(test1, i))
    target2 = 7
    assert(False == subset_sum(test1, target2))

def test_recursive():
    test1 = [1, 2, 3]
    for i in range(7):
        assert(True == subset_sum_top_down(test1, i))
    target2 = 7
    assert(False == subset_sum_top_down(test1, target2))