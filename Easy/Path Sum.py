"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values
along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = [[root, sum - root.val]]
        while stack:
            cur, curr_sum = stack.pop()
            if not cur.left and not cur.right and curr_sum == 0:
                return True
            if cur.right:
                stack.append((cur.right, curr_sum - cur.right.val))
            if cur.left:
                stack.append((cur.left, curr_sum - cur.left.val))
        return False


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(Solution().hasPathSum(root, 22))