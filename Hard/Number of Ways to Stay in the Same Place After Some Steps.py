from functools import lru_cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = (10 ** 9) + 7

        @lru_cache(maxsize=None)
        def dfs(steps_remaining, cur_pos):
            if steps_remaining == 0 and cur_pos == 0:
                return 1

            if cur_pos not in range(arrLen) or steps_remaining == 0:
                return 0

            ans = 0
            for steps in range(-1, 2):
                ans += dfs(steps_remaining - 1, cur_pos + steps)
            return ans

        return dfs(steps, 0) % MOD