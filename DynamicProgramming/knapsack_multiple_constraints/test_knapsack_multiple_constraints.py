from knapsack_multiple_constraints import *

def test_iterative():
    # test1 one item
    weights1 = [5]
    sizes1 = [4]
    values1 = [3]
    max_w1 = 5
    max_s1 = 4
    ans1 = knapsack_multiple_constraints(weights1, sizes1, values1, max_w1, max_s1)
    assert(3 == ans1)

    # test2 one item too heavy
    weights2 = [6]
    sizes2 = [4]
    values2 = [3]
    max_w2 = 5
    max_s2 = 4
    ans2 = knapsack_multiple_constraints(weights2, sizes2, values2, max_w2, max_s2)
    assert(0 == ans2)

    # test3 one item too big
    weights3 = [5]
    sizes3 = [5]
    values3 = [3]
    max_w3 = 5
    max_s3 = 4
    ans3 = knapsack_multiple_constraints(weights3, sizes3, values3, max_w3, max_s3)
    assert(0 == ans3)

    # two items
    # test3 one item too big
    weights4 = [2, 3]
    sizes4 = [3, 7]
    values4 = [4, 7]
    max_w4 = 5
    max_s4 = 10
    ans4 = knapsack_multiple_constraints(weights4, sizes4, values4, max_w4, max_s4)
    assert(11 == ans4)

    # drop second to get third
    weights5 = [2, 3, 2]
    sizes5 = [3, 7, 6]
    values5 = [4, 7, 8]
    max_w5 = 5
    max_s5 = 10
    ans5 = knapsack_multiple_constraints(weights5, sizes5, values5, max_w5, max_s5)
    assert(12 == ans5)

def test_recursive():
    # test1 one item
    weights1 = [5]
    sizes1 = [4]
    values1 = [3]
    max_w1 = 5
    max_s1 = 4
    ans1 = knapsack_mult_top_down(weights1, sizes1, values1, max_w1, max_s1)
    assert(3 == ans1)

    # test2 one item too heavy
    weights2 = [6]
    sizes2 = [4]
    values2 = [3]
    max_w2 = 5
    max_s2 = 4
    ans2 = knapsack_mult_top_down(weights2, sizes2, values2, max_w2, max_s2)
    assert(0 == ans2)

    # test3 one item too big
    weights3 = [5]
    sizes3 = [5]
    values3 = [3]
    max_w3 = 5
    max_s3 = 4
    ans3 = knapsack_mult_top_down(weights3, sizes3, values3, max_w3, max_s3)
    assert(0 == ans3)

    # two items
    # test3 one item too big
    weights4 = [2, 3]
    sizes4 = [3, 7]
    values4 = [4, 7]
    max_w4 = 5
    max_s4 = 10
    ans4 = knapsack_mult_top_down(weights4, sizes4, values4, max_w4, max_s4)
    assert(11 == ans4)

    # drop second to get third
    weights5 = [2, 3, 2]
    sizes5 = [3, 7, 6]
    values5 = [4, 7, 8]
    max_w5 = 5
    max_s5 = 10
    ans5 = knapsack_mult_top_down(weights5, sizes5, values5, max_w5, max_s5)
    assert(12 == ans5)