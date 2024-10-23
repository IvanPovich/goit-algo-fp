from linked_list.linked_list import LinkedList, Node

def reverse_list (list:LinkedList) -> LinkedList:
    new_list = LinkedList()
    current = list.head

    while current:
        new_node = Node(current.data)
        new_node.next = new_list.head
        new_list.head = new_node

        current = current.next

    return new_list