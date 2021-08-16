# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node):
            if not node:
                return 'None'

            if node:
                return str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')

        def dfs(ind):
            if ind >= len(data) or data[ind] == 'None':
                return None

            root = TreeNode(data[ind])
            root.left = dfs(ind + 1)
            if not root.left:
                root.right = dfs(ind + 2)
            return root

        return dfs(0)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
    print(ans)