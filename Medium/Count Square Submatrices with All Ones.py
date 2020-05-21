"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.


Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        counter = 0
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[row_index])):
                if row_index != 0 and col_index != 0 and matrix[row_index][col_index] != 0:
                    matrix[row_index][col_index] = min(matrix[row_index][col_index - 1], matrix[row_index - 1][col_index], matrix[row_index - 1][col_index - 1]) + 1
                counter += matrix[row_index][col_index]
        return counter


if __name__ == "__main__":
    matrix =[
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    print(Solution().countSquares(matrix))