# Heather Fryling
# 11/8/2021

# Recursive function to print
# the values at the odd indices in
# an array.
# Time complextiy is O(n).
# Space complexity is O(1).
def print_odd(arr):
    print_odd_helper(arr, 1)

def print_odd_helper(arr, i):
    if i % 2 != 1:
        print("Invalid index.")
        return
    if i >= len(arr):
        return
    print(arr[i])
    print_odd_helper(arr, i + 2)

arr1 = [1, 2, 3, 4]

print_odd(arr1)

arr2 = [1, 2, 3, 4, 5]

print_odd(arr2)

arr3 = []

print_odd(arr3)