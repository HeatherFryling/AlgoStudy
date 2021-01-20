from kth_with_partition import *

import random

def generate_random_list(n, k):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(-k, k))
    return rand_list

def test_median_of_3():
    test1 = [1, 2, 3]
    ans1 = 1
    test2 = [1, 3, 2]
    ans2 = 2
    test3 = [2, 1, 3]
    ans3 = 0
    test4 = [3, 1, 2]
    ans4 = 2
    test5 = [3, 2, 1]
    ans5 = 1
    test6 = [2, 3, 1]
    ans6 = 0

    assert(ans1 == median_of_three(test1, 0, 2))
    assert(ans2 == median_of_three(test2, 0, 2))
    assert(ans3 == median_of_three(test3, 0, 2))
    assert(ans4 == median_of_three(test4, 0, 2))
    assert(ans5 == median_of_three(test5, 0, 2))
    assert(ans6 == median_of_three(test6, 0, 2))

def test_partition():
    # array is already correctly sorted
    test1 = [1, 2, 3, 4, 5]
    ans1 = 2
    part1 = [1, 2, 3, 4, 5]
    # array is not correctly sorted
    test2 = [5, 2, 3, 4, 1]
    ans2 = 2
    part2 = [2, 1, 3, 4, 5]
    # median is the first value
    test3 = [1, 2, 1, 4, 1]
    ans3 = 2
    part3 = [1, 1, 1, 4, 2]
    # median is the last value
    test4 = [4, 3, 1, 5, 2]
    ans4 = 1
    part4 = [1, 2, 4, 5, 3]

    assert(ans1 == partition(test1, 0, len(test1) - 1))
    assert(part1 == test1)
    assert(ans2 == partition(test2, 0, len(test2) - 1))
    assert(part2 == test2)
    assert(ans3 == partition(test3, 0, len(test3) - 1))
    assert(part3 == test3)
    assert(ans4 == partition(test4, 0, len(test4) - 1))
    assert(part4 == test4)

def test_kth_with_partition1():
    test = [1, 2, 3, 4, 5]
    ans1 = 1
    ans2 = 2
    ans3 = 3
    ans4 = 4
    ans5 = 5

    assert(ans1 == kth_with_partition(test, 1))
    assert(ans2 == kth_with_partition(test, 2))
    assert(ans3 == kth_with_partition(test, 3))
    assert(ans4 == kth_with_partition(test, 4))
    assert(ans5 == kth_with_partition(test, 5))

def test_kth_with_partition2():
    test = [5, 2, 3, 1, 4]
    ans1 = 1
    ans2 = 2
    ans3 = 3
    ans4 = 4
    ans5 = 5

    assert(ans1 == kth_with_partition(test, 1))
    assert(ans2 == kth_with_partition(test, 2))
    assert(ans3 == kth_with_partition(test, 3))
    assert(ans4 == kth_with_partition(test, 4))
    assert(ans5 == kth_with_partition(test, 5))

def test_kth_with_partition3():
    n = 100
    for _ in range(100):
        k = random.randrange(n)
        test = generate_random_list(n, 1000)
        copy = test.copy()
        copy.sort()
        test_val = kth_with_partition(test, k)
        assert(copy[k - 1] == test_val)




