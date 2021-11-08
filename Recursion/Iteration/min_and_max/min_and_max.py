# Heather Fryling
# 11/8/2021

# Function to recursively find
# the min and max of an array.
# Illustrates building up an
# answer to return.
# Time complexity is O(n).
# Space complexity is O(n).

def min_and_max(arr):
    return min_max_helper(arr, 0, float('inf'), float('-inf'))

def min_max_helper(arr, i, minVal, maxVal):
    minVal = min(minVal, arr[i])
    maxVal = max(maxVal, arr[i])
    if i == len(arr) - 1:
        return minVal, maxVal
    return min_max_helper(arr, i + 1, minVal, maxVal)
    