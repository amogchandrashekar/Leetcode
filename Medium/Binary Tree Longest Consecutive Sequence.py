class Solution:
    def longestConsecutive(self, root: 'TreeNode') -> int:
        def longest_path(root):
            if not root:
                return 0
            length = 1
            l = longest_path(root.left)
            r = longest_path(root.right)
            if root.left and root.left.val == root.val + 1:
                length = max(length, 1 + l)
            if root.right and root.right.val == root.val + 1:
                length = max(length, 1 + r)
            res[0] = max(res[0], length)
            return length

        res = [0]
        longest_path(root)
        return res[0]