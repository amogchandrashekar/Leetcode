import collections
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonzeroes = [x for x in nums if x != 0]
        if nonzeroes and len(nonzeroes) < len(nums):
            nums[:len(nonzeroes)] = nonzeroes
            nums[len(nonzeroes):] = [0] * (len(nums) - len(nonzeroes))



print(Solution().moveZeroes([1,2,1,0,0,3]))