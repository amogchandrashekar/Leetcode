"""
Given a binary tree where node values are digits from 1 to 9.
A path in the binary tree is said to be pseudo-palindromic
if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        queue = collections.deque([(root, 0)])
        ans = 0
        while queue:
            node, flag = queue.popleft()
            flag ^= 1 << node.val
            if node.left:
                queue.append((node.left, flag))
            if node.right:
                queue.append((node.right, flag))
            if not node.left and not node.right:  # leaf
                if not flag or ((~flag + 1) & flag == flag):
                    ans += 1
        return ans


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.right = TreeNode(1)
    root.right.right = TreeNode(1)
    print(Solution().pseudoPalindromicPaths(root))
