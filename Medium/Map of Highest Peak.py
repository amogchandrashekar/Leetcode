from typing import List
from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])

        result = [[None] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    result[r][c] = 0
                    queue.append([0, r, c])

        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while queue:
            dist, r, c = queue.popleft()

            for dx, dy in dirs:
                dr, dc = dx + r, dy + c

                if dr not in range(rows) or dc not in range(cols) or result[dr][dc] is not None:
                    continue

                result[dr][dc] = dist + 1
                queue.append([dist + 1, dr, dc])

        return result