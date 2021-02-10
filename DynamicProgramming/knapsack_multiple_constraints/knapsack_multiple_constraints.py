# Heather Fryling
# 2/10/2021

# Implementation of the knapsack with multiple constraints algorithm.
# This is 01 knapsack in 3D to accomodate, two constraints rather than
# just one.

# PURPOSE
# Helper function to construct a 3d dp matrix for knapsack with multiple
# constraints with all values initialized to 0.
# SIGNATURE
# construct_dp :: Integer, Integer, Integer => List[List[List[Integer]]]
# TIME COMPLEXITY
# O(n*max_w*max_s)
# SPACE COMPLEXITY
# O(n*max_w*max_s)
def construct_dp(n, max_w, max_s):
    dp = []
    for i in range(n + 1):
        dp.append([])
        for j in range(max_w + 1):
            dp[i].append([])
            for _ in range(max_s + 1):
                dp[i][j].append(0)
    return dp

# PURPOSE
# Given an array of weights, sizes and values, calculate the maximum
# value that can be achieved with exceeding the maximum weight, max_w or
# the maximum size, max_s.
# SIGNATURE
# knapsack_multiple_constraints :: List, List, List, Integer, Integer =>
# Integer (could also be Double if values are Doubles)
# TIME COMPLEXITY
# O(n*max_w*max_s)
# SPACE COMPLEXITY
# O(n*max_w*max_s) -- for the dp array
def knapsack_multiple_constraints(weights, sizes, values, max_w, max_s):
    n = len(weights)
    dp = construct_dp(n, max_w, max_s)
    for i in range(1, n + 1):
        for w in range(1, max_w + 1):
            for s in range(1, max_s + 1):
                if sizes[i - 1] <= s and weights[i - 1] <= w:
                    dp[i][w][s] = max(values[i - 1] + \
                        dp[i - 1][w - weights[i - 1]][s - sizes[i - 1]],
                        dp[i - 1][w][s])
                else:
                    dp[i][w][s] = dp[i - 1][w][s]
    return dp[n][max_w][max_s]

# PURPOSE
# Helper function for recursive implementation of knapsack with multiple
# constraints.
# SIGNATURE
# top_down_helper :: List, List, List, Integer, Integer, Integer, Dictionary
# => Integer (or Double if values are Doubles)
def top_down_helper(weights, sizes, values, i,  w, s, dp):
    if i == 0:
        return 0
    if w == 0:
        return 0
    if s == 0:
        return 0
    if (i, w, s) in dp.keys():
        return dp[(i, w, s)]
    prev = top_down_helper(weights, sizes, values, i - 1, w, s, dp)
    if weights[i - 1] <= w and sizes[i - 1] <= s:
        curr = values[i - 1] + \
            top_down_helper(weights, sizes, values, i - 1, \
                w - weights[i - 1], s - sizes[i - 1], dp)
        dp[(i, w, s)] = max(curr, prev)
    else:
        dp[(i, w, s)] = prev
    return dp[(i, w, s)]

# PURPOSE
# Top-down implementation of knapsack with multiple constraints. Saves space
# by using a dictionary instead of a whole dp array. Whether or not the
# dictionary is worth the overhead will depend on the implementation.
# SIGNATURE
# knapsack_mult_top_down :: List, List, List, Integer, Integer => Integer
# (or Double if values are doubles)
# TIME COMPLEXITY
# O(n*max_w*max_s)
# SPACE COMPLEXITY
# O(n*max_w*max_s)
def knapsack_mult_top_down(weights, sizes, values, max_w, max_s):
    dp = {}
    return top_down_helper(weights, sizes, values, len(values), \
        max_w, max_s, dp)