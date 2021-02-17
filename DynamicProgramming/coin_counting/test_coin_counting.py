from coin_counting import *

def test_iterative():
    test1 = 4.31
    values1 = [1, 5, 10, 25]
    assert(18 == coin_counting(values1, test1))

def test_recursive():
    test1 = 4.31
    values1 = [1, 5, 10, 25]
    assert(18 == coin_counting_top_down(values1, test1))