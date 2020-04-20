"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a
value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal
displays the value of the node first, then traverses node.left, then traverses node.right.)
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, pre_order: List[int]) -> TreeNode:

        def dfs(arr=[], upper_limit=float("inf")):
            if arr and arr[0] < upper_limit:
                val = arr.pop(0)
                root = TreeNode(val)
                root.left = dfs(arr, val)
                root.right = dfs(arr, upper_limit)
                return root
        return dfs(pre_order)


if __name__ == "__main__":
    pre_order = [8, 5, 1, 7, 10, 12]
    print(Solution().bstFromPreorder(pre_order))