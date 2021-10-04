from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        all_serialized_trees = defaultdict(int)
        self.result = list()

        def serialize(node):
            if not node:
                return '#'

            tree_hash = serialize(node.left) + ',' + serialize(node.right) + ',' + str(node.val)

            if all_serialized_trees[tree_hash] == 1:
                self.result.append(node)

            all_serialized_trees[tree_hash] += 1

            return tree_hash

        serialize(root)
        return self.result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(4)
    root.right.right = TreeNode(4)
    print(Solution().findDuplicateSubtrees(root))