from LinkedList import LinkedList
from Node import Node

def is_palindrome(lst):
    length = get_length(lst)
    print(length)
    return is_palindrome_recursive(lst.head, length).ans

class Answer:
    def __init__(self, node, ans):
        self.node = node
        self.ans = ans

def is_palindrome_recursive(head, length):
    # Empty list is a palindrome.
    if length <= 0:
        return Answer(head, True)
    # List of length 1 is a palindrome
    if length == 1:
        return Answer(head.next, True)

    res = is_palindrome_recursive(head.next, length - 2)
    print(head.value, res.node.value)
    return Answer(res.node.next, head.value == res.node.value and res.ans)

def get_length(lst):
    curr = lst.head
    length = 0
    while curr != None:
        length += 1
        curr = curr.next
    return length

# test1 = LinkedList(Node(1))
# test1.add_node(Node(2))
# test1.add_node(Node(3))
# test1.add_node(Node(4))
# test1.add_node(Node(5))

# is_palindrome(test1)

test2 = LinkedList(Node(1))
test2.add_node(Node(2))
test2.add_node(Node(3))
test2.add_node(Node(2))
test2.add_node(Node(1))

print(is_palindrome(test2))

test3 = LinkedList(Node(1))
test3.add_node(Node(2))
test3.add_node(Node(3))
test3.add_node(Node(3))
test3.add_node(Node(1))

print(is_palindrome(test3))
