from LinkedList import LinkedList
from Node import Node

# O(n) time | O(1) space
def kth_to_last(head, k):
    if k < 1:
        return None
    length = get_length_of_list(head)
    target = length - k
    if target < 0:
        return None
    pos = 0
    curr = head
    while(pos != target):
        curr = curr.next
        pos += 1
    return curr.value
    

def get_length_of_list(head):
    curr = head
    count = 0
    while (curr != None):
        count += 1
        curr = curr.next
    return count

# O(n) time, optimized | O(1) space
def kth_to_last2(head, k):
    if k < 1:
        return None
    slow = head
    fast = head
    count = 0
    while (count != k - 1 and fast != None):
        fast = fast.next
        count += 1
    if fast == None:
        return None
    while(fast.next != None):
        fast = fast.next
        slow = slow.next
    return slow

class Index:
    def __init__(self):
        self.dist_to_end = 0

# O(n) time | O(n) space on the call stack.
def kth_to_last3(node, k):
    return kth_to_last_helper(node, k, Index())

def kth_to_last_helper(head, k, idx):
    if head == None:
        return None
    node = kth_to_last_helper(head.next, k, idx)
    idx.dist_to_end += 1
    if idx.dist_to_end == k:
        return head
    return node
    
test1 = LinkedList(Node(1))
test1.add_node(Node(2))
test1.add_node(Node(3))
test1.add_node(Node(4))

print(test1)
# for k in range(6):
#     print(k, kth_to_last(test1.head, k))

# for k in range(6):
#     print(k, kth_to_last2(test1.head, k))

for k in range(6):
    print(k, kth_to_last2(test1.head, k))
