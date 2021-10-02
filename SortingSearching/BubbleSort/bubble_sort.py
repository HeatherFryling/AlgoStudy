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
 
test1 = [1, 2, 3, 4, 5]
test2 = [5, 4, 3, 2, 1]
test3 = [1, 3, 4, 2, 5]
test4 = [1, 3, 4, 2, 5, 5]

ans1 = sorted(test1)
ans2 = sorted(test2)
ans3 = sorted(test3)
ans4 = sorted(test4)

bubble_sort(test1)
bubble_sort(test2)
bubble_sort(test3)
bubble_sort(test4)

assert(ans1 == test1)
assert(ans2 == test2)
assert(ans3 == test3)
assert(ans4 == test4)

print("Passed all tests.")
