from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)

        return root if root.val == 1 or root.left or root.right else None


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(0)
    tree.right.left = TreeNode(0)
    tree.right.right = TreeNode(1)
    print(Solution().pruneTree(tree))
