from collections import namedtuple, defaultdict


class Solution:
    """
    @param M: the 01 matrix
    @return: the longest line of consecutive one in the matrix
    """

    def longestLine(self, grid):

        cache = defaultdict(tuple)
        rows, cols = len(grid), len(grid[0])
        ans = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    cache[(r, c)] = (0, 0, 0, 0)

                else:
                    top = cache[(r - 1, c)][0] if (r - 1, c) in cache else 0
                    left = cache[(r, c - 1)][1] if (r, c - 1) in cache else 0
                    topleft = cache[(r - 1, c - 1)][2] if (r - 1, c - 1) in cache else 0
                    top_right = cache[(r - 1, c + 1)][3] if (r - 1, c + 1) in cache else 0

                    cache[(r, c)] = (grid[r][c] + top, grid[r][c] + left, grid[r][c] + topleft, grid[r][c] + top_right)
                    ans = max(ans, max(cache[(r, c)]))
        return ans


if __name__ == '__main__':
    m = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    print(Solution().longestLine(m))
