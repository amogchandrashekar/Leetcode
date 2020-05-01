# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left_node, right_node):
            if left_node and right_node:
                return (left_node.val == right_node.val) and dfs(left_node.left, right_node.right)\
                       and dfs(left_node.right, right_node.left)
            else:
                return left_node == right_node

        if not root:
            return True
        return dfs(root.left, root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))