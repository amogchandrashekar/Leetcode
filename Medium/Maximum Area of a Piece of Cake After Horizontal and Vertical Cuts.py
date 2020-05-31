"""
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts
where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly,
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays
horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.
"""
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10 ** 9 + 7

        def get_max(cuts, extend_elem):
            cuts.extend(extend_elem)
            cuts.sort()
            max_gap = float("-inf")
            for index in range(1, len(cuts)):
                max_gap = max(max_gap, cuts[index] - cuts[index - 1])
            return max_gap

        max_h, max_w = get_max(horizontalCuts, [0, h]), get_max(verticalCuts, [0, w])

        return (max_h * max_w) % mod


if __name__ == "__main__":
    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]
    print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))