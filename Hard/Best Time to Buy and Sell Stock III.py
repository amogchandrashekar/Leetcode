from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def dfs(ind, buy, transactions):

            if ind == len(prices) or transactions == 2:
                return 0

            if buy:
                hold = dfs(ind + 1, buy, transactions)
                buy_today = dfs(ind + 1, not buy, transactions) - prices[ind]
                return max(hold, buy_today)

            else:
                hold = dfs(ind + 1, buy, transactions)
                sell_today = dfs(ind + 1, not buy, transactions + 1) + prices[ind]
                return max(hold, sell_today)

        return dfs(0, True, 0)