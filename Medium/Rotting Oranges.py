"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1 instead.

Example:
Input:
    [[2,1,1],[0,1,1],[1,0,1]]
Output:
    -1
Explanation:
    The orange in the bottom left corner (row 2, column 0) is never rotten,
    because rotting only happens 4-directionally.
"""
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        queue = deque()
        row_len, col_len = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 2:
                    queue.append([r, c, 0])
                elif grid[r][c] == 1:
                    fresh.add((r, c))

        max_minute = 0

        while queue:
            r, c, minute = queue.popleft()
            if not fresh:
                return max_minute

            for dx, dy in directions:
                dr, dc = r + dx, c + dy
                if dr in range(row_len) and dc in range(col_len) and grid[dr][dc] == 1:
                    fresh.remove((dr, dc))
                    grid[dr][dc] = 2
                    queue.append([dr, dc, minute + 1])
                    max_minute = max(max_minute, minute + 1)

        return max_minute if not fresh else -1


if __name__ == "__main__":
    grid = [[1, 0, 0, 0, 2, 1, 0]]
    print(Solution().orangesRotting(grid))
