# Heather Fryling
# 1/18/2021
# Finally implementing heap sort!

# PURPOSE
# Swap the values at indices i and j in the heap.
# SIGNATURE
# swap :: Integer, Integer => None
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# PURPOSE
# Get the index parent index of the given index.
# If the parent does not exist, return -1.
# SIGNATURE
# parent :: Integer => Integer
def parent(arr, index):
    if (index == 0 or index > len(arr) - 1):
        return -1
    return (index - 1) // 2
# PURPOSE
# Get the index of the left child of the given index.
# If the child does not exist, return -1.
# SIGNATURE
# left_child :: Integer => Integer
def left_child(arr, index):
    child_dex = 2 * (index + 1) - 1
    return child_dex if child_dex < len(arr) else -1

# PURPOSE
# Get the index of the right child of the given index.
# If the child does not exist, return -1.
# SIGNATURE
# right_child :: Integer => Integer
def right_child(arr, index):
    child_dex = 2 * (index + 1)
    return child_dex if child_dex < len(arr) else -1

# PURPOSE
# Determine if a given position has a left child.
# SIGNATURE
# has_left_child :: Integer => Boolean
def has_left_child(arr, size, index):
    return left_child(arr, index) < size and left_child(arr, index) != -1

# PURPOSE
# Determine if a given position has a right child.
# SIGNATURE
# has_right_child :: Integer => Boolean
def has_right_child(arr, size, index):
    return right_child(arr, index) < size and right_child(arr, index) != -1

def max_heapify(arr, size, index):
    curr_pos = index
    while(has_left_child(arr, size, curr_pos) and has_right_child(arr, size, curr_pos)):
        l_child = left_child(arr, curr_pos)
        r_child = right_child(arr, curr_pos)
        max = curr_pos
        if arr[curr_pos] < arr[l_child]:
            max = l_child
        if arr[max] < arr[r_child]:
            max = r_child
        if max == curr_pos:
            break
        else:
            swap(arr, curr_pos, max)
            curr_pos = max
    if has_left_child(arr, size, curr_pos):
        if arr[curr_pos] < arr[left_child(arr, curr_pos)]:
            swap(arr, curr_pos, left_child(arr, curr_pos))
    return

# PURPOSE
# Take in a list of numbers and turn it into a valid max-heap.
# SIGNATURE
# build_heap :: List => None
def build_heap(arr):
    for i in range((len(arr) - 1) // 2, -1, -1):
        max_heapify(arr, len(arr), i)
    return arr

def heap_sort(arr):
    heap = build_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        max_heapify(heap, i, 0)
    return heap

test_list = [8, 9, 4, 2, 7, 3, 6]
print(heap_sort(test_list))