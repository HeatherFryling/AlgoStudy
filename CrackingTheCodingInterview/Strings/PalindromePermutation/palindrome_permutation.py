# O(n) time | O(1) space -- Number of letters in the alphabet.
def palindrome_permutation(s):
    counts = {}
    for c in s:
        if c.isalpha():
            c = c.lower()
            if c in counts.keys():
                counts[c] += 1
            else:
                counts[c] = 1
    odd = False
    for k in counts.keys():
        if (isOdd(counts[k])):
            if odd:
                return False
            else:
                odd = True
    return True

def isOdd(num):
    return num % 2 == 1

test1 = 'Tact coa'
test2 = 'doggy'

print(palindrome_permutation(test1))
print(palindrome_permutation(test2))