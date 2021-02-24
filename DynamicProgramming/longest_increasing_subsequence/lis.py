# Heather Fryling
# 2/18/2021

# PURPOSE
# Given a sequence of integers, return the length of the longest increasing
# subsequence.
# SIGNATURE
# longest_increasing_subsequence :: List => Integer
# TIME COMPLEXITY
# O(n^2)
# SPACE COMPLEXITY
# O(n)
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = []
    for i in range(n):
        dp.append(0)
    dp[0] = 1
    for i in range(1, n):
        dp[i] = dp[i - 1]
        for j in range((i - 1), -1, -1):
            if arr[j] < arr[i]:
                dp[i] = max(1 + dp[j], dp[i])
    print(dp)
    return dp[n - 1]


# PURPOSE
# Helper function for top-down lis.
# SIGNATURE
# lis_helper :: List, Integer, List => Integer
def lis_helper(arr, i, dp):
    if i == 0:
        dp[0] = 1
        return 1
    if dp[i] != -1:
        return dp[i]
    curr = lis_helper(arr, i - 1, dp)
    for j in range((i - 1), -1, -1):
        if arr[j] < arr[i]:
            curr = max(1 + lis_helper(arr, j, dp), curr)
    dp[i] = curr
    return dp[i]

# PURPOSE
# Given a sequence of integers, return the length of the longest increasing
# subsequence.
# This implementation uses a top-down approach.
# SIGNATURE
# lis_top_down :: List => Integer
# TIME COMPLEXITY
# O(n^2)
# SPACE COMPLEXITY
# O(n)
def lis_top_down(arr):
    n = len(arr)
    dp = []
    for _ in range(n):
        dp.append(-1)
    return lis_helper(arr, n - 1, dp)