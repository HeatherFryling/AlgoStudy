# Heather Fryling
# 11/8/2021

# Recursively flatten a 2D array such that for
# example [[1,2,3], [4, 5], [6], [], [7, 8, 9, 10]]
# becomes [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# This illustrates nested iteration in recursive functions.
# Time complexity is O(n * m) where n is the number of 
# rows in the 2D array and m is the max length of
# a row. Space complexity is O(n * m) for the output
# array. There is an additionaly O(m) space taken
# by the callstack.

def flatten(arr):
    res = []
    outer_loop(arr, 0, res)
    return res

def outer_loop(arr, i, res):
    if i >= len(arr):
        return

    inner_loop(arr, i, 0, res)
    outer_loop(arr, i + 1, res)

def inner_loop(arr, i, j, res):
    if j >= len(arr[i]):
        return
    res.append(arr[i][j])
    inner_loop(arr, i, j + 1, res)

arr = [[1,2,3], [4, 5], [6], [], [7, 8, 9, 10]]
print(flatten(arr))