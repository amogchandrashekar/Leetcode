from typing import Optional
from functools import lru_cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        self.cameras = 0

        # 1 -> is monitored
        # 2 -> has a camera on it
        # 0 -> needs to be monitored

        def dfs(node):

            if not node:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.cameras += 1
                return 2

            elif left == 2 or right == 2:
                return 1

            else:
                return 0

        is_root_monitored = dfs(root)
        return self.cameras + 1 if is_root_monitored == 0 else self.cameras


if __name__ == '__main__':
    root = TreeNode()
    root.left = TreeNode()
    root.left.left = TreeNode()
    root.left.right = TreeNode()
    print(Solution().minCameraCover(root))