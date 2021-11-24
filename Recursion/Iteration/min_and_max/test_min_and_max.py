from min_and_max import min_and_max

def test_min_and_max():
    test1 = [3, 2, 1, -4, 12, 16, -5, 21]
    ans1 = [-5, 21]
    assert(ans1 == min_and_max(test1))