from typing import List
from functools import lru_cache


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        @lru_cache(None)
        def dfs(ind, prev_color_id):

            if ind == len(costs):
                return 0

            ans = float('inf')

            for color in range(len(costs[0])):
                if color == prev_color_id:
                    continue

                ans = min(ans, costs[ind][color] + dfs(ind + 1, color))

            return ans

        return dfs(0, None)