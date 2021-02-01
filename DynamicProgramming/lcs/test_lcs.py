from lcs import *

def test_iterative():
    test1a = [3, 5, 1, 2, 4]
    test1b = [10, 1, 3, 5, 4]
    len1a = len(test1a)
    len1b = len(test1b)
    ans_length = 3
    ans = [3, 5, 4]
    dp1 = lcs_iterative(test1a, test1b)
    assert(ans_length == dp1[len1a][len1b])
    assert(ans == lcs_reconstruction(test1a, test1b, dp1))

def test_recursive():
    test1a = [3, 5, 1, 2, 4]
    test1b = [10, 1, 3, 5, 4]
    len1a = len(test1a)
    len1b = len(test1b)
    ans_length = 3
    ans = [3, 5, 4]
    dp1 = lcs_recursive(test1a, test1b)
    assert(ans_length == dp1[len1a][len1b])
    assert(ans == lcs_reconstruction(test1a, test1b, dp1))