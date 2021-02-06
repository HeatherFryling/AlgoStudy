# Heather Fryling
# 2/2/2021
# 01 Knapsack Algo Implementation

# PURPOSE
# Construct a dp array for a bottom up implementation, n + 1 rows by c + 1
# columns, all with values set to 0.
# SIGNATURE
# construct_ dp :: Integer, Integer => List[List]
def construct_dp(n, c):
    dp = []
    for i in range(n + 1):
        dp.append([])
        for _ in range(c + 1):
            dp[i].append(0)
    return dp

# PURPOSE
# Given a list of values and list of weights for objects plus the capacity, c,
# of a bag, return a dp array in which dp[n][c] contains the maximum value
# that can be selected from the list.
# SIGNATURE
# knapsack :: List, List, Integer => List[List]
# TIME COMPLEXITY
# O(nc)
# SPACE COMPLEXITY
# O(nc)
def knapsack(values, weights, c):
    # Base case: Weight of nothing is nothing, Value of nothing is also nothing.
    # Recursion:
    # f(0, 0) = 0
    # f(i, j) = max(value[i] + f(i - 1, capacity - weights[i]), f(i - 1))
    n = len(values)
    dp = construct_dp(n, c)
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            dp[i][j] = dp[i - 1][j]
            if (weights[i - 1] <= j):
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]],\
                    dp[i][j])
    return dp

# PURPOSE
# Construct a dp array for a top down implementation, n + 1 rows by c + 1
# columns, all base cases set to 0 and all other values -1.
# SIGNATURE
# construct_ dp_memo :: Integer, Integer => List[List]
def construct_dp_memo(values, c):
    dp = []
    n = len(values)
    dp.append([])
    for _ in range(c + 1):
        dp[0].append(0)
    for i in range(1, n + 1):
        dp.append([])
        dp[i].append(0)
        for _ in range(0, c):
            dp[i].append(-1)
    return dp

# PURPOSE
# Helper method for recursive implementation of knapsack.
# SIGNATURE
# knapsack_helper :: List, List, Integer, Integer, List[List]
def knapsack_helper(values, weights, i, j, dp):
    if i == 0 or j == 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = knapsack_helper(values, weights, i - 1, j, dp)
    if weights[i - 1] <= j:
        dp[i][j] = max(dp[i][j], knapsack_helper(values, weights, i - 1, j - weights[i - 1], dp) + values[i - 1])
    return dp[i][j]

# PURPOSE
# Given a list of values and list of weights for objects plus the capacity, c,
# of a bag, return a dp array in which dp[n][c] contains the maximum value
# that can be selected from the list.
# SIGNATURE
# knapsack_top_down :: List, List, Integer => List[List]
# TIME COMPLEXITY
# O(nc)
# SPACE COMPLEXITY
# O(nc)
def knapsack_top_down(values, weights, c):
    dp = construct_dp_memo(values, c)
    knapsack_helper(values, weights, len(weights), c, dp)
    return dp

# PURPOSE
# Reconstruct the indices of the items that yield the maximum total value
# from a knapsack dp matrix.
# SIGNATURE
# reconstruct_items :: List, List, List[List] => List
# TIME COMPLEXITY
# O(n) -- we check each row once.
# SPACE COMPLEXITY
# O(n) -- for the list of items.
def reconstruct_items(values, weights, dp):
    n = len(dp) - 1
    c = len(dp[0]) - 1
    i = n
    j = c
    items = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j - weights[i - 1]] + values[i - 1]:
            items.append(i - 1)
            j -= weights[i - 1]
            i -= 1
        else:
            i -= 1
    items.reverse()
    return items