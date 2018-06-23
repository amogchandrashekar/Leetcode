# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
# Input: [1,2,3,1]
# Output: true

import collections
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt=collections.Counter(nums)
        for c in cnt:
            if cnt[c]>1:
                return True
        return False

# print(Solution().containsDuplicate([1,1,2,3,4,5]))