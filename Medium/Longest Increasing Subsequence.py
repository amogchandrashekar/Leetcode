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


if __name__ == "__main__":
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(Solution().lengthOfLIS(nums))