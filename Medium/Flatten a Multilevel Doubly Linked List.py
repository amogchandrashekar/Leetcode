"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        stack = []
        dummy = Node(-1, None, None, None)
        dummy.next = head

        while head:

            if head.child:
                if head.next:
                    temp = head.next
                    temp.prev = None
                    stack.append(temp)
                child = head.child
                child.prev = head
                head.next = child
                head.child = None

            if not head.next and stack:
                curr = stack.pop()
                head.next = curr
                curr.prev = head

            head = head.next

        return dummy.next