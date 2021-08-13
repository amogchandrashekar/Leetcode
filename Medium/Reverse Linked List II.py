from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], start: int, end: int) -> Optional[ListNode]:
        if start == end or not head:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head

        node_before_reversed_sublist = dummy_head
        pos = 1
        while pos < start:
            node_before_reversed_sublist = node_before_reversed_sublist.next
            pos += 1

        sublist_working_ptr = node_before_reversed_sublist.next

        while start < end:
            start += 1

            node_coming_to_sublist_front = sublist_working_ptr.next
            sublist_working_ptr.next = node_coming_to_sublist_front.next

            node_coming_to_sublist_front.next = node_before_reversed_sublist.next
            node_before_reversed_sublist.next = node_coming_to_sublist_front

        return dummy_head.next