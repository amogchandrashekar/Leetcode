"""
Given a binary tree where each path going from the root to any leaf form a valid sequence,
check if a given string is a valid sequence in such binary tree.

We get the given string from the concatenation of an array of integers arr and
the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
"""


"""
Here I use the phrase "perfect branch" for the branch in the tree where we find arr
and the last number of arr is the leaf node.

Recursive call
Whenever you are at a node, you ask a question:

Whether the value of node is same as value of the number at the current position of the arr?
    If yes -> Check wether the position that you are indexing has reached to the end of the arr.
        If yes -> Check whether this node is the leaf node (i.e. whether the left and right children are both null.
                  If you find a perfect branch, you will reach here and True will be returned.
                  If both of them are not null, this will return False.
        If no -> You recursively call dfs function with left child with position+1 and right child with position+1.
                 At this point, one of the recursive calls will carry back True when you find the perfect branch
                 (as described by the point above). Therefore, you should or the result of both of these calls.
                 One thing to note is that you can even have multiple perfect branches.
        If you don't find any perfect branch while you are exploring with dfs for some branch,
        you will eventually reach to base case and False will be carried back up the recursion stack for that dfs path.
        If no -> forget about this branch -> return False.
You start the whole recursive call with the root node with position 0 (essentially the first character of arr).
And level of the tree you go down, you add 1 to that position.
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root or not arr:
            return False

        def dfs(node, ind):
            if node is None:
                return False

            if node.val == arr[ind]:
                if ind == len(arr) - 1:
                    return node.left is None and node.right is None
                else:
                    return dfs(node.left, ind + 1) or dfs(node.right, ind + 1)

            else:
                return False

        return dfs(root, 0)


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(0)
    root.right.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.left.right = TreeNode(1)
    root.left.right = TreeNode(1)
    root.left.right.left = TreeNode(0)
    root.left.right.right = TreeNode(0)
    arr = [0, 0,0]
    print(Solution().isValidSequence(root, arr))