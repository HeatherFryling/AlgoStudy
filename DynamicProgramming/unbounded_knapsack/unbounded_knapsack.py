# Heather Fryling
# 2/5/2021

# PURPOSE
# Given a list of values and weights for n types of items and given that the
# items are available in unlimited quantities, calculate the maximum value
# of a selection of items that fits within capacity c.
# SIGNATURE
# unbounded_knapsack :: List, List, Integer => Integer
# TIME COMPLEXITY
# O(nc)
# SPACE COMPLEXITY
# O(c)
def unbounded_knapsack(values, weights, c):
    max_so_far = []
    # Max value from 0 items is 0
    max_so_far.append(0)
    for i in range(1, c + 1):
        curr_max = 0
        for j in range(len(values)):
            curr_val = 0
            if weights[j] <= i:
                curr_val = values[j] + max_so_far[i - weights[j]]
                if curr_val > curr_max:
                    curr_max = curr_val
        max_so_far.append(curr_max)
    return max_so_far[c]

# PURPOSE
# Helper method for unbounded_knapsack_recursive.
# SIGNATURE
# unbounded_knapsack_helper :: List, List, Integer, Dictionary => Integer
def unbounded_knapsack_helper(values, weights, i, dp):
    if i == 0:
        return 0
    if i in dp.keys():
        return dp[i]
    curr_max = 0
    for j in range(len(values)):
        if weights[j] <= i:
            curr_val = values[j] + unbounded_knapsack_helper(values, \
                weights, i - weights[j], dp)
            if curr_val > curr_max:
                curr_max = curr_val
    return curr_max

# PURPOSE
# Given a list of values and weights for n types of items and given that the
# items are available in unlimited quantities, calculate the maximum value
# of a selection of items that fits within capacity c.
# This implementation is recursive using memoization.
# SIGNATURE
# unbounded_knapsack :: List, List, Integer => Integer
# TIME COMPLEXITY
# O(nc) Recursive implementation has the potential to reduce this quite a bit
# since it will only calculate answers for values of c that are needed.
# SPACE COMPLEXITY
# O(c) Also potentially much lower, since it will only contain entries for
# values of c that are possible with the given combination of items.
def unbounded_knapsack_recursive(values, weights, c):
    return unbounded_knapsack_helper(values, weights, c, {})