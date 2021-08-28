from LinkedList import LinkedList
from Node import Node

# O(n) time | O(n) space
def is_palindrome(lst):
    backwards = copy_and_reverse(lst)
    return is_equal(lst, backwards)

def copy_and_reverse(lst):
    curr = lst.head
    prev_new = None
    while(curr != None):
        new_node = Node(curr.value)
        new_node.next = prev_new
        prev_new = new_node
        curr = curr.next
    return LinkedList(prev_new)

def is_equal(lst1, lst2):
    curr1 = lst1.head
    curr2 = lst2.head
    while (curr1 != None and curr2 != None):
        if curr1.value != curr2.value:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1 == None and curr2 == None

test1 = LinkedList(Node(1))
test1.add_node(Node(2))
test1.add_node(Node(3))
test1.add_node(Node(4))
test1.add_node(Node(5))

print(copy_and_reverse(test1))
print(test1)

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