"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary
search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs
by more than one.
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def create_tree(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = create_tree(l, mid - 1)
            root.right = create_tree(mid + 1, r)
            return root

        return create_tree(0, len(nums) - 1)