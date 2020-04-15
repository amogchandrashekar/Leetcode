"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array
 (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        result = []

        for num in nums:
            result.append(curr)
            curr *= num

        curr = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= curr
            curr *= nums[i]

        return result


if __name__=="__main__":
    a = [1, 2, 3, 4]
    print(Solution().productExceptSelf(a))