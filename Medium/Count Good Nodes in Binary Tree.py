"""
Given a binary tree root,
a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = [(root, root.val)]
        counter = 0
        while queue:
            node, max_val = queue.pop(0)
            if node.val >= max_val:
                counter += 1
            if node.left:
                queue.append((node.left, max(node.left.val, max_val)))
            if node.right:
                queue.append((node.right, max(node.right.val, max_val)))
        return counter
