from linked_list.linked_list import LinkedList, Node

def get_middle(list:LinkedList) -> Node:
    if list.head is None:
        return list.head
    #Так, як поділити на 2 ми не можемо, використовуємо вказівники з різницею руху в 2 рази
    slow = list.head
    fast = list.head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_sort(list:LinkedList) -> LinkedList:
    if list.head is None or list.head.next is None:
        return list

    mid = get_middle(list)
    next_to_mid = mid.next
    mid.next = None #Розриваємо список

    left_half = LinkedList()
    left_half.head = list.head

    right_half = LinkedList()
    right_half.head = next_to_mid

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge(left:LinkedList, right:LinkedList) -> LinkedList:
    merged = LinkedList()
    left_current = left.head
    right_current = right.head
    tail = None

    while left_current is not None and right_current is not None:
        if left_current.data <= right_current.data:
            new_node = Node(left_current.data)
            left_current = left_current.next
        else:
            new_node = Node(right_current.data)
            right_current = right_current.next

        if merged.head is None:
            merged.head = new_node
            tail = merged.head
        else:
            tail.next = new_node
            tail = tail.next

    while left_current is not None:
        new_node = Node(left_current.data)
        if merged.head is None:
            merged.head = new_node
            tail = merged.head
        else:
            tail.next = new_node
            tail = tail.next
        left_current = left_current.next

    while right_current is not None:
        new_node = Node(right_current.data)
        if merged.head is None:
            merged.head = new_node
            tail = merged.head
        else:
            tail.next = new_node
            tail = tail.next
        right_current = right_current.next

    return merged

def merge_sorted_list(first_li: LinkedList, second_li: LinkedList) -> LinkedList:
    new_list = LinkedList()
    first_current = first_li.head
    second_current = second_li.head
    tail = None

    while first_current is not None or second_current is not None:
        if first_current is None:
            new_node = Node(second_current.data)
            second_current = second_current.next

        elif second_current is None or first_current.data <= second_current.data:
            new_node = Node(first_current.data)
            first_current = first_current.next
        elif first_current.data <= second_current.data:
            new_node = Node(first_current.data)
            first_current = first_current.next

        else:
            new_node = Node(second_current.data)
            second_current = second_current.next

        if new_list.head is None:
            new_list.head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return new_list
