from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for ind in range(len(nums) - 1):

            if ind % 2 == 0:
                if nums[ind] > nums[ind + 1]:
                    nums[ind], nums[ind + 1] = nums[ind + 1], nums[ind]

            else:
                if nums[ind] < nums[ind + 1]:
                    nums[ind], nums[ind + 1] = nums[ind + 1], nums[ind]