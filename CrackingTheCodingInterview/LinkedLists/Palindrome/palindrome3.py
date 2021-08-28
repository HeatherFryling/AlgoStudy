from LinkedList import LinkedList
from Node import Node

# O(n) time | O(n) space
def is_palindrome(lst):
    fast = lst.head
    slow = lst.head
    stack = []
    while(fast != None and fast.next != None):
        stack.append(slow)
        slow = slow.next
        fast = fast.next.next

    if fast != None:
        slow = slow.next

    while(len(stack) > 0 and slow != None):
        to_compare = stack.pop()
        if to_compare.value != slow.value:
            return False
        slow = slow.next
    
    return True

test = LinkedList(Node(1))
test.add_node(Node(2))
test.add_node(Node(3))
test.add_node(Node(2))
test.add_node(Node(1))

print(test)
print(is_palindrome(test))

test = LinkedList(Node(1))
test.add_node(Node(2))
test.add_node(Node(3))
test.add_node(Node(3))
test.add_node(Node(2))
test.add_node(Node(1))

print(test)
print(is_palindrome(test))

test = LinkedList(Node(1))
test.add_node(Node(2))
test.add_node(Node(3))
test.add_node(Node(3))
test.add_node(Node(7))
test.add_node(Node(1))

print(test)
print(is_palindrome(test))