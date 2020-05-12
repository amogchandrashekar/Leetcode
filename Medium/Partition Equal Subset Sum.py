"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        num_sum = sum(nums) // 2
        dp = [[False for i in range(num_sum + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = True

        for row_index in range(1, len(dp)):
            dp[row_index][0] = True

        for row_index in range(1, len(dp)):
            for col_index in range(len(dp[row_index])):
                dp[row_index][col_index] = (dp[row_index - 1][col_index]) or ((col_index - nums[row_index - 1] >= 0) and
                                                                              (dp[row_index - 1][col_index - nums[row_index - 1]]))
        return dp[-1][-1]


if __name__ == "__main__":
    nums = [1,5,11,5]
    print(Solution().canPartition(nums))
