# Heather Fryling
# 2/23/2021

# PURPOSE
# Given a set of integers and a target, return whether or not the set
# contains a subset whose sum equals the target.
# SIGNATURE
# subset_sum :: List, Integer => Boolean
# TIME COMPLEXITY
# O(n*target)
# SPACE COMPLEXITY
# O(n * target)
def subset_sum(arr, target):
    n = len(arr)
    dp = []
    for i in range(n + 1):
        dp.append([])
        for _ in range(target + 1):
            dp[i].append(False)
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for t in range(1, target + 1):
            curr = arr[i - 1]
            # If the current value is less than or equal to the target, we can
            # check to see if there's a prior calculation that will add us up
            # to the target.
            if curr <= t:
                dp[i][t] = dp[i - 1][t - curr]
            # We also need to check in each row if we already found a subset
            # that reaches the target in the prior row.
            dp[i][t] = dp[i][t] or dp[i - 1][t]
    return dp[n][target]

# PURPOSE
# Helper for top-down subset sum.
# SIGNATURE
# s_s_helper :: List, Integer, Integer, List => Boolean
def s_s_helper(arr, i, t, dp):
    if t == 0:
        return True
    if i == 0:
        return False
    if dp[i][t] != None:
        return dp[i][t]
    if arr[i - 1] <= t:
        prev = s_s_helper(arr, i - 1, t, dp)
        curr = s_s_helper(arr, i - 1, t - arr[i - 1], dp)
        dp[i][t] =  prev or curr
    else:
        dp[i][t] = s_s_helper(arr, i - 1, t, dp)
    return dp[i][t]

# PURPOSE
# Given a set of integers and a target, return whether or not the set
# contains a subset whose sum equals the target.
# Top-down implementation.
# SIGNATURE
# subset_sum_top_down :: List, Integer => Boolean
# TIME COMPLEXITY
# O(n*target)
# SPACE COMPLEXITY
# O(n * target)
def subset_sum_top_down(arr, target):
    n = len(arr)
    dp = []
    for i in range(n + 1):
        dp.append([])
        for _ in range(target + 1):
            dp[i].append(None)
    return s_s_helper(arr, n, target, dp)
