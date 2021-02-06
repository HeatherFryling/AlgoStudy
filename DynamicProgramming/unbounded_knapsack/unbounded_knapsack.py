# Heather Fryling
# 2/5/2021

def unbounded_knapsack(values, weights, c):
    max_so_far = []
    # Max value from 0 items is 0
    max_so_far.append(0)
    for i in range(1, c + 1):
        curr_max = 0
        for j in range(len(values)):
            curr_val = 0
            if weights[j] <= i:
                curr_max = values[j] + max_so_far[i - weights[j]]
                if curr_val > curr_max:
                    curr_max = curr_val
        max_so_far.append(curr_max)
    return max_so_far[c]

v1 = [1]
w1 = [4]
c1 = 4
unbounded_knapsack(v1, w1, c1)
assert(1 == unbounded_knapsack(v1, w1, c1))

v2 = [1]
w2 = [1]
c2 = 4
unbounded_knapsack(v2, w2, c2)
assert(4 == unbounded_knapsack(v2, w2, c2))

v3 = [1, 3]
w3 = [1, 2]
c3 = 4
unbounded_knapsack(v3, w3, c3)
assert(6 == unbounded_knapsack(v3, w3, c3))

v4 = [1, 3, 2]
w4 = [1, 2, 1]
c4 = 4
unbounded_knapsack(v4, w4, c4)
assert(8 == unbounded_knapsack(v4, w4, c4))