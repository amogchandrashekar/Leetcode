import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.hash_map = dict()

        curr = head
        counter = 0

        while curr:
            self.hash_map[counter] = curr.val
            counter += 1
            curr = curr.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.hash_map[random.randint(0, len(self.hash_map) - 1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()