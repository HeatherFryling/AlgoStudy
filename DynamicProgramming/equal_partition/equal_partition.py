# Heather Fryling
# 2/25/2021

# PURPOSE
# Helper function to determine if an array of integers can be divided into two 
# subsets of equal sum using brute force recursion.
# This is actually a knapsack problem looking for a specific value, that value
# being total / 2, since if we can fill one knapsack with total / 2, the
# leftover values will also sum to total / 2.
# SIGNATURE
# brute_force_helper :: List, Integer, Integer => Boolean
# TIME COMPLEXITY
# O(2^n) -- branching factor of 2 at each recursive call over n recursive 
# calls.
# SPACE COMPLEXITY
# O(n) calls on the stack at any given time.
def brute_force_helper(arr, sum, i):
    # This means we subtracted enough values from total for the
    # total subtraction to be total / 2, the target we're looking for.
    if sum == 0:
        return True
    # This means the items we selected sum to more than half the total.
    if sum < 0:
        return False
    # If the array is empty or we've stepped beyond the end of the array,
    # we've determined that we cannot arrive at total / 2.
    if len(arr) == 0 or i >= len(arr):
        return False
    # There are two options: Either the number at i is in the subset that
    # totals the sum, or it is not.
    return brute_force_helper(arr, sum - arr[i], i + 1) or \
        brute_force_helper(arr, sum, i + 1)

# PURPOSE
# Function to determine if an array of integers can be divided into two 
# subsets of equal sum using brute force recursion.
# SIGNATURE
# brute_force_helper :: List => Boolean
# TIME COMPLEXITY
# O(2^n) -- branching factor of 2 at each recursive call over n recursive 
# calls.
# SPACE COMPLEXITY
# O(n) calls on the stack at any given time.
def equal_brute_force(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False
    return brute_force_helper(arr, total / 2, 0)

# PURPOSE
# Helper method for recursive implementation of equal_partition with
# memoization.
# SIGNATURE
# memo_helper :: List, Integer, Integer, List[List] => Boolean
def memo_helper(arr, i, sum, dp):
    if sum == 0:
        return True
    if sum < 0:
        return False
    if i >= len(arr) or len(arr) == 0:
        return False
    if dp[i][sum] != None:
        return dp[i][sum]
    dp[i][sum] = memo_helper(arr, i + 1, sum - arr[i], dp) \
        or memo_helper(arr, i + 1, sum, dp)
    return dp[i][sum]

# PURPOSE
# Function to determine if an array of integers can be divided into two 
# subsets of equal sum using brute force recursion.
# This is a top-down implementation with memoization and is identical to 
# 0-1 knapsack.
# SIGNATURE
# memo_2_partition :: List => Boolean
# TIME COMPLEXITY
# O(n * total) -- thanks to memoization guarding against repeated calls
# calls.
# SPACE COMPLEXITY
# O(n * total) -- for the dp array
def memo_2_partition(arr):
    total = sum(arr)
    dp = []
    for i in range(len(arr)):
        dp.append([])
        for _ in range(int(total / 2) + 1):
            dp[i].append(None)
    if total % 2 != 0:
        return False
    ans = memo_helper(arr, 0, int(total / 2), dp)
    for i in range(len(dp)):
        print(dp[i])
    return ans

# PURPOSE
# Function to determine if an array of integers can be divided into two 
# subsets of equal sum using brute force recursion.
# This is a bottom-up implementation with dynamic programming and is identical 
# to 0-1 knapsack.
# SIGNATURE
# equal_partition_it :: List => Boolean
# TIME COMPLEXITY
# O(n * total) -- thanks to memoization guarding against repeated calls
# calls.
# SPACE COMPLEXITY
# O(n * total) -- for the dp array
def equal_partition_it(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False
    p_sum = int(total / 2)
    dp = []
    for i in range(len(arr)):
        dp.append([])
        for _ in range(p_sum + 1):
            dp[i].append(False)
    # Base cases.
    for i in range(len(arr)):
        dp[i][0] = True
    for j in range(1, p_sum + 1):
        dp[0][j] = True if arr[0] == j else False
    # Recursive cases.
    for i in range(1, len(arr)):
        for j in range(1, p_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i]]
    return dp[len(arr) - 1][p_sum]