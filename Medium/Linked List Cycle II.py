# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        cycle_found = False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                cycle_found = True
                break

            slow = slow.next
            fast = fast.next.next

        if not cycle_found:
            return None

        orig = slow.next
        loop_length = 0
        while orig != slow:
            orig = orig.next
            loop_length += 1

        end = head
        while loop_length:
            end = end.next
            loop_length -= 1

        orig = head
        while orig != end.next:
            orig = orig.next
            end = end.next
        return orig


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(Solution().detectCycle(head))
