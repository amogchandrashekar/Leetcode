from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        h, w = len(grid2), len(grid2[0])
        seen = set()

        def dfs(rid, cid):
            island = []
            stack = [[rid, cid]]
            seen.add((rid, cid))
            island.append([rid, cid])

            while stack:
                r, c = stack.pop()
                for x, y in directions:
                    if r + x in range(h) and c + y in range(w) and (r + x, c + y) not in seen and grid2[r + x][c + y] == 1:
                        stack.append([r + x, c + y])
                        seen.add((r + x, c + y))
                        island.append([r + x, c + y])
            return island

        islands = []
        for r in range(h):
            for c in range(w):
                if (r, c) not in seen and grid2[r][c] == 1:
                    islands.append(dfs(r, c))

        not_island = 0
        for island in islands:
            for r, c in island:
                if grid1[r][c] != 1:
                    not_island += 1
                    break

        return len(islands) - not_island



if __name__ == "__main__":
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    print(Solution().countSubIslands(grid1, grid2))