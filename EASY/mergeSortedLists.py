# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeSortedLists(head1, head2):
    l1 = head1
    l2 = head2
    dummy = ListNode()
    curr_node = dummy
    while l2 and l1:
        if l1.val > l2.val:
            curr_node.next = l2
            l2 = l2.next
        else:
            curr_node.next = l1
            l1 = l1.next
        curr_node = curr_node.next

    curr_node.next = l1 if l1 is not None else l2
    return dummy.next

#tests
arr1 = [1,2,4]
arr2 = [1,3,4]
dummy1 = ListNode()
list1 = dummy1
dummy2 = ListNode()
list2 = dummy2
for i in range(len(arr1)):
    temp_node1 = ListNode(arr1[i])
    temp_node2 = ListNode(arr2[i])
    list1.next = temp_node1
    list1 = list1.next
    list2.next = temp_node2
    list2 = list2.next
ans = mergeSortedLists(dummy1.next, dummy2.next)
print(ans.next.next.val)

