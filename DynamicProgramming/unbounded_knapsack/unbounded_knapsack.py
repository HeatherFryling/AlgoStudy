# Heather Fryling
# 2/5/2021

def unbounded_knapsack(values, weights, c):
    max_so_far = []
    # Max value from 0 items is 0
    max_so_far.append(0)
    for i in range(c + 1):
        curr_max = 0
        for j in range(len(values)):
            curr_val = 0
            if weights[j] <= i:
                curr_val = values[j]
                if curr_val > curr_max:
                    curr_max = curr_val
        max_so_far.append(curr_max + max_so_far[i - weights[j]])
    return max_so_far[c]

v1 = [1, 2, 3, 4]
w1 = [1, 2, 3, 4]
c1 = 6