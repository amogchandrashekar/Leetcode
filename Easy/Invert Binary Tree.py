"""
Invert a binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.extend([node.left, node.right])
        return root