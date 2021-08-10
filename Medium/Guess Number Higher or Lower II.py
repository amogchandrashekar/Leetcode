from functools import lru_cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:

        @lru_cache(maxsize=None)
        def dfs(l, r):
            if l >= r:
                return 0

            max_ans = float('inf')
            for mid in range(l, r + 1):
                max_ans = min(max_ans, max(mid + dfs(l, mid - 1), mid + dfs(mid + 1, r)))
            return max_ans

        return dfs(0, n)