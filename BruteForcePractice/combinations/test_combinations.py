from combinations import *

def test_count_combinations():
    test1 = []
    test2 = [1]
    test3 = [1, 2]
    test4 = [1, 2, 3]
    test5 = [1, 2, 3, 4]
    tests = [test1, test2, test3, test4, test5]
    for i, test in enumerate(tests):
        assert(2 ** i == countPowerset(test))