# Heather Fryling
# 2/1/2021

# PURPOSE
# Iteratively search 2 arrays for the longest common subsequence. Returns the
# dp array with the entry at dp[m][n] specifying the length of the lcs.
# SIGNATURE
# lcs_iterative :: List, List => List[List]
# TIME COMPLEXITY:
# O(m * n) -- for each call in the loop
# SPACE COMPLEXITY:
# O(m * n) -- for the dp array
def lcs_iterative(arr1, arr2):
    m = len(arr1) # rows
    n = len(arr2) # columns
    dp = []
    for i in range(m + 1):
        dp.append([])
        for j in range(n + 1):
            dp[i].append(0)
    i = 1
    while i < (m + 1):
        for j in range(1, n + 1):
            if arr1[i-1] == arr2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            if arr1[i-1] != arr2[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        i += 1
    return dp

# PURPOSE
# Calculate the length of the LCS while optimizing for space.
# SIGNATURE
# lcs_space_optimizied :: List, List => Integer
# TIME COMPLEXITY
# O(m*n)
# SPACE COMPLEXITY
# O(m) (2 arrays of length m)

def lcs_space_optimized(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    dp = []
    for i in range(2):
        dp.append([])
        for j in range(n + 1):
            dp[i].append(0)
    for i in range(1, m + 1):
        row = i % 2
        for j in range(1, n + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[row][j] = dp[(row - 1) % 2][j - 1] + 1
            else:
                dp[row][j] = max(dp[(row - 1) % 2][j], dp[row][j - 1])
    return dp[m % 2][n]

# PURPOSE
# Recursively calculate the longest common subsequence of two arrays. Returns 
# the dp array with the entry at dp[m][n] specifying the length of the LCS.
# SIGNATURE
# lcs_recurisve :: List, List => List[List]
# TIME COMPLEXITY
# O(m * n) -- It's possible we'd need to calculate every value in the dp array
# except the base cases.
# SPACE COMPLEXITY
# O(m * n) on the heap -- for the dp array.
# O(m * n) on the stack -- for the calls to calculate the entries in the array
def lcs_recursive(arr1, arr2):
    m = len(arr1) # rows
    n = len(arr2) # columns
    dp = []
    for i in range(m + 1):
        dp.append([])
        for j in range(n + 1):
            dp[i].append(-1)
    lcs_helper(arr1, m, arr2, n, dp)
    return dp

# PURPOSE
# Helper to fully implement the recursive method lcs_recursive.
# SIGNATURE
# lcs_helper :: List, Integer, List, Integer, List[List] => Integer
def lcs_helper(arr1, i, arr2, j, dp):
    # This keeps us from going outside the range and sets the base case.
    if i == 0 or j == 0:
        dp[i][j] = 0
    # This keeps us from recomputing things we already have.
    if dp[i][j] != -1:
        return dp[i][j]
    if arr1[i - 1] == arr2[j - 1]:
        dp[i][j] = lcs_helper(arr1, i - 1, arr2, j - 1, dp) + 1
    if arr1[i - 1] != arr2[j - 1]:
        dp[i][j] = max(lcs_helper(arr1, i - 1, arr2, j, dp),\
            lcs_helper(arr1, i, arr2, j - 1, dp))
    return dp[i][j]

# PURPOSE
# Reverses an array in place.
# SIGNATURE
# reverse_arr
def reverse_arr(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

# PURPOSE
# Traverse the dp array in reverse to reconstruct the lcs from the dp array.
# SIGNATURE
# lcs_reconstruction :: List, List, List[List] => List
# TIME COMPLEXITY
# O(m + n)
# SPACE COMPLEXITY
# O(n)
def lcs_reconstruction(arr1, arr2, dp):
    m = len(arr1)
    n = len(arr2)
    rev_ans = []
    i = m
    j = n
    while i > 0 and j > 0:
        if arr1[i-1] == arr2[j-1]:
            rev_ans.append(arr1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    reverse_arr(rev_ans)
    return rev_ans