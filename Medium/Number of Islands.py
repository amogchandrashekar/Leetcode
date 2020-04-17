"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        seen = [[False] * len(row) for row in grid]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        queue = []

        def bfs():
            while queue:
                row_index, col_index = queue.pop()
                if not seen[row_index][col_index]:
                    seen[row_index][col_index] = True
                    for x, y in directions:
                        if 0 <= x + row_index < len(grid) and 0 <= y + col_index < len(grid[row_index]) and \
                                grid[x + row_index][y + col_index] == "1" and not seen[x + row_index][y + col_index]:
                            queue.append([x + row_index, y + col_index])

        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == "1" and not seen[row_index][col_index]:
                    queue.append([row_index, col_index])
                    bfs()
                    islands += 1

        return islands

if __name__ == "__main__":
    grid = [list("11000"), list("11000"), list("00100"), list("00011")]
    print(Solution().numIslands(grid))