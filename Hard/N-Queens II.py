"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution():
    def totalNQueens(self, n):
        def dfs(queens, xy_dif, xy_sum):
            row_index = len(queens)
            if len(queens) == n:
                result[0] += 1
                return

            for col_index in range(n):
                if col_index not in queens: # If the queen is not in the same column
                    if row_index - col_index not in xy_dif: # If the queen is not in diagonal (start from top left to bottom right)
                        if row_index + col_index not in xy_sum: # If the queen is not in diagonal (start from top right to bottom left)
                            dfs(queens + [col_index], xy_dif + [row_index - col_index], xy_sum + [row_index + col_index])

        result = [0]
        dfs([], [], [])
        return result[0]