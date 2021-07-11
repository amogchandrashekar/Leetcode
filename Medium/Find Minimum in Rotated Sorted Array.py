from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m


if __name__ == '__main__':
    nums = [3, 1, 2]
    print(Solution().findMin(nums))