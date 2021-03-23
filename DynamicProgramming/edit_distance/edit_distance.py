# Heather Fryling
# 2/6/2021

# PURPOSE
# Determine the minimum number of operations to move from a start string to a
# target string.
# OPERATIONS:
# - insert() any letter = f(i, j - 1) + 1
# - delete() any letter = f(i - 1, j) + 1
# - replace() any letter = f(i - 1, j - 1) + (0 or 1) -- 0 if the chars are the
#   same and 1 if the chars are different
# SIGNATURE
# edit_distance :: String, String => Integer
# TIME COMPLEXITY
# O(nm)
# SPACE COMPLEXITY
# O(nm)
def edit_distance(start, target):
    n = len(start)
    m = len(target)
    dp = []
    for i in range(n + 1):
        dp.append([])
        for _ in range(m + 1):
            dp[i].append(0)
    # Base case 1:
    # If the target is the empty string, the cost to go from the start string
    # to the empty string is deletions equal to the number of chars in the
    # start.
    for i in range(1, n + 1):
        dp[i][0] = i
    # Base case 2:
    # If the start is the empty string, the cost to go from the start to the
    # target is insertions equal to the number of letters in the target string.
    for j in range(1, m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j] + 1 # delete
            if dp[i][j - 1] + 1 < dp[i][j]:
                dp[i][j] = dp[i][j - 1] + 1 # insert
            if start[i - 1] == target[j - 1]:
                if dp[i - 1][j - 1] < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - 1] # We can do nothing, because the cheapest cost is to leave them alone.
            else:
                if dp[i - 1][j - 1] + 1 < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 # Replace operation.
    print_dp(dp)
    return dp[n][m]

# PURPOSE
# Helper function to print the dp array for troubleshooting purposes.
# SIGNATURE
# print_dp :: List[List] => None
def print_dp(dp):
    for i in range(len(dp)):
        print(dp[i])

# PURPOSE
# Helper method for recursive, top-down edit distance with memoization.
# SIGNATURE
# edit_distance_helper :: String, String, Integer, Integer, Dictionary
def edit_distance_helper(start, target, i, j, dp):
    if i == 0:
        return j
    if j == 0:
        return i
    if (i, j) in dp.keys():
        return dp[(i, j)]
    delete = edit_distance_helper(start, target, i, j - 1, dp) + 1
    insert = edit_distance_helper(start, target, i - 1, j, dp) + 1
    replace = edit_distance_helper(start, target, i - 1, j - 1, dp) if \
        start[i - 1] == target[j - 1] \
            else edit_distance_helper(start, target, i - 1, j - 1, dp) + 1
    dp[(i, j)] = min(delete, insert)
    dp[(i, j)] = min(dp[i, j], replace)
    return dp[(i, j)]

# PURPOSE
# Determine the minimum number of operations to move from a start string to a
# target string.
# This implementation uses a top-down approach with memoization, however we do
# not get a benefit, because for every square, we require minimum of the square
# above, to the left, and diagonally, meaning all must be computed, meaning we
# are putting frames on the call stack for each square and not saving any
# time/space by avoiding calls.
# OPERATIONS:
# - insert() any letter = f(i, j - 1) + 1
# - delete() any letter = f(i - 1, j) + 1
# - replace() any letter = f(i - 1, j - 1) + (0 or 1) -- 0 if the chars are the
#   same and 1 if the chars are different
# SIGNATURE
# edit_distance :: String, String => Integer
# TIME COMPLEXITY
# O(nm)
# SPACE COMPLEXITY
# O(nm)
def edit_distance_top_down(start, target):
    dp = {}
    n = len(start)
    m = len(target)
    ans =  edit_distance_helper(start, target, n, m, dp)
    print(dp)
    return ans

print(edit_distance("sunday", "saturday"))