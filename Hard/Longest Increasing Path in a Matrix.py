from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_pathlen = 0
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        seen = set()
        memo = dict()

        def dfs(r, c, prev_val):

            if matrix[r][c] <= prev_val:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]

            seen.add((r, c))
            decision_tree = [0]
            for dx, dy in directions:
                if (r + dx, c + dy) not in seen and r + dx in range(rows) and c + dy in range(cols):
                    decision_tree.append(dfs(r + dx, c + dy, matrix[r][c]))
            memo[(r, c)] = 1 + max(decision_tree)
            seen.remove((r, c))
            return memo[(r, c)]

        for r in range(rows):
            for c in range(cols):
                max_pathlen = max(max_pathlen, dfs(r, c, float('-inf')))

        return max_pathlen


if __name__ == '__main__':
    matrix = [[13, 5, 13, 9], [5, 0, 2, 9], [10, 13, 11, 10], [0, 0, 13, 13]]
    print(Solution().longestIncreasingPath(matrix))
