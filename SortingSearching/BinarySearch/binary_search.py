# Heather Fryling
# 1/19/2021
# Implementation of binary search

# PURPOSE
# Given a sorted array of integers, determine if it contains the target
# integer. If the array contains the integer, return its index. Otherwise,
# return -1.
# SIGNATURE
# binary_search :: List, Integer => Integer
def binary_search(array, target):
	left = 0
	right = len(array) - 1
	while left <= right:
        # Do not calculate as (left + right) // 2.
        # (left + right) could overflow.
		mid = left + (right - left) // 2
		if array[mid] == target:
			return mid
		if array[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return -1