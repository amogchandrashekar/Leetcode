# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def splitBST(self, root, target):
        if not root:
            return [None, None]

        if root.val > target:
            left, right = self.splitBST(root.left, target)
            root.left = right
            return [left, root]
        else:
            left, right = self.splitBST(root.right, target)
            root.right = left
            return [root, right]


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print(Solution().splitBST(root, 2
                              ))