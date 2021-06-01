from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        seen = [[False] * len(grid[i]) for i in range(len(grid))]
        ans = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row_id, col_id):
            area = 0
            stack = [(row_id, col_id)]
            seen[row_id][col_id] = True

            while stack:
                area += 1
                r, c = stack.pop()
                for x, y in directions:
                    if r + x in range(rows) and c + y in range(cols) and not seen[r + x][c + y] and grid[r + x][c + y] == 1:
                        stack.append([r + x, c + y])
                        seen[r + x][c + y] = True
            return area

        for rid in range(rows):
            for cid in range(cols):
                if not seen[rid][cid] and grid[rid][cid] == 1:
                    area = dfs(rid, cid)
                    ans = max(area, ans)

        return ans


if __name__ == '__main__':
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(Solution().maxAreaOfIsland(grid))