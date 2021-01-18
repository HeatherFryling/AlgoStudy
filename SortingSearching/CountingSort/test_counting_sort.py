from counting_sort import *

import random

test1 = [0, 1, 2, 3, 4, 5]
test2 = [5, 4, 3, 2, 1, 0]
test3 = [3, 3, 4, 1, 1, 5]

def generate_random_list(n, k):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(0, k))
    return rand_list

def test_counting_sort_defined():
    assert(test1 == counting_sort(test1, 5))
    assert(test1 == counting_sort(test2, 5))
    assert([1, 1, 3, 3, 4, 5] == counting_sort(test3, 5))

def test_counting_sort_random():
    for _ in range(100):
        random_list = generate_random_list(100, 100)
        copy = random_list.copy()
        my_answer = counting_sort(random_list, 100)
        copy.sort()
        assert(copy == my_answer)
