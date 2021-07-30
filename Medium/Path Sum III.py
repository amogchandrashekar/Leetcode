from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        target_paths = 0
        if not root:
            return target_paths

        def dfs(node, cur_path, cur_sum):
            if cur_sum - targetSum in cur_path:
                nonlocal target_paths
                target_paths += cur_path[cur_sum - targetSum]

            cur_path[cur_sum] += 1
            if node.left:
                dfs(node.left, cur_path, cur_sum + node.left.val)
            if node.right:
                dfs(node.right, cur_path, cur_sum + node.right.val)
            cur_path[cur_sum] -= 1

        cur = defaultdict(int)
        cur[0] = 1

        dfs(root, cur, root.val)
        return target_paths