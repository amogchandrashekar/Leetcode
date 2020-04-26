from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        answer = list()

        for row_index, row in enumerate(nums):
            for column_index in range(len(row)):
                diagonals[row_index + column_index].append(nums[row_index][column_index])

        for index, diag_list in diagonals.items():
            answer.extend(diag_list[::-1])

        return answer


if __name__ == "__main__":
    nums = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    print(Solution().findDiagonalOrder(nums))
