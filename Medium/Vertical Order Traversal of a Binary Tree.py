"""
Given a binary tree, return the vertical order traversal of its nodes values.
For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report
the values of the nodes in order from top to bottom (decreasing Y coordinates).
If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

         3
       /  \
     9     20
          /  \
        15    7
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
"""

from collections import defaultdict
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def verticalTraversal(root: TreeNode) -> List[List[int]]:
        """
        Finding vertical distance using iteration
        """
        stack = list()
        stack.append([root, 0])
        horizontal_dist = defaultdict(list)
        while stack:
            node, dist = stack.pop(-1)
            if not node:
                continue
            horizontal_dist[dist].append(node.val)
            stack.append([node.left, dist - 1])
            stack.append([node.right, dist + 1])

        answer = list()
        for dist in sorted(horizontal_dist):
            answer.append(horizontal_dist[dist])

        return answer