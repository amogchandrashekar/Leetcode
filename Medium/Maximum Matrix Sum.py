from typing import List, Optional


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_total = neg = 0
        mi = float('inf')

        for row in matrix:
            for num in row:
                abs_total += abs(num)
                if num < 0:
                    neg += 1
                mi = min(mi, abs(num))
        return abs_total if neg % 2 == 0 else abs_total - 2 * mi


if __name__ == "__main__":
    matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
    print(Solution().maxMatrixSum(matrix))
