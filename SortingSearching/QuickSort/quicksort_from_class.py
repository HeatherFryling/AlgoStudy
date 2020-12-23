# This is an implementation of the quicksort algorithm
# as taught in CS5800 at Northeastern University Seattle
# by Zhifeng Sun.
# Author: Heather Fryling
# Date: 12/23/2020

import random
import itertools as it

# Quicksort's best case time complexity is O(nlogn)
# worst case = O(n^2)
# average = (nlogn)
# Worst case happens when we always choose either the minimum
# or maximum value as the pivot.

# SPACE COMPLEXITY
# O(logn) -- logn calls on the call stack


# sorts an array in place starting at the begin index and ending
# at the end index
def quicksort(arr, begin, end, option=1):
    if (end <= begin):
        return
    else:
        sorted = partition(arr, begin, end, option)
        quicksort(arr, begin, sorted - 1)
        quicksort(arr, sorted + 1, end)

def partition(arr, begin, end, option):
    pivot_index = choose_pivot(arr, begin, end, option)
    swap(arr, pivot_index, end)
    lessThanPivot = begin - 1
    for curr in range(begin, end + 1):
        if arr[curr] < arr[end]: # I initially made a mistake here and had this set to pivot_index even though 
            lessThanPivot += 1   # I'd swapped the item at the pivot_index to the end.
            swap(arr, curr, lessThanPivot)
    swap(arr, curr, lessThanPivot + 1)
    final_pivot_index = lessThanPivot + 1
    return final_pivot_index

# I made this method to allow options for various choices between
# just using the item at the end, using the median of three approach,
# and using a random pivot.
# Median of three is considered fastest.
# Both median of three and random require O(1) time to return an pivot index,
# but the random operation is a larger constant.
def choose_pivot(arr, begin, end, option):
    if (option != 1 and option != 2 and option != 3):
        return end
    if option == 1:
        return end
    elif option == 2:
        return median_of_three(arr, begin, end)
    elif option == 3:
        return random_pivot(arr, begin, end)

def median_of_three(arr, begin, end):
    mid = begin + ((end - begin) // 2)
    if arr[begin] <= arr[end]: # begin is less than end
        if arr[begin] > arr[mid]: # begin is less than end and more than mid
            return begin
        elif arr[begin] <= arr[mid]: # begin is the minimum
            return mid if arr[mid] <= arr[end] else end
    else: # end is less than begin
        if arr[end] > arr[mid]: # end is less than begin and greater than mid
            return end
        return mid if arr[mid] <= arr[begin] else begin # end is less than begin and less than mid. mid and begin remain
    return -1

def random_pivot(arr, begin, end):
    return random.randint(begin, end)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]