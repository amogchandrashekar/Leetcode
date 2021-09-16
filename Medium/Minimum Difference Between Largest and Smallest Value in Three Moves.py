from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) > 1 and len(nums) <= 4:
            return 0

        nums.sort()
        window_len = len(nums) - 4
        l, r = 0, window_len
        ans = float('inf')

        while r < len(nums):
            ans = min(ans, nums[r] - nums[l])
            r += 1
            l += 1

        return ans