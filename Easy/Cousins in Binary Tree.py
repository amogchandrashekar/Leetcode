"""
n a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [[root, None]]
        while queue:
            same_level, temp = dict(), list()
            for node, parent_val in queue:
                temp.append([node.left, node.val])
                temp.append([node.right, node.val])
                same_level[node.val] = parent_val
            if x in same_level and y in same_level and same_level[x] != same_level[y]:
                return True
            if x in same_level or y in same_level:
                return False
            queue = [[node, val] for node, val in temp if node]
        return False


if __name__ == "__main__":
    root = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.left = TreeNode(9)
    root.right.left.right = TreeNode(6)
    root.left = TreeNode(7)
    root.left.left = TreeNode(1)
    print(Solution().isCousins(root, 10, 15))
