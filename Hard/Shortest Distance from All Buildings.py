from typing import List
import math
from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        total_sum = [[0] * cols for _ in range(rows)]

        def bfs(r, c, step):
            queue = deque([[r, c, 0]])
            min_dist = float('inf')

            while queue:
                cur_row, cur_col, dist = queue.popleft()

                for dx, dy in dirs:
                    next_row, next_col = cur_row + dx, cur_col + dy

                    if next_row in range(rows) and next_col in range(cols) and grid[next_row][next_col] == -step:
                        grid[next_row][next_col] -= 1
                        total_sum[next_row][next_col] += dist + 1
                        min_dist = min(min_dist, total_sum[next_row][next_col])
                        queue.append([next_row, next_col, dist + 1])

            return min_dist

        step = 0
        for cur_row in range(rows):
            for cur_col in range(cols):
                if grid[cur_row][cur_col] == 1:
                    min_dist = bfs(cur_row, cur_col, step)
                    step += 1

                    if min_dist == float('inf'):
                        return -1

        return min_dist


if __name__ == '__main__':
    grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    print(Solution().shortestDistance(grid))
