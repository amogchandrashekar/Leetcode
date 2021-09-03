from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(row, search):
            low, high = 0, len(row) - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == search:
                    return True
                elif row[mid] < search:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        for row in matrix:
            if row[0] > target:
                return False

            if row[-1] < target:
                continue

            if binary_search(row, target):
                return True

        return False
