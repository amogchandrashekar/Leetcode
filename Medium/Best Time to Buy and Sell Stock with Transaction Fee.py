from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        memo = dict()

        def dfs(ind, buy):
            if ind == len(prices):
                return 0

            if (ind, buy) in memo:
                return memo[(ind, buy)]

            ans = 0
            if buy:
                ans += max(
                    -(prices[ind] + fee) + dfs(ind + 1, not buy),
                    dfs(ind + 1, buy)
                )
            else:
                ans += max(
                    prices[ind] + dfs(ind + 1, not buy),
                    dfs(ind + 1, buy)
                )

            memo[(ind, buy)] = ans
            return ans

        return dfs(0, True)


if __name__ == '__main__':
    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    print(Solution().maxProfit(prices, fee))
