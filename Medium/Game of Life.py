from typing import List
from collections import defaultdict, Counter


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours = defaultdict(Counter)
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]

        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                for dx, dy in directions:
                    dr, dc = dx + r, dy + c
                    if dr in range(ROWS) and dc in range(COLS):
                        val = board[dr][dc]
                        neighbours[(r, c)][val] += 1
                        neighbours[(r, c)][1 - val] += 0

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                counter_1 = neighbours[(r, c)][1]

                if val == 1 and counter_1 < 2 or counter_1 > 3:
                    board[r][c] = 0
                elif val == 0 and counter_1 == 3:
                    board[r][c] = 1


if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print(Solution().gameOfLife(board))