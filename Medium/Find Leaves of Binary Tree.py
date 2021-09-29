from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.leaves = defaultdict(list)

        def find_height(node):

            if not node:
                return -1

            left = find_height(node.left)
            right = find_height(node.right)
            max_height = 1 + max(left, right)
            self.leaves[max_height].append(node.val)
            return max_height

        return list(self.leaves.values())