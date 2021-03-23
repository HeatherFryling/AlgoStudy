# Heather Fryling
# 2/10/2021
# Program to determine the optimal order for matrix chain multiplication to
# minimize the cost of the multiplications.

# PURPOSE
# Construct a dp matrix for the iterative version of the matrix chain
# multiplication algorithm.
# SIGNATURE
# construct_dp :: Integer => List[List]
def construct_dp(n):
    dp = []
    for i in range(n):
        dp.append([])
        for _ in range(n):
            dp[i].append(0)
    return dp

# PURPOSE
# Determine the minimum number of operations to multiply all matrices specified
# by an array of sizes.
# A0 = (sizes[0], sizes[1]), A[1] = (sizes[1], sizes[2]) ...
# A(n-1) = (sizes[n - 1], sizes[n]).
# SIGNATURE
# matrix_chain :: List => Integer
# TIME COMPLEXITY
# O(n^3)
# SPACE COMPLEXITY
# O(n^2)
def matrix_chain(sizes):
    n = len(sizes) - 1
    dp = construct_dp(n)
    # Base cases
    for i in range(n):
        dp[i][i] = 0
    for i in range(n - 1):
        s = i + 1
        dp[i][i + 1] = sizes[s - 1] * sizes[s] * sizes[s + 1]
    for j in range(2, n):
        for i in range(j - 2, -1, -1):
            dp[i][j] = float('inf')
            for k in range(i, j):
                s = k + 1
                cost = sizes[i]*sizes[s]*sizes[j + 1]
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + cost)
    return dp[0][n - 1]

# PURPOSE
# Helper method for recursive matrix chain.
# SIGNATURE
# matrix_chain_helper :: List, Integer, Integer, List[List] => Integer
def matrix_chain_helper(sizes, i, j, dp):
    if i == j:
        return 0
    if dp[i][j] != float('inf'):
        return dp[i][j]
    if j == i + 1:
        return sizes[i]*sizes[i + 1]* sizes[j + 1]
    else:
        for k in range(i, j):
            cost = sizes[i] * sizes[k + 1] * sizes[j + 1]
            left = matrix_chain_helper(sizes, i, k, dp)
            right = matrix_chain_helper(sizes, k + 1, j, dp)
            dp[i][j] = min(dp[i][j], left + right + cost)
    return dp[i][j]

# PURPOSE
# Determine the minimum number of operations to multiply all matrices specified
# by an array of sizes using a recursive approach.
# A0 = (sizes[0], sizes[1]), A[1] = (sizes[1], sizes[2]) ...
# A(n-1) = (sizes[n - 1], sizes[n]).
# SIGNATURE
# matrix_chain :: List => Integer
# TIME COMPLEXITY
# O(n^3)
# SPACE COMPLEXITY
# O(n^2)
def matrix_chain_top_down(sizes):
    n = len(sizes) - 1
    dp = []
    for i in range(n):
        dp.append([])
        for _ in range(n):
            dp[i].append(float('inf'))
    ans = matrix_chain_helper(sizes, 0, n - 1, dp)
    for i in range(len(dp)):
        print(dp[i])
    return ans