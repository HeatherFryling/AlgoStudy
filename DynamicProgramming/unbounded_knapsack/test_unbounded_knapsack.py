from unbounded_knapsack import *

def test_iterative():
    v1 = [1]
    w1 = [4]
    c1 = 4
    ans1 = unbounded_knapsack(v1, w1, c1)
    assert(1 == ans1)

    v2 = [1]
    w2 = [1]
    c2 = 4
    ans2 = unbounded_knapsack(v2, w2, c2)
    assert(4 == ans2)

    v3 = [1, 3]
    w3 = [1, 2]
    c3 = 4
    ans3 = unbounded_knapsack(v3, w3, c3)
    assert(6 == ans3)

    v4 = [1, 3, 2]
    w4 = [1, 2, 1]
    c4 = 4
    ans4 = unbounded_knapsack(v4, w4, c4)
    assert(8 == ans4)

def test_recursive():
    v1 = [1]
    w1 = [4]
    c1 = 4
    ans1 = unbounded_knapsack_recursive(v1, w1, c1)
    assert(1 == ans1)

    v2 = [1]
    w2 = [1]
    c2 = 4
    ans2 = unbounded_knapsack_recursive(v2, w2, c2)
    assert(4 == ans2)

    v3 = [1, 3]
    w3 = [1, 2]
    c3 = 4
    ans3 = unbounded_knapsack_recursive(v3, w3, c3)
    assert(6 == ans3)

    v4 = [1, 3, 2]
    w4 = [1, 2, 1]
    c4 = 4
    ans4 = unbounded_knapsack_recursive(v4, w4, c4)
    assert(8 == ans4)