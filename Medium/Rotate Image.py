from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        transpose_len = len(matrix)
        for row_ind in range(transpose_len // 2):
            transpose_row = transpose_len - row_ind - 1
            for ind in range(len(matrix[row_ind])):
                matrix[row_ind][ind], matrix[transpose_row][ind] = matrix[transpose_row][ind], matrix[row_ind][ind]

        row_len, col_len = len(matrix), len(matrix[0])
        row, col = 0, 0
        while row < row_len and col < col_len:
            for temp_col in range(col, col_len):
                matrix[row][temp_col], matrix[temp_col][row] = matrix[temp_col][row], matrix[row][temp_col]
            row += 1
            col += 1
