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
# [1, 2, 3]             [1, 3, 2]
# mid < start < end,    mid < end < start
# [2, 1, 3]             [3, 1, 2]
# end < mid < start,    end < start < mid
# [3, 2, 1]             [2, 3, 1]
# COMMENT
# This isn't really necessary for the kth order statistic in an unsorted array,
# but I wanted to practice.

def median_of_three(arr, start, end):
    mid = start + (end - start) // 2
    if arr[start] < arr[mid]:
        if arr[mid] < arr[end]:
            return mid # start < mid < end
        elif arr[start] < arr[end]:
            return end # start < end < mid
        else:
            return start # end < start < mid
    else:
        if arr[start] < arr[end]:
            return start # mid < start < end
        elif arr[end] < arr[mid]:
            return mid # end < mid < start
        else:
            return end # mid < end < start

# PURPOSE
# Swap two values in a list.
# SIGNATURE
# swap :: List, Integer, Integer => None
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# PURPOSE
# Choose a pivot value using the median of three method.
# SIGNATURE
# choose_pivot :: List, Integer, Integer => Integer
def choose_pivot(arr, start, end):
    return median_of_three(arr, start, end)

# PURPOSE
# Partition an array between the start and end indices (inclusive) such that
# all values to the left of the pivot are <= the pivot and all values to the
# right of the pivot are > pivot.
# SIGNATURE
# partition :: List, Integer, Integer
# TIME COMPLEXITY
# O(n) -- for loop from start to end
# SPACE COMPLEXITY
# O(1) -- only single variables allocated
def partition(arr, start, end):
    pivot_index = choose_pivot(arr, start, end)
    swap(arr, pivot_index, end)
    i = start - 1 # position we can guarantee is <= pivot
    for j in range(start, end):
        if arr[j] <= arr[end]:
            i += 1
            swap(arr, j, i)
    swap(arr, i + 1, end)
    return i + 1

# PURPOSE
# Get the kth largest value from a list of integers.
# SIGNATURE
# kth_with_partition :: List, Integer => Integer
# TIME COMPLEXITY
# O(n)
# On average, partition will choose a value that's neither the first or last
# in the range, so the recurrence will be T(n) = O(n) + T(n/b).
# log_b(1) < 1, so by master theorem, this is O(n).
# If we are unlucky and choose the first or last element every time,
# this becomes O(kn) or O((n-k)n).
# SPACE COMPLEXITY
# No extra space is allocated except for single variables.
# O(1).
# If we did this recursively, it would be O(logn) calls on the call stack,
# since unless we were very unlucky with every partition, we would divide
# the problem size by a number > 1 at each call.
def kth_with_partition(arr, k):
    if (k > len(arr) or k < 0):
        return None
    start = 0
    end = len(arr) - 1
    ans = partition(arr, start, end)
    while ans != k - 1:
        if ans < k - 1:
            start = ans + 1
        else:
            end = ans - 1
        ans = partition(arr, start, end)
    return arr[ans]