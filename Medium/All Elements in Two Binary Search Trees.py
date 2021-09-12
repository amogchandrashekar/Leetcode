# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.stack = list()
        self.add_left_nodes(root)

    def add_left_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        if not self.stack:
            return None

        node = self.stack.pop()
        if node.right:
            self.add_left_nodes(node.right)
        return node.val


class Solution:

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.iterator1 = BSTIterator(root1)
        self.iterator2 = BSTIterator(root2)

        root1_val, root2_val = self.iterator1.next(), self.iterator2.next()
        merged = list()

        while root1_val is not None and root2_val is not None:
            if root1_val <= root2_val:
                merged.append(root1_val)
                root1_val = self.iterator1.next()
            else:
                merged.append(root2_val)
                root2_val = self.iterator2.next()

        while root1_val is not None:
            merged.append(root1_val)
            root1_val = self.iterator1.next()
        while root2_val is not None:
            merged.append(root2_val)
            root2_val = self.iterator2.next()

        return merged


if __name__ == '__main__':
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)

    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(3)

    print(Solution().getAllElements(root1, root2))


