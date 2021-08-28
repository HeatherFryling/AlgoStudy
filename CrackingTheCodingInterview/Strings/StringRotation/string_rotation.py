# O(n + m) time where n i len(s1) and m is len(s2) | O(m + m) space
def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    concatenated = s2 + s2
    return s1 in concatenated

s1 = 'waterbottle'
s2 = 'aterbottlew'
s3 = 'terbottlewa'
s4 = 'erbottlewat'
s5 = 'ewaterbottl'
s6 = 'bottlewater'
s7 = 'retawelttob'

print(string_rotation(s1, s2))
print(string_rotation(s1, s3))
print(string_rotation(s1, s4))
print(string_rotation(s1, s5))
print(string_rotation(s1, s6))
print(string_rotation(s2, s1))
print(string_rotation(s1, s7))
