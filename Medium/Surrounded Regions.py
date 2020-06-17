"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        seen = [[False for _ in range(len(board[i]))] for i in range(len(board))]

        def dfs(r, c):
            queue = [[r, c]]
            directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            while queue:
                row, col = queue.pop()
                seen[row][col] = True
                zeroes.add((row, col))
                for x, y in directions:
                    r, c = row + x, col + y
                    if (0 <= r < len(board)) and (0 <= c < len(board[0])) and not seen[r][c] and board[r][c] == "O":
                        queue.append([r, c])

        zeroes = set()
        rows, cols = [0, len(board) - 1], [0, len(board[0]) - 1]
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r in rows or c in cols) and board[r][c] == "O" and not seen[r][c]:
                    dfs(r, c)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r, c) not in zeroes:
                    board[r][c] = "X"


if __name__ == "__main__":
    grid = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    print(Solution().solve(grid))
