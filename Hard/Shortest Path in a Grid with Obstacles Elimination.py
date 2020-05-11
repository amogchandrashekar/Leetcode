"""
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



Example 1:

Input:
grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).


Example 2:

Input:
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
Output: -1
Explanation:
We need to eliminate at least two obstacles to find such a walk.


Constraints:

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
"""

from typing import List
import collections


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        q = collections.deque([(0, 0, 0, 0)])
        m, n = len(grid), len(grid[0])
        visited = set()

        while q:
            x, y, obstacle, path = q.popleft()
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1 and obstacle < k and (i, j, obstacle + 1) not in visited:
                        visited.add((i, j, obstacle + 1))
                        q.append((i, j, obstacle + 1, path + 1))
                    if grid[i][j] == 0 and (i, j, obstacle) not in visited:
                        if (i, j) == (m - 1, n - 1):
                            return path + 1
                        visited.add((i, j, obstacle))
                        q.append((i, j, obstacle, path + 1))

        return -1


if __name__ == "__main__":
    grid = [[0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0]]
    k = 1
    print(Solution().shortestPath(grid, k))
