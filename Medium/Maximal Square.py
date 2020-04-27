"""
Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(row) for row in matrix]
        max_side = 0

        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[row_index])):
                if (row_index == 0 or col_index == 0) and matrix[row_index][col_index] == "1":
                    dp[row_index][col_index] = 1
                else:
                    if matrix[row_index][col_index] == "1":
                        dp[row_index][col_index] = int(min(dp[row_index - 1][col_index - 1],
                                                           dp[row_index - 1][col_index],
                                                           dp[row_index][col_index - 1])) + 1
                max_side = max(max_side, dp[row_index][col_index])

        return max_side * max_side


if __name__ == "__main__":
    matrix = [["1", "1", "1", "1"], ["1", "1", "1", "1"], ["1", "1", "1", "1"]]
    print(Solution().maximalSquare(matrix))
