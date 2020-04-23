"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

from typing import List
from bisect import bisect_left


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.sort()
        for num in nums2:
            nums1.remove(0)
            index = bisect_left(nums1, num)
            nums1.insert(index, num)


if __name__ == "__main__":
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    print(Solution().merge(nums1, m, nums2, n))