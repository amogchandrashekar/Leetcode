# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            for ind, node in enumerate(queue[:-1]):
                node.next = queue[ind + 1]
            temp = list()
            for node in queue:
                temp.extend([node.left, node.right])
            queue = [node for node in temp if node is not None]
        return root


if __name__ == "__main__":
    # root = Node(1)
    # root.left = Node(2)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # root.right = Node(3)
    # root.right.left = Node(6)
    # root.right.right = Node(7)
    root = []
    print(Solution().connect(root))