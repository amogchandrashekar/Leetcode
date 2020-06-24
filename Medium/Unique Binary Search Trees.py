"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
import math


class Solution:
    def numTrees(self, n):
        return math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1))


if __name__ == "__main__":
    n = 3
    print(Solution().numTrees(n))