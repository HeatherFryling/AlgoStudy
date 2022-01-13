# PURPOSE
# Given two strings, return a list of all possible ways they can be interleaved.
# TIME COMPLEXITY
# O((n + m) 2^(n + m))
# SPACE COMPLEXITY
# O(n + m) (If we do not count the combinations we generate to return to the client.)
def interleave_strings(s1, s2):
    path = []
    res = []
    interleave_helper(s1, s2, 0, 0, res, path)
    return res


def interleave_helper(s1, s2, idx1, idx2, res, path):
    if len(path) == len(s1) + len(s2):
        res.append("".join(path))
    if idx1 < len(s1):
        path.append(s1[idx1])
        interleave_helper(s1, s2, idx1 + 1, idx2, res, path)
        path.pop()
    if idx2 < len(s2):
        path.append(s2[idx2])
        interleave_helper(s1, s2, idx1, idx2 + 1, res, path)
        path.pop()

s1 = "ab"
s2 = "cd"
print(interleave_strings(s1, s2))

# Time complexity: O(n2^n)
# Space complexity: O(n2^n)
def combinations_of_length(items, length):
    res = []
    combinations_helper(items, 0, length, res, [])
    return res

def combinations_helper(items, idx, length, res, path):
    if len(path) > length:
        return
    if len(path) == length:
        res.append(path)
        return
    if idx == len(items):
        return
    path_with_current = path.copy()
    path_with_current.append(items[idx])
    # exclude current
    combinations_helper(items, idx + 1, length, res, path)
    # include current
    combinations_helper(items, idx + 1, length, res, path_with_current)
    return

items = [1,2,3]

print(combinations_of_length(items, 3))
print("hello")

# Time complexity is time complexity of combinations of length.
# Space complexity is also dominated by combinations of length.
def interleave_with_combos(s1, s2):
    n = len(s1) + len(s2)
    idxes = [i for i in range(n)]
    s1_idxes = combinations_of_length(idxes, len(s1))
    print('s1_idxes', s1_idxes)
    res = []

    for idx, ls in enumerate(s1_idxes):
        s1_pos = 0
        s2_pos = 0
        to_string = []
        for i in range(n):
            if i in ls:
                to_string.append(s1[s1_pos])
                s1_pos += 1
            else:
                to_string.append(s2[s2_pos])
                s2_pos += 1
        res.append("".join(to_string))
    return res

print(interleave_with_combos(s1, s2))

