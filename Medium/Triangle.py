"""
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

from typing import List


class Solution:
    def minimumTotal_tops_down(self, triangle: List[List[int]]) -> int:
        for row_index in range(1, len(triangle)):
            for col_index in range(len(triangle[row_index])):
                left_elem = triangle[row_index - 1][col_index - 1] if col_index - 1 >= 0 else float("inf")
                center_elem = triangle[row_index - 1][col_index] if col_index < len(triangle[row_index - 1]) else float(
                    "inf")
                triangle[row_index][col_index] += min(left_elem, center_elem)
        return min(triangle[-1])

    def minimumTotal_bottoms_up(self, triangle: List[List[int]]) -> int:
        for row_index in range(len(triangle) - 2, -1, -1):
            for col_index in range(len(triangle[row_index])):
                triangle[row_index][col_index] += min(triangle[row_index + 1][col_index],
                                                      triangle[row_index + 1][col_index + 1])
        return triangle[0][0]


if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(Solution().minimumTotal_bottoms_up(triangle))
    print(Solution().minimumTotal_tops_down(triangle))
