from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def flippable(node1, node2):

            if not node1 or not node2:
                return node1 == node2

            return node1.val == node2.val and (
                        (flippable(node1.left, node2.right) and flippable(node1.right, node2.left)) or (
                            flippable(node1.left, node2.left) and flippable(node1.right, node2.right)))

        return flippable(root1, root2)


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.left.right = TreeNode(6)
    root2.right = TreeNode(2)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    root2.right.right.left = TreeNode(8)
    root2.right.right.right = TreeNode(7)

    print(Solution().flipEquiv(root1, root2))



