from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0

        if not matrix:
            return max_area

        heights = [0] * len(matrix[0])

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == "0":
                    heights[c] = 0
                else:
                    heights[c] += 1

            stack = []
            for ind, h in enumerate(heights):
                start = ind

                while stack and stack[-1][0] > h:
                    val, prev = stack.pop()
                    start = prev
                    area = (val) * (ind - prev)
                    max_area = max(area, max_area)

                stack.append([h, start])

            while stack:
                val, prev = stack.pop()
                area = (val) * (len(heights) - prev)
                max_area = max(area, max_area)

        return max_area