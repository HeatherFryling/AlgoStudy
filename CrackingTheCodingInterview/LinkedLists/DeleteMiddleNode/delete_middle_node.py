from LinkedList import LinkedList
from Node import Node

# O(1) time | O(1) space
def delete_middle_node(node):
    if (node == None or node.next == None):
        return None
    node.value = node.next.value
    node.next = node.next.next

test1 = LinkedList(Node(1))
node_to_delete = Node(3)
test1.add_node(node_to_delete)
test1.add_node(Node(2))
test1.add_node(Node(4))

print(test1)

delete_middle_node(node_to_delete)
print(test1)


