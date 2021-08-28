import collections
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1


print(Solution().moveZeroes([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))