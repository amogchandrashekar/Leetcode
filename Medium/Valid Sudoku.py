from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_hash_map = defaultdict(set)
        cols_hash_map = defaultdict(set)
        subgrid_hash_map = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue

                sudoku_val = board[r][c]
                if sudoku_val in rows_hash_map[r] or sudoku_val in cols_hash_map[c] or sudoku_val in subgrid_hash_map[
                    (r // 3, c // 3)]:
                    return False

                subgrid_hash_map[(r // 3, c // 3)].add(sudoku_val)
                rows_hash_map[r].add(sudoku_val)
                cols_hash_map[c].add(sudoku_val)

        return True