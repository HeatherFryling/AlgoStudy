# Heather Fryling
# 2/11/2021

# PURPOSE
# Helper function to help with troubleshooting.
# SIGNATURE
# print_table :: List[List] => None
def print_table(table):
    for i in range(len(table)):
        print(table[i])

# PURPOSE
# Helper method for is_palindrome_table.
# Constructs an n x n table of boolean values all initialized to False.
# SIGNATURE
# bool_table :: Integer => List[List[Boolean]]
def bool_table(n):
    table = []
    for i in range(n):
        table.append([])
        for _ in range(n):
            table[i].append(False)
    return table

# PURPOSE
# Helper method for preprocessing to speed up string palindrome.
# Given a string, preprocess the string to produce a lookup table
# that indicates whether letters from index k to index i are a
# palindrome.
# SIGNATURE
# is_palindrome_table :: String => List[List[Boolean]]
# TIME COMPLEXITY
# O(n^2)
# SPACE COMPLEXITY
# O(n^2)
def is_palindrome_table(str):
    n = len(str)
    table = bool_table(n)
    for i in range(n):
        table[i][i] = True
    for i in range(n - 1):
        table[i][i + 1] = (str[i] == str[i + 1])
    for i in range(2, n):
        for k in range(i - 1):
            # table[k][i] = "meep"
            table[k][i] = str[k] == str[i] and table[k + 1][i - 1]
    return table

# PURPOSE
# Given a string, determine the minimum number of palindromes it can be
# divided into.
# For example, "banana" could be divided into:
#    - 'b', 'a', 'n', 'a', 'n', 'a'
#    - 'b', 'ana', 'n, 'a'
#    - 'b', 'anana'
# The third option would be the minimum, as it is only 2 palindromes
# SIGNATURE
# string_palindrome :: String => Integer
def string_palindrome(str):
    dp = []
    for _ in range(len(str) + 1):
        dp.append(0)
    dp[1] = 1
    is_palindrome = is_palindrome_table(str)
    for i in range(2, len(str) + 1):
        dp[i] = i
        for k in range(0, i):
            if is_palindrome[k][i - 1]:
                dp[i] = min(dp[i], dp[k] + 1)
    return dp[len(str)]

# PURPOSE
# Helper method for recursive implementation of string_palindrome.
# SIGNATURE
# string_pal_helper :: String, Integer, List[List[Boolean]], Dictionary
# => Integer
def string_pal_helper(str, i, is_palindrome, dp):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i in dp.keys():
        return dp[i]
    dp[i] = i
    for k in range(0, i):
        if is_palindrome[k][i - 1]:
            dp[i] = min(dp[i], 1 + string_pal_helper(str, k, is_palindrome, dp))
    return dp[i]

# PURPOSE
# Given a string, determine the minimum number of palindromes it can be
# divided into.
# For example, "banana" could be divided into:
#    - 'b', 'a', 'n', 'a', 'n', 'a'
#    - 'b', 'ana', 'n, 'a'
#    - 'b', 'anana'
# The third option would be the minimum, as it is only 2 palindromes
# SIGNATURE
# string_palindrome :: String => Integer
# TIME COMPLEXITY
# O(n^2) with O(n^2) preprocessing time to construct is_palindrome.
# SPACE COMPLEXITY
# O(n^2)
# Note: It is probably not worth the overhead to use a dictionary instead of
# an array in this case, but I did it for convenience as this is for study
# purposes.
def string_pal_top_down(str):
    dp = {}
    is_palindrome = is_palindrome_table(str)
    ans = string_pal_helper(str, len(str), is_palindrome, dp)
    return ans