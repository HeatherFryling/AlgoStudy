from flatten_array import flatten

def test_flatten():
    arr = [[1,2,3], [4, 5], [6], [], [7, 8, 9, 10]]
    ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert(ans == flatten(arr))