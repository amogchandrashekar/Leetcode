from typing import List


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = dict()
        parent[root] = None

        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        seen = set()
        level = 0
        queue = [target]

        while queue:
            if level == k:
                return [node.val for node in queue]

            next_level = []
            for node in queue:

                seen.add(node)

                if node.left and node.left not in seen:
                    next_level.append(node.left)
                if node.right and node.right not in seen:
                    next_level.append(node.right)
                if node in parent and parent[node] not in seen:
                    if not parent[node]:
                        continue
                    next_level.append(parent[node])
            level += 1
            queue = next_level

        return []


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(6)
    tree.right.right = TreeNode(7)

    k = 2
    x = 3
    print(Solution().distanceK(tree, x, k))