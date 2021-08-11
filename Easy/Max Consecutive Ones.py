from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        max_ones = 0

        for num in nums:
            if num == 1:
                ones += 1
                max_ones = max(ones, max_ones)
            else:
                ones = 0

        return max_ones