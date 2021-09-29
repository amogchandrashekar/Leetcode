from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def check_valid_subtree(node, node_val):
            if not node:
                return True

            left = check_valid_subtree(node.left, node.val)
            right = check_valid_subtree(node.right, node.val)

            if left and right:
                self.ans += 1

            return left and right and node.val == node_val

        check_valid_subtree(root, None)
        return self.ans