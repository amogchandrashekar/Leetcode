from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy_node = ListNode(next=head)
        wptr = dummy_node

        def get_kth_node(curr, times):
            while curr and times > 0:
                curr = curr.next
                times -= 1
            return curr

        while True:
            kth_node = get_kth_node(wptr, k)
            if not kth_node:
                break

            next_group = kth_node.next

            prev, curr = kth_node.next, wptr.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = wptr.next
            wptr.next = kth_node
            wptr = temp
            
        return dummy_node.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    k = 2
    print(Solution().reverseKGroup(head, k))