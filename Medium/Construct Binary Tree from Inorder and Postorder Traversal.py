"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hash_dict = {node:ind for ind, node in enumerate(inorder)}
        def recur(low, high):
            if low > high: return None
            root = TreeNode(postorder.pop())
            mid = hash_dict[root.val]
            root.right = recur(mid + 1, high)
            root.left = recur(low, mid - 1)
            return root
        return recur(0, len(postorder) - 1)


if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    print(Solution().buildTree(inorder, postorder))