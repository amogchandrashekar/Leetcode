from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return 0

            if r not in range(len(grid)) or c not in range(len(grid[r])) or grid[r][c] == 0:
                return 1

            perimeter = 0
            visited.add((r, c))
            for x, y in directions:
                perimeter += dfs(r + x, c + y)
            return perimeter

        for row_id in range(len(grid)):
            for col_id in range(len(grid[row_id])):
                if grid[row_id][col_id] == 1:
                    return dfs(row_id, col_id)


if __name__ == '__main__':
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(Solution().islandPerimeter(grid))