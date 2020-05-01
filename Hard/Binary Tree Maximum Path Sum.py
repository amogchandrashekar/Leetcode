"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the
parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal max_path_sum

            if not node:
                return 0

            # limit by zero to avoid their contribution if node, left and right all are -ve
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # check if all three sum is greater than the global maxima
            max_path_sum = max(max_path_sum, node.val + left + right)
            return node.val + max(left, right) # return either left or right branch contribution

        max_path_sum = float("-inf")
        max_path_sum = dfs(root)
        return max_path_sum


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    root.right.left = TreeNode(13)
    print(Solution().maxPathSum(root))