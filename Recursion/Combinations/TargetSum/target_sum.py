# PURPOSE:
# Given an array of integers, return
# all combinations with repetition that
# sum to a target value.
# TIME COMPLEXITY
# Tree height: O(n)
# Branching factor: 2
# Work per call: O(n)
# Total: O(n*2^n)
# SPACE COMPLEXITY
# O(n) for recursive calls.
# All other space is allocated for the client.
def target_sum(nums, target):
    res = []
    path = []
    ts_recursive(nums, target, path, res, 0)
    return res

def ts_recursive(nums, target, path, res, idx):
    if target < 0:
        return
    if target == 0:
        cp = path.copy()
        res.append(cp)
        return
    if idx >= len(nums):
        return
    # Don't use the current position again.
    ts_recursive(nums, target, path, res, idx + 1)
    # Use the current position.
    path.append(nums[idx])
    ts_recursive(nums, target - nums[idx], path, res, idx)
    path.pop()

nums = [1, 2, 3, 4]
target = 4

print(target_sum(nums, target))
    