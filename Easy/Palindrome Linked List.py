# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(1)

    print(Solution().isPalindrome(head))
