class Solution:
    def isBalanced(self, root) -> bool:
        def height(node):
            if not node:
                return -1

            left = height(node.left)
            right = height(node.right)
            return 1 + max(left, right)

        def is_balanced(node):
            if not node:
                return True

            left = height(node.left)
            right = height(node.right)
            return abs(left - right) <= 1 and is_balanced(node.left) and is_balanced(node.right)

        return is_balanced(root)