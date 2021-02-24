# Heather Fryling
# 2/23/2021

# PURPOSE
# Initialize an m x n matrix with all val.
# SIGNATURE
# initialize_dp :: Integer, Integer, Integer => List[List]
def initialize_dp(m, n, val):
    dp = []
    for i in range(m):
        dp.append([])
        for _ in range(n):
            dp[i].append(val)
    return dp

# PURPOSE
# Given a matrix of positive integers, return the max value.
# SIGNATURE
# get_max :: List[List] => Integer
def get_max(matrix):
    max = float('-inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max:
                max = matrix[i][j]
    return max

# PURPOSE
# Given a matrix of positive integers, determine the length of the longest
# increasing path if the path can start anywhere and can move down or right.
# SIGNATURE
# matrix_path :: List[List] => Integer
# TIME COMPLEXITY
# O(mn)
# SPACE COMPLEXITY
# O(mn)
def matrix_path(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = initialize_dp(m, n, 0)
    # First base case. If we start at the upper left and end in the upper left,
    # we can only move one square.
    dp[0][0] = 1
    # Second base case. With the upper left square filled in, we can fill in
    # the first column.
    for i in range(0, m):
        if matrix[i - 1][0] < matrix[i][0]:
            dp[i][0] = 1 + dp[i - 1][0]
        else:
            dp[i][0] = 1
    # Third base case. With the upper left square filled in, we can fill in
    # the first row.
    for j in range(0, n):
        if matrix[0][j - 1] < matrix[0][j]:
            dp[0][j] = 1 + dp[0][j - 1]
        else:
            dp[0][j] = 1
    # Now we can fill in the rest of the table.
    for i in range(1, n):
        for j in range(1, n):
            above = dp[i - 1][j] + 1 if matrix[i- 1][j] < matrix[i][j] else 1
            left = dp[i][j - 1] + 1 if matrix[i][j - 1] < matrix[i][j] else 1
            dp[i][j] = max(above, left)
    return get_max(dp)

# PURPOSE
# Helper function for top-down implementation of matrix path.
# SIGNATURE
# matrix_helper :: List[List], Integer, Integer, List[List]
def matrix_helper(matrix, i, j, dp):
    if i == 0 and j == 0:
        return 1
    if i == 0:
        val = 1
        if matrix[i][j - 1] < matrix[i][j]:
            val += matrix_helper(matrix, i, j - 1, dp)
        dp[i][j] = val
        return val
    if j == 0:
        val = 1
        if matrix[i - 1][j] < matrix[i][j]:
            val += matrix_helper(matrix, i - 1, j, dp)
        dp[i][j] = val
        return val
    if dp[i][j] != -1:
        return dp[i][j]
    above = 1 + matrix_helper(matrix, i - 1, j, dp)
    if matrix[i- 1][j] >= matrix[i][j]:
        above = 0
    left = 1 + matrix_helper(matrix, i, j - 1, dp)
    if matrix[i][j - 1] >= matrix[i][j]:
        left = 0
    dp[i][j] = max(above, left, 1)
    return dp[i][j]

# PURPOSE
# Given a matrix of positive integers, determine the length of the longest
# increasing path if the path can start anywhere and can move down or right.
# Top-down implementation.
# SIGNATURE
# matrix_path_td :: List[List] => Integer
# TIME COMPLEXITY
# O(mn)
# SPACE COMPLEXITY
# O(mn)
def matrix_path_td(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = initialize_dp(m, n, -1)
    matrix_helper(matrix, m - 1, n - 1, dp)
    return get_max(dp)
