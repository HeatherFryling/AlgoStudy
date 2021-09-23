# Heather Fryling
# 9/22/2021

# PURPOSE
# Count the number of combinations possible in a powerset.
# SIGNATURE
# countPowerset :: List[Integer] => Integer
# TIME AND SPACE COMPLEXITY
# O(2^n) time | O(n) space
def countPowerset(nums):
    return countP(nums, 0)

# PURPOSE
# Helper function to recursively count the number of combinations possible in a powerset.
# SIGNATURE
# countPowerset :: List[Integer] , Integer=> Integer
def countP(nums, i):
    # Base case: The powerset is as long as the whole array.
    if i == len(nums):
        return 1

    # For the next element, we can include it or excluse it.
    # Branching factor is 2.
    include = countP(nums, i + 1)
    exclude = countP(nums, i + 1)

    return include + exclude

# PURPOSE
# Return the powerset of a list of items.
# SIGNATURE
# powerSet :: List => List[List]
# TIME AND SPACE COMPLEXITY
# O(n*2^n) time | O(n*2^n) space
def powerSet(nums, i = None):
    # If no index is provided, start with the end of the list.
    if i is None:
        i = len(nums) - 1
    # If the whole list is processed, return the empty set.
    if i < 0:
        return [[]]
    subsets = powerSet(nums, i - 1)
    for idx in range(len(subsets)):
        currentSubset = subsets[idx]
        subsets.append(currentSubset + [nums[i]])
    return subsets

print(powerSet([1, 2, 3]))

# PURPOSE
# Return the powerset of a list of items.
# SIGNATURE
# powerSet :: List => List[List]
# TIME AND SPACE COMPLEXITY
# O(n*2^n) time | O(n*2^n) space
def powerSet2(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [num])
    return subsets

print(powerSet2([1, 2, 3]))

# PURPOSE
# Return the powerset of a list of items.
# SIGNATURE
# powerSet :: List => List[List]
# TIME AND SPACE COMPLEXITY
# O(n*2^n) time | O(n*2^n) space
def powerSet3(nums):
    results = []
    powerSet3Helper(nums, 0, results, [])
    return results

def powerSet3Helper(nums, idx, results, path):
    # All of them will hit the length of nums and get appended to the results.
    if idx == len(nums):
        results.append(path)
        return
    
    # Make a copy of the previous subset.
    pathWithCurrent = [p for p in path]
    # Add the current item to the previous subset.
    pathWithCurrent.append(nums[idx])

    # Recursively call without using the current number.
    powerSet3Helper(nums, idx + 1, results, path)
    # Recursively call with using the current number.
    powerSet3Helper(nums, idx + 1, results, pathWithCurrent)

print(powerSet3([1,2,3]))

# PURPOSE
# Return the powerset of a list of items.
# SIGNATURE
# powerSet :: List => List[List]
# TIME AND SPACE COMPLEXITY
# O(n*2^n) time | O(n*2^n) space
def powerSet4(nums, idx = 0):
    # If the whole list is processed, return the empty set.
    if idx == len(nums):
        return [[]]
    subsets = []
    for subset in powerSet4(nums, idx + 1):
        # Add a copy without the new number.
        subsets.append([x for x in subset])
        # Add a copy with the new number.
        subset.append(nums[idx])
        subsets.append([x for x in subset])

    return subsets

print(powerSet4([1, 2, 3]))