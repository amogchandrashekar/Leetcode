from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        node = self.queue[0]
        par_val = node.val if node else None

        if not node.left:
            node.left = TreeNode(val)
            self.queue.append(node.left)
        else:
            self.queue.popleft()
            node.right = TreeNode(val)
            self.queue.append(node.right)

        return par_val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)

    obj = CBTInserter(root)
    print(obj.insert(3))
    print(obj.insert(4))
    obj.get_root()

