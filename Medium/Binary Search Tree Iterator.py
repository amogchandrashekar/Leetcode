from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.add_left(root)

    def add_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.add_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right= TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    bSTIterator = BSTIterator(root)
    print(bSTIterator.next())
    print(bSTIterator.next())
    print(bSTIterator.hasNext())
    print(bSTIterator.next())
    print(bSTIterator.hasNext())
    print(bSTIterator.next())
    print(bSTIterator.hasNext())
    print(bSTIterator.next())
    print(bSTIterator.hasNext())
