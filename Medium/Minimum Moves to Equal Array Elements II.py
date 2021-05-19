from typing import List


import statistics

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = int(statistics.median(nums))
        return sum([abs(median - num) for num in nums])