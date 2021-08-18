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
        l, r = 0, 0
        cur_sum = 0
        ans = float('inf')

        while r < len(nums):

            while cur_sum < target and r < len(nums):
                cur_sum += nums[r]
                r += 1

            while l < min(r, len(nums)) and cur_sum >= target:
                ans = min(ans, r - l)
                cur_sum -= nums[l]
                l += 1

        return ans if ans != float('inf') else 0


if __name__ == "__main__":
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(s, nums))
