from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        def get_max_path(node):
            if not node:
                return 0

            left = get_max_path(node.left)
            right = get_max_path(node.right)

            left_count = left + 1 if node.left and node.val == node.left.val else 0
            right_count = right + 1 if node.right and node.val == node.right.val else 0

            cur_longest_path = left_count + right_count
            self.longest_path = max(self.longest_path, cur_longest_path)
            return max(left_count, right_count)

        get_max_path(root)
        return self.longest_path


if __name__ == '__main__':
    root = TreeNode(5)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    print(Solution().longestUnivaluePath(root))
