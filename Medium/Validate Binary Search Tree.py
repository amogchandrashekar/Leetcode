"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example:
    2
   / \
 1    3
Input:
>>> [2, 1, 3]
Output:
>>> True
"""

import numpy as np


# Definition for a binary tree node.
class TreeNode:
    """
    Data structure of tree
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def isValidBST(root: TreeNode, lower_limit=-(np.inf), upper_limit=np.inf) -> bool:
        """
        Function to find if a tree is binary tree or not.
        """
        if not root:
            return True
        value = root.val
        if value <= lower_limit or value >= upper_limit:
            return False
        return Solution.isValidBST(root.left, lower_limit=lower_limit, upper_limit=root.val) and Solution.isValidBST(
            root.right, lower_limit=root.val, upper_limit=upper_limit)


if __name__=="__main__":
    print(Solution.isValidBST([2, 1, 3]))