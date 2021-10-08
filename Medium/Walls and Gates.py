from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows = len(rooms)
        cols = len(rooms[0])

        queue = list()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append([r, c])

        dist = 0
        while queue:
            next_level = []

            for r, c in queue:
                for dx, dy in dirs:
                    dr = r + dx
                    dc = c + dy

                    if dr in range(rows) and dc in range(cols) and rooms[dr][dc] == 2147483647:
                        rooms[dr][dc] = dist + 1
                        next_level.append([dr, dc])
            dist += 1
            queue = next_level
