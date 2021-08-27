# # O(n^2) time | O(n^2) space
# def one_away(s1, s2):
#     n = len(s1)
#     m = len(s2)

#     if abs(n - m) > 1:
#         return False

#     dp = make_dp(n, m)

#     for row in range(n + 1):
#         dp[row][0] = 0
#     for col in range(m + 1):
#         dp[0][col] = 0

#     for row in range(1, n + 1):
#         for col in range(1, m + 1):
#             if s1[row - 1] == s2[col - 1]:
#                 dp[row][col] = dp[row - 1][col - 1]
#             else:
#                 dp[row][col] = min(dp[row - 1][col] + 1, dp[row][col - 1])
#                 if dp[row][col] > 1:
#                     return False
#     return True

# def make_dp(n, m):
#     dp = []
#     for row in range(n + 1):
#         dp.append([])
#         for col in range(m + 1):
#             dp[row].append(0)
#     return dp

# O(n) time | O(1) space
def one_away2(s1, s2):
    n = len(s1)
    m = len(s2)
    if abs(n - m) > 1:
        return False
    if (n == m):
        return one_away_replace(s1, s2)
    if (n < m):
        return one_away_insert(s1, s2)
    if (n > m):
        return one_away_delete(s1, s2)

def one_away_replace(s1, s2):
    num_diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            num_diff += 1
            if num_diff > 1:
                return False
    return True

def one_away_insert(s1, s2):
    pos1 = 0
    pos2 = 0
    while (pos1 < len(s1) - 1 and pos2 < len(s2) - 1):
        if s1[pos1] == s2[pos2]:
            pos1 += 1
            pos2 += 1
        if s1[pos1] != s2[pos2]:
            pos2 += 1
            if pos2 - pos1 > 1:
                return False
    return True

def one_away_delete(s1, s2):
    return one_away_insert(s2, s1)

def one_away3(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    str1 = s1 if len(s1) < len(s2) else s2
    str2 = s2 if len(s1) < len(s2) else s1
    found_difference = False
    pos1 = 0
    pos2 = 0
    while (pos1 < len(str1) and pos2 < len(str2)):
        if str1[pos1] == str2[pos2]:
            pos1 += 1
            pos2 += 1
            continue
        if found_difference:
            return False
        elif len(str1) < len(str2):
            pos2 += 1
            found_difference = True
        else:
            found_difference = True
            pos1 += 1
            pos2 += 1
    return True



test_delete = ['pafle', 'pale']
test_insert = ['ple', 'pale']
test_replace = ['rabcit', 'rabbit']
test_delete2 = ['paflee', 'pale']
test_insert2 = ['pe', 'pale']
test_replace2 = ['raccit', 'rabbit']

print(one_away2(test_delete[0], test_delete[1]))
print(one_away2(test_insert[0], test_insert[1]))
print(one_away2(test_replace[0], test_replace[1]))
print(one_away2(test_delete2[0], test_delete2[1]))
print(one_away2(test_insert2[0], test_insert2[1]))
print(one_away2(test_replace2[0], test_replace2[1]))

print()
print(one_away3(test_delete[0], test_delete[1]))
print(one_away3(test_insert[0], test_insert[1]))
print(one_away3(test_replace[0], test_replace[1]))
print(one_away3(test_delete2[0], test_delete2[1]))
print(one_away3(test_insert2[0], test_insert2[1]))
print(one_away3(test_replace2[0], test_replace2[1]))

