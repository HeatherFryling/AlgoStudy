# O(n) time | O(1) space
def is_unique1(s):
    seen = set({}) # seen will never exceed the number of chars in the alphabet, so it's O(1)
    for c in s:
        if c in seen:
            return False
        else:
            seen.add(c)
    return True

# O(n^2) time | O(1) space
def is_unique2(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# To do this without extra space, you could sort the characters, but you would need to be
# able to get the char array without extra space.

test1 = 'abdc'
test2 = 'abda'

print(is_unique1(test1)) # True
print(is_unique1(test2)) # False
print(is_unique2(test1)) # True
print(is_unique2(test2)) # False