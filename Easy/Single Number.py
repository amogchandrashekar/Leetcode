# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
# Input: [2,2,1]
# Output: 1
#
# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res

# print(Solution().singleNumber([4,1,1,2,2,3,3]))