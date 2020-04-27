"""
Given an integer array, you need to find one continuous subarray that
if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9]
 in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums == nums:
            return 0

        first_mismatch, last_mismatch = len(nums) - 1, 0
        for index, num in enumerate(nums):
            if num != sorted_nums[index]:
                first_mismatch = min(first_mismatch, index)
                last_mismatch = max(last_mismatch,index)

        return last_mismatch - first_mismatch + 1


if __name__ == "__main__":
    nums = [5,4,3,2,1]
    print(Solution().findUnsortedSubarray(nums))