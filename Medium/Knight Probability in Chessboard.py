class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        total_moves = 8 ** k

        memo = dict()

        def dfs(r, c, rem):

            if rem == 0:
                return 1

            if (r, c, rem) in memo:
                return memo[(r, c, rem)]

            ans = 0
            for dx, dy in directions:
                dr, dc = dx + r, dy + c
                if dr in range(n) and dc in range(n):
                    ans += dfs(dr, dc, rem - 1)
            memo[(r, c, rem)] = ans

            return ans

        return dfs(row, column, k) / total_moves


if __name__ == '__main__':
    n = 8
    k = 30
    row = 6
    column = 4
    print(Solution().knightProbability(n, k, row, column))