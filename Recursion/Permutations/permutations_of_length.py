# Time: O(n!n)
# Space: O(n)
def permutations_of_length(array, length):
    res = []
    path = []
    helper(array, 0, length, path, res)
    return res

def helper(array, idx, length, path, res):
    if len(path) == length:
        cp = path.copy()
        res.append(cp)
        return
    # Swapping around the item at position i,
    # keeping everything else the same.
    # Everything before i has already been permuted.
    # Everything after i needs to be swapped.
    for j in range(idx, len(array)):
        swap(array, idx, j)
        path.append(array[idx])
        helper(array, idx + 1, length, path, res)
        swap(array, idx, j)
        path.pop()

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

arr = [1,2,3]

print(permutations_of_length(arr, 2))

