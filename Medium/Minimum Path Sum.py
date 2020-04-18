"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output:
 7
Explanation:
    Because the path 1→3→1→1→1 minimizes the sum
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # add the values cumulatively for the first row (as we can only move in right direction to reach them)
        for i in range(1, cols):
            grid[0][i] += grid[0][i - 1]

        # add the values cumulatively for the first column (as we can only move in bottom direction to reach them)
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]

        # add the one which is minimum between upper and left value, grid is updated in place
        for row_index in range(1, rows):
            for col_index in range(1, cols):
                grid[row_index][col_index] += min(grid[row_index - 1][col_index], grid[row_index][col_index - 1])

        return grid[rows - 1][cols - 1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))