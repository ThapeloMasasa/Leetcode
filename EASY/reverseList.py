# Given the head of a singly linked list, reverse the list, and return the reversed list.


def reverseList(head):
    if not head or not head.next:
        return head
    node = head
    temp_node = head.next
    node.next = None
    temp_node.next = node
    while temp_node.next:
        curr_node = temp_node.next
        temp_node.next = node
        node = temp_node
        temp_node = curr_node
    temp_node.next = node
    return temp_node