
# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums) - 1

        if (len(nums) <= 0):
            return -1

        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1

        return -1

# print(Solution().search([-1,0,3,5,9,12],0))