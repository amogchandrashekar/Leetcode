from typing import List
import heapq


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
            1: [0, 1],
            2: [0, -1],
            3: [1, 0],
            4: [-1, 0]
        }

        rows, cols = len(grid), len(grid[0])
        cost = [[float('inf')] * cols for _ in range(rows)]
        cost[0][0] = 0
        heap = [[0, 0, 0]]
        seen = set()

        while heap:

            dist, r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return dist

            if dist > cost[r][c] or (r, c) in seen:
                continue

            seen.add((r, c))

            for direction, (dx, dy) in directions.items():
                cur_dist = dist if direction == grid[r][c] else dist + 1
                dr, dc = dx + r, dy + c
                if dr not in range(rows) or dc not in range(cols) or cost[dr][dc] < cur_dist:
                    continue
                cost[dr][dc] = cur_dist
                heapq.heappush(heap, [cur_dist, dr, dc])


if __name__ == '__main__':
    grid = [[1, 2], [4, 3]]
    print(Solution().minCost(grid))
