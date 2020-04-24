"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        heap = list()
        for cur_head in lists:
            while cur_head:
                heap.append(cur_head.val)
                cur_head = cur_head.next

        res = cur = ListNode(0)
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        return res.next


if __name__=="__main__":
    listnodes = list()
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)
    listnodes.append(a)
    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    listnodes.append(b)
    print(listnodes)
    print(Solution().mergeKLists(listnodes))