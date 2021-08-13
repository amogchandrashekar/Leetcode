from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        ans = list()

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                diagonals[r + c].append(mat[r][c])

        for d in sorted(diagonals):
            if d % 2 != 0:
                ans.extend(diagonals[d])
            else:
                ans.extend(diagonals[d][::-1])

        return ans


if __name__ == '__main__':
    mat = [[1,2],[3,4]]
    print(Solution().findDiagonalOrder(mat))