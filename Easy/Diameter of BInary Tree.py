"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree

    1
   / \
  2   3
 / \
4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(node):
            nonlocal diameter
            if node is None:
                return 0
            lheight = height(node.left)
            rheight = height(node.right)
            diameter = max(diameter, lheight + rheight)
            return 1 + max(lheight, rheight)

        diameter = 0
        if root:
            height(root)
        return diameter


if __name__ == "__main__":
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(node))
