# Heather Fryling
# 1/18/2021
# Implementation of radix sort.
# Much of this code comes from the GeeksForGeeks tutorial:
# https://www.geeksforgeeks.org/radix-sort/

# PURPOSE
# Run counting sort on individual digits of an array.
# Sorts the input array by the digit specified by exp,
# then copies the sorted array to the input array for use
# with the next digit of radix sort.
# SIGNATURE
# counting_sort_exp :: List, Integer => None
# TIME COMPLEXITY:
# O(n) --since in this case, k is a constant, 10
# SPACE COMPLEXITY:
# O(n) --again, k is 10, so not considered
def counting_sort_exp(arr, exp):
    DIGITS_BASE_10 = 10
    output = [0] * len(arr)
    counts = [0] * DIGITS_BASE_10

    # Counting the occurences of each digit in the place given by exp.
    for i in range(len(arr)):
        # Divide by the exponent to get the leading digits.
        leading_digits = arr[i] / exp
        # Mod with 10 to get the last digit.
        digit = int(leading_digits % DIGITS_BASE_10)
        counts[digit] += 1

    # Adjust for 0-based indexing and transform the counts to cumulative sums.
    counts[0] -= 1
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in range(len(arr) - 1, -1, -1):
        leading_digits = arr[i] / exp
        digit = int(leading_digits % DIGITS_BASE_10)
        output[counts[digit]] = arr[i]
        counts[digit] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

# PURPOSE
# Sort an array of positive integers with at most d digits.
# SIGNATURE
# radix_sort :: List, Integer => List
# TIME COMPLEXITY
# O(d*n) -- counting sort (with constant k=10) runs d times
# SPACE COMPLEXITY
# O(n) --for counting sort (with constant k=10)
def radix_sort(arr, d):
    max_exp = 10**(d - 1)
    exp = 1
    while(exp <= max_exp):
        counting_sort_exp(arr, exp)
        exp *= 10
    return arr