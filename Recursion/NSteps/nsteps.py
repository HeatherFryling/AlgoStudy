# Heather Fryling
# 10/3/2021

# PURPOSE
# Given a number of steps, n, return
# how many ways there are to get to the top
# of the steps, given that you may take 1 step,
# 2 steps, or 3 steps.
# SIGNATURE
# nsteps :: Integer => List[List[Integer]]
def nsteps(n):
    if n < 0:
        return []
    return stair_helper(n, 0)

def stair_helper(n, current_step):
    if current_step == n:
        # The path from the top to the top is an empty list.
        # There is one way to get to the top from the top.
        return [[]]

    if current_step > n:
        # No paths to the step beyond the top.
        return []

    result = []
    # Take one step.
    r1 = stair_helper(n, current_step + 1)
    # Take two steps.
    r2 = stair_helper(n, current_step + 2)
    # Take three steps.
    r3 = stair_helper(n, current_step + 3)
    subproblems = [r1, r2, r3]
    # Add all ways to the top from the current position
    # to the results list.
    for s in subproblems:
        for path in s:
            result.append(path)

    # Prepend the step we're on to the list of ways to get to the top.
    for l in result:
        l.insert(0, current_step)
    
    return result

print(nsteps(0))

assert([[]] == nsteps(0))
assert([[0]] == nsteps(1))
assert([[0, 1], [0]] == nsteps(2))
assert([[0, 1, 2], [0, 1], [0, 2], [0]] == nsteps(3))
assert([[0, 1, 2, 3], [0, 1, 2], [0, 1, 3], [0, 1], [0, 2, 3], [0, 2], [0, 3]] == nsteps(4))
print("Passed all tests.")

