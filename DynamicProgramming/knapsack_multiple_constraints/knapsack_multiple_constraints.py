# Heather Fryling
# 2/10/2021

def construct_dp(n, max_w, max_s):
    dp = []
    for i in range(n + 1):
        dp.append([])
        for j in range(max_w + 1):
            dp[i].append([])
            for _ in range(max_s + 1):
                dp.append(0)
    return dp

def knapsack_multiple_constraints(weights, sizes, values, max_w, max_s):
    n = len(weights)
    dp = construct_dp(n, max_w, max_s)
    for i in range(1, n + 1):
        for w in range(1, max_w + 1):
            for s in range(1, max_s + 1):
                if sizes[i - 1] <= s and weights[i - 1] <= w:
                    dp[i][w][s] = max(values[i - 1] + \
                        dp[i - 1][w - weights[i - 1]][s - sizes[i - 1]],
                        dp[i - 1][w][s])
    return dp[n][max_w][max_s]