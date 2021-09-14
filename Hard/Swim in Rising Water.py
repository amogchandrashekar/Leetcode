from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        heap = [[grid[0][0], 0, 0, grid[0][0]]]  # dist r c

        while heap:
            cur_dist, r, c, prev_val = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return cur_dist

            if cur_dist > dist[r][c]:
                continue

            for dx, dy in directions:
                dr, dc = r + dx, c + dy

                if dr not in range(rows) or dc not in range(cols):
                    continue

                if grid[dr][dc] <= prev_val and dist[dr][dc] > cur_dist:
                    heapq.heappush(heap, [cur_dist, dr, dc, prev_val])
                    dist[dr][dc] = cur_dist
                elif grid[dr][dc] > prev_val and dist[dr][dc] > cur_dist + (grid[dr][dc] - prev_val):
                    heapq.heappush(heap, [grid[dr][dc] - prev_val + cur_dist, dr, dc, grid[dr][dc]])
                    dist[dr][dc] = cur_dist + grid[dr][dc] - prev_val


if __name__ == '__main__':
    grid = [[0, 0], [0, 5]]
    print(Solution().swimInWater(grid))
