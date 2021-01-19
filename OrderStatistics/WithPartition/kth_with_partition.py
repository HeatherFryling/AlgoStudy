# Heather Fryling
# 1/19/2021
# Program to find the kth smallest number using the
# partition algorithm.

# PURPOSE
# Get the index of the median of 3 values in a specified range within an array.
# SIGNATURE
# median_of_three :: List, Integer, Integer => Integer
# EXPLANATION:
# There are 3! possible orderings of the values, leading to
# 6 cases within the code:
# start < mid < end,    start < end < mid
# mid < start < end,    mid < end < start
# end < mid < start,    end < start < mid

def median_of_three(arr, start, end):
    mid = start + (end - start) / 2


def choose_pivot(arr, start, end):
    return median_of_three(arr, start, end)