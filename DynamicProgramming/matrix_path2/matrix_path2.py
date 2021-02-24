# Heather Fryling
# 2/23/2021

# PURPOSE
# Helper function to initialize an m x n matrix with all values set to val.
# SIGNATURE
# initialize_dp :: Integer, Integer, Integer => List[List]
def initialize_dp(m, n, val):
    dp = []
    for i in range(n):
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
# Helper function for matrix_path2.
# SIGNATURE
# matrix_helper2 :: List[List], Integer, Integer, dp
def matrix_helper2(matrix, i, j, dp):
    if dp[i][j] != -1:
        return dp[i][j]
    m = len(matrix)
    n = len(matrix[0])
    val = 1
    if (i - 1) >= 0 and matrix[i - 1][j] < matrix[i][j]:
        val = max(val, 1 + matrix_helper2(matrix, i - 1, j, dp))
    if (j - 1) >= 0 and matrix[i][j - 1] < matrix[i][j]:
        val = max(val, 1 + matrix_helper2(matrix, i, j - 1, dp))
    if (i + 1) <= (m - 1) and matrix[i + 1][j] < matrix[i][j]:
        val = max(val, 1 + matrix_helper2(matrix, i + 1, j, dp))
    if (j + 1) <= (n - 1) and matrix[i][j + 1] < matrix[i][j]:
        val = max(val, 1 + matrix_helper2(matrix, i, j + 1, dp))
    dp[i][j] = val
    return val

# PURPOSE
# Given a matrix of positive integers, return the length of the longest
# increasing path where a path may start anywhere and legal moves are up,
# down, left, and right.
# This is implemented top-down, because it is difficult to write out iteratively
# exactly where to start and to make sure every square gets calculated.
# SIGNATURE
# matrix_helper2 :: List[List], Integer, Integer, List[List]
# TIME COMPLEXITY
# O(mn) -- Thanks to dp guarding against recalculating values.
# SPACE COMPLEXITY
# O(mn) for the dp matrix
def matrix_path2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = initialize_dp(m, n, -1)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_helper2(matrix, i, j, dp)
    return get_max(dp)