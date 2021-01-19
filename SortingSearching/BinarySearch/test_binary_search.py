from binary_search import *

def test_binary_search():
    test1 = [1, 2, 3, 4]
    target1 = 1
    target2 = 0
    test2 = [1, 9, 14, 17, 99]
    target3 = 99
    target4 = 3

    assert(0 == binary_search(test1, target1))
    assert(-1 == binary_search(test1, target2))
    assert(0 == binary_search(test2, target1))
    assert(-1 == binary_search(test2, target4))
    assert(4 == binary_search(test2, target3))