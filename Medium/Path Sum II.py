"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, p_sum: int) -> List[List[int]]:

        if not root:
            return []

        def dfs(node, path, path_sum):
            nonlocal answer
            if node and not node.left and not node.right and path_sum + node.val == p_sum:
                answer.append(path + [node.val])
                return
            if node.left:
                dfs(node.left, path + [node.val], path_sum + node.val)
            if node.right:
                dfs(node.right, path + [node.val], path_sum + node.val)

        answer = list()
        dfs(root, [], 0)
        return answer