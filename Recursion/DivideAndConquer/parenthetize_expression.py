# Given a string, s, return all the valid ways
# to parenthesize it.
# TIME COMPLEXITY
# Branching factor: O(n)
# Height: O(n)
# Outer loop: O(n)
# Inner loop: Requires combinatorics
# Overestimate for inner loop: O(n!) * O(n!) * O(n)
# O(n^(3n + 2)

def parenthesize_expression(s):
    print(s)
    if len(s) == 1:
        return [s]

    results = []
    for i in range(1, len(s)):
        s1 = s[0 : i]
        s2 = s[i : len(s)]
        left = parenthesize_expression(s1)
        right = parenthesize_expression(s2)

        for s1 in left:
            for s2 in right:
                results.append("(" + s1 + s2 + ")")
    return results

s = "abcd"

print(parenthesize_expression(s))