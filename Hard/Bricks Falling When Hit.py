class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """

        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # remove all the hits from the grid
        for r, c in hits:
            grid[r][c] -= 1

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                return 0

            grid[r][c] = 2
            connected_components = 1

            for dx, dy in directions:
                dr, dc = dx + r, dy + c
                connected_components += dfs(dr, dc)

            return connected_components

        # mark all the connected components to 2 which would remain after all the hits
        for c in range(cols):
            dfs(0, c)

        def is_connected(r, c):
            if r == 0:
                return True

            for dx, dy in directions:
                dr, dc = dx + r, dy + c
                if dr in range(rows) and dc in range(cols) and grid[dr][dc] == 2:
                    return True

            return False

        res = [0] * len(hits)
        for ind in reversed(range(len(hits))):
            r, c = hits[ind]
            grid[r][c] += 1
            if grid[r][c] != 1 or not is_connected(r, c):
                continue
            res[ind] = dfs(r, c) - 1
        return res


if __name__ == '__main__':
    grid = [[1], [1], [1], [1], [1]]
    hits = [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]
    print(Solution().hitBricks(grid, hits))
