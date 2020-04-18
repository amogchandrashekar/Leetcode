"""
A robot is located at the top-left corner of a m x n grid

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initiate grid with ones, then no need to re initialise first row and first column to 1
        # (as there exists only one way)
        grid = [[1] * m for _ in range(n)]

        # the number of ways to reach a cell is sum of number of ways to reach the cell to its left and its top
        for row_index in range(1, n):
            for col_index in range(1, m):
                grid[row_index][col_index] = grid[row_index - 1][col_index] + grid[row_index][col_index - 1]

        return grid[-1][-1]


if __name__ == "__main__":
    Solution().uniquePaths(7, 3)