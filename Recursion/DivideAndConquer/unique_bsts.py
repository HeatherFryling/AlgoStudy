def numTrees(n):
    dp = {}
    dp[0] = 1
    dp[1] = 1
    return helper(n, dp)

def helper(n, dp):
    if n in dp.keys():
        return dp[n]
    count = 0
    for root in range(n):
        numLeftTrees = helper(root, dp)
        numRightTrees = helper(n - root - 1, dp)
        count += numLeftTrees * numRightTrees
    dp[n] = count
    return count