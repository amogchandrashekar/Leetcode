from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = dict()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col1, col2):
            if col1 not in range(COLS) or col2 not in range(COLS) or row not in range(ROWS):
                return 0

            if (row, col1, col2) in memo:
                return memo[(row, col1, col2)]

            ans = 0
            if col1 == col2:  # selected by one robot
                ans += grid[row][col1]
            else:  # both are selected
                ans += grid[row][col1] + grid[row][col2]

            max_pickable = float('-inf')
            for ind1 in range(-1, 2):
                for ind2 in range(-1, 2):
                    max_pickable = max(max_pickable, dfs(row + 1, col1 + ind1, col2 + ind2))

            memo[(row, col1, col2)] = ans + max_pickable
            return memo[(row, col1, col2)]

        return dfs(0, 0, COLS - 1)


if __name__ == '__main__':
    grid = [[1,1],[1,1]]
    print(Solution().cherryPickup(grid))