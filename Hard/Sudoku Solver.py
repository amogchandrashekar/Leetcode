from typing import List
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        subgrid_hash = defaultdict(set)

        EMPTY = '.'
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]

                if val == EMPTY:
                    continue

                row_hash[r].add(val)
                col_hash[c].add(val)
                subgrid_hash[(r // 3, c // 3)].add(val)

        def dfs(r, c):

            if r == 9:
                return True

            while board[r][c] != EMPTY:
                c += 1

                if c == 9:
                    c = 0
                    r += 1

                if r == 9:
                    return True

            for num in "0123456789":
                if num not in row_hash[r] and num not in col_hash[c] and num not in subgrid_hash[(r // 3, c // 3)]:

                    board[r][c] = num
                    row_hash[r].add(num)
                    col_hash[c].add(num)
                    subgrid_hash[(r // 3, c // 3)].add(num)

                    if dfs(r, c):
                        return True

                    board[r][c] = EMPTY
                    row_hash[r].remove(num)
                    col_hash[c].remove(num)
                    subgrid_hash[(r // 3, c // 3)].remove(num)

            return False

        dfs(0, 0)
        return board


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().solveSudoku(board))