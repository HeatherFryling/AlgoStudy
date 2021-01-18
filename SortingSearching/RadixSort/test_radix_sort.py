import random
from radix_sort import *

def generate_random_list(n, k):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(0, k))
    return rand_list

def test_radix_sort_1_digit():
    ans = [0, 1, 2, 3, 4, 5]
    test1 = [0, 1, 2, 3, 4, 5]
    test2 = [5, 4, 3, 2, 1, 0]
    test3 = [3, 2, 1, 0, 5, 4]
    assert(ans == radix_sort(test1, 1))
    assert(ans == radix_sort(test2, 1))
    assert(ans == radix_sort(test3, 1))

def test_radix_sort_2_digits():
    ans = [0, 1, 2, 3, 4, 5, 9, 11, 12, 22, 99]
    test1 = [0, 1, 2, 3, 4, 5, 9, 11, 12, 22, 99]
    test2 = [99, 22, 12, 11, 9, 5, 4, 3, 2, 1, 0]
    test3 = [99, 2, 1, 9, 4, 5, 11, 0, 12, 3, 22]
    assert(ans == radix_sort(test1, 2))
    assert(ans == radix_sort(test2, 2))
    assert(ans == radix_sort(test3, 2))

def test_radix_sort_randomized():
    for _ in range(101):
        d = random.randint(1, 5)
        test_list = generate_random_list(50, 10**(d) - 1)
        copy_list = test_list.copy()
        my_answer = radix_sort(test_list, d)
        copy_list.sort()
        assert(copy_list == my_answer)
