from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = defaultdict(dict)

        stack = [root]
        parent[root] = None

        while stack:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q:
            if q in ancestors:
                return q
            q = parent[q]

        return None


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(2)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(4)

    print(Solution().lowestCommonAncestor(root, root.left, root.right))