# Heather Fryling
# 2/16/2021

CENTS_PER_DOLLAR = 100

# Given an array of available values for coins and an infinite supply of 
# each coin type, determine if it is possible to make change for a given target
# amount using at most k coins.

# PURPOSE
# Given an array of available values for coins and an infinite supply of 
# each coin type, calculate the minimum number of coins to make change for
# a specified amount, then return whether or not that minimum is less than
# or equal to k.
# Targets are in collar amounts and coin amounts are in cents.
# SIGNATURE
# coin_counting :: List, Float, Integer => Boolean
# TIME COMPLEXITY
# O(n*t)
# SPACE COMPLEXITY
# O(t)
def coin_counting(values, target, k):
    dp = []
    t = target * CENTS_PER_DOLLAR
    t = int(t)
    for _ in range(t + 1):
        dp.append(0)
    for i in range(1, t + 1):
        dp[i] = float('inf')
        for j in range(0, len(values)):
            if values[j] <= i:
                dp[i] = min(dp[i], 1 + dp[i - values[j]])
    return dp[t] <= k

# PURPOSE
# Helper method for the top-down implementation of coin counting.
# SIGNATURE
# coin_helper :: Integer, Integer, List => Integer
def coin_helper(values, t, i, dp):
    if i == 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    dp[i] = float('inf')
    for j in range(len(values)):
        if values[j] <= i:
            dp[i] = min(dp[i], 1 + coin_helper(values, t, i - values[j], dp))
    return dp[i]

# PURPOSE
# Given an array of available values for coins and an infinite supply of 
# each coin type, calculate the minimum number of coins to make change for
# a specified amount, then return whether or not that minimum is less than
# or equal to k.
# Targets are in collar amounts and coin amounts are in cents.
# This version uses a top-down approach.
# SIGNATURE
# coin_counting :: List, Float => Integer
# TIME COMPLEXITY
# O(n*t)
# SPACE COMPLEXITY
# O(t)
def coin_counting_top_down(values, target, k):
    dp = []
    t = target * CENTS_PER_DOLLAR
    t = int(t)
    for _ in range(t + 1):
        dp.append(-1)
    ans = coin_helper(values, t, t, dp)
    return ans <= k