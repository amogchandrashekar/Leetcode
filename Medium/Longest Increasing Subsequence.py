"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(dp)):
            for j in range(i):
                dp[i] = max(dp[j] + 1 if nums[j] < nums[i] else 0, dp[i])
        return max(dp) if dp else 0

    def lengthOfLIS_memoization(self, nums: List[int]) -> int:
        memo = dict()

        def dfs(ind, prev_max):
            if (ind, prev_max) in memo:
                return memo[(ind, prev_max)]

            if ind == len(nums):
                return 0

            cur_num = nums[ind]
            if cur_num > prev_max:
                memo[(ind, prev_max)] = max(1 + dfs(ind + 1, cur_num), dfs(ind + 1, prev_max))
            else:
                memo[(ind, prev_max)] = dfs(ind + 1, prev_max)

            return memo[(ind, prev_max)]

        return dfs(0, float('-inf'))


if __name__ == "__main__":
    nums = [0,1,0,3,2,3]
    print(Solution().lengthOfLIS(nums))