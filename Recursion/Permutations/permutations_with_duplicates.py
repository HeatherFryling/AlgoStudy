# Time Complexity
# Branching factor: O(n)
# Height: O(n)
# Work per call: O(n)
# - for copying path or set to array.
# O(n*n^n) aka O(n!n)

# Space Complexity
# Height: O(n)
# Space per recursive call:
# O(1)
# O(n) for the path and the hash map.
# (Not counting the size of the returned array.)

def perms_with_dups(items):
    res = []
    path = []
    item_counts = {}
    for item in items:
        if item not in item_counts.keys():
            item_counts[item] = 0
        item_counts[item] += 1
    helper(item_counts, path, res)
    return res

def helper(item_counts, path, res):
    if len(item_counts) == 0:
        res.append(path.copy())

    item_set = set(item_counts.keys())
    
    for item in item_set:
        curr_count = item_counts[item]
        if curr_count == 1:
            del item_counts[item]
        else:
            item_counts[item] -= 1
    
        path.append(item)
        helper(item_counts, path, res)
        item_counts[item] = curr_count
        path.pop()

items = [1, 2, 3, 1]

ans = [[1, 1, 2, 3], [1, 1, 3, 2], [1, 2, 1, 3], [1, 2, 3, 1], [1, 3, 1, 2], [1, 3, 2, 1], [2, 1, 1, 3], [2, 1, 3, 1], [2, 3, 1, 1], 
[3, 1, 1, 2], [3, 1, 2, 1], [3, 2, 1, 1]]
assert(ans == perms_with_dups(items))

print("Working as expected.")