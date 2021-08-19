"""
Definition for a binary tree node.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return root

        parent = dict()
        stack = [root]
        parent[root] = None

        while stack:
            node = stack.pop()

            if node.val == p:
                if node.right:
                    curr = node.right
                    while curr.left:
                        curr = curr.left
                    return curr

                else:
                    par = parent[node]
                    while par and par.val < p:
                        par = parent[par]
                    return par

            if node.left:
                parent[node.left] = node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        return None


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(Solution().inorderSuccessor(root, 1))