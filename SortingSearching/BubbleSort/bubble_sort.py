# Heather Fryling
# 10/2/2021

# PURPOSE
# Given an unsorted array of integers, sort it in place.
# SIGNATURE
# bubble_sort :: List[Integer] => None
# TIME AND SPACE COMPLEXITY
# O(n^2) time | O(1) space
# The nested for loop does n * (n + 1)/ 2 operations, and the
# algorithm is in place, so no extra work is done.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # The guarantee is that by the time this loop runs,
        # the values from the end to n - i - 1 will be sorted,
        # because we will always bubble up the maximum value
        # to the last available position.
        for j in range(n - i - 1):
            # bubble up
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
