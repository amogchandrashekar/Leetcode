"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
"""

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count_dec = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count_dec += 1
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i + 1] = nums[i]
            if count_dec > 1:
                return False
        return True


if __name__ == "__main__":
    nums = [2, 3, 3, 2, 4]
    print(Solution().checkPossibility(nums))
