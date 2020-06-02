"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.
(A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = [(root, None, None)]
        ans = 0
        while queue:
            node, parent, grandparent = queue.pop(0)
            if node:
                if grandparent and grandparent % 2 == 0:
                    ans += node.val
                queue.append([node.left, node.val, parent])
                queue.append([node.right, node.val, parent])
        return ans