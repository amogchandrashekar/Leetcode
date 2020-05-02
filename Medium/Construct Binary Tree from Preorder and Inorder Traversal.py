"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        hash_dict = {node_val: ind for ind, node_val in enumerate(inorder)}

        def recur(low, high):
            if low > high: return None
            root = TreeNode(preorder.pop(0))
            mid = hash_dict[root.val]
            root.left = recur(low, mid - 1)
            root.right = recur(mid + 1, high)
            return root

        return recur(0, len(inorder) - 1)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(Solution().buildTree(preorder, inorder))