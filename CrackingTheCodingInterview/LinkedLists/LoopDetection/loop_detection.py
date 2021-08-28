from LinkedList import LinkedList
from Node import Node

# O(n) time | O(1) space
def loop_detection(lst):
    fast = lst.head
    slow = lst.head

    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        # I initially put this if statement in the wrong spot.
        if fast == slow:
            break

    if fast == None or fast.next == None:
        return False

    slow = lst.head

    while fast != slow:
        slow = slow.next
        fast = fast.next

    return fast

no_loop = LinkedList(Node(1))
no_loop.add_node(Node(2))
no_loop.add_node(Node(3))
no_loop.add_node(Node(4))
no_loop.add_node(Node(5))

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)

# self_loop = LinkedList(node1)
# self_loop.add_node(node2)
# self_loop.add_node(node2)

# print(loop_detection(self_loop))

# short_loop = LinkedList(node1)
# short_loop.add_node(node2)
# short_loop.add_node(node3)
# short_loop.add_node(node4)
# short_loop.add_node(node5)
# short_loop.add_node(node6)
# short_loop.add_node(node7)
# short_loop.add_node(node8)
# short_loop.add_node(node10)
# short_loop.add_node(node11)
# short_loop.add_node(node12)
# node12.next = node10

# print('short loop', loop_detection(short_loop))

long_loop = LinkedList(node1)
long_loop.add_node(node2)
long_loop.add_node(node3)
long_loop.add_node(node4)
long_loop.add_node(node5)
long_loop.add_node(node6)
long_loop.add_node(node7)
long_loop.add_node(node8)
long_loop.add_node(node10)
long_loop.add_node(node11)
long_loop.add_node(node12)
node12.next = node4

print('long loop', loop_detection(long_loop))