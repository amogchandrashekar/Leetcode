"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""

from typing import List
import numpy as np


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        cur_sum = 0
        sub_array_len = np.Inf

        while start < len(nums):
            if cur_sum < target and end < len(nums):
                cur_sum += nums[end]
                end += 1
            elif cur_sum >= target:
                sub_array_len = min(sub_array_len, end - start)
                cur_sum -= nums[start]
                start += 1
            else:
                cur_sum -= nums[start]
                start += 1

        if sub_array_len is np.Inf:
            return 0
        return sub_array_len


if __name__ == "__main__":
    s = 11
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(s, nums))
