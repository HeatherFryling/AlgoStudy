from matrix_chain import *

def test_iterative():
    # Unused A arrays show the dimensions of the individual matrices.
    A1 = [(100, 2), (2, 100), (100, 10)]
    test1 = [100, 2, 100, 10]
    ans1 = matrix_chain(test1)
    assert(4000 == ans1)

    A2 = [(10, 2), (2, 10), (10, 100), (100, 10)]
    test2 = [10, 2, 10, 100, 10]
    ans2 = matrix_chain(test2)
    assert(4200 == ans2)

def test_recursive():
    # Unused A arrays show the dimensions of the individual matrices
    A1 = [(100, 2), (2, 100), (100, 10)]
    test1 = [100, 2, 100, 10]
    ans1 = matrix_chain_top_down(test1)
    assert(4000 == ans1)

    A2 = [(10, 2), (2, 10), (10, 100), (100, 10)]
    test2 = [10, 2, 10, 100, 10]
    ans2 = matrix_chain_top_down(test2)
    assert(4200 == ans2)