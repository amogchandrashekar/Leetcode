"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy_odd = odd = ListNode(0)
        dummy_even = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy_even.next
        return dummy_odd.next


if __name__ == "__main__":
    root = ListNode(2)
    root.next = ListNode(1)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(5)
    root.next.next.next.next = ListNode(6)
    root.next.next.next.next.next = ListNode(4)
    root.next.next.next.next.next.next = ListNode(7)
    print(Solution().oddEvenList(root))