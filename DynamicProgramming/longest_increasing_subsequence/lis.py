# Heather Fryling
# 2/18/2021

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = []
    for i in range(n):
        dp.append(0)
    dp[0] = 1
    print(dp)
    for i in range(1, n):
        dp[i] = dp[i - 1]
        for j in range((i - 1), -1, -1):
            if arr[j] < arr[i]:
                dp[i] = max(1 + dp[j], dp[i])
    return dp[n - 1]

test1 = [5, 1, 3, 2, 7, 9]
print(longest_increasing_subsequence(test1))