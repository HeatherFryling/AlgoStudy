# Two ways to generate all substrings.
# Both have a time complexity of
# O(n^3). The recursive function will take
# an O(n) space on the call stack.

# Given a string, s, return a list of
# all its substrings.
def all_substrings(s):
    res = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            res.append(s[i : j])
    return res

# Given a string, s, return a list of
# all its substrings.
def all_recursive_substrings(s):
    res = []
    outer_loop(0, s, res)
    return res

# Helper function to recursively run
# the outer loop of all_recursive_substrings.
def outer_loop(i, s, res):
    if i > len(s) - 1:
        return
    inner_loop(i, i + 1, s, res)
    outer_loop(i + 1, s, res)

# Helper function to recursively run
# the inner loop of all_recursive_substrings.
def inner_loop(i, j, s, res):
    if j > len(s):
        return
    res.append(s[i : j])
    inner_loop(i, j + 1, s, res)