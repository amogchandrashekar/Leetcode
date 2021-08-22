from typing import List
from functools import lru_cache


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        min_val = float('inf')
        for i in range(len(mat)):
            mat[i] = sorted(mat[i])

        @lru_cache(maxsize=None)
        def dfs(rid, rem):
            nonlocal min_val
            if abs(rem) > min_val:
                # pruning trees
                return float('inf')

            if rem == 0 and rid == len(mat):
                min_val = 0
                return 0

            if rid == len(mat):
                return abs(rem)

            ans = float('inf')
            for c in range(len(mat[rid])):
                ans = min(ans, dfs(rid + 1, rem - mat[rid][c]))

            return ans

        return dfs(0, target)




if __name__ == '__main__':
    mat = [[3,5],[5,10]]
    target = 47
    print(Solution().minimizeTheDifference(mat, target))
