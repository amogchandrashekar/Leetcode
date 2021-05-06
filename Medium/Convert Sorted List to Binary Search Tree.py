"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        head_list = list()
        while head:
            head_list.append(head.val)
            head = head.next

        def create_bst(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(head_list[mid])
            root.left = create_bst(l, mid - 1)
            root.right = create_bst(mid + 1, r)
            return root

        return create_bst(0, len(head_list) - 1)