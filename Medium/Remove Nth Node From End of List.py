"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    head = [1]
    n = 1
    node = dummy = ListNode(0)
    for val in head:
        node.next = ListNode(val)
        node = node.next

    list_node = Solution().removeNthFromEnd(dummy.next, n)
    flattened_list = list()
    while list_node:
        val = list_node.val
        list_node = list_node.next
        flattened_list.append(val)
    print(flattened_list)