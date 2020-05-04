"""
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other,
otherwise return False.

Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other. 
"""

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        p = -int(1e9 + 7)
        for i, v in enumerate(nums):
            if v == 1:
                if (i - p - 1) < k: return False
                p = i
        return True


if __name__ == "__main__":
    nums = [1, 0, 0, 1, 0, 1, 1]
    k = 2
    print(Solution().kLengthApart(nums, k))
