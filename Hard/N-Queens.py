"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle
"""


class Solution:
    def solveNQueens(self, n):
        def dfs(queens, xy_dif, xy_sum):
            row_index = len(queens)
            if len(queens) == n:
                result.append(queens)
                return

            for col_index in range(n):
                if col_index not in queens: # If the queen is not in the same column
                    if row_index - col_index not in xy_dif: # If the queen is not in diagonal (start from top left to bottom right)
                        if row_index + col_index not in xy_sum: # If the queen is not in diagonal (start from top right to bottom left)
                            dfs(queens + [col_index], xy_dif + [row_index - col_index], xy_sum + [row_index + col_index])

        result = list()
        dfs([], [], [])
        return [["".join("." if i != col_index else "Q" for i in range(n)) for col_index in answer] for answer in result]


if __name__ == "__main__":
    size = 4
    print(Solution().solveNQueens(size))
