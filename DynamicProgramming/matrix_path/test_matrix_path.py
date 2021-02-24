from matrix_path import *

def test_iterative():
    test1 = [[5, 1, 2],
            [3, 7, 1],
            [4, 5, 6]]
    ans1 = 4
    assert(ans1 == matrix_path(test1))

    test2 = [[5, 8, 2],
            [3, 7, 1],
            [4, 5, 6]]
    ans2 = 4
    assert(ans2 == matrix_path(test2))

    test3 = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    ans3 = 1
    assert(ans3 == matrix_path(test3))

def test_recursive():
    test1 = [[5, 1, 2],
            [3, 7, 1],
            [4, 5, 6]]
    ans1 = 4
    assert(ans1 == matrix_path_td(test1))

    test2 = [[5, 8, 2],
            [3, 7, 1],
            [4, 5, 6]]
    ans2 = 4
    assert(ans2 == matrix_path_td(test2))

    test3 = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    ans3 = 1
    assert(ans3 == matrix_path_td(test3))