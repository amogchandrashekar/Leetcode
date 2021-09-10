from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0]) if rows else 0

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        entrance_x, entrance_y = entrance

        queue = deque([[0, entrance_x, entrance_y]])
        seen = set()
        seen.add((entrance_x, entrance_y))

        def is_reached(r, c):
            if r == entrance_x and c == entrance_y:
                return False
            for dx, dy in directions:
                dr, dc = r + dx, c + dy
                if dr not in range(rows) or dc not in range(cols):
                    return True
            return False

        while queue:
            dist, r, c = queue.popleft()

            if is_reached(r, c):
                return dist

            for dx, dy in directions:
                dr, dc = dx + r, dy + c

                if dr not in range(rows) or dc not in range(cols):
                    continue

                if (dr, dc) not in seen and maze[dr][dc] == '.':
                    queue.append([dist + 1, dr, dc])
                    seen.add((dr, dc))

        return -1

