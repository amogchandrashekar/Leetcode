from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][-1] > h:
                ind, height = stack.pop()
                max_area = max(max_area, height * (i - ind))
                start = ind

            stack.append([start, h])

        while stack:
            ind, height = stack.pop()
            max_area = max(max_area, (len(heights) - ind) * height)

        return max_area