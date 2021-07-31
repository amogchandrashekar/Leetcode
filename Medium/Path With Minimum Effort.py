import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        min_heap = [[0, 0, 0]]
        distances = [[float('inf')] * COLS for _ in range(ROWS)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while min_heap:
            dist, r, c = heapq.heappop(min_heap)

            if dist > distances[r][c]:
                continue

            if r == ROWS - 1 and c == COLS - 1:
                return dist

            for dx, dy in directions:
                dr, dc = r + dx, c + dy
                if dr in range(ROWS) and dc in range(COLS):
                    new_dist = max(dist, abs(heights[dr][dc] - heights[r][c]))
                    if new_dist < distances[dr][dc]:
                        heapq.heappush(min_heap, (new_dist, dr, dc))
                        distances[dr][dc] = new_dist


if __name__ == '__main__':
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(Solution().minimumEffortPath(heights))
