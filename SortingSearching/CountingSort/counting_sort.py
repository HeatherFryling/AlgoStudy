# Heather Fryling
# 1/17/2021
# Implementation of counting sort as taught by
# Zhifeng Sun in CS5800, Northeastern University, Seattle

# PURPOSE
# Sort a list with k possible values.
# SIGNATURE
# counting_sort :: List, Integer => List
def counting_sort(arr, k):
    counts = [0] * (k + 1)
    sorted_arr = [0] * len(arr)
    # First count how many instances there are of each value.
    for i in range(len(arr)):
        counts[arr[i]] += 1
    # Correct for zero-based indexing.
    counts[0] -= 1
    # Then add the previous total in order to have a record of
    # the correct index for the last index for each value.
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    # Set the index given in counts in the sorted array to the value
    # of the input array at index i.
    for i in range(len(arr)-1, -1, -1):
        sorted_arr[counts[arr[i]]] = arr[i]
        counts[arr[i]] -= 1
    return sorted_arr
