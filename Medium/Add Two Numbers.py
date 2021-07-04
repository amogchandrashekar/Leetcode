# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        new_ll = dummy

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            value = l1_val + l2_val + carry
            carry = value // 10
            value = value % 10
            new_ll.next = ListNode(value)
            new_ll = new_ll.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)

    ll = Solution().addTwoNumbers(l1, l2)
    while ll:
        print(ll.val)
        ll = ll.next