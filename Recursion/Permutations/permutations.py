# Time Complexity
# Braching factor: O(n)
# Height: O(n)
# Work per call: O(n)
# - for copying path or set to array.
# O(n*n^n) aka O(n!n)

# Space Complexity
# Height: O(n)
# Space per recursive call:
# O(1)
# O(n)
# (Not counting the size of the returned array.)

def simple_permutations(ls):
    available = set(ls)
    path = []
    res = []
    sp(available, path, res)
    return res

def sp(available, path, res):
    if len(available) == 0:
        cp = path.copy()
        res.append(cp)
        return
    # Have to convert available to a list to prevent
    # unpredictable iteration issues.
    for item in list(available):
        path.append(item)
        available.remove(item)
        sp(available, path, res)
        path.pop()
        available.add(item)

ls = [1, 2, 3]

print(simple_permutations(ls))

# No copying the set into an array, but
# the time complexity is still the same due to
# copying the path over and over.
# Time: O(n!n)
# Space: O(n)
def permutations(ls):
    res = []
    path = []
    i = 0
    swapping_permutations(ls, i, path, res)
    return res

# Invariant:
#   The items up to index i are in the path.
def swapping_permutations(ls, i, path, res):
    if i == len(ls):
        cp = path.copy()
        res.append(cp)
        return
    # This swaps every unused item into position i
    # where it will be added to the path.
    for j in range(i, len(ls)):
        swap(ls, i, j)
        path.append(ls[i])
        swapping_permutations(ls, i + 1, path, res)
        swap(ls, i, j)
        path.pop()

def swap(ls, i, j):
    ls[i], ls[j] = ls[j], ls[i]

print(permutations(ls))
    