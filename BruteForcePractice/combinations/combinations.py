# Heather Fryling
# 4/21/2021

# The purpose of this file is to practice brute force algorithms that
# cycle through all possible combinations of elements in an array.

# Starting off with my Python implementation of Java code found at
# https://www.baeldung.com/java-combinations-algorithm, just to get
# a feel for how the process works.

# PURPOSE
# Generate a list of all possible combinations of values from 0 to n - 1 of
# length r.
# SIGNATURE
# generate :: Integer, Integer => List[List]
# TIME COMPLEXITY
# O(nCr)*r -- Time will be dominated by the leaves.
# SPACE COMPLEXITY
# O(n) calls on the stack.
# O(nCr) space for the combinations list.
def generate(n, r):
    combinations = []
    data = [0 for x in range(r)]
    print(data)
    helper(combinations, data, 0, n-1, 0)
    return combinations

# PURPOSE
# Recursively generate combinations based upon the cases:
#    * Base case: Once r elements are chosen, stop.
#    * Recursive cases:
#      * Take the element at start.
#      * Do not take the element at start.
def helper(combinations, data, start, end, num_chosen):
    if (num_chosen == len(data)):
        combination = data.copy()
        combinations.append(combination)
    elif (start <= end):
        # This is ok to do for both cases, because it will be overwritten if
        # num_chosen is not incremented.
        data[num_chosen] = start
        helper(combinations, data, start + 1, end, num_chosen + 1)
        helper(combinations, data, start + 1, end, num_chosen)

n = 4
r = 2
print(generate(n, r))