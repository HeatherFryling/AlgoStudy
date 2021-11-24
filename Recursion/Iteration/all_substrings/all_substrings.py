# Three ways to generate all substrings.
# All have a time complexity of
# O(n^3). The recursive functions will take
# an additional O(n) space on the call stack.

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

# Function to recursively get all
# substrings without separate functions
# for the inner and outer loops.
def all_substrings_one_recursion(s):
    res = []
    all_substrings_one(s, 0, 1, res)
    return res

def all_substrings_one(s, i, j, res):
    # If i is out of bounds, we're done.
    if i >= len(s):
        return
    # If j is out of bounds, increment i.
    if j > len(s):
        all_substrings_one(s, i + 1, i + 2, res)
        return

    res.append(s[i : j])
    all_substrings_one(s, i, j + 1, res)