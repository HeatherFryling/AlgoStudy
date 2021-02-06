from knapsack01 import *

# Test cases come from Grokking Algorithms by Aditya Y. Bhargava.

def test_knapsack():
    v1 = [1500, 3000, 2000]
    w1 = [1, 4, 3]
    c1 = 4
    assert(3500 == knapsack(v1, w1, c1)[len(v1)][c1])

    v2 = [1500, 3000, 2000, 2000]
    w2 = [1, 4, 3, 1]
    c2 = 4
    assert(4000 == knapsack(v2, w2, c2)[len(v2)][c2])

def test_knapsack_top_down():
    v1 = [1500, 3000, 2000]
    w1 = [1, 4, 3]
    c1 = 4
    assert(3500 == knapsack_top_down(v1, w1, c1)[len(v1)][c1])

    v2 = [1500, 3000, 2000, 2000]
    w2 = [1, 4, 3, 1]
    c2 = 4
    assert(4000 == knapsack_top_down(v2, w2, c2)[len(v2)][c2])

def test_reconstruction():
    v1 = [1500, 3000, 2000]
    w1 = [1, 4, 3]
    c1 = 4
    dp1 = knapsack(v1, w1, c1)
    assert([0, 2] == reconstruct_items(v1, w1, dp1))

    v2 = [1500, 3000, 2000, 2000]
    w2 = [1, 4, 3, 1]
    c2 = 4
    dp2 = knapsack(v2, w2, c2)
    assert([2, 3] == reconstruct_items(v2, w2, dp2))

def test_reconstruction_top_down():
    v1 = [1500, 3000, 2000]
    w1 = [1, 4, 3]
    c1 = 4
    dp1 = knapsack_top_down(v1, w1, c1)
    assert([0, 2] == reconstruct_items(v1, w1, dp1))

    v2 = [1500, 3000, 2000, 2000]
    w2 = [1, 4, 3, 1]
    c2 = 4
    dp2 = knapsack_top_down(v2, w2, c2)
    assert([2, 3] == reconstruct_items(v2, w2, dp2))