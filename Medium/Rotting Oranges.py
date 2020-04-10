"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1 instead.

Example:
Input:
    [[2,1,1],[0,1,1],[1,0,1]]
Output:
    -1
Explanation:
    The orange in the bottom left corner (row 2, column 0) is never rotten,
    because rotting only happens 4-directionally.
"""

import heapq


class Solution:
    def orangesRotting(self, grid):
        queue, fresh, distance = list(), list(), 0
        adj = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        row_len = len(grid)
        col_len = len(grid[0])

        for row_index, row in enumerate(grid):
            for col_index, column in enumerate(row):
                if grid[row_index][col_index] == 2:
                    heapq.heappush(queue, [distance, row_index, col_index])
                elif grid[row_index][col_index] == 1:
                    fresh.append([row_index, col_index])

        while queue:
            dist, row, column = heapq.heappop(queue)

            for row_index, col_index in adj:
                new_row, new_column = row + row_index, column + col_index
                if 0 <= new_row < row_len and\
                        0 <= new_column < col_len and\
                        grid[new_row][new_column] == 1:
                    grid[new_row][new_column] = 2
                    distance = max(distance, dist + 1)
                    heapq.heappush(queue, [dist + 1, new_row, new_column])
                    fresh.remove([new_row, new_column])

        return distance if not fresh else -1




if __name__=="__main__":
    grid = [[2],[1],[1],[1],[2],[1],[1]]
    print(Solution().orangesRotting(grid))