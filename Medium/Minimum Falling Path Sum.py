'''
Given a square array of integers A, we want the minimum sum of a falling path through A.
A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by at most one.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

Note:
1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
'''

from typing import List


class Solution:
    def minFallingPathSum(self, nums: List[List[int]]) -> int:
        for row_index in range(1, len(nums)):
            for col_index in range(len(nums[row_index])):
                top_left = nums[row_index - 1][col_index - 1] if col_index - 1 >= 0 else float("inf")
                top_right = nums[row_index - 1][col_index + 1] if col_index + 1 < len(nums[row_index]) else float("inf")
                nums[row_index][col_index] += min(nums[row_index - 1][col_index], top_left, top_right)
        return min(nums[len(nums) - 1])


if __name__ == "__main__":
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().minFallingPathSum(nums))
