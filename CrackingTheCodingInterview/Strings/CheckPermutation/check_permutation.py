# O(n + m) time | O(n + m) space
def check_permutation(s1, s2):
    s1_char_counts = count_chars(s1)
    s2_char_counts = count_chars(s2)
    for key in s1_char_counts:
        if key not in s2_char_counts.keys():
            return False
        if s2_char_counts[key] != s1_char_counts[key]:
            return False
    return True

def count_chars(s):
    char_counts = {}
    for c in s:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts

test1 = ["tacco", "otacc"] # True
test2 = ["taco", "cato"] # True
test3 = ["taco", "cat"] # False

print(check_permutation(test1[0], test1[1]))
print(check_permutation(test2[0], test2[1]))
print(check_permutation(test3[0], test3[1]))