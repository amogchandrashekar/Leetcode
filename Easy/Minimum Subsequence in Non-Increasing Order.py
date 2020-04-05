"""
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the
non included elements in such subsequence.
If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions,
return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by
erasing some (possibly zero) elements from the array.
Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in
non-increasing order.

Example 1:

Input:
    nums = [4,3,10,9,8]
Output:
    [10,9]
Explanation:
    The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater
    than the sum of elements not included, however, the subsequence [10,9] has the maximum total sum of its elements.
"""


from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        i = 0
        subset = list()
        while i < len(nums):
            if sum(subset) == sum(nums[i:]):
                subset.append(nums[i])
            elif sum(nums[:i]) < sum(nums[i:]):
                subset.append(nums[i])
            i += 1
        return subset


if __name__=="__main__":
    nums = [4, 3, 10, 9, 8]
    print(Solution().minSubsequence(nums))