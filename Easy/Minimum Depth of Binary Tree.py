"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = float("Inf")
        stack = [[root, 1]]
        
        while stack:
            node, dep = stack.pop()
            if not node.right and not node.left:
                depth = min(dep, depth)
            if node.left and depth > dep + 1:
                stack.append([node.left, dep + 1])
            if node.right and depth > dep + 1:
                stack.append([node.right, dep + 1])
                
        return depth
