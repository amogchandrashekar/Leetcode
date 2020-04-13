"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input:
    [0,1]
Output:
    2
Explanation:
    [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input:
    [0,1,0]
Output:
    2
Explanation:
    [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = dict()
        hash_map[0] = -1
        max_pairs, count = 0, 0
        for index, num in enumerate(nums):
            count -= 1 if num == 0 else 1
            if count not in hash_map:
                hash_map[count] = index
            else:
                max_pairs = max(max_pairs, index - hash_map[count])
        return max_pairs


if __name__ == "__main__":
    nums = [0, 1, 1, 1, 0]
    print(Solution().findMaxLength(nums))