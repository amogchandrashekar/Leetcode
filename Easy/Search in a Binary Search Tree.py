# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.val == val:
                return node
            elif node.val < val and node.right:
                queue.append(node.right)
            elif node.left:
                queue.append(node.left)

        return None