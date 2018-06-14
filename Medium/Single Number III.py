# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
# Example:
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
#
# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

import collections
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        cnt=collections.Counter(nums)
        for key in cnt:
            if cnt[key]==1:
                a.append(key)
        return a



# print(Solution().singleNumber([1,2,1,3,2,5]))