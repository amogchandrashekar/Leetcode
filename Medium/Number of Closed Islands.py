from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        def dfs(r, c):
            stack = [[r, c]]
            seen.add((r, c))
            is_island = True

            while stack:
                r, c = stack.pop()

                for dx, dy in directions:
                    dr, dc = r + dx, c + dy

                    if dr not in range(rows) or dc not in range(cols):
                        is_island = False
                        continue

                    if (dr, dc) not in seen and grid[dr][dc] == 0:
                        seen.add((dr, dc))
                        stack.append((dr, dc))

            return is_island

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in seen and dfs(r, c):
                    islands += 1

        return islands