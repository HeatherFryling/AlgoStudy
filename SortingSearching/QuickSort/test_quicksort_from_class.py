from quicksort_from_class import *
import itertools as it

def test_median_of_three():
    list1 = [1, 2, 3] # median at position 1
    list2 = [3, 2, 1] # median at position 1
    list3 = [2, 3, 1] # median at position 0
    list4 = [2, 1, 3] # median at position 0
    list5 = [3, 1, 2] # median at position 2
    list6 = [1, 3, 2] # median at position 2
    list7 = [1, 1, 1] # all values the same
    assert(median_of_three(list1, 0, 2) == 1)
    assert(median_of_three(list2, 0, 2) == 1)
    assert(median_of_three(list3, 0, 2) == 0)
    assert(median_of_three(list4, 0, 2) == 0)
    assert(median_of_three(list5, 0, 2) == 2)
    assert(median_of_three(list6, 0, 2) == 2)
    assert(median_of_three(list7, 0, 2) == 1)

def test_quicksort_end_pivot():
    unsorted_lists = list(map(list, it.permutations(range(-1, 4))))
    sorted = [-1, 0, 1, 2, 3]
    for lst in unsorted_lists:
        quicksort(lst, 0, len(lst) - 1)
        assert(lst == sorted)

def test_quicksort_median_of_three():
    unsorted_lists = list(map(list, it.permutations(range(-1, 4))))
    sorted = [-1, 0, 1, 2, 3]
    for lst in unsorted_lists:
        print(lst)
        quicksort(lst, 0, len(lst) - 1, 2)
        assert(lst == sorted)

# def test_quicksort_random():
#     unsorted_lists = list(map(list, it.permutations(range(-1, 4))))
#     sorted = [-1, 0, 1, 2, 3]
#     for lst in unsorted_lists:
#         quicksort(lst, 0, len(lst) - 1, 3)
#         assert(lst == sorted)