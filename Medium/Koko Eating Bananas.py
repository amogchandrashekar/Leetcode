from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = None

        while left <= right:
            mid = (left + right) // 2
            eating_time = sum([math.ceil(pile / mid) for pile in piles])

            if eating_time > h:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans
