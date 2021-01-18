import random

from heap_sort import *

def generate_random_list(n, k):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(-k, k))
    return rand_list

def test_heap_sort():
    for i in range(101):
        test_list = generate_random_list(100, 100)
        copy = test_list.copy()
        test_list = heap_sort(test_list)
        copy.sort()
        assert(copy == test_list)

