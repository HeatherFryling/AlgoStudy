from matrix_path2 import *

def test_matrix_path2():
    test1 = [[0, 1, 2],
            [5, 4, 3],
            [6, 7, 8]]
    ans1 = 9
    assert(ans1 == matrix_path2(test1))

    test2 = [[4, 3, 2],
            [5, 0, 1],
            [6, 7, 8]]
    ans2 = 9
    assert(ans2 == matrix_path2(test2))

    test3 = [[8, 7, 6],
            [3, 4, 5],
            [2, 1, 0]]
    ans3 = 9
    assert(ans3 == matrix_path2(test3))

    test4 = [[0, 0, 0],
            [3, 4, 0],
            [2, 1, 0]]
    ans4 = 5
    assert(ans4 == matrix_path2(test4))

    test5 = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    ans5 = 1
    assert(ans5 == matrix_path2(test5))