from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows, cols = len(land), len(land[0])
        seen = set()
        ans = list()

        def dfs(r, c):
            stack = [[r, c]]
            max_r, max_c = r, c
            seen.add((r, c))

            while stack:
                r, c = stack.pop()
                max_r = max(max_r, r)
                max_c = max(max_c, c)

                for dx, dy in directions:
                    dr, dc = r + dx, c + dy
                    if dr in range(rows) and dc in range(cols) and land[dr][dc] == 1 and (dr, dc) not in seen:
                        stack.append([dr, dc])
                        seen.add((dr, dc))

            return max_r, max_c

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and land[r][c] == 1:
                    ans.append([r, c, *dfs(r, c)])

        return ans