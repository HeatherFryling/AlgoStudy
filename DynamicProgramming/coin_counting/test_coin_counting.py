from coin_counting import *

def test_iterative():
    test1 = 4.31
    values1 = [1, 5, 10, 25]
    k1_t = 18
    k1_f = 17
    assert(True == coin_counting(values1, test1, k1_t))
    assert(False == coin_counting(values1, test1, k1_f))

    values2 = [5, 10]
    test2_t = 0.55
    test2_f = 0.65
    k2 = 6
    assert(True == coin_counting(values2, test2_t, k2))
    assert(False == coin_counting(values2, test2_f, k2))

    # Making sure the algorithm returns false when no number of the given
    # denominations will fulfill the requirement.
    values3 = [7, 15]
    test3_impossible = 0.10
    k3 = 1000
    assert(False == coin_counting(values3, test3_impossible, k3))

def test_recursive():
    test1 = 4.31
    values1 = [1, 5, 10, 25]
    k1_t = 18
    k1_f = 17
    assert(True == coin_counting_top_down(values1, test1, k1_t))
    assert(False == coin_counting_top_down(values1, test1, k1_f))

    values2 = [5, 10]
    test2_t = 0.55
    test2_f = 0.65
    k2 = 6
    assert(True == coin_counting_top_down(values2, test2_t, k2))
    assert(False == coin_counting_top_down(values2, test2_f, k2))

    # Making sure the algorithm returns false when no number of the given
    # denominations will fulfill the requirement.
    values3 = [7, 15]
    test3_impossible = 0.10
    k3 = 1000
    assert(False == coin_counting_top_down(values3, test3_impossible, k3))