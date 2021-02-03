from lcs import *

def test_iterative():
    test1a = [3, 5, 1, 2, 4]
    test1b = [10, 1, 3, 3, 5, 4]
    len1a = len(test1a)
    len1b = len(test1b)
    ans1_length = 3
    ans1 = [3, 5, 4]
    dp1 = lcs_iterative(test1a, test1b)
    assert(ans1_length == dp1[len1a][len1b])
    assert(ans1 == lcs_reconstruction(test1a, test1b, dp1))

    test2a = [1, 0, 0, 1, 0, 1, 0, 1]
    test2b = [0, 1, 0, 1, 1, 0, 1, 1, 0]
    len2a = len(test2a)
    len2b = len(test2b)
    ans2_length = 6
    ans2 = [0, 1, 0, 1, 0, 1]
    dp2 = lcs_iterative(test2a, test2b)
    assert(ans2_length == dp2[len2a][len2b])
    assert(ans2 == lcs_reconstruction(test2a, test2b, dp2))

def test_recursive():
    test1a = [3, 5, 1, 2, 4]
    test1b = [10, 1, 3, 3, 5, 4]
    len1a = len(test1a)
    len1b = len(test1b)
    ans_length = 3
    ans = [3, 5, 4]
    dp1 = lcs_recursive(test1a, test1b)
    assert(ans_length == dp1[len1a][len1b])
    assert(ans == lcs_reconstruction(test1a, test1b, dp1))

    test2a = [1, 0, 0, 1, 0, 1, 0, 1]
    test2b = [0, 1, 0, 1, 1, 0, 1, 1, 0]
    len2a = len(test2a)
    len2b = len(test2b)
    ans2_length = 6
    ans2 = [0, 1, 0, 1, 0, 1]
    dp2 = lcs_recursive(test2a, test2b)
    assert(ans2_length == dp2[len2a][len2b])
    assert(ans2 == lcs_reconstruction(test2a, test2b, dp2))

def test_space_optimized():
    test1a = [3, 5, 1, 2, 4]
    test1b = [10, 1, 3, 3, 5, 4]
    len1a = len(test1a)
    len1b = len(test1b)
    ans_length = 3
    assert(ans_length == lcs_space_optimized(test1a, test1b))

    test2a = [1, 0, 0, 1, 0, 1, 0, 1]
    test2b = [0, 1, 0, 1, 1, 0, 1, 1, 0]
    len2a = len(test2a)
    len2b = len(test2b)
    ans2_length = 6
    assert(ans2_length == lcs_space_optimized(test2a, test2b))